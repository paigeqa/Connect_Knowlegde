# TestRail 폴더 지도

Notion "v2 Connect Cloud" 체크리스트를 TestRail로 옮기고, 회귀 런을 관리하는 도구 모음.
모든 스크립트는 **`testrail/` 폴더에서** 실행한다(경로가 상대). 인증은 `testrail/.env`의 `TESTRAIL_USER`/`TESTRAIL_KEY` (커밋 금지).

## 폴더 구성

| 폴더 | 역할 |
|---|---|
| `migrate/` | Notion 체크리스트 메뉴 → TestRail 케이스 변환·업로드 (스킬 `testrail-migrate` 본체) |
| `runs/` | TestRail 런·플랜 관리 (회귀 R1→R2 이월, 결과 통계) |
| `이전_TestCase/` | 옛 테스트케이스 CSV 아카이브 (마이그레이션과 무관, 참고용) |
| `build/` | 스크립트 산출물(raw·plan·이미지·통계). git 미추적, 재생성 가능 |

## migrate/ — 체크리스트 → 케이스

절차 상세는 스킬 파일: `.claude/skills/testrail-migrate/SKILL.md`.

| 파일 | 역할 |
|---|---|
| `_tr.py` | 공용 헬퍼: `.env` 로드 + TestRail API GET. `suites.json` 로드 |
| `suites.json` | 메뉴↔suite_id 맵 (project 91, protopie.testrail.io) |
| `extract_menu.py` | Notion 덤프 → `build/<menu>_raw.md` + 이미지 다운로드(S3 1시간 만료) |
| `convert_api.py` | raw → `build/<menu>_plan.json` (leaf=Case 모델) |
| `upload.py` | plan → TestRail 업로드 (섹션 중첩 + 케이스 + 이미지). `--dry-run` / `--verify` |
| `split_connectmode.py` | Connect Mode 블록 1개를 3개 suite raw로 분할 |

실행 순서: `extract_menu` → (ConnectMode면 `split_connectmode`) → `convert_api` → `upload --dry-run` → `upload` → `upload --verify`.

## runs/ — 런·플랜 관리

`migrate/_tr.py`를 import해 인증·CFG를 공유한다(경로는 스크립트 상단에서 보정).

| 파일 | 역할 |
|---|---|
| `build_r2.py` | R2 플랜 생성 + R1(plan 2227) 결과(status/comment/defect) 이월 |
| `plan_stats.py` | 플랜 결과 통계 → 콘솔 + `build/plan_<id>_stats.json` |

## 주의

- ⏰ 이미지 S3 링크는 1시간 만료 → `extract_menu` 직후 지체 없이 진행. 403이면 Notion 재fetch.
- 🧪 `upload`는 dry-run 먼저. 같은 메뉴 재업로드 시 섹션 중복 → 기존 섹션 삭제 후 재실행.
- 🔑 API 키는 `.env`에서만 읽고 커밋·로그 노출 금지.
