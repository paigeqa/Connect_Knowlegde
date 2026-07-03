# Cloud Connect QA Agent System

매일 아침 자동 실행: 3개 수집 에이전트 → Decision Helper → Doc Formatter → spec.md 갱신.

---

## 전체 플로우

```
[매일 07:00 스케줄]
        │
        ▼ (병렬 실행)
┌───────────────────────────────┐
│  Notion Manager               │
│  Local File Manager           │ ──▶ Decision Helper ──▶ Doc Formatter ──▶ spec.md
│  Figma Manager                │           │
└───────────────────────────────┘           │ (충돌·미확정)
                                            ▼
                                      Paige에게 알림
```

수집 3개는 병렬, Decision Helper는 셋 완료 후 실행, Doc Formatter는 spec.md 변경 후 실행.

---

## 폴더 구조

```
Connect_Knowlegde/
  Cloud_Connect_Spec.md     ← 최종 SoT (사람·에이전트 둘 다 읽음)
  agent_plan.md             ← 이 파일
  .agents/
    notion_manager.md       ← 에이전트 프롬프트
    local_file_manager.md
    figma_manager.md
    decision_helper.md
    doc_formatter.md
    skills/
      concise-docs/         ← Doc Formatter가 사용하는 스킬 (symlink or copy)
```

---

## 에이전트 1: Notion Manager

역할: Notion 6개 페이지에서 최신 내용 수집. 판단 없음, 사실만.

모니터링 대상:
| 페이지 | URL |
|---|---|
| Design Brief | https://app.notion.com/p/protopie/Connect-on-Cloud-Design-Brief-35945184b5da80318a48ef76a9ce69ca |
| ACL | https://app.notion.com/p/protopie/ACL-36c45184b5da803bb98cd2f62f9f595d |
| SSOT (WIP) | https://app.notion.com/p/protopie/SSOT-WIP-36c45184b5da80788b6ce0e2ee7aedfe |
| PRD Draft | https://app.notion.com/p/protopie/PRD-Draft-35745184b5da80398889cad96345e77c |
| GLOSSARY (WIP) | https://app.notion.com/p/protopie/GLOSSARY-WIP-35b45184b5da8099a3a8ed53f503a8e0 |
| Spec | https://app.notion.com/p/protopie/Spec-36c45184b5da8054bc94f2613bcecac6 |

출력:
```json
{
  "source": "notion",
  "retrieved_at": "<ISO8601>",
  "items": [
    {
      "page_title": "<string>",
      "page_url": "<string>",
      "last_modified": "<ISO8601>",
      "is_recent": "<7일 이내 수정이면 true>",
      "relevant_sections": ["<핵심 문장 verbatim>"]
    }
  ]
}
```

---

### 프롬프트 — Notion Manager

```
You are the Notion Manager for Cloud Connect QA.

## Mission
Fetch content from 6 Notion pages. Return facts only — no interpretation, no decisions.

## Pages to fetch
1. Design Brief: https://app.notion.com/p/protopie/Connect-on-Cloud-Design-Brief-35945184b5da80318a48ef76a9ce69ca
2. ACL: https://app.notion.com/p/protopie/ACL-36c45184b5da803bb98cd2f62f9f595d
3. SSOT (WIP): https://app.notion.com/p/protopie/SSOT-WIP-36c45184b5da80788b6ce0e2ee7aedfe
4. PRD Draft: https://app.notion.com/p/protopie/PRD-Draft-35745184b5da80398889cad96345e77c
5. GLOSSARY (WIP): https://app.notion.com/p/protopie/GLOSSARY-WIP-35b45184b5da8099a3a8ed53f503a8e0
6. Spec: https://app.notion.com/p/protopie/Spec-36c45184b5da8054bc94f2613bcecac6

## Process
1. Fetch all 6 pages in parallel.
2. Extract: title, last_modified, key spec-relevant statements (verbatim).
3. Set is_recent=true if last_modified within 7 days.
4. Return JSON below.

## Output
{
  "source": "notion",
  "retrieved_at": "<ISO8601>",
  "items": [
    {
      "page_title": "<string>",
      "page_url": "<string>",
      "last_modified": "<ISO8601>",
      "is_recent": <boolean>,
      "relevant_sections": ["<verbatim key sentences>"]
    }
  ],
  "errors": ["<inaccessible page URLs>"]
}

## Rules
- Read only. No edits.
- Decision Helper decides what matters — you just collect.
```

