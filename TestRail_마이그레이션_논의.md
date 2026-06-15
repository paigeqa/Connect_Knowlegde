# Notion CheckList → TestRail 마이그레이션 (논의 중)

> 상태: **계획 단계** (실행 전 / 시작 신호 대기 중)
> 최종 업데이트: 2026-06-15
> 대상 문서: Notion "v2 Connect Cloud" CheckList
> https://app.notion.com/p/protopie/v2-Connect-Cloud-38045184b5da80859707f179d576f9f9

---

## 1. 배경 / 상황

- **일정**: 통합 테스트 내일 시작, 총 2주 반.
- **개발 현황**: 피쳐테스트 중, 아직 미구현 항목 있음.
- **특징**: 기간이 짧아 스펙/디자인 미확정 부분 존재 (TD 기준 TBD 약 30개).
- **협업**: 동료 1명과 함께 진행. **테스트 결과 매일 스쿼드에 공유** 필요.
  - 동료 PC가 느림 → TestRail 로딩 속도가 이슈.

## 2. 결론: TestRail로 옮긴다 (Notion 토글 유지 X)

- 이유: 매일 결과 공유(진행률·Pass/Fail/Blocked 자동 집계) + 2인 분업 추적은
  TestRail이 압도적으로 유리. Notion 토글로는 매일 수동 집계가 비현실적.
- 미구현 항목은 TestRail의 `Blocked` 상태로, 스펙 미정은 Run에서 제외/라벨로 관리.

## 3. 체크리스트 규모 (Notion 분석 결과)

전체 큰 메뉴 4개 / 실제 체크 항목(불릿) 합계 **659개**.

| 메뉴 | 전체 체크 항목 | 상위불릿=Case |
|---|---:|---:|
| 🏠 Connect Home | 92 | **54** |
| ✏️ Connect Mode | 385 | **174** |
| 🖼️ Preview Mode | 111 | **70** |
| 🖇️ Share & Run | 71 | **38** |
| **합계** | **659** | **336** |

### Connect Mode 세분화 (큰 메뉴라 3개로 분리)

| 하위 그룹 | 전체 항목 | Case |
|---|---:|---:|
| Left Panel (Groups+Layers+Plugin) | 173 | **65** |
| Right Panel (=Console) | 81 | **40** |
| Canvas & Stage (나머지) | 131 | **69** |

> 'Canvas & Stage' = Stage GNB / Connect↔Preview 전환 / Canvas / 레이어 속성 다이얼로그 / Backstage / Nav Menu.
> ('나머지' 대신 붙인 이름. Left/Right Panel과 나란히 두면 "패널 vs 캔버스"로 직관적)

## 4. TestRail Suite 구성 (이미 생성 완료)

6개 Suite로 분리:
- `[Cloud] Connect Home` (54 Case)
- `[Cloud] Connect Mode > Left Panel` (65)
- `[Cloud] Connect Mode > Right Panel` (40)
- `[Cloud] Connect Mode > Canvas & Stage` (69)
- `[Cloud] Preview Mode` (70)
- `[Cloud] Share & Run` (38)

> 분업 팁: 가장 작은 **Right Panel(40)** 을 느린 PC 동료에게.

## 5. 변환 규칙 (확정)

### 계층
| Notion | → TestRail |
|---|---|
| `### 메뉴` | Suite (CSV 미포함, 파일/Run 단위로 분리) |
| `📍 Edit Role: X` | 최상위 Section "Edit Role: X" (다음 Edit Role 전까지 그 아래 전부 소속) |
| `<summary>` 토글 | Section (중첩 토글 = 중첩 Section, 경로는 " > "로 연결) |
| 상위 `- ` 불릿 | **Case (Title)** |
| 하위 `- ` 불릿 | 그 Case **본문(Steps)** 에 들여쓰기 유지 불릿 리스트 |

- **Case 단위**: 상위 불릿(가장 얕은 들여쓰기) = Case. 자식 불릿은 본문으로.
- **Case 템플릿**: `Test Case (Text)` — 자식은 Steps 필드에 "- " 불릿 리스트.
- Title 정리: `\[`→`[`, `\]`→`]`, `\>`→`>`, 양끝 공백·끝 쉼표/콜론 정리.

### 우선순위 (Priority) — 키워드 자동 초안 + 사람 검수
- 케이스의 (제목 + 모든 자식) 텍스트로 판정, 매칭 중 **가장 높은 등급** 채택, 무매칭 = **P2**.
- 매핑: **P1→High, P2→Medium, P3→Low** (TestRail 네이티브 Priority, 3단계).

| 등급 | 키워드/패턴 |
|---|---|
| **P1** | 접근/진입(접근되는지, role·Editor 유지 이동), 생성, 이동(~로 이동/화면 이동), 성공(요청 성공·성공 토스트·정상동작), 로드(list 로드), 권한 미노출(Viewer 권한 검증) |
| **P3** | 경계값(긴 경우, N개 초과, 30개, 최대 길이, ~개씩 추가), 비주얼(깨짐, 말줄임표, 탭 길이, 썸네일 비율/레이어 케이스), 허용(중복 허용), 디자인 일치(UI가 다음과 같음, 디자인) |
| **P2** | 그 외(Cancel/Dismiss/뒤로가기, 정상 표시·이름 일치·날짜규칙, 노출/미노출 조건) + 무매칭 기본값 |

