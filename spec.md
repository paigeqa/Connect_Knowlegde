---
doc_id: CC-SPEC
title: Cloud Connect — SSOT에 없는 스펙
purpose: SSOT가 다루지 않는 제품 동작을 기록한다. 체크리스트 작성·버그 티켓 작성의 참조점.
maintainer: Paige (QA)
ssot: https://ssot.protopie.works/ko/connect/
extracted_from: Cloud_Connect_Spec.md rev16 (2026-06-12)
ssot_reviewed: 2026-08-17 (changelog 2026-07-27 ~ 08-13, 68개 항목)
last_updated: 2026-08-17
---

# Cloud Connect — SSOT에 없는 스펙

**스펙의 기준은 SSOT다.** → https://ssot.protopie.works/ko/connect/

이 문서는 SSOT가 다루지 않는 것만 담는다. 내용이 겹치면 **SSOT가 정답**이다.

| 담는 것 | 안 담는 것 (→ SSOT 보기) |
|---|---|
| 권한 모델 (Team / Edit / Stage Role) | 기능 동작 설명 |
| 미결 질문 | 아키텍처·데이터 모델 |
| 레거시 Connect와 다른 점 (Δ) | 용어 정의 |
| 에러 목록 | 플랫폼별 지원 여부 |
| Bridge ↔ Server REST API | 변경 이력 (→ SSOT `changelog`) |

> ⚠️ **공백 구간 있음.** SSOT changelog는 2026-07-27부터 시작한다. **2026-06-12 ~ 07-27 사이 6주의 변경은 changelog에 없다.** 이 구간에서 온 변경이 아직 안 잡혔을 수 있다.

"상태" 컬럼은 **스펙이 확정됐는지**를 뜻한다.

- `확정` — 결정된 사양
- `미결` — 아직 안 정해짐. §4와 연결
- `폐기` — 예전엔 이랬는데 지금은 아님. 케이스가 있으면 삭제 대상

---

## 0. 지금 무엇을 제공하고 있나 (2026-08-17)

여기가 다른 모든 판단의 전제다.

| | 현재 | 정식 출시 |
|---|---|---|
| **배포 형태** | **Enterprise만** — 기업이 서버를 사고, 그 안에 CoC를 영업팀을 통해 추가 구매 | Self-serve(유저가 플랜을 사서 쓰는 클라우드) + Enterprise **둘 다 제공 검토 중** |
| **등급 게이팅** | **없음.** Enterprise 서버가 CoC를 쓰면 기능 제한 없이 다 된다 | 미정 |
| **유일한 게이트** | **Edit Role ≥ Editor** | 미정 |

**정식 출시 플랜 정책은 2026년 10월에 정해진다.** 그때까지는 등급·플랜 기반 테스트를 하지 않는다.

2026-08-13에 코드에서 등급 게이팅이 전부 제거됐다.
> "Connect 등급 이용 자격이 사라졌다. none/core/enterprise 게이팅 축과 17행 이용 자격 표, 등급 기반 집행 지점을 모두 걷어냈다"
> `features.ts:6` · `feature-limits.ts:1` · `participant-cap.ts:1,26`

대신 들어온 것: **라이브 참가자 상한 = min(운영 실링, 호스트가 정한 max members).** 실링 기본 200, 배포별 조정 가능.

---

## 1. 권한 모델

권한은 **세 축**으로 나뉜다. 세 축은 서로 독립이라 한 사람이 같은 Team에서 `Team Member + Edit Role Editor + Stage A owner + Stage B viewer` 같은 조합을 가질 수 있다.

| 축 | 무엇에 대한 권한 | 누가 정답을 갖고 있나 |
|---|---|---|
| **Team Role** | 팀 자체의 관리 | ProtoPie Cloud |
| **Edit Role** | Cloud 콘텐츠 전반 (프로젝트·파이·라이브러리) | ProtoPie Cloud |
| **Stage Role** | Connect의 Stage 단위 | Connect |

### Team Role (3종)

| Role | 권한 |
|---|---|
| Owner | 팀의 주인. 팀 관리·팀원 관리 가능 |
| Admin | 팀 관리·팀원 관리 가능 (Owner와 동등 관리 권한) |
| Member | 초대된 멤버. 팀 관리 권한 없음 |

### Edit Role (3종, UT 권한 모델 기반)

| Role | 권한 |
|---|---|
| Moderator | Editor의 모든 권한 + User Testing 기능 사용 가능 |
| Editor | 프로젝트·파이·라이브러리 관리 가능. Studio·Connect에 Cloud 계정 인증으로 접근 가능 |
| Viewer | 프로젝트·파이·라이브러리 **조회만** 가능 |

### Stage Role (3종)

| Role | 권한 | 어떻게 부여되나 |
|---|---|---|
| owner | Stage 생성·삭제·멤버 관리 | **Stage를 만든 사용자 1인.** Stage 단위 unique. Team Owner라고 자동 부여되지 않는다 |
| editor | Stage 안의 Pie·Group·Plugin 편집 | **같은 Team에서 Cloud Edit Role이 Editor 이상(Editor·Moderator)인 모든 유저에게 자동 부여.** 별도 추가 액션 불필요. Edit Role 강등 시 즉시 박탈 |
| viewer | Stage 안 자원 조회만 (기본 View Mode) | **공유 링크(토큰)로 진입한 게스트.** Cloud 계정 불필요 |

