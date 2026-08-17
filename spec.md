---
doc_id: CC-SPEC
title: Cloud Connect — SSOT에 없는 스펙
purpose: SSOT가 다루지 않는 제품 동작을 기록한다. 체크리스트 작성·버그 티켓 작성의 참조점.
maintainer: Paige (QA)
ssot: https://ssot.protopie.works/ko/connect/
extracted_from: Cloud_Connect_Spec.md rev16 (2026-06-12)
last_updated: 2026-08-17
---

# Cloud Connect — SSOT에 없는 스펙

**스펙의 기준은 SSOT다.** → https://ssot.protopie.works/ko/connect/

이 문서는 SSOT가 다루지 않는 것만 담는다. 내용이 겹치면 **SSOT가 정답**이다.

| 담는 것 | 안 담는 것 (→ SSOT 보기) |
|---|---|
| 권한 모델 3축 (Team / Edit / Stage Role) | 기능 동작 설명 |
| 미결 질문 (ACL Q-1~Q-5 등) | 아키텍처·데이터 모델 |
| 레거시 Connect와 다른 점 | 용어 정의 |
| 에러 목록 | 플랫폼별 지원 여부 (Capability Matrix) |
| Bridge ↔ Server REST API | 변경 이력 (→ SSOT `changelog`) |

> ⚠️ **이 문서는 2026-06-12(rev16) 시점 내용이다.** 베타 출시(2026-06-30) 이후의 변경은 아직 반영되지 않았다. SSOT changelog로 대조하는 작업이 남아 있다.

"상태" 컬럼은 **스펙이 확정됐는지**를 뜻한다.

- `확정` — 결정된 사양
- `미결` — 아직 안 정해짐. §4 미결 질문과 연결
- `범위 외` — Beta 범위 아님

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
| viewer | Stage 안 자원 조회만 (기본 View Mode) | **외부 게스트가 ViewerInvite 토큰(URL·QR·PIN)으로 진입한 상태.** Cloud 계정 불필요 |

### 🔴 여기가 제일 자주 틀리는 지점

**Stage editor 멤버를 하나하나 부여하는 UI는 없다.**

- 같은 Team에서 누군가의 Cloud Edit Role이 Editor로 승격되면 → 그 사람은 그 Team의 **모든 Stage에 editor 권한이 자동으로 생긴다**
- 반대로 Edit Role이 Viewer로 강등되면 → Connect 진입 자격 자체가 사라져서 Stage 진입이 차단된다

레거시 Connect는 멤버를 명시적으로 관리하는 모델이었다. 여기가 뒤집혔다 (→ §5 Δ-04).

### Connect 사용 자격

| 배포 형태 | 조건 |
|---|---|
| **Self-serve** (`.io` 공유 클라우드) | Team Plan이 Connect 사용 가능 Plan **AND** Edit Role ≥ Editor |
| **Enterprise** (전용 서버) | Edit Role ≥ Editor (Plan gate 없음) |

이 자격을 통과한 뒤, 각 Stage 안에서의 동작은 Stage Role이 추가로 게이트한다.

### View Mode / Interaction Mode / Participant

| 용어 | 뜻 |
|---|---|
| **View Mode** | Viewer가 Stage에 진입했을 때의 **기본 상태**. Pie 시청만 가능. 메시지 전송·인터랙션 차단. Node View 편집·Console 로그·Player 연결·하드웨어 등 모든 편집 액션 불가 |
| **Interaction Mode** | Viewer가 화면 안의 **개인 토글**로 전환한 상태. Pie 실행·메시지 전송 허용. 단 Stage 편집·구조 변경은 어느 상태에서도 불가. **권한 전환이 아니라 mode 전환** — Role은 viewer로 유지 |
| **Participant** | Interaction Mode 토글이 ON인 Viewer를 가리키는 **호칭**. 레거시의 "Guest/Participant"가 mode로 흡수된 것 |

