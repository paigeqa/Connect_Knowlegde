---
doc_id: CC-QA
title: Cloud Connect — QA 테스트 기준
purpose: 어떤 환경에서 무엇을 먼저, 어디까지 테스트하는지의 기준. 릴리즈 테스트 계획을 잡을 때 본다.
maintainer: Paige (QA)
ssot: https://ssot.protopie.works/ko/connect/
extracted_from: Cloud_Connect_Spec.md rev16 (2026-06-12)
last_updated: 2026-08-17
---

# Cloud Connect — QA 테스트 기준

**제품이 어떻게 동작하는가**는 이 문서가 아니다.

- SSOT → https://ssot.protopie.works/ko/connect/
- SSOT에 없는 스펙 → [spec.md](spec.md)

이 문서는 **우리가 어떻게 테스트하는가**만 담는다.

| § | 내용 | 언제 보나 |
|---|---|---|
| 1 | 테스트 환경 | 릴리즈 테스트 계획 잡을 때 |
| 2 | 위험 우선순위 | 시간이 부족해서 뭘 먼저 볼지 정할 때 |
| 3 | 테스트 제외 범위 | "이거 왜 안 봤어?" 소리 나올 때 |
| 4 | 옛 케이스 변환 (S280·S503) | 레거시 회귀 케이스를 손볼 때 |

> ⚠️ 이 문서는 2026-06-12(rev16) 시점 기준이다. 베타 출시 이후 바뀐 게 반영되지 않았다.
> F-* ID 중 [spec.md](spec.md)에 없는 것은 SSOT가 다루는 기능이다 (ID는 검색·추적용으로 남겨둠).

---

## 1. 테스트 환경

회귀·통합 테스트에서 다뤄야 할 차원이다. **모든 조합을 다 하지는 않되**, 결과가 달라질 수 있는 차원을 빠뜨리지 않기 위해 명시한다.

| 차원 | 값 |
|---|---|
| **OS** | macOS, Windows |
| **모드** | Cloud (브라우저), Desktop Cloud-login, Desktop License-key, Embedded (터미널·헤드리스) |
| **네트워크** | LAN only, Cloud Relay, Hybrid |
| **Team 타입** | B2C silo (Self-serve), B2B silo (Enterprise) |
| **사용자 권한** | Team Owner/Admin/Member × Edit Role Moderator/Editor/Viewer × Stage owner/editor/viewer |
| **하드웨어** | USB, Serial, MQTT 대표 디바이스 1종 이상 (Arduino, G29, MIDI, Gamepad, blokdots) |
| **외부 클라이언트** | 모바일 iOS·Android, 웹 브라우저 (Chrome·Safari·Edge) |
| **운영 시간** | 단발성(1~2시간), 일상(8시간), 장시간(2~3일 연속 — 이벤트·전시회) |
| **진입 경로** | URL 직접 입력, 북마크, Cloud 로그인 후 redirect, Desktop 첫 실행, Embedded 터미널 부팅 |

**권한 차원은 특히 조심한다.** 세 축이 독립이라 조합이 많다 → [spec.md §1 권한 모델](spec.md)

---

## 2. 위험 우선순위

### P0 — 실패하면 출시 차단 권고

전부 **격리·인증 우회** 계열이다.

| 항목 | 관련 |
|---|---|
| Team 간 자원 누출 (RLS 우회) | F-CLD-team-rls |
| Stage 간 자원 격리 위반 (다른 Stage의 Pie·플러그인 노출) | — |
| 변조된 Bridge 빌드가 부팅됨 | F-BRG-build-protect |
| 무서명 자동 업데이트 허용 | F-BRG-auto-update |
| 분실 Device 토큰 revoke 지연 | — |
| License-only 모드에서 Cloud 자원 접근 (Capability Matrix 위반) | — |
| URL의 Team ID로 다른 Team 자원 접근 | F-HOM-url-teamid |
| Cookie/JWT 위변조 또는 만료 토큰으로 진입 | F-IDM-cookie-jwt |
| Public Pie 정책 우회로 Private Pie 노출 | F-HOM-public-pie-only |
| 장시간(2~3일) 실행 시 메모리 누수·디스크 폭주로 서비스 중단 | F-CLD-long-run |

### P1 — 레거시 동등 보장

레거시 Connect에서 되던 게 안 되면 사용자가 바로 알아챈다.

