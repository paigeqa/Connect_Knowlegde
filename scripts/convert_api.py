# -*- coding: utf-8 -*-
"""Notion CheckList(메뉴 raw.md) -> TestRail build_plan.json (Checklist 모델).

규칙(플랜 확정):
- Case = leaf(자식 없는 최하위 체크) 단위.
- 비-leaf 불릿: 자식 >=2 -> subsection 승격(이름=불릿). 자식 1개 -> em-dash 접두로 운반.
- 제목 자기완결. 마크다운/raw URL -> refs 필드로 분리, 제목엔 링크 텍스트만.
- Priority 키워드 자동초안(High=6/Medium=2/Low=5). 'TBD' -> label 25.
- 이미지: 디자인 토글 -> 섹션 첫(또는 첫 하위) 케이스 / 액션 토글 -> 성공·실패 키워드 케이스.
- 섹션명의 '>'는 그대로 둠(API는 분리 안 함).

사용법:  python scripts/convert_api.py <menu>
  입력  build/<menu>_raw.md , build/<menu>_images/*.png
  출력  build/<menu>_plan.json  (+ 진단 stdout)
"""
import re, json, sys, io, os, glob

# ---- Priority keyword tables (문서 섹션 5) ----
P1 = ['접근', '진입', 'Editor 롤을 유지', '생성', '이동', '화면 이동', '요청 성공',
      '성공 토스트', '정상동작', 'list 로드', '로드', 'Viewer 권한', '권한 미노출']
P3 = ['긴 경우', '초과', '30개', '최대 길이', '개씩', '깨짐', '말줄임표', '말줌임표',
      '탭 길이', '썸네일', '레이어', '중복', '허용', 'UI가 다음과 같음', '디자인', '비율']
PRIO_ID = {'P1': 6, 'P2': 2, 'P3': 5}  # High / Medium / Low
TBD_LABEL_ID = 25
DESIGN_TOGGLES = ('디자인', '디자인 드래프트')


def clean(t):
    t = t.replace(r'\[', '[').replace(r'\]', ']').replace(r'\>', '>')
    t = re.sub(r'[\s,:]+$', '', t.strip())
    return t.strip()