### 레거시 명칭 → CoC 명칭 매핑

레거시 카피가 UI에 남아 있는지 검출할 때 쓴다.

| 레거시 | CoC |
|---|---|
| Host | **Editor** (Stage 생성자·편집자에 흡수) |
| Editor | Editor |
| Participant (Guest) | **Viewer + Interaction Mode ON** (토글로 흡수) |
| Viewer | Viewer (기본 View Mode) |

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
| F-IDM-pin-24h | 확정 | PIN + 24시간 토큰 인증 (레거시 동등, 저장소만 영속화) | 토큰 만료 후 자동 로그아웃 |
| F-IDM-pin-method | 확정 | 게스트 진입은 PIN 방식. 호스트 승인(30초 제한, UT 방식)도 검토했으나 PIN 유지 | Unity 등 typing 불가 환경의 UX 이슈는 알려진 한계로 인지 |
| F-IDM-cookie-jwt | 확정 | Connect 주소 접속 시 Cloud와 동일한 로그인 확인 로직. Cookie는 항상 발급되고 JWT로 판별. 실패 시 로그인 페이지로 리다이렉트 → Cloud 로그인 후 Connect로 재리다이렉트 | Cookie 미발급·JWT 만료·서명 위변조 시 모두 차단되는지 |
| F-IDM-license-then-cloud | 확정 | 라이센스 로그인 상태에서 Cloud 로그인을 추가하면 화면이 즉시 Cloud 모드 범위로 확장. Cloud 로그아웃 시 라이센스 모드 복귀, 키 값은 로컬 보존 | 모드 업그레이드/다운그레이드가 즉시 반영되는지 |
| F-IDM-login-entrypoint | 확정 | 로그인 진입점 두 갈래. (a) **Log in** = Self-serve (`.io`). (b) **Log in with Secure Enterprise** = Enterprise, 전용 서버 주소 입력 필요. 레거시 v2.10.2 패턴 유지 | Enterprise 버튼이 서버 주소 입력 화면으로 이동. 잘못된 주소·도달 불가·인증서 오류 시 명확한 에러 카피. Self-serve 자격으로 Enterprise 주소 로그인 시도 시 거부 (반대도 동일) |
| F-IDM-team-role-cloud-sot | 확정 | Team Role 3종 enum만 spec. 권한 매트릭스 detail은 Cloud team-management API가 정답 | Cloud API 응답이 바뀌면 Connect 권한 판정이 따라가는지 |
| F-IDM-edit-role | 확정 | Edit Role 3종 enum. UT 권한 모델 기반. Connect 사용 자격은 Editor 이상 | Editor 미만(Viewer) 계정이 Connect 진입·편집을 시도하면 차단 |
| F-IDM-connect-entitlement | 확정 | Connect 사용 자격 = Self-serve: 사용 가능 Plan AND Edit Role ≥ Editor / Enterprise: Edit Role ≥ Editor | Self-serve의 Plan 다운그레이드, Enterprise의 Edit Role 강등 시 즉시 차단되는지 |
| F-IDM-perm-ut-base | 확정 | 대부분의 권한은 UT 권한 모델 기반. Edit Role이 UT enum과 동일 | UT 권한 정책이 바뀌면 Connect에 영향이 있는지 추적 |
| F-IDM-plan-feature-matrix | 확정 | Connect 진입 자격 통과 후, **Custom Plugin Import(+버튼)는 Enterprise 구독에서만 동작.** Pro 구독은 +버튼 자체가 비노출 (레거시 동등) | Pro 구독자에게 +버튼 비노출 (P0). Enterprise 구독자가 import 가능. Plan 다운그레이드 시 기존 import 플러그인 처리 정책 → **미결** (Q-6) |
| F-IDM-upsell-modal | 확정 | Plan 한도 초과·비가용 기능 트리거 시 뜨는 **공통 Upsell Modal.** 3 액션 = (a) [X] 닫기, (b) [Upgrade] → `https://checkout.protopie.io/{unique url}`, (c) [Chat with us] → `https://www.protopie.io/form/request-demo`. Enterprise 비가용 기능(Custom Plugin·Wear OS·Custom Font·Unity)은 별도 Enterprise variant (타이틀 문구만 다름) | Free·Core 양쪽 모든 한도 트리거 지점에서 동일 modal (레거시 S280에 21개 지점 케이스화됨). 3 버튼 URL·닫기 동작·외부 링크 새 탭 여부. 다운그레이드 직후 기존 자원 접근 시 modal 일관성 |
| F-IDM-team-switch-ux | 미결 | Team 전환 UI 패턴(모달/토스트/인라인) 미결정 | 결정 후 케이스 정의 |
| F-IDM-cross-team-pie | 미결 | Cloud Pie 라이브러리의 cross-team 접근 정책 미결정. **레거시는** Enterprise·Self-serve 둘 다 Edit Role Viewer로 보이는 다른 Team의 Pie도 Connect에 업로드 가능했다. CoC는 "Team 간 자원 누출 0건"과 충돌해서 명문화 필요 → Q-7 | 결정 후: ① Cloud Pie 모달이 cross-team 폴더를 노출하는지 ② Edit Role Viewer 자격으로 import 시도 시 허용/거부 ③ import된 Pie의 team_id 귀속 (원본 Team vs 현재 Team) ④ PieVersion에 source_team_id 메타 보존 여부 ⑤ Team 격리 정합성 |