**하드웨어·플러그인**
- 하드웨어 통합: Arduino, G29, MIDI, Gamepad, blokdots, Unity, Custom Bridge App(.zip)
- 프리셋 플러그인: API, IFTTT, Unity(Stage view 양방향), Custom
- 플러그인 동시 실행·시간 제한 매트릭스 (F-PLG-tier-limits)
- 외부 디바이스 플러그인 라이프사이클 4단계(연결·Run·Stop·Send/Receive) — Arduino·Blokdots·IFTTT·Wear OS
- **G29 메시지 12종** — 자동차 산업 데모에 직결
- **Custom Bridge App boilerplate 호환성** — 외부 사용자가 만든 기존 Node.js 앱이 Beta에서 도는지

**Stage View·Stageview**
- 기본 미러링, QR 진입, 다중 시청
- **MultiView URL 파라미터** (fullscreen / bg / hotspotHints / cursorHide / scaleToFit)
- 커스텀 레이어 3종: Web Embed, Live Camera, Unity (플랜별 한도)
- Edit Mode 4종 레이어 속성 패널 (Position·Size·Lock·Original·Fit/Fill·Insert)
- **Multi-view broadcast 모델** — 모든 Pie가 모든 메시지를 받는 라우팅

**연결**
- 모바일/웹 Player: QR(iOS·Android·**iPadOS**) / IP(9981) / USB / Wear OS(두 번 탭, **Apple Watch 미지원**)
- 웹 원격 접속: `http://[IP]:9981` + PIN code 입력
- 음성 프로토타이핑(Voice Command/Speak/Listen): Chrome·Edge(Chromium) 최적화
- Studio 연동: SocketIO 양방향, `.pie` 업로드

**Pie·Group**
- **모든 Pie는 Group 종속 강제** — UI New 비활성 동작, group_id 누락 API 거부, root↔Group 이동 케이스 거부 전환 (→ [spec.md](spec.md) Δ-01)
- Pie 교체 시 **pieId 유지** → 메시지 연결 보존
- **Cloud Pie는 수동 리로드**, Local Pie만 자동 동기화

**권한**
- **Stage Role 자동 부여 룰** — Cloud Edit Role ≥ Editor 유저가 같은 Team 모든 Stage에서 editor로 자동 부여되는지, 강등 시 즉시 박탈되는지. **"Stage editor 멤버 추가 UI"가 없는지 negative test** (→ [spec.md](spec.md) Δ-04)
- **Cloud Stage 생성이 Desktop에서도 되는지** + cross-mode 동기화 (→ Δ-13)
- **REST API 인증·권한 응답 일관성** — `/api/pies` `/api/groups` `/api/players` (→ [spec.md §7](spec.md)). P0 후보

**디버그·기타**
- **메시지 디버거 5컬럼** (Time·Message·Value·Pie·Source) + Clear 동작
- **메시지 Recording & Playback (CSV)** — Enterprise 전용. 데모 자동화의 핵심
- **커스텀 폰트 = Enterprise 전용**
- Embedded Connect: 터미널 부팅·라이센스 키 검증·헤드리스 호스트 동작 (Enterprise 한정)
- 라이센스 키 단독 로그인: **5분 무료 만료 정책이 폐기됐는지** 확인 (→ Δ-08)
- Home 화면 일관성: Cloud 모드 vs Desktop 첫 실행 화면이 같은 레이아웃인지
- **공통 Upsell Modal 3 버튼 URL·카피** 일관성 — Plan 한도 모든 트리거 지점에서 (S280에 21개 지점)

### 미결이 풀리면 바로 케이스화할 것

[spec.md §4 미결 질문](spec.md)의 Q-1~Q-11이 확정되면 즉시 케이스를 만든다.

그 외 rev16 시점 미결 항목:

| 영역 | 항목 |
|---|---|
| 권한·인증 | F-IDM-team-switch-ux, F-IDM-plan-feature-matrix, F-STG-external-guest |
| Stage·Pie | F-STG-pie-move, F-HOM-start-button |
| 플러그인 | F-PLG-perm-enforce, F-PLG-disp-multi-route |
| Relay | F-REL-envelope (**우선 처리 권고**), F-REL-flood-prevention, F-REL-hw-conflict |
| Viewer | F-VWR-auth-policy, F-VWR-nodeview-access, F-VWR-editor-notify, F-VWR-link-expiry, F-VWR-interaction-isolation |
| Bridge | F-BRG-17 (HTML import 보안 정책) |
| 운영 | F-CLD-enterprise-cost |

---

## 3. 테스트 제외 범위