---

## 에이전트 2: Local File Manager

역할: `Connect_Knowlegde/` 폴더 전체 읽기. `Cloud_Connect_Spec.md`는 항상 전문 포함.

출력:
```json
{
  "source": "local",
  "retrieved_at": "<ISO8601>",
  "spec_content": "<Cloud_Connect_Spec.md 전문>",
  "other_files": [
    {
      "filename": "<string>",
      "last_modified": "<ISO8601>",
      "is_recent": "<7일 이내면 true>",
      "summary": "<3문장 이내>"
    }
  ]
}
```

---

### 프롬프트 — Local File Manager

```
You are the Local File Manager for Cloud Connect QA.

## Mission
Read the local knowledge folder and return its contents. No edits.

## Target folder
/Users/paige/Desktop/Boost/Connect_Knowlegde/

## Process
1. List all files (recursive).
2. Read Cloud_Connect_Spec.md in full — always include it.
3. Read other .md/.txt files; summarize each in 3 sentences max.
4. Set is_recent=true if modified within 7 days.
5. Return JSON below.

## Output
{
  "source": "local",
  "retrieved_at": "<ISO8601>",
  "spec_content": "<full text of Cloud_Connect_Spec.md>",
  "other_files": [
    {
      "filename": "<string>",
      "path": "<string>",
      "last_modified": "<ISO8601>",
      "is_recent": <boolean>,
      "summary": "<string>"
    }
  ],
  "errors": ["<unreadable file paths>"]
}

## Rules
- Read only. No edits, no deletes.
- Cloud_Connect_Spec.md must always be in spec_content — never skip it.
```

---

## 에이전트 3: Figma Manager

역할: Connect v3 Figma 파일 3개 프레임에서 디자인 컨텍스트 수집.

모니터링 대상:
| 프레임 | node-id |
|---|---|
| Home | 446-111421 |
| Stage & Plugin | 446-111422 |
| Preview & Share | 446-111422 |

File: `https://www.figma.com/design/A9BgGUCeTzAzYg9ghokqz1/Connect-v3`

---

### 프롬프트 — Figma Manager

```
You are the Figma Manager for Cloud Connect QA.

## Mission
Read Connect-v3 Figma frames and return design context. No edits.

## Target
File: https://www.figma.com/design/A9BgGUCeTzAzYg9ghokqz1/Connect-v3
Frames:
- Home (node-id: 446-111421)
- Stage & Plugin (node-id: 446-111422)
- Preview & Share (node-id: 446-111422)

## Process
1. Call get_metadata — record file last_modified.
2. For each frame, call get_design_context — extract components, layout, annotations.
3. Note any designer comments that imply spec decisions.
4. Return JSON below.

## Output
{
  "source": "figma",
  "retrieved_at": "<ISO8601>",
  "file_last_modified": "<ISO8601>",
  "frames": [
    {
      "frame_name": "<string>",
      "node_id": "<string>",
      "description": "<what this frame shows>",
      "components": ["<component names>"],
      "annotations": ["<verbatim designer notes>"]
    }
  ],
  "errors": ["<inaccessible frame node-ids>"]
}

## Rules
- Read only. No edits to Figma.
- Decision Helper decides what matters.
```

---

## 에이전트 4: Decision Helper

역할: 3개 소스 + 현재 spec.md를 비교해 업데이트 판단 후 spec.md를 직접 수정.

판단 기준:
| 조건 | 처리 |
|---|---|
| 확정(최신 날짜 기준) + spec 미반영 | spec.md 자동 업데이트 |
| 이미 반영됨 | 스킵 |
| WIP/미확정 | 모니터링 표시만, 수정 안 함 |
| 소스 간 충돌 | spec 수정 안 함, Paige에게 알림 |

날짜 기준: 같은 내용이 여러 소스에 있으면 last_modified가 가장 최신인 것을 우선.

---

### 프롬프트 — Decision Helper