**확인 우선순위**
1. 토큰 lifecycle (만료·revoke·24h grace)
2. License → Cloud 로그인 전환 시 capability 즉시 반영
3. Cookie/JWT 위변조 차단
4. 결제 → Bridge 가시성 지연 (폴링 15초)

**인증 상태 조합**: (License 유무) × (Cloud 로그인 유무) × (Cloud entitlement 유효성) = 8개 조합. 명시적으로 케이스화하면 누락을 막을 수 있다.

---

## 3. Viewer 권한 (F-VWR)

기능 동작 자체는 SSOT `46-share`를 본다. 여기는 **권한·모드 부분만** 담는다.

| ID | 상태 | 요구사항 | 확인 포인트 |
|---|---|---|---|
| F-VWR-readonly | 확정 | Viewer 기본 상태는 **View Mode = 시청 전용.** Pie 실행·메시지 전송 불가. 단 Interaction Mode 토글 ON 시는 예외. Stage 편집·구조 변경은 어느 모드에서도 불가 | View Mode 기본 진입 시 인터랙션 거부, 메시지 전송 차단. 토글 ON 시 즉시 인터랙션 허용으로 전환. Node View 편집·Console 로그·Player QR/USB 연결·하드웨어 액션은 어느 모드에서도 차단 |
| F-VWR-interaction-toggle | 미결 | Viewer는 화면 내 **개인 토글로 View Mode ↔ Interaction Mode 전환** 가능. Role 전환이 아니라 mode 전환이며 Stage Role은 viewer 유지. 같은 Pie에서 다수 Viewer가 동시에 Interaction Mode를 켤 수 있다 | ① View↔Interaction 전환 시 즉시 인터랙션 가능/차단 ② Stage 편집 액션은 두 모드 모두 차단 ③ 토글 상태가 새로고침·재진입 시 보존되는지 **미결** ④ 관련 미결: Q-1, Q-2, Q-5 |
| F-VWR-acl-mapping | 확정 | 레거시 → CoC 명칭 매핑을 이 문서의 정답으로 둔다 (→ §1 매핑 표) | 레거시 카피("Host", "Guest", "Participant")가 UI에 남아 있지 않은지 검출. §5 Δ-15와 1:1 |
| F-VWR-nodeview-access | 미결 | **Node View 접근 경로 규칙.** Editor: URL로 접근·편집 가능. 단 Player를 통해서는 접근 불가 — **Player 내 Editor도 차단인지 TBD**. Viewer: URL 직접 공유만 가능, 확인은 되고 편집은 불가. Viewer는 Player/Stage 화면 안에서 진입 경로 없음 | Editor: Stage 내 접근 가능, Player 탭 내 진입 불가. Viewer: URL로만 접근, Stage/Player 화면 내 직접 진입 차단. 인증 정책(Q-4) 확정 후 보안 케이스 추가 |
| F-VWR-editor-notify | 미결 | Viewer가 Interaction Mode ON 시 **Editor에게 알림이 가는가** (Q-1) | 알림 있으면: Editor 화면에 Viewer 상태 변경 표시. 없으면 변경 없음 |
| F-VWR-link-expiry | 미결 | Viewer 공유 링크(URL/QR/PIN) **만료 정책.** 시간 제한 vs 무기한 (Q-3) | 시간 제한이면: 만료 후 접근 차단 + 에러 처리. 무기한이면: 링크 revoke 수단 확인 |
| F-VWR-interaction-isolation | 미결 | **다수 Viewer가 동시에 Interaction Mode일 때 상태 격리.** 같은 Stage를 열어도 각자 개별 instance를 가지며, 한 Viewer의 인터랙션으로 생긴 화면·변수 상태가 다른 Viewer에게 실시간 동기화되지 않는 것이 현재 합의된 기본값. 예외: Pie 추가/삭제 같은 Stage 구성 변경은 브로드캐스트될 수 있음 | Viewer A의 인터랙션 결과가 Viewer B에게 미반영됨을 확인. Stage 구성 변경은 전체 반영되는지 확인 |
| F-VWR-auth-policy | 미결 | 시청자 인증 정책 (공개 URL vs Team 한정 vs 토큰 게스트) | 결정 후 케이스화 |
| F-VWR-player-participant | 확정 | **Player가 시청자(viewer)가 아니라 참여자(participant)로 진입하는 경우.** Stage View 안의 각 Pie는 QR 코드를 노출하고, Player 앱에서 QR을 스캔하면 그 Pie 1개를 실행하며 같은 Stage 컨텍스트의 메시지를 양방향 송수신한다. F-VWR-readonly(외부 게스트 시청 전용)와 다르다. 테스트 제외 항목인 "Stage view from the Player"(Player에서 Stage 화면 자체를 보는 것)와도 **별개 개념** | 데스크탑 브라우저 + 실제 모바일·태블릿 여러 대가 같은 Stage View 안의 Pie를 각자 실행하면서 메시지를 주고받는지. Player 측 send가 다른 디바이스로 전파되는지 |