이번 Beta에서 **테스트하지 않는** 항목이다. Post-Beta 진입 시 재검토한다.

### PRD 명시 Non-goals

- AI 기능 (Bridge·Cloud 양쪽). 별도 정책 결정 대기
- 플러그인 마켓플레이스 / 공용 레지스트리. Team별 프라이빗 공유만 지원
- 3rd-party 플러그인 개발자 생태계. 사용자 직접 작성만 허용
- 플러그인 결제·수익 분배
- 플러그인 URL/git import. 파일 업로드만 허용
- 플러그인 코드 서명·검수. **사용자 본인 책임 모델**
- On-prem / air-gapped 배포. Beta는 Connect-managed만
- Team 간 자원 공유 / 워크스페이스 초대
- 엔터프라이즈 운영 기능 (SSO·SAML·SCIM·CMEK)
- Local DB ↔ Cloud DB 동기화. 모드 전환 시 새 환경으로 인지 (자동 이전 없음)
- UT (Connect-aware User Testing). Post-Beta 후보
- **Stage view from the Player** — Player 네이티브 web embed/Unity/camera에서 Stage 화면 자체를 띄우는 것.
  ⚠️ 단, Player가 QR 스캔으로 단일 Pie를 실행하면서 Stage 메시지에 참여하는 건 **범위에 포함**된다 (F-VWR-player-participant). 혼동 주의
- Webhook (외부 인터넷 트리거)
- Send/Receive SDK 공개.
  ⚠️ Custom Plugin Import는 Enterprise 한정으로 **지원**되지만, SDK 명세·boilerplate·공식 문서는 공개하지 않는다. 사용자가 socket.io-client 등으로 자체 구현 → 패키징 절차만 노출
- Cross-network 원격 연결의 P2P/VPN/LAN 브리징 대안

### 2026-05-21 회의에서 추가 제외

- Stage 필터·검색 기능
- Stage 정렬 (최근 편집순·Recently Opened)
- **실시간 Sync 보강.** 알려진 한계: 중간 참여자는 이전 상태를 볼 수 없다. 새 참여자 진입 시 전체 리셋 대신 사용자 간 차이를 허용하는 방향 검토 중
- **Kick 기능.** 호스트가 Editor 권한으로 플레이어(디바이스) 단위 Kick하는 안이 검토됐으나 미포함

### 2026-05-28 ACL 반영으로 추가 제외

- **Private Stage / Shared Stage 구분.** Beta Cloud Stage는 단일 공유 모델 (→ [spec.md](spec.md) Δ-14)
- **"내 작업실" 자동 생성.** 가입 직후 빈 상태는 별도 UX로 처리

### 검토했지만 범위에 유지한 것 (제외 아님)

- Embedded Connect는 **포함**된다 (제외 후보에서 정정)
- 게스트 인증은 **PIN 방식 유지** (호스트 승인 방식은 추후 검토 여지)

### 알려진 이슈로 지켜보기만 하는 것

- 클라우드 파이 편집 시 처리 방안 검토 필요
- 커스텀 폰트가 로컬 환경에 함께 다운로드되지 않는 이슈

---

## 4. 옛 케이스 변환 (S280 · S503)

레거시 ProtoPie Connect의 TestRail suite 2개를 Beta 회귀의 출발점으로 쓴다.
**새로 쓰는 게 아니라 케이스 ID를 살려서 Beta 환경에 맞게 변환**한다 (레거시 PC 화면 → Cloud 브라우저, 단일 사용자 → 멀티 사용자·멀티 디바이스).

`is_converted` 컬럼이 `1`이면 이미 신규 포맷으로 전환된 것, `0`이면 검토 후 변환·삭제를 결정해야 한다.

| Suite | 명칭 | 케이스 수 | 초점 | 파일 |
|---|---|---|---|---|
| **S280** | 2.9.0 POR Plan | 309 | Plan entitlement 매트릭스 (Free / Basic-Core / Pro-Core / Pro Plus-Core / Pro Plus-Enterprise / Enterprise) | `testrail/이전_TestCase/connect_feature(2.9.0 POR Plan).csv` |
| **S503** | Master Regression | 232 | Pie List·Stage View·Plugin·Debug·API·Custom Font 등 기능 회귀 전반 | `testrail/이전_TestCase/connect_regression_test_case.csv` |

### S280 매핑 (Plan 등급 6종 × 영역 6종)

