# Notion CheckList → TestRail 마이그레이션 파이프라인

Notion "v2 Connect Cloud" CheckList을 TestRail 케이스로 옮기는 **재사용 파이프라인**.
규칙·결정·배경은 [TestRail_마이그레이션_논의.md](TestRail_마이그레이션_논의.md) 참고.

Claude Code 안에서는 **`/testrail-migrate <menu>`** 스킬로 전 과정을 자동 진행할 수 있고,
아래는 수동 실행(런북)이다.

## 모델 한 줄 요약

- **Case = leaf(최하위 체크) 단위.** 부모 불릿은 자식 ≥2면 subsection, 1개면 제목에 `—` 접두.
- TestRail을 **체크리스트처럼** 사용 → 제목만 읽고 Pass/Fail. 제목이 자기완결적.
- Figma 등 링크는 **References 필드**, 이미지는 **케이스 첨부**.
- 섹션 중첩은 API `parent_id`로 생성(CSV 위저드 X) → `>` 구분자/공백 이슈 없음.

## 사전 준비

```powershell
pip install requests
$env:TESTRAIL_USER = "you@protopie.io"   # 본인 TestRail 계정
$env:TESTRAIL_KEY  = "<본인 API Key>"     # My Settings > API Keys 에서 발급
```
- **키를 레포에 커밋하지 말 것.** 환경변수로만. 작업 후 키 폐기 권장.
- 대상 Suite는 [scripts/suites.json](scripts/suites.json)의 `menus` 맵 참고 (project 91).

## 5단계

```powershell
# 1) Notion 페이지를 notion-fetch로 받아 JSON(dump) 저장.  ⚠ 여기서 이미지 1시간 만료 카운트 시작.
#    (Claude Code의 Notion MCP fetch 결과 파일 경로를 <dump>로.)

# 2) 메뉴 블록 추출 + 이미지 즉시 다운로드 (만료 전!)
python scripts/extract_menu.py <menu> <dump>     # 예: Home

# 3) 변환 + 검증 (네트워크 X). 진단에서 Case 수·Priority·이미지 매핑 확인.
python scripts/convert_api.py <menu>             # build/<menu>_plan.json 생성

# 4) DRY RUN — 섹션 체인 1개 + 케이스 1개 + 이미지 1장만 올려 눈으로 확인
python scripts/upload.py <menu> --dry-run

# 5) 전체 업로드 + 검증
python scripts/upload.py <menu>
python scripts/upload.py <menu> --verify         # TestRail 케이스 수 == plan 수
```

## Gotcha (꼭 지킬 것)

- ⏰ **S3 스크린샷은 fetch 후 1시간 만료.** extract는 fetch 직후 바로. 403 나면 Notion 재fetch부터.
- 🔑 키는 **env에서만**. 스크립트에 하드코딩/커밋 금지.
- 🧪 **항상 dry-run 먼저.** 이상 없으면 전체. 문제 시 `delete_section`(cascade)로 정리 후 재실행.
- 🔁 같은 메뉴를 다시 올리면 **섹션이 중복 생성**된다. 재업로드 전 해당 Suite의 기존 섹션 삭제.
- 🖼 `get_attachments_for_case`는 한 첨부를 응답에 2번 표시하는 쿼크가 있음(=실제 1개). id로 중복 제거해 셀 것.

## 메뉴 키 / Suite

| menu 키 | Suite | suite_id |
|---|---|---|
| `Home` | [Cloud] Connect Home | 1361 |
| `LeftPanel` | [Cloud] Connect Mode > Left Panel | 1362 |
| `RightPanel` | [Cloud] Connect Mode > Right Panel | 1363 |
| `CanvasStage` | [Cloud] Connect Mode > Canvas & Stage | 1364 |
| `Preview` | [Cloud] Preview Mode | 1365 |
| `ShareRun` | [Cloud] Share & Run | 1366 |

> **Connect Mode 3분할**: `extract_menu.py`는 `### Connect Mode` 한 블록을 통째로 뽑는다.
> Left/Right/Canvas&Stage 3개 Suite로 나누는 것은 블록 내부 토글 그룹 기준 후속 분할이 필요
> (논의 문서 §3 참고). 그 전까지 `ConnectMode`로 한 번에 받아 수동 분할.

## 산출물 구조

```
scripts/extract_menu.py   convert_api.py   upload.py   suites.json
build/<menu>_raw.md   <menu>_plan.json   <menu>_images/*.png   (생성물, git 제외 권장)
```