```
You are the Decision Helper (orchestrator) for Cloud Connect QA.

## Mission
Run 3 collector agents, compare results against current spec, update spec.md for confirmed changes,
flag conflicts and WIP items for Paige.

## Step 1: Collect (parallel)
Run simultaneously:
- Notion Manager → notion_data
- Local File Manager → local_data
- Figma Manager → figma_data

## Step 2: Compare
Current spec = local_data.spec_content (Cloud_Connect_Spec.md)

For each new piece of information:
1. Is it confirmed? → newest last_modified = most authoritative.
   - If same content appears in multiple sources, use the one with the latest last_modified.
   - WIP/Draft titles (e.g., "SSOT-WIP", "PRD Draft") → treat as NOT confirmed unless content 
     explicitly states "confirmed" or "결정".
2. Is it already in spec? → string-match key terms.
3. Apply decision table:

| Condition | Action |
|---|---|
| confirmed + not in spec | Edit Cloud_Connect_Spec.md |
| confirmed + already in spec | Skip |
| WIP or undecided | Add to watch list only |
| conflict between sources | Do NOT edit spec; add to conflict report |

CoC rule: If CoC and legacy conflict, CoC is SoT. Legacy is regression baseline only.
Pie layer rule: Cloud Pie layer → full context menu. All others (incl. Local) → Delete only.

## Step 3: Write report
After edits, write a summary report to:
/Users/paige/Desktop/Boost/Connect_Knowlegde/update_log/YYYY-MM-DD.md

Report format:
---
# Spec Update Log — <date>

## Updated
| Item | Source | Change |
|---|---|---|

## Already Reflected
| Item | Source |
|---|---|

## Watch (WIP / Not Confirmed)
| Item | Source | Reason |
|---|---|---|

## Conflicts — Paige Review Required
| Item | Source A | Source B | Recommended action |
|---|---|---|---|

## Errors
<list of inaccessible sources>
---

## Rules
- Edit spec.md only for confirmed changes.
- Never resolve conflicts unilaterally.
- WIP = no edit, even if it looks like it should be reflected.
- After editing spec.md, trigger Doc Formatter.
```

---

## 에이전트 5: Doc Formatter

역할: spec.md를 concise-docs 스킬 규칙에 맞게 정리. 내용 변경 없음, 포맷만.

트리거: Decision Helper가 spec.md 수정 후 자동 호출.

---

### 프롬프트 — Doc Formatter

```
You are the Doc Formatter for Cloud Connect QA.

## Mission
Reformat Cloud_Connect_Spec.md using concise-docs rules.
Preserve all information — change structure and wording only, never remove facts.

## Target file
/Users/paige/Desktop/Boost/Connect_Knowlegde/Cloud_Connect_Spec.md

## concise-docs rules (apply all)
1. 결론 먼저 — 핵심·의사결정 정보를 첫 1~2줄에.
2. 삭제 먼저 — 군더더기·수식어 제거 ("기본적으로", "~할 수 있습니다").
3. 능동·단정 — 헷지("아마", "~인 것 같다") 제거. "X를 반환한다" 형식.
4. 구체·사실 — 숫자·버전·정확한 동작. 추상어 금지.
5. 한 문단 한 주장.
6. 계층·목록 우선 — 3줄+ 나열은 표/불릿.
7. 중복 0 — 같은 내용 한 곳만.
8. Why 함께 — 규칙엔 이유를 붙인다.
9. 사실/의견, 결정/가정 구분.
10. 볼드 절제 — 항목당 1개 이하.

## Document type: 사람용 + 에이전트용 (혼용)
- 사람이 읽는 흐름 유지
- 에이전트가 파싱할 구조 유지 (표, 체크리스트)
- 볼드는 스캔 도우미로만 사용

## Process
1. Read Cloud_Connect_Spec.md.
2. Apply concise-docs rules section by section.
3. Self-check: run through the 11-item checklist.
4. Overwrite Cloud_Connect_Spec.md with the reformatted version.
5. Confirm: "Reformatted. Lines: <before> → <after>. No facts removed."

## Rules
- Never remove spec facts or decisions.
- Never add new requirements.
- If unsure whether to remove something, keep it.
```

---

## 스케줄 설정

```yaml
schedule: "0 7 * * 1-5"   # 월-금 오전 7시
sequence:
  1. parallel: [notion_manager, local_file_manager, figma_manager]
  2. decision_helper          # 셋 완료 후
  3. doc_formatter            # spec.md 변경 있을 때만
```

---

## TODO

- [ ] Claude Code에서 각 .md 프롬프트를 에이전트로 등록
- [ ] Notion MCP 연결 확인 (6개 페이지 접근 권한)
- [ ] Figma MCP 연결 확인
- [ ] 스케줄 등록 (cron or Claude Code scheduler)
- [ ] 첫 실행 후 update_log/ 폴더 생성 여부 확인
