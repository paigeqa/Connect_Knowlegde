# -*- coding: utf-8 -*-
"""TestRail API 공용 헬퍼: .env 로드 + GET 호출."""
import os, sys, json, time
try:
    import requests
except ImportError:
    sys.exit('requests 필요: pip install requests')

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def load_env():
    p = os.path.join(ROOT, '.env')
    if os.path.exists(p):
        for line in open(p, encoding='utf-8'):
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            k, v = line.split('=', 1)
            v = v.strip().strip('"').strip("'")
            os.environ.setdefault(k.strip(), v)


load_env()
CFG = json.load(open(os.path.join(HERE, 'suites.json'), encoding='utf-8'))
USER = os.environ.get('TESTRAIL_USER')
KEY = os.environ.get('TESTRAIL_KEY')
if not USER or not KEY:
    sys.exit('환경변수/.env 의 TESTRAIL_USER / TESTRAIL_KEY 를 설정하세요.')
AUTH = (USER, KEY)
API = CFG['base_url'].rstrip('/') + '/index.php?/api/v2'


def get(method, tries=4):
    url = f'{API}/{method}'
    for i in range(tries):
        r = requests.get(url, auth=AUTH, allow_redirects=False, timeout=60)
        if r.status_code == 429 or r.status_code >= 500:
            wait = float(r.headers.get('Retry-After', 2 * (i + 1)))
            time.sleep(wait); continue
        if r.is_redirect or 300 <= r.status_code < 400:
            raise RuntimeError(f'{method} -> 리다이렉트 {r.status_code} (인증/권한 확인)')
        if not r.ok:
            raise RuntimeError(f'{method} -> {r.status_code}: {r.text[:300]}')
        return r.json() if r.text else {}
    raise RuntimeError(f'{method} 재시도 초과')


def get_paged(method, key):
    """TestRail v2 페이지네이션 대응 (offset/limit)."""
    out = []
    offset = 0
    while True:
        sep = '&' if '?' in method else '&'
        data = get(f'{method}{sep}limit=250&offset={offset}')
        if isinstance(data, dict) and key in data:
            chunk = data[key]
        elif isinstance(data, list):
            chunk = data
        else:
            chunk = data.get(key, []) if isinstance(data, dict) else []
        out.extend(chunk)
        # _links.next 있으면 계속
        nxt = data.get('_links', {}).get('next') if isinstance(data, dict) else None
        if not nxt or not chunk:
            break
        offset += 250
    return out