---

## 4. 미결 질문

**출처: ACL 문서 §6 (2026-06-01 갱신본) + spec rev16 시점 미결 항목**

> ⚠️ 이 목록은 2026-06-12 기준이다. 베타가 나왔으니 **코드나 SSOT에 답이 이미 있을 수 있다.** 새 QA 프로세스(1→2→3단계)로 하나씩 확인해야 한다.

| ID | 질문 | 관련 | 1단계 확인처 (SSOT) |
|---|---|---|---|
| Q-1 | Viewer가 Interaction Mode를 켰을 때 Editor에게 알림이 필요한가 | F-VWR-editor-notify, F-VWR-interaction-toggle | `46-share` |
| Q-2 | 같은 Pie에 여러 Participant가 동시 인터랙션할 때 충돌을 어떻게 처리하나 | F-VWR-interaction-toggle, E-PLG-MSG-FLOOD | `46-share`, `44-core-features` |
| Q-3 | Viewer 공유 링크 만료 정책 — 시간 제한 vs 무기한 | F-VWR-link-expiry | `46-share` |
| Q-4 | Node View URL을 Viewer가 열 때 인증을 요구하나 (무인증 허용 vs PIN 게이트) | F-VWR-nodeview-access | `46-share`, `49-backstage` |
| Q-5 | Editor가 Viewer의 Interaction Mode 토글을 잠글 수 있나 | F-VWR-interaction-toggle | `46-share` |
| Q-6 | Plan 다운그레이드 시 이미 import한 Custom Plugin을 어떻게 처리하나 (즉시 비활성 vs 유예) | F-IDM-plan-feature-matrix | `47-layers-plugins`, `30-bm-pricing` |
| Q-7 | Cloud Pie 라이브러리 cross-team 접근 정책 (3안 중 선택) | F-IDM-cross-team-pie | `44-core-features` |
| Q-8 | Team 전환 UI 패턴 | F-IDM-team-switch-ux | `45-workspace` |
| Q-9 | Interaction Mode 토글 상태가 새로고침·재진입 후 보존되나 | F-VWR-interaction-toggle | `46-share` |
| Q-10 | 시청자 인증 정책 (공개 URL vs Team 한정 vs 토큰 게스트) | F-VWR-auth-policy | `46-share` |
| Q-11 | Record 중에 Import를 동시 호출하면 어떻게 되나 | F-AUD-record-ui-sequence | `48-console` |

