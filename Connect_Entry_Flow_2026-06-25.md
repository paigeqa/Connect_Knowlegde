# Connect v3 진입/인증 플로우 매핑

> 작성일: 2026-06-25
> 출처: Figma Connect v3 다이어그램 (node-id 2898-218090)
> https://www.figma.com/design/A9BgGUCeTzAzYg9ghokqz1/Connect-v3?node-id=2898-218090

## 핵심 개념
- **토큰 valid** = 링크 만든 지 **5분 이하** (`valid token: 만든지 5분 이하`)
- **세션 alive** = **에디터가 1명이라도 Stage를 열어둠**
- **우리 팀(Team Y)** = **토큰 유효성 안 봄** (멤버는 토큰 무관)
- 푸터(계정 정보) 변형: `Logged in?` 값으로만 갈림
  - logged-out → "You are currently logged out. / Log in >"
  - logged-in → "You are currently logged in as: {email} / Log in using a different account >"
- **PIN 입력 통과 = 항상 Viewer – Preview mode**

## 결정 노드 (다이어그램 다이아몬드)
- `Logged in? (Stage와 같은 tenant)`
- `Team member?`
- `Editor?`
- `URL includes valid token?` (valid = 5분 이하)
- `Session alive?`

## 화면(프레임) 목록
| 화면 | Figma Frame | 비고 |
|---|---|---|
| Editor – Connect mode | (Editor) | 편집 가능 |
| Viewer – Stage Preview mode | (Viewer) | 보기/인터랙션만 |
| Login or PIN (선택 화면) | Enterprise / Frame 2085662519 | `Log in` 또는 `Enter Passcode` 선택. logged-out 전용 |
| PIN 입력 (logged-out) | Frame 2085662524 | 푸터: logged out |
| PIN 입력 (logged-in) | Frame 2085662520 | 푸터: logged in as {email} |
| Session expired (logged-out) | Frame 2085662522 | `Go to Cloud` / 푸터 logged out |
| Session expired (logged-in) | Frame 2085662523 | `Go to Cloud` / 푸터 logged in |

> 이번 작업 범위: **Enterprise 플랜만**. Basic/Pro 화면, Login 폼 화면(클릭 시 공통 노출)은 무시.

---

## 전체 leaf 경로 매핑

### A. 로그인 안 함 (Logged N)
| 조건 | 화면 |
|---|---|
| 토큰 **valid** | **Viewer – Stage Preview mode** |
| 토큰 invalid · 세션 **alive** | **Login or PIN [519]** → `Enter Passcode` → **PIN(logged-out) [524]** → **Viewer Preview** |
| 토큰 invalid · 세션 **dead** | **Session expired (logged-out) [522]** |

### B. 로그인 함 · 우리 팀 (Team Y) — *토큰 유효성 안 봄*
| 조건 | 화면 |
|---|---|
| **Editor** | **Editor – Connect mode** (바로 접근) |
| Viewer · 세션 **alive** (에디터 1명+ 존재) | **Viewer – Stage Preview mode** |
| Viewer · 세션 **dead** | **Session expired (logged-in) [523]** |

### C. 로그인 함 · 우리 팀 아님 (Team N)
| 조건 | 화면 |
|---|---|
| 토큰 **valid** | **Viewer – Stage Preview mode** |
| 토큰 invalid · 세션 **alive** | **PIN(logged-in) [520]** → **Viewer Preview** |
| 토큰 invalid · 세션 **dead** | **Session expired (logged-in) [523]** |

---

## 남은 작업 (집에서 이어서)
- [ ] `Cloud_Connect_Spec.md`에 진입/인증 플로우 섹션으로 반영할지 결정
- [ ] TestRail 케이스용 시나리오 표로 변환할지 결정
- [ ] Basic/Pro 플랜 화면 매핑 (이번엔 제외함)
- [ ] Login 폼 화면 흐름 (이번엔 제외함)
