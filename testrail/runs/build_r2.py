# -*- coding: utf-8 -*-
"""R2 플랜 생성 + R1(plan 2227) 결과 carry-over.

- R2 = 모든 우선순위(스위트 전체 케이스, include_all=true)
- R1에서 실행했던 case_id 들의 status/comment/defect 를 그대로 R2 런에 push
사용: python runs/build_r2.py   (testrail/ 에서 실행)
인증: migrate/_tr.py (.env)
"""
import os, sys, json, requests
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'migrate'))
import _tr as t

R1_PLAN = 2227
R2_NAME = "Connect Cloud Regression R2 — All priorities"
API = t.API
AUTH = t.AUTH
HDR = {'Content-Type': 'application/json'}


def post(method, payload):
    r = requests.post(f'{API}/{method}', auth=AUTH, headers=HDR,
                      data=json.dumps(payload), allow_redirects=False, timeout=120)
    if r.is_redirect or 300 <= r.status_code < 400:
        raise RuntimeError(f'{method} -> 리다이렉트 {r.status_code} (인증/권한)')
    if not r.ok:
        raise RuntimeError(f'{method} -> {r.status_code}: {r.text[:400]}')
    return r.json() if r.text else {}


def main():
    # 1) R1 carry-over 맵: suite_id -> {case_id: {status_id, comment, defects}}
    plan = t.get(f'get_plan/{R1_PLAN}')
    r1_runs = [(r.get('suite_id'), r['id'], r['name'])
               for e in plan.get('entries', []) for r in e.get('runs', [])]
    carry = {}            # suite_id -> {case_id: result}
    run_names = {}        # suite_id -> R1 run name (R2 런 이름 재사용)
    for suite_id, run_id, name in r1_runs:
        run_names[suite_id] = name
        m = {}
        tests = t.get_paged(f'get_tests/{run_id}', 'tests')
        for x in tests:
            res = t.get_paged(f"get_results/{x['id']}", 'results')
            latest = res[0] if res else {}
            entry = {'case_id': x['case_id'], 'status_id': x['status_id']}
            if latest.get('comment'):
                entry['comment'] = latest['comment']
            if latest.get('defects'):
                entry['defects'] = latest['defects']
            m[x['case_id']] = entry
        carry[suite_id] = m
        print(f'  R1 {name:14} (suite {suite_id}) → {len(m)} 케이스 수집')

    # 2) R2 플랜 생성 (R1 런 순서 유지, 스위트 전체 포함)
    entries = [{'suite_id': sid, 'name': run_names[sid], 'include_all': True}
               for sid, _, _ in r1_runs]
    print(f'\n▶ R2 플랜 생성: "{R2_NAME}"  (entries {len(entries)})')
    new_plan = post(f'add_plan/{t.CFG["project_id"]}',
                    {'name': R2_NAME, 'entries': entries})
    r2_plan_id = new_plan['id']
    r2_runs = {r['suite_id']: (r['id'], r['name'])
               for e in new_plan.get('entries', []) for r in e.get('runs', [])}
    print(f'  생성됨 plan_id={r2_plan_id}')

    # 3) carry-over push
    print('\n▶ carry-over push')
    total = 0
    for sid, (run_id, name) in r2_runs.items():
        results = list(carry.get(sid, {}).values())
        if not results:
            print(f'  {name:14} (run {run_id}) → carry 없음, 건너뜀')
            continue
        post(f'add_results_for_cases/{run_id}', {'results': results})
        total += len(results)
        print(f'  {name:14} (run {run_id}) → {len(results)} 건 반영')

    print(f'\n✅ 완료. R2 plan {r2_plan_id}, carry-over {total}건')
    print(f'   {t.CFG["base_url"]}/index.php?/plans/view/{r2_plan_id}')


if __name__ == '__main__':
    main()