### 확정되면 뭘 하나

1단계에서 답이 나오면 → 이 문서의 해당 항목을 `미결` → `확정`으로 바꾸고 요구사항을 채운다.
1단계에서 안 나오면 → 2단계(코드 확인) → 3단계(개발자 리뷰 요청).

---

## 5. 레거시 Connect와 다른 점 (Δ)

**레거시 Connect를 써온 사람이 헷갈리는 지점.** 옛 케이스(S280·S503)를 변환할 때 이 표를 먼저 본다 — "이 케이스가 거부로 뒤집혔나, 그대로인가"를 판단해서 변환 누락을 막는 게 목적이다.

읽는 법: **CoC 컬럼이 정답.** 레거시 컬럼은 회귀 베이스라인.

| ID | 항목 | 레거시 | CoC | 회귀 변환 |
|---|---|---|---|---|
| Δ-01 | Pie ↔ Group 관계 | Pie는 root 또는 Group 둘 중 하나 | **모든 Pie는 Group 종속** (root 직속 금지) | root 관련 정상 케이스는 ID 보존하고 expected를 "거부"로 뒤집기 |
| Δ-02 | Stage 명칭 | Room | **Stage** (Room은 UI 노출 금지) | "Room" 카피 잔존 검출 케이스 추가 |
| Δ-03 | Tenant 용어 | v0.7.0 이전 사용 | **UI 노출 금지** | "Tenant" 카피 잔존 검출 케이스 추가 |
| Δ-04 | 권한 모델 | Stage role 단일축 (명시적 멤버 부여) | **3축** (Team + Edit + Stage Role). Stage editor는 Cloud Edit Role ≥ Editor 유저에게 **자동 부여** | 권한 케이스에 3축 조합 매트릭스 적용. **"Stage editor 멤버 추가 UI"가 없는지 negative test 추가.** Edit Role 승격·강등 시 모든 Stage에 즉시 반영되는 케이스 신규 |
| Δ-05 | 배포 형태 | 단일 배포 | **듀얼** — Self-serve(`.io`, Plan gate) / Enterprise(전용 서버, Editor 이상) | 모든 entitlement 케이스에 배포 차원 분리 |
| Δ-06 | Multi-view Group | 별도 그룹 모델 | **Stage View가 동등 이상으로 흡수** | 레거시 multi-view 케이스 → Stage View 케이스로 ID 매핑 |
| Δ-07 | 인증 영속성 | 메모리 only | **DB/Redis 영속** (서버 재시작 후에도 로그인 유지) | 서버 재시작 시나리오 신규 |
| Δ-08 | License 5분 무료 | 5분 무료 후 만료 | **정책 폐기.** 라이센스 키 단독 모드로 통일 | "5분 만료" 케이스 삭제 |
| Δ-09 | Studio 의존성 | Studio 설치 필수 | **의존성 없음.** 미설치 시 자동 다운로드 페이지로 이동 | "Studio 미설치 거부" 케이스 → "자동 다운로드" 케이스로 변환 |
| Δ-10 | Plan 정량 한도 | 비명문화 또는 등급 2종 | **3등급**(Free/Core/Enterprise) × 영역별 정량 매트릭스 명문화 | S280 6등급 표기 → 3등급으로 재맵핑. 공통 Upsell Modal 회귀 추가 |
| Δ-11 | Custom Bridge SDK | 공식 공개 검토 이력 | **비공개.** 패키징 절차만 노출 | SDK 문서 케이스 삭제, 패키징 케이스 유지 |
| Δ-12 | Stageview 시청 모델 | 모든 Pie 강제 시청 | **시청자가 Pie 선택 가능** | 선택 UX 신규 케이스 추가 |
| Δ-13 | Cloud Stage 생성 모드 | 단일 진입 (데스크탑 한정) | **Cloud Web과 Desktop Cloud-login 두 모드 모두에서 생성 가능** | 데스크탑에서 Cloud Stage 생성 진입점 노출 회귀 추가. 생성 후 Cloud Web에서 같은 Stage 확인 (cross-mode) |
| Δ-14 | Private Stage 정책 | Cloud Stage = Private/Shared 구분 + 가입 시 "내 작업실" 자동 생성 | **Beta 범위에서 Private/Shared 구분 제외, 자동 생성 제외.** 단일 공유 모델 | 레거시 Private 케이스 → "거부 또는 옵션 부재"로 전환. 가입 직후 빈 상태 가이드 UX 회귀 신규 |
| Δ-15 | Stageview 행위자 모델 | Host / Editor / Participant(Guest) / Viewer **4종 Role** | **2-Role(Editor/Viewer) + 개인 토글**(View Mode ↔ Interaction Mode). Participant = Interaction Mode ON 상태의 호칭. Role 전환이 아니라 mode 전환 | "Host"·"Guest"·"Participant" 카피 잔존 검출 케이스 신규. View↔Interaction 토글 UI 회귀 |
| Δ-16 | Cloud ↔ Local Stage 핸드오프 | 단일 환경(로컬 LAN). 복제 개념 없음 | **양방향 복제** — Handoff to local(Cloud→Local) + Upload to Cloud(Local→Cloud). 단 local pie 포함·Bridge App 활용 Stage는 Upload to Cloud 불가 | 복제 정상 케이스 + 제약 negative test(local pie·Bridge App Stage Upload 거부). 라이센스 단독 모드 차단 회귀 |