def split_refs(text):
    """제목에서 URL 분리. 마크다운 링크는 텍스트만 남기고 url은 refs로. 반환 (title, [urls])."""
    urls = []

    def md(m):
        label, url = m.group(1), m.group(2)
        urls.append(url)
        return label
    text = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', md, text)
    # 남은 raw URL 제거 -> refs
    for u in re.findall(r'https?://[^\s)]+', text):
        urls.append(u)
    text = re.sub(r'https?://[^\s)]+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'[\s:,>]+$', '', text).strip()
    return text, urls


def decide_prio(text):
    if any(k in text for k in P1):
        return 'P1'
    if any(k in text for k in P3):
        return 'P3'
    return 'P2'


def tabs(line):
    n = 0
    for ch in line:
        if ch == '\t':
            n += 1
        else:
            break
    return n


class Node:
    __slots__ = ('type', 'title', 'children', 'uuid')

    def __init__(self, type, title='', uuid=None):
        self.type = type      # 'role' | 'toggle' | 'bullet' | 'image'
        self.title = title
        self.children = []
        self.uuid = uuid


def parse_tree(raw):
    root = Node('root')
    stack = [(-2, root)]   # (tab-depth, node). role는 -1에 위치시켜 depth0 자식이 붙도록.
    for line in raw.split('\n'):
        d = tabs(line)
        s = line.strip()
        if not s or s.startswith('### ') or s == '<details>' or s.startswith('<unknown'):
            continue
        m = re.match(r'📍\s*\*\*(.+?)\*\*', s)
        if m:
            node = Node('role', clean(m.group(1)))
            root.children.append(node)
            stack = [(-2, root), (-1, node)]
            continue
        if s.startswith('<summary>'):
            title = clean(re.sub(r'</?summary>', '', s))
            while stack[-1][0] >= d:
                stack.pop()
            node = Node('toggle', title)
            stack[-1][1].children.append(node)
            stack.append((d, node))
            continue
        if s == '</details>':
            continue   # lazy pop으로 처리
        mi = re.match(r'!\[\]\((https://prod-files-secure\.s3[^)]+)\)', s)
        if mi:
            u = re.search(r'amazonaws\.com/[^/]+/([0-9a-f-]+)/image\.png', mi.group(1))
            stack[-1][1].children.append(Node('image', uuid=(u.group(1) if u else '?')))
            continue
        if s.startswith('- '):
            while stack[-1][0] >= d:
                stack.pop()
            node = Node('bullet', s[2:])
            stack[-1][1].children.append(node)
            stack.append((d, node))
            continue
    return root


def has_bullet(node):
    for c in node.children:
        if c.type == 'bullet' or (c.type == 'toggle' and has_bullet(c)):
            return True
    return False


def is_real_section(node):
    return node.type == 'role' or (node.type == 'toggle' and has_bullet(node))


def main():
    menu = sys.argv[1] if len(sys.argv) > 1 else 'Home'
    raw_path = os.path.join('build', f'{menu}_raw.md')
    img_dir = os.path.join('build', f'{menu}_images')
    raw = open(raw_path, encoding='utf-8').read()
    root = parse_tree(raw)

    # uuid8 -> 이미지 파일명 매핑
    img_files = {}
    for p in glob.glob(os.path.join(img_dir, '*.png')):
        mm = re.search(r'([0-9a-f]{8})\.png$', os.path.basename(p))
        if mm:
            img_files[mm.group(1)] = os.path.basename(p)

    sections = []   # {tmp_id, parent_tmp_id, name}
    cases = []      # {tmp_id, section_tmp_id, title, priority_id, labels, refs}
    images = []     # {uuid, file, toggle, kind, owner_section_tmp}
    node_sid = {}   # id(node) -> section tmp_id (real sections only)
    seq = {'sec': 0, 'case': 0}

    def new_section(parent_tmp, name):
        seq['sec'] += 1
        sid = f's{seq["sec"]}'
        sections.append({'tmp_id': sid, 'parent_tmp_id': parent_tmp, 'name': name})
        return sid

    def new_case(section_tmp, prefix, leaf_text):
        full = ' — '.join([clean(x) for x in prefix] + [clean(leaf_text)])
        title, refs = split_refs(full)
        seq['case'] += 1
        cid = f'c{seq["case"]}'
        cases.append({'tmp_id': cid, 'section_tmp_id': section_tmp, 'title': title,
                      'priority_id': PRIO_ID[decide_prio(full)],
                      'labels': [TBD_LABEL_ID] if 'TBD' in full else [],
                      'refs': ', '.join(dict.fromkeys(refs))})
        return cid

    def process_bullets(bullets, sid, prefix):
        for b in bullets:
            kids = [c for c in b.children if c.type == 'bullet']
            if not kids:
                new_case(sid, prefix, b.title)
            elif len(kids) >= 2:
                name = ' — '.join([clean(x) for x in prefix] + [clean(b.title)])
                sub = new_section(sid, name)
                process_bullets(kids, sub, [])
            else:
                process_bullets(kids, sid, prefix + [b.title])

    def walk(node, parent_tmp):
        sid = new_section(parent_tmp, clean(node.title))
        node_sid[id(node)] = sid
        direct = [c for c in node.children if c.type == 'bullet']
        process_bullets(direct, sid, [])
        for c in node.children:
            if c.type == 'toggle' and is_real_section(c):
                walk(c, sid)

    for r in root.children:
        if is_real_section(r):
            walk(r, None)

    # ---- 이미지 매핑 ----
    # owner = "이미지를 담은 토글의 부모 real-section". real-section을 지날 때마다 cur 갱신.
    def walk_images(node, owner_sid):
        is_sec = id(node) in node_sid
        cur = node_sid[id(node)] if is_sec else owner_sid
        for c in node.children:
            if c.type == 'image':
                toggle = node.title
                kind = 'design' if toggle in DESIGN_TOGGLES else 'action'
                images.append({'uuid': c.uuid, 'toggle': toggle, 'kind': kind, 'owner': owner_sid})
            elif c.type == 'toggle':
                walk_images(c, cur)
    for r in root.children:
        walk_images(r, None)

    # descendant section ids
    children_of = {}
    for s in sections:
        children_of.setdefault(s['parent_tmp_id'], []).append(s['tmp_id'])

    def subtree_sids(sid):
        out = [sid]
        for ch in children_of.get(sid, []):
            out += subtree_sids(ch)
        return out

    def cases_in(sid):
        return [c for c in cases if c['section_tmp_id'] == sid]

    def first_case_subtree(sid):
        ids = set(subtree_sids(sid))
        for c in cases:  # 생성 순서 = 트리 깊이우선
            if c['section_tmp_id'] in ids:
                return c
        return None

    img_out = []
    for im in images:
        owner = im['owner']
        target = None
        sect_cases = cases_in(owner) if owner else []
        if im['kind'] == 'action':
            tg = im['toggle']
            if '성공' in tg:
                target = next((c for c in sect_cases if '성공' in c['title']), None)
            if target is None and '실패' in tg:
                target = next((c for c in sect_cases if '실패' in c['title']), None)
            if target is None:
                target = sect_cases[0] if sect_cases else (first_case_subtree(owner) if owner else None)
        else:
            target = sect_cases[0] if sect_cases else (first_case_subtree(owner) if owner else None)
        fn = img_files.get(im['uuid'][:8], f'(missing:{im["uuid"][:8]})')
        if target is not None:
            target.setdefault('_img', []).append(fn)
        img_out.append({'uuid': im['uuid'][:8], 'file': fn, 'toggle': im['toggle'],
                        'kind': im['kind'], 'target_case': target['tmp_id'] if target else None})

    plan = {'menu': menu, 'sections': sections, 'cases': cases}
    os.makedirs('build', exist_ok=True)
    out_path = os.path.join('build', f'{menu}_plan.json')
    json.dump(plan, open(out_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

    # ---- 진단 ----
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    print(f'[{menu}] sections={len(sections)}  cases={len(cases)}  images={len(images)}')
    from collections import Counter
    pc = Counter(c['priority_id'] for c in cases)
    name = {6: 'High', 2: 'Medium', 5: 'Low'}
    print('Priority:', {name[k]: v for k, v in pc.items()})
    print('TBD label:', sum(1 for c in cases if c['labels']))
    print('refs 보유 케이스:', sum(1 for c in cases if c['refs']))
    print('이미지 첨부:', sum(len(c.get('_img', [])) for c in cases), '/', len(images))
    miss = [i for i in img_out if i['target_case'] is None or i['file'].startswith('(missing')]
    if miss:
        print('⚠ 이미지 이슈:', miss)
    print('→', out_path)


if __name__ == '__main__':
    main()
