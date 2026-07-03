# -*- coding: utf-8 -*-
"""TestRail Plan 결과 통계.

사용법:
  python runs/plan_stats.py [plan_id]      # 기본 2227 (testrail/ 에서 실행)
출력: 콘솔 리포트 + build/plan_<id>_stats.json

집계:
  - 전체 status 분포
  - 런(메뉴)별 status 분포
  - 섹션별 status 분포
  - N/A(Not Available) 중 TBD 라벨 개수
인증: .env 의 TESTRAIL_USER / TESTRAIL_KEY (migrate/_tr.py 가 로드)
"""
import os, sys, json, re, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'migrate'))
import _tr as t

PLAN_ID = int(sys.argv[1]) if len(sys.argv) > 1 else 2227
NA_ID = 8       # Not Available
BLOCKED_ID = 2  # Blocked

# status id -> label
STATUSES = {s['id']: s['label'] for s in t.get('get_statuses')}


def strip_html(s):
    return re.sub(r'\s+', ' ', re.sub('<[^>]+>', '', s or '')).strip()


def latest_comment(test_id):
    res = t.get_paged(f'get_results/{test_id}', 'results')
    return strip_html(res[0].get('comment')) if res else ''


def case_index(suite_id):
    """case_id -> {section_id, labels(set of names)} 를 만든다."""
    cases = t.get_paged(f'get_cases/{t.CFG["project_id"]}&suite_id={suite_id}', 'cases')
    idx = {}
    for c in cases:
        labs = {(l.get('title') if isinstance(l, dict) else l) for l in (c.get('labels') or [])}
        idx[c['id']] = {'section_id': c.get('section_id'), 'labels': labs}
    return idx


def section_names(suite_id):
    secs = t.get_paged(f'get_sections/{t.CFG["project_id"]}&suite_id={suite_id}', 'sections')
    return {s['id']: s['name'] for s in secs}


def fmt(counter):
    return {STATUSES.get(k, str(k)): v for k, v in sorted(counter.items())}


def main():
    plan = t.get(f'get_plan/{PLAN_ID}')
    runs = [r for e in plan.get('entries', []) for r in e.get('runs', [])]

    overall = collections.Counter()
    tbd_total = 0           # TBD 라벨 케이스 (테스트 기준)
    tbd_na = 0              # N/A 이면서 TBD 라벨
    blocked = []            # Blocked 케이스 상세
    per_run = []
    per_section = []

    def pass_rate(cnt):
        executed = sum(cnt.values()) - cnt.get(NA_ID, 0)
        return (cnt.get(1, 0) / executed) if executed else None

    for r in runs:
        suite_id = r.get('suite_id')
        tests = t.get_paged(f'get_tests/{r["id"]}', 'tests')
        cidx = case_index(suite_id)
        snames = section_names(suite_id)

        run_cnt = collections.Counter()
        sec_cnt = collections.defaultdict(collections.Counter)
        for x in tests:
            sid = x['status_id']
            run_cnt[sid] += 1
            overall[sid] += 1
            meta = cidx.get(x.get('case_id'), {})
            sec = meta.get('section_id')
            sec_cnt[sec][sid] += 1
            has_tbd = 'TBD' in meta.get('labels', set())
            if has_tbd:
                tbd_total += 1
                if sid == NA_ID:
                    tbd_na += 1
            if sid == BLOCKED_ID:
                blocked.append({'run': r['name'], 'title': x.get('title'),
                                'comment': latest_comment(x['id'])})

        per_run.append({
            'run': r['name'], 'run_id': r['id'], 'total': len(tests),
            'status': fmt(run_cnt), 'na': run_cnt.get(NA_ID, 0),
            'pass_rate': pass_rate(run_cnt),
        })
        for sid, cnt in sec_cnt.items():
            per_section.append({
                'run': r['name'],
                'section': snames.get(sid, f'(section {sid})'),
                'total': sum(cnt.values()),
                'executed': sum(cnt.values()) - cnt.get(NA_ID, 0),
                'status': fmt(cnt),
                'pass_rate': pass_rate(cnt),
            })

    total = sum(overall.values())
    na_total = overall.get(NA_ID, 0)
    report = {
        'plan_id': PLAN_ID, 'plan': plan.get('name'), 'total_tests': total,
        'overall_status': fmt(overall),
        'na_total': na_total,
        'na_tbd': tbd_na,
        'na_real_unimplemented': na_total - tbd_na,
        'tbd_label_total': tbd_total,
        'blocked': blocked,
        'per_run': per_run,
        'per_section': per_section,
    }
    os.makedirs(os.path.join(t.ROOT, 'build'), exist_ok=True)
    out = os.path.join(t.ROOT, 'build', f'plan_{PLAN_ID}_stats.json')
    json.dump(report, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

    # ---- 콘솔 리포트 ----
    print(f'\n📋 {report["plan"]}  (plan {PLAN_ID})')
    print(f'   총 케이스: {total}개\n')
    print('=== 전체 status 분포 ===')
    for k, v in report['overall_status'].items():
        pct = v / total * 100 if total else 0
        print(f'  {v:4}  ({pct:4.1f}%)  {k}')
    print(f'\n  N/A {na_total}개  =  TBD {report["na_tbd"]}건  +  순수 미구현(TBD 라벨 없음) {report["na_real_unimplemented"]}건')

    print('\n=== Blocked 상세 ===')
    for b in blocked:
        print(f'  [{b["run"]}] {b["title"]}')
        print(f'     ↳ {b["comment"] or "(코멘트 없음)"}')

    print('\n=== 런(메뉴)별 (pass율 = Passed/실행) ===')
    for pr in per_run:
        parts = ', '.join(f'{k} {v}' for k, v in pr['status'].items())
        pr_s = f'{pr["pass_rate"]*100:.0f}%' if pr['pass_rate'] is not None else 'N/A'
        print(f'  ▸ {pr["run"]} (총 {pr["total"]}, pass {pr_s})  →  {parts}')

    print('\n=== pass율 낮은 섹션 (실행 ≥2개 한정) ===')
    ranked = [s for s in per_section if s['executed'] >= 2 and s['pass_rate'] is not None]
    ranked.sort(key=lambda s: (s['pass_rate'], -s['executed']))
    for s in ranked[:12]:
        parts = ', '.join(f'{k} {v}' for k, v in s['status'].items())
        print(f'  {s["pass_rate"]*100:5.0f}%  [{s["run"]}] {s["section"][:40]} (실행 {s["executed"]})  →  {parts}')
    print(f'\n💾 저장: {out}')


if __name__ == '__main__':
    main()