**운영 규칙**
- 레거시와 동작이 갈리는 게 새로 확인되면 **Δ-NN 한 행을 추가**한다.
- "회귀 변환" 컬럼은 케이스 변환 작업의 체크리스트로 쓴다.
- 아직 결정이 안 된 충돌은 행으로 만들지 않고 §4 미결 질문에 둔다.

---

## 6. 에러 목록 (S-ERR)

모든 에러는 운영 메트릭에 기록된다.

| 코드 | 상황 | 사용자 화면 | 시스템 동작 | 복구 |
|---|---|---|---|---|
| E-AUTH-1 | ProtoPie Cloud 로그인 실패 | "로그인 실패. 다시 시도" 모달 | Bridge 시작 화면 유지 | 사용자 재시도 |
| E-AUTH-2 | Device 토큰 만료 | "세션이 만료되었습니다. 다시 로그인" | 자동 로그아웃 + 로그인 화면 | 재로그인 |
| E-AUTH-3 | Device 토큰 차단 (분실 신고 등) | "이 디바이스는 차단되었습니다" | Bridge 잠금 | 관리자가 차단 해제 |
| E-ENT-1 | Team Entitlement 만료·결제 실패 | "Connect 사용 기간이 끝났습니다" 차단 | 즉시 읽기 전용 모드 | 결제 갱신 시 즉시 복구 |
| E-ENT-2 | Cloud 장애로 Entitlement 검증 불가 | (무음) | 캐시 토큰으로 24h 읽기 전용 grace | Cloud 복구 시 자동 |
| E-NET-1 | Cloud 연결 끊김 | "Cloud 연결 끊김. 재연결 시도 중…" 토스트 | 자동 재연결 (지수 백오프) | 네트워크 복구 |
| E-NET-2 | Relay 방 연결 끊김 | "방에서 끊어졌습니다. 재입장" | 5초 후 자동 재입장 시도 | 자동 또는 수동 |
| E-DEV-1 | Device 등록 실패 (네트워크·시계 오차) | "디바이스 등록 실패: [이유]" + 재시도 | 등록 화면 유지 | 사용자 재시도 |
| E-PLG-1 | 플러그인 실행 크래시 | 카드에 빨간색 + "재시작" | 자동 1회 재시작, 실패 시 정지 | 사용자 재시작 또는 코드 수정 |
| E-PLG-2 | manifest 잘못됨 (Import 시) | "플러그인 형식 오류: [상세]" | Import 거부 | 사용자가 zip 수정 후 재업로드 |
| E-USB-1 | USB 디바이스 권한 없음 (macOS) | "Arduino 사용 권한 필요" + 시스템 설정 deep-link | 디바이스 미인식 유지 | 사용자가 권한 부여 |
| E-PAY-1 | 결제 → Bridge 가시성 지연 | "결제 처리 중. 1~2분 후 새로고침" + 버튼 | 폴링 (15초 간격) | 1~2분 내 자동 또는 수동 새로고침 |
| E-TEAM-1 | Connect 사용 가능 Team 없음 | "Connect Addon 구매하기" + Cloud 결제 링크 | Bridge 잠금 | 결제 후 자동 |
| E-RELAY-1 | Relay 방 만료·종료 | "이 방은 종료되었습니다" + 새 방 생성 | 방 목록으로 복귀 | 새 방 생성 |
| E-OS-1 | macOS Gatekeeper / Windows SmartScreen 경고 | OS 기본 경고 화면 | (Bridge가 직접 안내 불가) | OS 신뢰 후 재실행 또는 코드 서명 정상화 |
| E-MSG-CHANNEL-MISMATCH | Pie의 send/receive 채널이 ProtoPi Studio가 아니거나 양측 불일치 | (레거시 무음. Beta에서 디버거 경고 표시 검토) | 메시지 silent drop | 사용자가 채널을 ProtoPi Studio로 일치시킴 |
| E-PLG-BAUD-MISMATCH | Arduino 플러그인 baud rate와 보드 코드 baud rate 불일치 | 메시지 미수신, 에러 미표시 | 시리얼 통신 무응답 | 사용자가 baud rate 일치 (예: 115200) |
| E-PLG-PORT-BUSY | Arduino IDE 또는 다른 앱이 시리얼 포트 점유 | 플러그인 실행 실패 또는 무응답 | 포트 open 실패 | 점유 앱 종료 후 플러그인 재실행 |
| E-BRG-API-AUTH | Custom Bridge App이 외부 API 인증 실패 (token 만료·잘못된 키) | 앱 stdout에 에러, Connect 메시지 로그는 무음 | 앱 종료 또는 idle | 사용자가 토큰 갱신 후 Bridge App 재시작 |
| E-PLG-MSG-FLOOD | 다중 컴포넌트 인스턴스의 연속 send로 메시지 폭주 | (현재 무음) | 메시지 큐 적체·Cloud Relay 부하 | rate limit 트리거 후 dispatch 제한 |

