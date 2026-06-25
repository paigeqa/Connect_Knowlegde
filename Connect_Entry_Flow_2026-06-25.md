# Connect v3 진입/인증 플로우 매핑

Share 링크로 진입할 때 로그인·팀·토큰·세션 상태에 따라 어느 화면으로 가는지 매핑한다. 범위는 Enterprise 플랜. 확인 체크리스트는 TestRail suite 1366 `Share flow 확인`(C218114~C218134)에 반영 완료.

> 작성일: 2026-06-25 · 출처: Figma Connect v3 다이어그램 (node-id 2898-218090)
> https://www.figma.com/design/A9BgGUCeTzAzYg9ghokqz1/Connect-v3?node-id=2898-218090

## 핵심 개념
- 토큰 valid = 링크 만든 지 5분 이하.
- 세션 alive = 에디터가 1명이라도 Stage를 열어둠.
- 우리 팀(Team Y)은 토큰 유효성을 안 본다 (멤버는 토큰 무관).
- Passcode 입력 통과 시 항상 Viewer – Preview mode로 간다.
- 푸터(계정 정보)는 `Logged in?` 값으로만 갈린다.
  - logged-out → "You are currently logged out. / Log in >"
  - logged-in → "You are currently logged in as: {email} / Log in using a different account >"

## 결정 노드 (다이어그램 다이아몬드)
- `Logged in? (Stage와 같은 tenant)`
- `Team member?`
- `Editor?`
- `URL includes valid token?` (valid = 5분 이하)
- `Session alive?`

## 범위
Enterprise 플랜만. Basic/Pro 화면은 제외. Login 폼은 상단 요요 화면(Enterprise)만 사용.

## 화면(프레임) 목록
| 화면 | Figma Frame | 비고 |
|---|---|---|
| Editor – Connect mode | (Editor) | 편집 가능 |
| Viewer – Stage Preview mode | (Viewer) | 보기/인터랙션만 |
| Log in or Passcode (선택 화면) | Frame 2085662519 | `Log in` 또는 `Passcode` 선택. logged-out 전용 |
| Passcode 입력 (logged-out) | Frame 2085662524 | 푸터: logged out |
| Passcode 입력 (logged-in) | Frame 2085662520 | 푸터: logged in as {email} |
| Login 폼 (Enterprise) | Login (상단 요요 화면) | `Log in` 클릭 시 |
| Session expired (logged-out) | Frame 2085662522 | `Go to Cloud` / 푸터 logged out |
| Session expired (logged-in) | Frame 2085662523 | `Go to Cloud` / 푸터 logged in |

---

## 확인 체크리스트 (Enterprise 기준)

진입/인증 경로 3그룹: A = 로그인 안 함 / B = 로그인·우리 팀(토큰 무관) / C = 로그인·타 팀.

| # | Logged in? | Team? | Editor? | Token valid (≤5분) | Session alive | 기대 화면 | ✓ |
|---|---|---|---|---|---|---|---|
| A-1 | N | – | – | valid | – | Viewer – Preview | ☐ |
| A-2 | N | – | – | invalid | alive | Log in or Passcode [519] → `Passcode` → Passcode 입력(logged-out)[524] → Viewer Preview | ☐ |
| A-3 | N | – | – | invalid | dead | Session expired (logged-out) [522] | ☐ |
| A-4 | N | – | – | invalid | alive | Log in or Passcode [519] → `Log in` → Login 폼(Enterprise 요요) | ☐ |
| B-1 | Y | Y | Y | (안 봄) | – | Editor – Connect mode (바로 접근) | ☐ |
| B-2 | Y | Y | N | (안 봄) | alive | Viewer – Preview | ☐ |
| B-3 | Y | Y | N | (안 봄) | dead | Session expired (logged-in) [523] | ☐ |
| C-1 | Y | N | – | valid | – | Viewer – Preview | ☐ |
| C-2 | Y | N | – | invalid | alive | Passcode 입력(logged-in)[520] → Viewer Preview | ☐ |
| C-3 | Y | N | – | invalid | dead | Session expired (logged-in) [523] | ☐ |

### 기준 정의
| # | 확인 포인트 | ✓ |
|---|---|---|
| D-1 | Token valid 기준 = 링크 생성 후 5분 이하 경계값 (4:59 vs 5:01) | ☐ |
| D-2 | Session alive 기준 = 에디터 1명 이상 Stage 열어둠 | ☐ |

### 세션 동작
| # | 확인 포인트 | ✓ |
|---|---|---|
| S-1 | 여러 사용자가 동일한 Share Token으로 입장할 수 있음 | ☐ |
| S-2 | Editor가 있는 한 세션은 종료되지 않음 (2시간 켜놓아보기) | ☐ |
| S-3 | Editor가 있는 상태로 Viewer가 새로고침해도 접속 유지됨 | ☐ |
| S-4 | Editor가 나가면 60초 후 세션 종료됨 | ☐ |
| S-5 | Editor가 세션 만료였던 방에 들어오면 방이 다시 열림. 단, Viewer는 자동 재입장 안 되고 Passcode 또는 Share URL로 재인증 필요 | ☐ |

