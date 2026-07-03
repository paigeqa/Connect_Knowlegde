---
name: testrail-migrate
description: Notion "v2 Connect Cloud" CheckList의 한 메뉴를 TestRail 케이스로 변환·업로드한다. 사용자가 체크리스트를 TestRail로 옮기거나, Home/Connect Mode/Preview/Share&Run 같은 메뉴를 TestRail에 올려달라고 할 때 사용. leaf=Case 모델, 섹션 API 중첩, 이미지 첨부, dry-run 우선.
---

# TestRail 마이그레이션 스킬

Notion 체크리스트 메뉴 1개 → TestRail Suite. 결정론적 스크립트(`testrail/migrate/`)를 절차대로 호출한다.
모든 스크립트는 `testrail/` 폴더에서 실행한다(경로가 상대). 폴더 지도·런북: `testrail/README.md`.

## 입력
- 인자 `<menu>` ∈ `Home | ConnectMode | Preview | ShareRun` (suite 맵은 `migrate/suites.json`).
- 못 받았으면 어떤 메뉴인지 사용자에게 묻는다.

## 절차 (순서 엄수)

1. **인증 확인** — `$env:TESTRAIL_USER`, `$env:TESTRAIL_KEY`가 있는지 확인.
   없으면 사용자에게 설정을 요청(키는 env로만, 레포 커밋 금지).

2. **Notion 재fetch** — Notion MCP로 페이지를 fetch:
   `https://app.notion.com/p/protopie/v2-Connect-Cloud-38045184b5da80859707f179d576f9f9`
   결과가 커서 파일로 저장되면 그 경로를 `<dump>`로 사용.
   ⏰ **이 시점부터 S3 스크린샷 1시간 만료** — 이후 단계를 지체 없이 진행.

3. **추출 + 이미지 다운로드** (만료 전):
   `python migrate/extract_menu.py <menu> <dump>`
   403(만료) 나오면 2번부터 다시.

4. **변환 + 검증**: `python migrate/convert_api.py <menu>`
   진단 출력(Case 수, Priority 분포, 이미지 매핑, refs)을 사용자에게 보여주고
   누락 0·Case 수가 합리적인지 같이 확인.

5. **DRY RUN**: `python migrate/upload.py <menu> --dry-run`
   생성된 케이스 URL을 사용자에게 주고 **TestRail에서 눈으로 확인**(제목 자기완결·섹션 중첩·
   priority·label·refs·첨부). 확인 전까지 6번으로 넘어가지 말 것.

6. **전체 업로드**: 사용자 OK 후 `python migrate/upload.py <menu>`
   → `python migrate/upload.py <menu> --verify` 로 TestRail 케이스 수 == plan 수 확인.

## 반드시 지킬 것 (gotcha)

- ⏰ 이미지 1시간 만료 → fetch 직후 extract. 403이면 재fetch.
- 🧪 dry-run 없이 전체 업로드 금지. dry-run 데이터는 본 업로드 전 `delete_section`(cascade)으로 정리.
- 🔁 같은 메뉴 재업로드 시 섹션 중복 생성됨 → 기존 섹션 삭제 후 재실행.
- 🔑 API 키는 env에서만 읽고, 출력/로그/커밋에 노출하지 말 것.
- 🖼 `get_attachments_for_case`는 첨부를 2번 표시하는 쿼크(실제 1개) → id로 중복 제거해 셀 것.
- 🧩 변환 규칙(leaf=Case, ≥2 subsection 승격, refs 분리, priority 키워드)은 `convert_api.py`에 있음.
  규칙 변경은 문서 §5와 스크립트를 함께 고친다.

## 변환 규칙 미세조정 포인트

- subsection 승격 임계값(자식 ≥2). 너무 깊으면 상향하거나 일부를 em-dash 제목으로.
- Priority 키워드 표(P1/P3/P2)는 자동초안 → 업로드 후 사람이 검수·수정.