---

## 7. Bridge ↔ Server REST API (F-API)

옛 회귀 케이스(S503)에서 직접 검증되던 API 표면이다. 모든 엔드포인트는 인증 실패·권한 부족·잘못된 ID 입력 시 **명확한 4xx 응답**을 반환해야 한다.

| ID | 엔드포인트 | 요구사항 | 확인 포인트 | 옛 케이스 |
|---|---|---|---|---|
| F-API-pies | `GET /api/pies` | Pie List 조회. 빈 상태·존재 상태 모두 정상 응답 | 빈 리스트 시 200 + `[]`. 존재 시 권한 필터링된 목록만 반환 | C127794~795 |
| F-API-pies-upload | `POST /api/pies/upload` | Local Pie 업로드. 인증 필수 | Connect 미로그인·Connect 종료 상태에서 차단. 잘못된 파일 거부 | C127808~811 |
| F-API-pies-uploadCloud | `POST /api/pies/uploadCloud` | Cloud Pie 업로드. Cloud login + Pie/Project 권한 필요. **Pro plan 계정에서는 실패** | 6 실패 케이스: Cloud 미로그인 / Connect 미로그인 / Pro plan / Pie 권한 없음 / Project 권한 없음 / Pie id 불일치 | C127800~807 |
| F-API-pies-delete | `POST /api/pies/delete` | 1개·다수 Pie 삭제. 잘못된 ID 혼합 시 부분 실패 정책 | 정상 1건, 다중 삭제, 무효 ID 단독, 무효 ID 혼합 | C127796~799 |
| F-API-groups | `GET /api/groups`<br>`POST /api/groups/add`<br>`POST /api/groups/remove` | Group 조회·생성·삭제. Group 1 level 강제 | 빈/존재 조회. add 후 정렬 namespace 유지. remove 시 cascade 동작. 무효 ID 단독·혼합 | C127785~788<br>C127791~793 |
| F-API-groups-updatePie | `POST /api/groups/updatePie` | Pie를 **Group ↔ Group 이동 한정.** 모든 Pie는 Group 종속이므로 root를 source/target으로 지정한 요청은 거부 | 정상 1패턴(Group→Group) + **root 지정 요청 400 거부** + 무효 Pie ID·무효 Group ID·group_id 누락 | C127777~784<br>(root 이동 케이스는 거부로 전환) |
| F-API-players | `GET /api/players` | Player 연결 정보 조회. 미연결·연결 상태 모두 정상 응답 | 빈 상태 200 + 빈 목록. 연결 상태 목록 정확성 | C127775~776 |
| F-API-players-run | `POST /api/players/run` | 특정 Player에서 Pie 실행. 이미 실행 중·미연결 시 명확한 에러 | 정상 실행, 중복 실행, 미연결 에러 | C127770~772<br>C127789~790 |
| F-API-players-runAll | `POST /api/players/runAll` | 전체 연결 Player에서 일괄 실행 | 전체 실행 정확성. Player 0개일 때 에러 응답 | C127773~774 |
| F-API-players-loadPie | `POST /api/players/loadPie` | 특정 Player에 특정 Pie 로드 | 정상·실패 케이스 | C127768~769 |
| F-API-auth-uniform | (공통) | 모든 API의 **인증·권한 실패 응답 카피·코드 일관.** Connect 미로그인 / Cloud 미로그인 / 권한 없음 / 무효 ID 4 카테고리를 동일 패턴으로 처리 | 카피 일관성. HTTP status 일관(401/403/404 구분). 멤버·Stage role별 거부 응답이 §6 에러 목록과 매핑되는지 | — |

**확인 우선순위**
1. 권한 우회를 차단하는 인증·권한 응답 일관성 (P0)
2. Pie/Group 이동·삭제 시 cascade + "모든 Pie는 Group 종속" 강제 (P1)
3. 잘못된 ID 혼합 시 부분 실패 정책 명문화
