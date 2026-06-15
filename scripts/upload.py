# -*- coding: utf-8 -*-
"""build/<menu>_plan.json -> TestRail API 업로드 (섹션 중첩 + 케이스 + 이미지 첨부).

인증: 환경변수에서 읽음 (하드코딩/커밋 금지)
  $env:TESTRAIL_USER  (예: qa+1@protopie.io)
  $env:TESTRAIL_KEY   (API Key)

사용법:
  python scripts/upload.py <menu> --dry-run   # 첫 (이미지 포함) 케이스 1개만: 섹션 체인+케이스+이미지1
  python scripts/upload.py <menu>             # 전체 업로드
  python scripts/upload.py <menu> --verify    # 업로드 후 get_cases 카운트 검증

config: scripts/suites.json (base_url, project_id, template_id, menus->suite_id)
입력: build/<menu>_plan.json , build/<menu>_images/*.png
"""
import os, sys, json, time, io

try:
    import requests
except ImportError:
    sys.exit('requests 필요: pip install requests')

HERE = os.path.dirname(os.path.abspath(__file__))
CFG = json.load(open(os.path.join(HERE, 'suites.json'), encoding='utf-8'))
USER = os.environ.get('TESTRAIL_USER')
KEY = os.environ.get('TESTRAIL_KEY')
if not USER or not KEY:
    sys.exit('환경변수 TESTRAIL_USER / TESTRAIL_KEY 를 설정하세요.')
AUTH = (USER, KEY)
API = CFG['base_url'].rstrip('/') + '/index.php?/api/v2'


def call(method, payload=None, files=None, tries=4):
    url = f'{API}/{method}'
    for i in range(tries):
        if files is not None:
            r = requests.post(url, auth=AUTH, files=files, allow_redirects=False, timeout=60)
        elif payload is not None:
            r = requests.post(url, auth=AUTH, json=payload, allow_redirects=False,
                              headers={'Content-Type': 'application/json'}, timeout=60)
        else:
            r = requests.get(url, auth=AUTH, allow_redirects=False, timeout=60)
        if r.status_code == 429 or r.status_code >= 500:
            wait = float(r.headers.get('Retry-After', 2 * (i + 1)))
            print(f'   …{r.status_code} 재시도 {wait}s'); time.sleep(wait); continue
        if r.is_redirect or 300 <= r.status_code < 400:
            raise RuntimeError(f'{method} -> 예기치 않은 리다이렉트 {r.status_code} ({r.headers.get("Location")})')
        if not r.ok:
            raise RuntimeError(f'{method} -> {r.status_code}: {r.text[:300]}')
        return r.json() if r.text else {}
    raise RuntimeError(f'{method} 재시도 초과')


def main():
    menu = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('-') else 'Home'
    dry = '--dry-run' in sys.argv
    verify = '--verify' in sys.argv
    suite_id = CFG['menus'][menu]
    pid = CFG['project_id']
    tpl = CFG['template_id']
    plan = json.load(open(os.path.join('build', f'{menu}_plan.json'), encoding='utf-8'))
    img_dir = os.path.join('build', f'{menu}_images')
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    if verify:
        res = call(f'get_cases/{pid}&suite_id={suite_id}')
        cs = res['cases'] if isinstance(res, dict) and 'cases' in res else res
        print(f'[{menu}] TestRail 케이스 수 = {len(cs)} (plan = {len(plan["cases"])})')
        return

    sections = plan['sections']
    cases = plan['cases']
    real = {}   # tmp_id -> real section id

    def create_section(s):
        body = {'suite_id': suite_id, 'name': s['name']}
        if s['parent_tmp_id']:
            body['parent_id'] = real[s['parent_tmp_id']]
        rid = call(f'add_section/{pid}', body)['id']
        real[s['tmp_id']] = rid
        return rid

    def create_case(c, section_real_id):
        body = {'title': c['title'][:250], 'template_id': tpl, 'priority_id': c['priority_id']}
        if c.get('labels'):
            body['labels'] = c['labels']
        if c.get('refs'):
            body['refs'] = c['refs'][:250]
        return call(f'add_case/{section_real_id}', body)['id']

    def attach(case_id, fn):
        path = os.path.join(img_dir, fn)
        with open(path, 'rb') as f:
            data = f.read()   # 바이트로 읽어 전달(재시도 안전)
        call(f'add_attachment_to_case/{case_id}', files={'attachment': (fn, data, 'image/png')})

    if dry:
        # 이미지 포함 첫 케이스 선택 → 그 ancestry 섹션 + 케이스 + 이미지1
        target = next((c for c in cases if c.get('_img')), cases[0])
        chain = []
        sid = target['section_tmp_id']
        smap = {s['tmp_id']: s for s in sections}
        while sid:
            chain.append(smap[sid]); sid = smap[sid]['parent_tmp_id']
        chain.reverse()
        print('DRY RUN — 섹션 체인:', ' > '.join(s['name'] for s in chain))
        for s in chain:
            create_section(s)
            print('  + section', s['name'], '->', real[s['tmp_id']])
        cid = create_case(target, real[target['section_tmp_id']])
        print('  + case', repr(target['title']), '->', cid,
              '| prio', target['priority_id'], '| labels', target.get('labels'), '| refs', target.get('refs'))
        if target.get('_img'):
            attach(cid, target['_img'][0])
            print('  + attachment', target['_img'][0])
        print(f'\n확인: {CFG["base_url"]}/index.php?/cases/view/{cid}')
        return

    # 전체 업로드
    print(f'[{menu}] 섹션 {len(sections)}개 생성…')
    for s in sections:
        create_section(s)
    print(f'  완료. 케이스 {len(cases)}개 생성…')
    n_att = 0
    for i, c in enumerate(cases, 1):
        cid = create_case(c, real[c['section_tmp_id']])
        for fn in c.get('_img', []):
            attach(cid, fn); n_att += 1
        if i % 10 == 0:
            print(f'    {i}/{len(cases)}')
    print(f'  완료. 케이스 {len(cases)}, 첨부 {n_att}.')
    print(f'확인: {CFG["base_url"]}/index.php?/suites/view/{suite_id}')


if __name__ == '__main__':
    main()