### 🔴 여기가 제일 자주 틀리는 지점

**Stage editor 멤버를 하나하나 부여하는 UI는 없다.**

- 같은 Team에서 누군가의 Cloud Edit Role이 Editor로 승격되면 → 그 사람은 그 Team의 **모든 Stage에 editor 권한이 자동으로 생긴다**
- 반대로 Edit Role이 Viewer로 강등되면 → Connect 진입 자격 자체가 사라져서 Stage 진입이 차단된다

레거시 Connect는 멤버를 명시적으로 관리하는 모델이었다. 여기가 뒤집혔다 (→ §5 Δ-04).

### Connect 사용 자격

**현재는 조건이 하나다 — Edit Role ≥ Editor.**

Plan·등급 조건은 없다 (→ §0). 자격을 통과한 뒤, 각 Stage 안에서의 동작은 Stage Role이 추가로 게이트한다.

### View Mode / Interaction Mode / Participant

| 용어 | 뜻 |
|---|---|
| **View Mode** | Viewer가 Stage에 진입했을 때의 **기본 상태**. Pie 시청만 가능. 메시지 전송·인터랙션 차단. Node View 편집·Console 로그·Player 연결·하드웨어 등 모든 편집 액션 불가 |
| **Interaction Mode** | Viewer가 화면 안의 **개인 토글**로 전환한 상태. Pie 실행·메시지 전송 허용. 단 Stage 편집·구조 변경은 어느 상태에서도 불가. **권한 전환이 아니라 mode 전환** — Role은 viewer로 유지 |
| **Participant** | Interaction Mode 토글이 ON인 Viewer를 가리키는 **호칭**. 레거시의 "Guest/Participant"가 mode로 흡수된 것 |

토글 자체는 구현 확인됨 — SSOT `45-workspace`: "View / Interact 모드는 서로 오갈 수 있다"

### 레거시 명칭 → CoC 명칭 매핑

레거시 카피가 UI에 남아 있는지 검출할 때 쓴다.

| 레거시 | CoC |
|---|---|
| Host | **Editor** (Stage 생성자·편집자에 흡수). 단 SSOT는 "현재 Session의 host"라는 뜻으로도 쓴다 — 문맥 주의 |
| Editor | Editor |
| Participant (Guest) | **Viewer + Interaction Mode ON** (토글로 흡수) |
| Viewer | Viewer (기본 View Mode). SSOT 표기는 **guest** = 공유 링크로 들어온 사람 |

Guest ↔ Viewer는 Role 전환이 아니라 **mode 전환**이다.

---

## 2. 인증·권한 기능 (F-IDM)

