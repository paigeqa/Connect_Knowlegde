# TestRail 마이그레이션 — 동료 안내 (먼저 읽기)

Notion "v2 Connect Cloud" CheckList을 TestRail 케이스로 옮기는 작업입니다.
**Connect Home은 이미 완료**(72 Case 업로드)했고, 나머지 5개 메뉴를 **분업**합니다.
이 폴더엔 다른 작업 파일도 섞여 있으니, **아래 "관련 파일"만 보면 됩니다.**

---

## 1. 이 작업과 관련된 파일 (이것만 보세요)

| 파일 | 용도 |
|---|---|
| **TestRail_마이그레이션_동료안내.md** | (이 문서) 시작점 |
| **TestRail_마이그레이션_README.md** | 실행 런북 — 5단계 명령어 + 주의사항 |
| **TestRail_마이그레이션_논의.md** | 변환 규칙·결정·TestRail ID (배경. §11이 최신 모델) |
| **scripts/** | 실제 변환·업로드 코드 (extract_menu · convert_api · upload · suites.json) |
| **.claude/skills/testrail-migrate/** | `/testrail-migrate` 스킬 (Claude Code가 절차를 자동 진행) |

> ⛔ **무관한 폴더/파일** (이 작업과 상관없음, 무시하세요):
> `Cloud_Connect_Spec.md`, `AGENTS.md`, `agent_plan.md`, `update_log/`,
> `Connect 강의 영상 자막 추출/`, `Notion 문서/`, `공식 Document/`, `이전 TestCase/`,
> `.claude/agents/`, `.claude/skills/concise-docs/`.

## 2. 작업 전 준비 (1회)

```powershell
pip install requests
# 본인 TestRail 계정으로 API Key 발급: TestRail > My Settings > API Keys
$env:TESTRAIL_USER = "you@protopie.io"
$env:TESTRAIL_KEY  = "<본인 API Key>"
```
- 키는 **환경변수로만**. 문서/코드/커밋에 절대 넣지 마세요.

## 3. 분업 — 본인 메뉴 하나 고르기

| menu 키 | Suite | 상태 |
|---|---|---|
| `Home` | [Cloud] Connect Home | ✅ 완료 (72 Case) |
| `Preview` | [Cloud] Preview Mode | ⬜ |
| `ShareRun` | [Cloud] Share & Run | ⬜ |
| `ConnectMode` | [Cloud] Connect Mode (Left/Right/Canvas&Stage 3분할) | ⬜ ※아래 주의 |

> **Connect Mode**는 한 블록을 3개 Suite로 나눠야 해서 규칙을 먼저 정해야 합니다.
> 혼자 하지 말고 Paige와 분할 기준부터 맞추세요. (논의 문서 §3)

## 4. Claude Code에게 요청하기

이 폴더에서 Claude Code를 열고 **둘 중 하나**:

**(A) 스킬로 한 번에** — 권장
```
/testrail-migrate Preview
```

**(B) 아래 문장을 그대로 붙여넣기** (스킬이 안 뜰 때)
```
이 폴더의 TestRail 마이그레이션 작업을 이어서 해줘. 내 담당 메뉴는 "Preview"야.
- 먼저 TestRail_마이그레이션_동료안내.md, TestRail_마이그레이션_README.md, TestRail_마이그레이션_논의.md(특히 §11 최신 모델)를 읽어.
- 환경변수 TESTRAIL_USER / TESTRAIL_KEY 는 내가 설정해뒀어.
- scripts/의 파이프라인을 그대로 써: Notion 재fetch → extract_menu → convert_api(진단 검토) → upload --dry-run(나한테 확인 받고) → 전체 upload → --verify.
- 변환 규칙(leaf=Case, 자식≥2 subsection, refs 분리, priority 키워드)은 바꾸지 말고, 결과만 같이 검수하자.
```
("Preview" 자리에 본인 menu 키를 넣으세요.)

## 5. 꼭 지킬 것

- ⏰ **Notion S3 스크린샷은 fetch 후 1시간 만료** → 재fetch 직후 바로 extract. 403 뜨면 재fetch부터.
- 🧪 **dry-run 먼저**, 눈으로 확인 후 전체 업로드. 같은 메뉴 재업로드 시 섹션이 중복되니 다시 올릴 땐 기존 섹션 삭제.
- 🔑 API 키는 env에서만. 출력/커밋 노출 금지.
- ✅ 업로드 후 `upload.py <menu> --verify`로 케이스 수 일치 확인.
- 🙋 Priority(High/Medium/Low)는 자동초안 → TestRail에서 사람이 검수.

질문은 Paige에게.