### 라벨 (Labels)
- 케이스 제목/본문 어디든 **"TBD" 포함 시 `TBD` 라벨**. (우선순위는 키워드대로 별도 판정)
- TestRail **Labels는 8.0+ 만 지원**. 미지원 시 import 후 일괄 라벨 or custom 필드. (버전 확인 필요)
- (제목 prefix 아님 — 네이티브 라벨 기능 사용)

### 이미지 / 링크
- **Figma 링크(19개)**: 안 만료 → 케이스 본문/References에 텍스트 링크로 포함.
- **S3 스크린샷(80개)**: Notion S3 URL은 **`X-Amz-Expires=3600` = 1시간 만료**.
  → URL 임베드 불가. **다운로드 후 TestRail에 첨부**(자체 호스팅되어 영구 보존).
  - ⏰ **실행 당일 순서**: ①Notion 페이지 재fetch(신선한 URL) → ②즉시 80개 다운로드 → ③CSV 생성 + API로 케이스에 첨부. (CSV import는 첨부 불가, 첨부는 별도 단계)
- **이미지 첨부 위치 규칙**:
  - 특정 동작 토글 안 이미지(예: `Rename 클릭 시 다이얼로그 오픈`+img) → **그 케이스에 첨부**
  - 섹션 단위 `디자인` 참고 토글 이미지 → **그 섹션 첫 케이스 본문**에 첨부
  - 본문(Steps)에 인라인 임베드 (Text 템플릿)
- 디자인 전용 토글: 제외 안 함 (위 규칙대로 이미지 첨부에 사용).

### 제외 대상
- (없음 — 이미지/디자인 토글/TBD 모두 포함하기로 결정)
- 본문에서 단순 이미지 줄(`![]()`) 텍스트만 제거, 이미지는 첨부로 대체.

## 6. CSV 컬럼 스펙

UTF-8 (BOM 권장, 엑셀 한글). 컬럼:
`Section`(" > " 계층) / `Title` / `Priority`(High·Medium·Low) / `Labels`(TBD 등) / `Steps`(자식 불릿 리스트)

검증: 변환 후 Case 수를 위 기준치(섹션별 상위불릿 수)와 대조해 누락 확인.

## 7. 재사용 변환 프롬프트

```
[TestRail 변환 프롬프트 — Notion CheckList → TestRail CSV]

■ 입력: Notion "v2 Connect Cloud" 문서에서 한 메뉴(### ~ 다음 ### 전까지) 블록.
■ 출력: TestRail import용 CSV (UTF-8 BOM). 컬럼 = Section, Title, Priority, Labels, Steps.
   Case Template = "Test Case (Text)".

■ 계층 규칙
 1) `### 메뉴`        → Suite (CSV 미포함, 파일/Run 단위로 분리)
 2) `📍 Edit Role: X` → 최상위 Section "Edit Role: X". 다음 Edit Role 줄 전까지 그 아래 전부 소속.
 3) `<summary>...</summary>` 토글 → Section. 중첩 토글 = 중첩 Section. 경로 " > " 연결.
 4) 디자인 전용/이미지 토글도 Section 처리하되, 이미지는 아래 규칙으로 첨부.

■ Case 규칙 (상위 불릿 = Case)
 5) 한 Section에 직접 속한 불릿 중 "가장 얕은 들여쓰기" 불릿 = Case.
 6) 더 깊은 자식 불릿 = 그 Case의 Steps에 들여쓰기 유지 "- " 불릿 리스트로.
 7) Title = 상위 불릿 텍스트. 정리: \[→[, \]→], \>→>, 양끝 공백·끝 쉼표/콜론 정리.

■ 우선순위 (Priority) — 키워드 자동 판정(초안), 케이스의 (제목+모든 자식) 대상, 매칭 중 최고 등급, 무매칭=P2.
    · P1: 접근/진입, 생성, 이동, 성공(요청 성공·성공 토스트·정상동작), 로드, 권한 미노출(Viewer 권한 검증)
    · P3: 경계값(긴 경우·N개 초과·최대 길이·~개씩·30개), 비주얼(깨짐·말줄임표·탭 길이·썸네일), 허용(중복), 디자인 일치(UI가 다음과 같음·디자인)
    · P2: 그 외 + 무매칭
    · 매핑: P1→High, P2→Medium, P3→Low
    · 자동 판정은 초안 → 사람이 검수·수정.

■ 라벨: 제목/본문에 "TBD" 포함 시 Labels에 TBD. (TestRail 8.0+ 필요)

■ 이미지/링크
    · Figma 링크 → 본문에 텍스트 링크 포함.
    · S3 이미지 → 실행 당일 재fetch 후 1시간 내 다운로드 → 케이스에 첨부(인라인).
      특정 동작 토글 이미지=그 케이스, 섹션 디자인 참고 이미지=섹션 첫 케이스.

■ 검증: 변환 후 Case 수를 상위 불릿 수와 대조.
   기준치 — Connect Home 54 / Connect Mode 174(Left65·Right40·Canvas&Stage69) / Preview 70 / Share&Run 38, 합계 336.
```

## 8. 다음 액션

1. **시작 신호** 대기 → Connect Home(54 Case + 이미지 14개)부터 trial.
2. trial 시 **Notion 재fetch부터** 시작(이미지 만료 때문).
3. 변환 결과 같이 검수 → 규칙 미세조정 → 나머지 5개 Suite 진행.

## 9. 미해결 / 확인 필요
- TestRail 버전이 Labels(8.0+) 지원하는지 확인.
- 이미지 첨부 위치 규칙 최종 확인(섹션 첫 케이스 vs 별도 참고 케이스).
- CSV의 Section 계층 구분자(" > ")를 TestRail import 마법사에서 인식하도록 설정.