| ID | 상태 | 요구사항 | 확인 포인트 |
|---|---|---|---|
| F-IDM-team-root | 확정 | Team이 결제·격리·UI 노출의 root | Team 간 자원 누출 0건 |
| F-IDM-device-2tier | 확정 | Team → Device 2계층. User identity는 Cloud가 정답 | JWT에 Team role이 들어가지 않는다 |
| F-IDM-nm-team | 확정 | 한 사용자가 여러 Team에 동시 소속 | Team 전환 시 컨텍스트가 완전히 분리된다 |
| F-IDM-persisted-auth | 확정 | 인증 상태는 DB/Redis에 영속 저장 | 서버 재시작 후에도 로그인 상태 유지 |
| F-IDM-device-token | 확정 | Device 단위 토큰 발급·revoke | 분실 신고된 Device만 차단되고 사용자 전체가 차단되지 않는다 |
| F-IDM-cookie-jwt | 확정 | Connect 주소 접속 시 Cloud와 동일한 로그인 확인 로직. Cookie는 항상 발급되고 JWT로 판별. 실패 시 로그인 페이지로 리다이렉트 → Cloud 로그인 후 Connect로 재리다이렉트 | Cookie 미발급·JWT 만료·서명 위변조 시 모두 차단되는지 |
| F-IDM-license-then-cloud | 확정 | 라이센스 로그인 상태에서 Cloud 로그인을 추가하면 화면이 즉시 Cloud 모드 범위로 확장. Cloud 로그아웃 시 라이센스 모드 복귀, 키 값은 로컬 보존 | 모드 업그레이드/다운그레이드가 즉시 반영되는지. SSOT: License 사용자는 계정 메뉴에서 `/login` 게이트를 열고 **Back to Connect**로 복귀 (`AccountMenu.tsx:123`) |
| F-IDM-team-role-cloud-sot | 확정 | Team Role 3종 enum만 spec. 권한 매트릭스 detail은 Cloud team-management API가 정답 | Cloud API 응답이 바뀌면 Connect 권한 판정이 따라가는지 |
| F-IDM-edit-role | 확정 | Edit Role 3종 enum. UT 권한 모델 기반. **Connect 사용 자격 = Editor 이상** | Editor 미만(Viewer) 계정이 Connect 진입·편집을 시도하면 차단 |
| F-IDM-connect-entitlement | 확정 (2026-08-17 정정) | Connect 사용 자격은 **Edit Role ≥ Editor 하나뿐이다.** Plan·등급 조건 없음 (→ §0) | Edit Role 강등 시 즉시 차단되는지. **등급으로 차단되는 지점이 남아 있지 않은지 negative test** |
| F-IDM-perm-ut-base | 확정 | 대부분의 권한은 UT 권한 모델 기반. Edit Role이 UT enum과 동일 | UT 권한 정책이 바뀌면 Connect에 영향이 있는지 추적 |
| F-IDM-login-entrypoint | 확정 (범위 축소) | **현재는 Enterprise 진입만 제공** — 전용 서버 주소 입력 필요. Self-serve 진입("Log in")은 정식 출시 정책 확정(2026-10) 후 | Enterprise 진입이 서버 주소 입력 화면으로 이동. 잘못된 주소·도달 불가·인증서 오류 시 명확한 에러 카피 |
| F-IDM-host-approval | 확정 (2026-08-17 신설) | **로컬 네트워크 기기는 호스트 승인으로 접근한다.** 페어링 안 된 브라우저가 호스트에 접근을 요청하고, 호스트가 승인하면 접근 권한을 얻는다. 거부 가능. 무응답 시 **2분 후 만료**. IP당 **분당 최대 3개** 요청. 호스트가 페어링된 기기를 제거하면 기존 자격 증명 무효화 | 승인·거부·타임아웃 3경로. 분당 4번째 요청 차단. 제거 후 기존 링크로 재접근 시도 차단. 근거: `pairing.ts:130,236,245` · `DevicePairingManager.ts:45,118,145,324` |
| F-IDM-pin-24h | **폐기** | ~~PIN + 24시간 토큰 인증~~ → **없어졌다.** 지금은 로그인 아니면 토큰 링크뿐 | **PIN 입력 관련 케이스는 삭제.** 단 SSOT 내부에 상충 표기 있음 → Q-15 |
| F-IDM-pin-method | **폐기** | ~~게스트 진입은 PIN 방식. 호스트 승인은 추후 검토~~ → **뒤집혔다.** 호스트 승인이 실제로 구현됨 (F-IDM-host-approval) | 위와 같음 |
| F-IDM-plan-feature-matrix | **폐기** | ~~Custom Plugin Import = Enterprise 구독 한정~~ → 2026-08-13 제거. "Connect Enterprise 사용자 외에도 커스텀 플러그인을 사용할 수 있다" (`plugins.ts:79` · `features.ts:53`) | **Enterprise 전용 여부 케이스 삭제.** +버튼 비노출 케이스도 삭제 |
| F-IDM-upsell-modal | **폐기** | ~~Plan 한도 초과 시 공통 Upsell Modal 3 액션~~ → 등급 게이팅 제거로 트리거 자체가 없어짐 | **Upsell Modal 케이스 전부 삭제** (레거시 S280에 21개 지점) |
| F-IDM-team-switch-ux | 미결 | Team 전환 UI 패턴(모달/토스트/인라인) 미결정 → Q-8 | 결정 후 케이스 정의 |
| F-IDM-cross-team-pie | 미결 | Cloud Pie 라이브러리의 cross-team 접근 정책 미결정. **레거시는** Edit Role Viewer로 보이는 다른 Team의 Pie도 Connect에 업로드 가능했다. "Team 간 자원 누출 0건"과 충돌해서 명문화 필요 → Q-7 | 결정 후: ① Cloud Pie 모달이 cross-team 폴더를 노출하는지 ② Edit Role Viewer 자격으로 import 시도 시 허용/거부 ③ import된 Pie의 team_id 귀속 ④ Team 격리 정합성 |

**확인 우선순위**
1. 토큰 lifecycle (만료·revoke)
2. License → Cloud 로그인 전환 시 capability 즉시 반영
3. Cookie/JWT 위변조 차단
4. **호스트 승인 페어링 우회** (신규)

**인증 상태 조합**: (License 유무) × (Cloud 로그인 유무) = 조합을 명시적으로 케이스화하면 누락을 막을 수 있다. Cloud entitlement 축은 등급 게이팅 제거로 사라졌다.

---

## 3. Viewer 권한 (F-VWR)

