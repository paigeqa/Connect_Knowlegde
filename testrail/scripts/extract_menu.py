# -*- coding: utf-8 -*-
"""Notion 'v2 Connect Cloud' 덤프(JSON) → 한 메뉴 블록 raw.md + 이미지 다운로드.

notion-fetch 결과(거대 JSON, {"text": "...전체 페이지..."})를 입력으로 받아
지정 메뉴의 `### <메뉴>` ~ 다음 `### ` 직전까지를 잘라 build/<menu>_raw.md 로 저장하고,
그 안의 S3 스크린샷(X-Amz-Expires=3600, 1시간 만료)을 build/<menu>_images/ 로 즉시 다운로드.

⚠ 이미지는 fetch 시점부터 1시간 만료 → notion-fetch 직후 바로 이 스크립트를 실행할 것.

사용법:
  python scripts/extract_menu.py <menu> <dump.json 경로>
  <menu> ∈ Home | ConnectMode | Preview | ShareRun
    (LeftPanel/RightPanel/CanvasStage 는 ConnectMode 한 블록을 내부 분할 → 후속 작업, TestRail_마이그레이션_README.md 참고)
"""
import sys, os, json, re, io, urllib.request

# 메뉴 키 → ### 헤딩에 포함된 식별 문자열
MENU_HEADING = {
    'Home': 'Connect Home',
    'ConnectMode': 'Connect Mode',
    'Preview': 'Preview Mode',
    'ShareRun': 'Share & Run',
}


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    if len(sys.argv) < 3:
        sys.exit('사용법: python scripts/extract_menu.py <menu> <dump.json 경로>')
    menu, dump = sys.argv[1], sys.argv[2]
    if menu not in MENU_HEADING:
        sys.exit(f'알 수 없는 menu: {menu} (가능: {list(MENU_HEADING)})')

    obj = json.load(open(dump, encoding='utf-8'))
    text = obj['text'] if isinstance(obj, dict) and 'text' in obj else obj
    # 모든 ### 헤딩 위치
    heads = [(m.start(), text[m.start():m.start() + 60]) for m in re.finditer(r'### ', text)]
    target = next((i for i, (_, t) in enumerate(heads) if MENU_HEADING[menu] in t), None)
    if target is None:
        sys.exit(f'덤프에서 "{MENU_HEADING[menu]}" 헤딩을 못 찾음.')
    start = heads[target][0]
    end = heads[target + 1][0] if target + 1 < len(heads) else len(text)
    block = text[start:end]

    os.makedirs('build', exist_ok=True)
    raw_path = os.path.join('build', f'{menu}_raw.md')
    open(raw_path, 'w', encoding='utf-8').write(block)
    print(f'raw 저장: {raw_path} ({len(block)} chars)')

    # S3 이미지 다운로드
    img_dir = os.path.join('build', f'{menu}_images')
    os.makedirs(img_dir, exist_ok=True)
    urls = re.findall(r'!\[\]\((https://prod-files-secure\.s3[^)]+)\)', block)
    print(f'S3 이미지 {len(urls)}개 다운로드 중…')
    ok = 0
    for i, u in enumerate(urls, 1):
        m = re.search(r'amazonaws\.com/[^/]+/([0-9a-f-]+)/image\.png', u)
        uuid8 = (m.group(1)[:8] if m else f'{i:08d}')
        fn = os.path.join(img_dir, f'ch_{i:02d}_{uuid8}.png')
        try:
            req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
            data = urllib.request.urlopen(req, timeout=60).read()
            open(fn, 'wb').write(data); ok += 1
        except Exception as e:
            print(f'  {i} FAIL {e} (만료됐을 수 있음 → Notion 재fetch 후 즉시 재실행)')
    print(f'이미지 {ok}/{len(urls)} 저장 → {img_dir}')
    print(f'다음: python scripts/convert_api.py {menu}')


if __name__ == '__main__':
    main()