| S280 영역 | 매핑 | Beta 변환 시 유의점 |
|---|---|---|
| Account plan 표시 확인 | F-HOM, F-IDM-edit-role | Plan 라벨 카피만 변경 (Free → Connect Free 등). Cloud SoT 의존 |
| [Local Pie] Disable / Cloud Pie Upload 한도 | F-PLG-tier-limits, F-STG-pie-source | 한도 수치는 SSOT 플랜 표에 따라 재확정 |
| Players Connected 제한 | F-PLG-tier-limits, F-BRG-player-connect | Web/iOS/Android/USB 4 채널 모두 |
| Plugins (API/IFTTT/Arduino/Blokdots/Gamepad) | F-PLG-tier-limits, F-PLG-preset-* | Free 3분 만료·동시 실행 한도 강제 |
| Stage View (Pie/Web Embed/Camera/Smart Watch) | F-STG-svw-layers, F-STG-svw-edit-mode, F-BRG-wear-os | Plan별 레이어 수량 한도 + 비가용 시 Upsell |
| Dashboard / Pie upload / Players Connect | F-HOM, F-STG-pie-source, F-PLG-tier-limits | 등급 상승 시 한도 해제가 즉시 반영되는지 |
| 모든 Upsell 트리거 | F-IDM-upsell-modal | 3 버튼 URL·카피 variant (Enterprise vs Core) |

### S503 매핑 (기능 회귀 전반)

| S503 영역 | 매핑 | 케이스 ID 범위 |
|---|---|---|
| Plan Login > Free / Connect core (lite) | F-IDM-connect-entitlement, F-IDM-upsell-modal | C127812~127828 |
| New (Upload) > Local Pie / Cloud Pie / Pie Role | F-STG-pie-source, F-STG-cloud-pie-browser, F-STG-stage-role | C127695~127741 |
| Open From ProtoPie Cloud 기능 | F-STG-cloud-pie-browser, F-STG-cloud-pie-cross | C127706~ |
| Pie List > Local/Cloud/Group/Check box | F-STG-group-1level, F-STG-pie-list-multiselect, F-STG-display-order | C127* |
| Web View Player > Group Web Player + Edit Mode 4종 레이어 | F-STG-svw-view-settings, F-STG-svw-edit-mode, F-STG-svw-layers | C127833~128665 |
| Debug > Message / Send-Receive / Record | F-BRG-debugger-baseline, F-AUD-msg-record, F-AUD-record-ui-sequence | C127680~127693 |
| Plugin / Blokdots / Arduino / IFTTT / Wear OS 연결 | F-PLG-plugin-mgmt, F-PLG-lifecycle-baseline, F-PLG-preset-*, F-BRG-wear-os | C127748~127767 |
| Bottom menu / Information + [Enterprise] Custom Font | F-BRG-bottom-info, F-STG-teamfont | C127676~127679<br>C127829~127832 |
| API > `/api/{pies,groups,players}` | F-API-* (→ [spec.md §7](spec.md)) | C127768~127811 |

### 변환 절차

1. **케이스 단위가 아니라 기능 단위로 묶는다** → 중복·obsolete 제거 → §1 환경 차원을 곱해서 케이스 수를 산정
2. `is_converted = 0`인 케이스는 셋 중 하나로 결정
   - Beta에서도 유효 → 신규 포맷으로 작성
   - 레거시 PC 화면 전용 → Cloud/Bridge로 대체
   - Beta 비대상 (예: 단종된 Basic plan 영역) → 삭제
3. **옛 케이스 ID는 출처 컬럼에 남긴다** — 회귀 결함이 났을 때 레거시 동작과 비교하기 위해
4. Plan entitlement 영역(S280)은 **자동화 우선 후보.** "UI 한도 트리거 → Upsell modal 노출"은 데이터 주도 테스트(등급 × 한도)로 회귀량을 줄일 수 있다

### 변환 전에 반드시 볼 것

[spec.md §5 레거시와 다른 점](spec.md) — Δ 표를 먼저 봐야 "이 케이스가 거부로 뒤집혔나, 그대로인가"를 판단할 수 있다.

### TestRail 구조

```
protopie.testrail.io / project 91

메뉴 6개 = suite 6개
  Home 1361 · LeftPanel 1362 · RightPanel 1363
  CanvasStage 1364 · Preview 1365 · ShareRun 1366
```

체크리스트 → TestRail 업로드 절차는 [testrail/README.md](testrail/README.md)와 `.claude/skills/testrail-migrate/SKILL.md`.