기능 동작 자체는 SSOT [`46-share`](https://ssot.protopie.works/ko/connect/46-share) · [`45-workspace`](https://ssot.protopie.works/ko/connect/45-workspace)를 본다. 여기는 **권한·모드 부분만** 담는다.

| ID | 상태 | 요구사항 | 확인 포인트 |
|---|---|---|---|
| F-VWR-readonly | 확정 | Viewer 기본 상태는 **View Mode = 시청 전용.** Pie 실행·메시지 전송 불가. 단 Interaction Mode 토글 ON 시는 예외. Stage 편집·구조 변경은 어느 모드에서도 불가 | View Mode 기본 진입 시 인터랙션 거부, 메시지 전송 차단. 토글 ON 시 즉시 허용으로 전환. Node View 편집·Console 로그·Player 연결·하드웨어 액션은 어느 모드에서도 차단. SSOT: 레이어 재생 버튼은 "호스트/Editor 전용"으로 숨김 |
| F-VWR-interaction-toggle | 확정 (부분) | Viewer는 화면 내 **개인 토글로 View Mode ↔ Interaction Mode 전환** 가능. Role 전환이 아니라 mode 전환이며 Stage Role은 viewer 유지. 같은 Pie에서 다수 Viewer가 동시에 켤 수 있다. **토글 존재는 구현 확인됨** | ① 전환 시 즉시 인터랙션 가능/차단 ② Stage 편집 액션은 두 모드 모두 차단 ③ 남은 미결: Q-5(Editor가 잠글 수 있나), Q-9(새로고침 후 보존), Q-1(Editor 알림), Q-2(동시 충돌) |
| F-VWR-acl-mapping | 확정 | 레거시 → CoC 명칭 매핑을 이 문서의 정답으로 둔다 (→ §1 매핑 표) | 레거시 카피("Host", "Guest", "Participant")가 UI에 남아 있지 않은지 검출. **주의: SSOT는 "host"를 현재 Session의 호스트라는 뜻으로 쓴다** — 레거시 잔재가 아님 |
| F-VWR-nodeview-access | 미결 | **Node View(Backstage) 접근 경로 규칙.** Viewer는 URL 직접 공유만 가능, 확인은 되고 편집은 불가. Player/Stage 화면 안에서 진입 경로 없음. **단 Backstage 구조가 바뀌었다** — SSOT: Backstage에는 host와 Plugin 노드만 나타나고 Player App·Bridge 노드는 숨긴다 (`BackstageCanvas.tsx:216`) → 질문 재작성 필요 (Q-4) | 바뀐 Backstage 기준으로 Viewer 접근 경로를 다시 확인해야 함 |
| F-VWR-editor-notify | 미결 | Viewer가 Interaction Mode ON 시 **Editor에게 알림이 가는가** (Q-1). SSOT에 없음 | 알림 있으면: Editor 화면에 Viewer 상태 변경 표시. 없으면 변경 없음 |
| F-VWR-link-expiry | **확정** (2026-08-17 해결) | **토큰은 만료되지 않는다. Stage마다 토큰 하나.** 토큰으로 들어오면 6시간 동안 따로 인증할 필요 없음. revoke 수단 = **공유 링크 재설정**(host 동작, 발급된 링크 전부 무효화 + 새 링크 발급). 토큰 교환에 **IP당 분당 5회 + 단계적 백오프** rate limit | ① 오래된 토큰으로 진입 성공 (만료 없음) ② 6시간 경과 후 재인증 요구되는지 ③ 재설정 후 옛 링크 전부 차단 ④ 분당 6번째 교환 차단 + 재시도 화면. 근거: SSOT `46-share`, `41-cloud`, `stage.ts:786-900,842-870` |
| F-VWR-interaction-isolation | 미결 | **다수 Viewer가 동시에 Interaction Mode일 때 상태 격리.** 각자 개별 instance를 가지며, 한 Viewer의 인터랙션으로 생긴 화면·변수 상태가 다른 Viewer에게 실시간 동기화되지 않는 것이 현재 합의된 기본값. 예외: Pie 추가/삭제 같은 Stage 구성 변경은 브로드캐스트될 수 있음 (Q-2) | Viewer A의 인터랙션 결과가 Viewer B에게 미반영됨을 확인. Stage 구성 변경은 전체 반영되는지 확인 |
| F-VWR-auth-policy | **확정** (2026-08-17 해결) | 시청자 인증 = **로그인 아니면 토큰 링크.** PIN·Passcode 방식은 폐기. 익명 게스트에는 제한이 걸릴 수 있다 | 무효 토큰의 화면이 표면마다 다른지 — cloud 익명은 **로그인 게이트**, 로그인된 비멤버·local 전체는 **no access** 화면 (`StageGateScreen.tsx` · `StageJoinClient.tsx`) |
| F-VWR-player-participant | 확정 | **Player가 시청자가 아니라 참여자로 진입하는 경우.** Stage View 안의 각 Pie를 Player에서 열면 그 Pie 1개를 실행하며 같은 Stage 컨텍스트의 메시지를 양방향 송수신한다. F-VWR-readonly와 다르다. 테스트 제외 항목 "Stage view from the Player"와도 **별개 개념** | 데스크탑 브라우저 + 실제 모바일·태블릿 여러 대가 같은 Stage View 안의 Pie를 각자 실행하면서 메시지를 주고받는지. **주의: QR 진입은 현재 미구현** (→ §5 Δ-18) |

---

## 4. 미결 질문

> 2026-08-17에 SSOT 1단계 대조를 한 결과다. 해결된 것은 §2·§3 본문에 반영했고, 여기엔 남은 것만 둔다.

| ID | 질문 | 관련 | 다음 단계 |
|---|---|---|---|
| **Q-13** | **Wear OS·음성 프로토타이핑·Player IP(9981) 연결이 지금 범위인가** | qa-guide P1 | 2단계 → 3단계. SSOT 4개 페이지에서 못 찾음 (`42-desktop`·`44-core-features`·`45-workspace`·`47-layers-plugins`) |
| **Q-15** | **PIN이 완전히 폐기됐나** | F-IDM-pin-24h | 2단계. **SSOT 안에서 상충** — `46-share`는 "PIN 없앴다", `40-product-overview`(08-06)는 "PIN으로 입장한 게스트"를 접근 권한 구분에 포함 |
| **Q-16** | **REST API 엔드포인트가 아직 있나** (`/api/pies` `/api/groups` `/api/players`) | §7 전체 | 2단계. SSOT에 API 페이지가 없음. 없어졌으면 §7과 관련 케이스 전부 삭제 |
| Q-14 | 커스텀 폰트·메시지 Recording·Embedded의 **등급 제한이 남아 있나** | qa-guide P1 | 2단계. 등급 축은 사라졌는데 이 기능들은 Enterprise 전용이었음 |
| Q-4 | Node View(Backstage) URL을 Viewer가 열 때 인증을 요구하나 | F-VWR-nodeview-access | 2단계. **Backstage 구조가 바뀌어 질문 재작성 필요** |
| Q-5 | Editor가 Viewer의 Interaction Mode 토글을 잠글 수 있나 | F-VWR-interaction-toggle | 2단계 |
| Q-9 | 토글 상태가 새로고침·재진입 후 보존되나 | F-VWR-interaction-toggle | 2단계 |
| Q-1 | Viewer가 Interaction ON 시 Editor에게 알림이 가나 | F-VWR-editor-notify | 2단계 |
| Q-2 | 다수 Participant 동시 인터랙션 충돌 처리 | F-VWR-interaction-isolation | 2단계 |
| Q-7 | Cloud Pie cross-team 접근 정책 | F-IDM-cross-team-pie | 3단계 (정책 결정) |
| Q-8 | Team 전환 UI 패턴 | F-IDM-team-switch-ux | 2단계 |
| Q-11 | Record 중 Load 동시 호출 정책 | Console | 2단계 |

### 해결된 질문 (기록)

| ID | 질문 | 답 |
|---|---|---|
| **Q-12** | 등급 게이팅 제거가 영구인가 | **현재는 Enterprise만 제공하므로 등급 매트릭스가 없다.** Enterprise 서버가 CoC를 쓰면 다 되고, Edit Role Editor 이상만 게이트한다. 정식에는 Self-serve + Enterprise 둘 다 제공할 수도 있으나 **2026년 10월에 정해진다.** → S280 폐기 결정 (2026-08-17 Paige) |
| **Q-3** | Viewer 공유 링크 만료 정책 | **토큰 무기한, Stage당 1개, 진입 후 6시간 재인증 면제.** revoke = 링크 재설정 → F-VWR-link-expiry |
| **Q-6** | Plan 다운그레이드 시 플러그인 처리 | **질문 소멸.** 등급 게이팅 제거 |
| **Q-10** | 시청자 인증 정책 | **로그인 아니면 토큰 링크** → F-VWR-auth-policy |

### 확정되면 뭘 하나

1단계(SSOT)에서 답이 나오면 → 해당 항목을 `미결` → `확정`으로 바꾸고 요구사항을 채운다.
안 나오면 → 2단계(코드 확인) → 3단계(개발자 리뷰 요청).

---

## 5. 레거시 Connect와 다른 점 (Δ)

**레거시 Connect를 써온 사람이 헷갈리는 지점.** 옛 케이스를 변환할 때 이 표를 먼저 본다 — "이 케이스가 거부로 뒤집혔나, 그대로인가"를 판단해서 변환 누락을 막는 게 목적이다.

읽는 법: **CoC 컬럼이 정답.** 레거시 컬럼은 회귀 베이스라인.

| ID | 항목 | 레거시 | CoC | 회귀 변환 |
|---|---|---|---|---|
| Δ-01 | Pie ↔ Group 관계 | Pie는 root 또는 Group 둘 중 하나 | **모든 Pie는 Group 종속** (root 직속 금지) | root 관련 정상 케이스는 ID 보존하고 expected를 "거부"로 뒤집기 |
| Δ-02 | Stage 명칭 | Room | **Stage** (Room은 UI 노출 금지) | "Room" 카피 잔존 검출 케이스 추가 |
| Δ-03 | Tenant 용어 | v0.7.0 이전 사용 | **UI 노출 금지** | "Tenant" 카피 잔존 검출 케이스 추가 |
| Δ-04 | 권한 모델 | Stage role 단일축 (명시적 멤버 부여) | **3축** (Team + Edit + Stage Role). Stage editor는 Cloud Edit Role ≥ Editor 유저에게 **자동 부여** | 권한 케이스에 3축 조합 매트릭스 적용. **"Stage editor 멤버 추가 UI"가 없는지 negative test.** Edit Role 승격·강등 시 모든 Stage에 즉시 반영되는 케이스 신규 |
| Δ-05 | 배포 형태 | 단일 배포 | **현재는 Enterprise만** (기업 서버 + CoC 추가 구매). Self-serve는 정식 정책 확정(2026-10) 후 검토 | Self-serve 관련 케이스는 **보류.** 판단 근거를 남길 것 |
| Δ-06 | Multi-view Group | 별도 그룹 모델 | **Stage View가 동등 이상으로 흡수** | 레거시 multi-view 케이스 → Stage View 케이스로 ID 매핑 |
| Δ-07 | 인증 영속성 | 메모리 only | **DB/Redis 영속** (서버 재시작 후에도 로그인 유지) | 서버 재시작 시나리오 신규 |
| Δ-08 | License 5분 무료 | 5분 무료 후 만료 | **정책 폐기.** 라이센스 키 단독 모드로 통일 | "5분 만료" 케이스 삭제 |
| Δ-09 | Studio 의존성 | Studio 설치 필수 | **의존성 없음.** 미설치 시 자동 다운로드 페이지로 이동 | "Studio 미설치 거부" 케이스 → "자동 다운로드" 케이스로 변환 |
| Δ-10 | 등급·플랜 게이팅 | 등급별로 기능·수량 제한 (플러그인 동시 1개·3분, 워터마크 등) | **없음.** 2026-08-13에 게이팅 축·17행 이용 자격 표·집행 지점을 코드에서 전부 제거. 남은 제한은 **참가자 상한**(min(운영 실링, host의 max members), 기본 200) 하나 | **등급 매트릭스 케이스 전부 폐기**(S280 309건). Upsell Modal 케이스 폐기. 참가자 상한 케이스 신규 |
| Δ-11 | Custom Bridge SDK | 공식 공개 검토 이력 | **비공개.** 패키징 절차만 노출 | SDK 문서 케이스 삭제, 패키징 케이스 유지 |
| Δ-12 | Stageview 시청 모델 | 모든 Pie 강제 시청 | **시청자가 Pie 선택 가능** | 선택 UX 신규 케이스 추가 |
| Δ-13 | Cloud Stage 생성 모드 | 단일 진입 (데스크탑 한정) | **Cloud Web과 Desktop Cloud-login 두 모드 모두에서 생성 가능** | 데스크탑에서 Cloud Stage 생성 진입점 노출 회귀 추가. cross-mode 확인 |
| Δ-14 | Private Stage 정책 | Cloud Stage = Private/Shared 구분 + 가입 시 "내 작업실" 자동 생성 | **범위 제외.** 단일 공유 모델 | 레거시 Private 케이스 → "거부 또는 옵션 부재"로 전환 |
| Δ-15 | Stageview 행위자 모델 | Host / Editor / Participant(Guest) / Viewer **4종 Role** | **2-Role(Editor/Viewer) + 개인 토글**(View ↔ Interaction). Participant = 토글 ON 상태의 호칭 | "Host"·"Guest"·"Participant" 카피 잔존 검출. **단 SSOT는 "host"를 Session 호스트 뜻으로 쓴다** — 오검출 주의 |
| Δ-16 | Stage 파일 저장·이동 | 없음 | **Local Stage를 `.stage` 파일로 내보내고 가져온다** (Desktop·Embedded). 번들 내용 = Stage 그래프·로컬 Pie 파일·Unity 파일·글꼴·사용자 지정 Plugin 패키지. rev16에 적었던 "Handoff to local / Upload to Cloud"와는 **이름·동작이 다르다** — Cloud↔Local 양방향 복제가 아니라 로컬 파일 입출력 | 내보내기·가져오기 정상 케이스 + **거부 5종**(미지원·손상·불완전·이전 버전·이후 버전 번들) + 진행 중 취소 |
| Δ-17 | 게스트 인증 방식 | **PIN·Passcode 입력** | **폐기.** 로그인 아니면 **토큰 링크**. 로컬 기기는 **호스트 승인 페어링**(2분 만료, IP당 분당 3개) | **PIN 입력 케이스 전부 삭제.** 호스트 승인 승인·거부·타임아웃 케이스 신규. Q-15 확인 후 확정 |
| Δ-18 | QR 진입 | QR 코드로 Player 연결·시청 진입 | **현재 미구현.** "지금 공유 수단은 링크뿐이다. QR 코드는 아직 만들지 않았다"(`46-share`). 단 `45-workspace`에 Player 연결 "QR • USB (Desktop app 전용)" 표기가 있어 **범위 확인 필요** | QR 케이스는 **보류**(삭제 아님). Q-13과 함께 확인 |
| Δ-19 | 프리셋 플러그인 구성 | 7종 (API·IFTTT·Arduino·Blokdots·Gamepad·G29·Unity) | **5종** — API, G29, Arduino, Gamepad, **MQTT Broker**. IFTTT·Blokdots는 `scopeout`. Unity는 플러그인이 아님(Δ-20) | IFTTT·Blokdots 케이스 → 제외 범위로 이동. MQTT Broker 케이스 신규 |
| Δ-20 | Unity 통신 경로 | Unity **플러그인**을 통해 통신 | **별도 플러그인 없이 Unity 레이어에서 직접** Send/Receive (`features.ts:53` · `MultiStageCanvas.tsx:595`) | "Unity 플러그인 실행" 케이스 → "Unity 레이어 통신" 케이스로 변환 |
| Δ-21 | 메시지 목록 컬럼 | **5컬럼** (Time·Message·Value·**Pie**·Source) | **4컬럼** — Message는 항상 표시, Time·Value·Source는 헤더 우클릭으로 토글. **Pie 컬럼 없음.** 모든 컬럼 드래그 리사이즈, 남는 너비를 채우는 건 하나뿐 | "Pie 컬럼" 검증 케이스 삭제. 컬럼 표시/숨김 토글 케이스 신규 |
| Δ-22 | Stage View URL 파라미터 | `fullscreen`·bg·hotspotHints·cursorHide·scaleToFit | **`pieid`·`stageid`·`group`**·bg·hotspotHints·cursorHide·scaleToFit. **`fullscreen` 없어짐** | `fullscreen` 케이스 삭제. `pieid`·`stageid`·`group` 케이스 신규 |
| Δ-23 | 플러그인 동시 실행 | Stage 여러 곳에서 동시 실행 가능 | **Stage 간 배타.** 한 Stage에서 Plugin을 시작하면 다른 Stage의 실행 중 Plugin을 중지. Stage를 나가면 그 Stage의 Plugin 중지 (`ipc-handlers.ts:277,605`) | 두 Stage를 오가며 배타 동작 확인 케이스 신규 |

**운영 규칙**
- 레거시와 동작이 갈리는 게 새로 확인되면 **Δ-NN 한 행을 추가**한다.
- "회귀 변환" 컬럼은 케이스 변환 작업의 체크리스트로 쓴다.
- 아직 결정이 안 된 충돌은 행으로 만들지 않고 §4 미결 질문에 둔다.

---

## 6. 에러 목록 (S-ERR)

| 코드 | 상황 | 사용자 화면 | 시스템 동작 | 복구 |
|---|---|---|---|---|
| E-AUTH-1 | ProtoPie Cloud 로그인 실패 | "로그인 실패. 다시 시도" 모달 | Bridge 시작 화면 유지 | 사용자 재시도 |
| E-AUTH-2 | Device 토큰 만료 | "세션이 만료되었습니다. 다시 로그인" | 자동 로그아웃 + 로그인 화면 | 재로그인 |
| E-AUTH-3 | Device 토큰 차단 (분실 신고 등) | "이 디바이스는 차단되었습니다" | Bridge 잠금 | 관리자가 차단 해제 |
| E-NET-1 | Cloud 연결 끊김 | "Cloud 연결 끊김. 재연결 시도 중…" 토스트 | 자동 재연결 (지수 백오프) | 네트워크 복구 |
| E-NET-2 | Relay 방 연결 끊김 | "방에서 끊어졌습니다. 재입장" | 5초 후 자동 재입장 시도 | 자동 또는 수동 |
| E-DEV-1 | Device 등록 실패 (네트워크·시계 오차) | "디바이스 등록 실패: [이유]" + 재시도 | 등록 화면 유지 | 사용자 재시도 |
| E-PLG-1 | 플러그인 실행 크래시 | 카드에 빨간색 + "재시작" | 자동 1회 재시작, 실패 시 정지 | 사용자 재시작 또는 코드 수정 |
| E-PLG-2 | manifest 잘못됨 (Import 시) | "플러그인 형식 오류: [상세]" | Import 거부 | 사용자가 패키지 수정 후 재업로드 |
| E-USB-1 | USB 디바이스 권한 없음 (macOS) | "Arduino 사용 권한 필요" + 시스템 설정 deep-link | 디바이스 미인식 유지 | 사용자가 권한 부여 |
| E-RELAY-1 | Relay 방 만료·종료 | "이 방은 종료되었습니다" + 새 방 생성 | 방 목록으로 복귀 | 새 방 생성 |
| E-OS-1 | macOS Gatekeeper / Windows SmartScreen 경고 | OS 기본 경고 화면 | (Bridge가 직접 안내 불가) | OS 신뢰 후 재실행 또는 코드 서명 정상화 |
| E-MSG-CHANNEL-MISMATCH | Pie의 send/receive 채널이 양측 불일치 | (레거시 무음. Beta에서 Console 경고 표시 검토) | 메시지 silent drop | 사용자가 채널을 일치시킴 |
| E-PLG-BAUD-MISMATCH | Arduino 플러그인 baud rate와 보드 코드 baud rate 불일치 | 메시지 미수신, 에러 미표시 | 시리얼 통신 무응답 | 사용자가 baud rate 일치. **프리셋 8종에서 선택, 기본값 9600.** Run 중에는 Port·Baud rate 변경 불가 (`ArduinoSettingsForm.tsx:19,61`) |
| E-PLG-PORT-BUSY | Arduino IDE 또는 다른 앱이 시리얼 포트 점유 | 플러그인 실행 실패 또는 무응답 | 포트 open 실패 | 점유 앱 종료 후 플러그인 재실행 |
| E-BRG-API-AUTH | Custom Bridge App이 외부 API 인증 실패 | 앱 stdout에 에러, Connect 메시지 로그는 무음 | 앱 종료 또는 idle | 사용자가 토큰 갱신 후 재시작 |
| E-PLG-MSG-FLOOD | 다중 컴포넌트 인스턴스의 연속 send로 메시지 폭주 | (현재 무음) | 메시지 큐 적체·Relay 부하 | rate limit 트리거 후 dispatch 제한 |
| **E-STG-BUNDLE-REJECT** | `.stage` 번들이 미지원·손상·불완전·이전 버전·이후 버전 | (거부 안내) | Local Stage 생성 안 함 | 올바른 번들로 재시도. `stage-export-import.ts:523` · `stage-bundle-io.ts:416,589` |
| **E-EMB-LICENSE** | Embedded 라이선스가 없음·읽기 불가·형식 오류·만료·호스트 불일치 | (터미널 출력) | **Connect Embedded가 시작하지 않음** | 유효한 라이선스 배치. `FileLicenseAdapter.ts:87` · `auth.ts:163` |
| **E-WEB-INVALID-LINK** | Web embed URL이 안전하지 않음·자기 참조·연결 불가·프레이밍 거부 | "**Invalid link**" 알림 | 레이어 로드 차단 | 사용자가 URL 수정. `webViewUrl.ts:47,72,91` · `WebViewLayerView.tsx:102` |
| **E-PLG-NOT-AVAILABLE** | 커스텀 플러그인이 이 기기에 설치되지 않음 | Plugins 목록에서 제외 + Backstage 노드에 "**Plugin not available**" | 연결은 유지한 채 오류 표시. Cloud Stage·owner 세션 없는 게스트·목록 로딩 중/실패 시에는 **판정 보류** | 해당 기기에 플러그인 설치. `useStagePlugins.ts:90` · `BackstagePluginNode.tsx:413` · `useMissingCustomPlugins.ts:55,71` |
| **E-SHARE-THROTTLE** | 공유 토큰 교환이 IP당 분당 5회 초과 | "**Can't connect to this stage**" 재시도 화면 | 단계적 백오프. **일시적 5xx·네트워크 오류도 같은 화면** | 잠시 후 재시도. `StageJoinClient.tsx:299` |
| **E-SHARE-NO-ACCESS** | 무효 토큰 | **표면마다 다름** — cloud 익명은 로그인 게이트, 로그인된 비멤버·local 전체는 no access 화면 | 진입 차단 | 유효한 링크 또는 로그인. `StageGateScreen.tsx` · `StageJoinClient.tsx` |
| **E-SESSION-EXPIRED** | Session 만료 | "Session expired" 화면 + Log in | Log in은 **토큰을 보존한 채** 같은 join 링크로 복귀. login gate의 Log in은 **죽은 토큰만 제거**하고 나머지 URL 파라미터 보존 | 재로그인. `StageJoinClient.tsx:290,320` |
| **E-PAIR-REJECT** | 로컬 기기 페어링 요청이 거부·타임아웃 | (요청 측에 실패 표시) | 무응답 시 **2분 후 만료.** IP당 분당 3개 초과 요청 거부 | 호스트에게 재요청. `DevicePairingManager.ts:45,118,324` |

**삭제된 에러** (등급 게이팅 제거로 발생하지 않음): `E-ENT-1`(Entitlement 만료 차단), `E-ENT-2`(Entitlement 검증 불가 grace), `E-PAY-1`(결제 가시성 지연), `E-TEAM-1`(사용 가능 Team 없음).

---

## 7. Bridge ↔ Server REST API (F-API)

> ⚠️ **Q-16 — 이 API가 아직 있는지 확인되지 않았다.** SSOT에 API 페이지가 없다. 2단계(코드 확인)에서 없어진 것으로 나오면 이 섹션과 관련 케이스를 전부 삭제한다. 그때까지 옛 케이스(S503) 참조용으로 남긴다.

모든 엔드포인트는 인증 실패·권한 부족·잘못된 ID 입력 시 **명확한 4xx 응답**을 반환해야 한다.

| ID | 엔드포인트 | 요구사항 | 확인 포인트 | 옛 케이스 |
|---|---|---|---|---|
| F-API-pies | `GET /api/pies` | Pie List 조회 | 빈 리스트 시 200 + `[]`. 존재 시 권한 필터링된 목록만 | C127794~795 |
| F-API-pies-upload | `POST /api/pies/upload` | Local Pie 업로드. 인증 필수 | Connect 미로그인·종료 상태에서 차단. 잘못된 파일 거부 | C127808~811 |
| F-API-pies-uploadCloud | `POST /api/pies/uploadCloud` | Cloud Pie 업로드. Cloud login + Pie/Project 권한 필요. **~~Pro plan 실패~~ 조건은 등급 게이팅 제거로 무효** | Cloud 미로그인 / Connect 미로그인 / Pie 권한 없음 / Project 권한 없음 / Pie id 불일치 | C127800~807 (Pro plan 케이스 삭제) |
| F-API-pies-delete | `POST /api/pies/delete` | 1개·다수 Pie 삭제. 잘못된 ID 혼합 시 부분 실패 정책 | 정상 1건, 다중 삭제, 무효 ID 단독·혼합 | C127796~799 |
| F-API-groups | `GET /api/groups`<br>`POST /api/groups/add`<br>`POST /api/groups/remove` | Group 조회·생성·삭제. Group 1 level 강제 | 빈/존재 조회. add 후 정렬 유지. remove 시 cascade. 무효 ID 단독·혼합 | C127785~788<br>C127791~793 |
| F-API-groups-updatePie | `POST /api/groups/updatePie` | Pie를 **Group ↔ Group 이동 한정.** root를 source/target으로 지정한 요청은 거부 | 정상 1패턴 + **root 지정 요청 400 거부** + 무효 Pie ID·무효 Group ID·group_id 누락 | C127777~784 |
| F-API-players | `GET /api/players` | Player 연결 정보 조회 | 빈 상태 200 + 빈 목록. 연결 상태 목록 정확성 | C127775~776 |
| F-API-players-run | `POST /api/players/run` | 특정 Player에서 Pie 실행 | 정상 실행, 중복 실행, 미연결 에러 | C127770~772<br>C127789~790 |
| F-API-players-runAll | `POST /api/players/runAll` | 전체 연결 Player 일괄 실행 | 전체 실행 정확성. Player 0개일 때 에러 | C127773~774 |
| F-API-players-loadPie | `POST /api/players/loadPie` | 특정 Player에 특정 Pie 로드 | 정상·실패 케이스 | C127768~769 |
| F-API-auth-uniform | (공통) | 모든 API의 **인증·권한 실패 응답 카피·코드 일관.** Connect 미로그인 / Cloud 미로그인 / 권한 없음 / 무효 ID 4 카테고리 | 카피 일관성. HTTP status 일관(401/403/404 구분). 거부 응답이 §6과 매핑되는지 | — |

**확인 우선순위**
1. 권한 우회를 차단하는 인증·권한 응답 일관성 (P0)
2. Pie/Group 이동·삭제 시 cascade + "모든 Pie는 Group 종속" 강제 (P1)
3. 잘못된 ID 혼합 시 부분 실패 정책 명문화
