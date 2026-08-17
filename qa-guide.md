---
doc_id: CC-QA
title: Cloud Connect — QA 테스트 기준
purpose: 어떤 환경에서 무엇을 먼저, 어디까지 테스트하는지의 기준. 릴리즈 테스트 계획을 잡을 때 본다.
maintainer: Paige (QA)
ssot: https://ssot.protopie.works/ko/connect/
extracted_from: Cloud_Connect_Spec.md rev16 (2026-06-12)
ssot_reviewed: 2026-08-17 (changelog 2026-07-27 ~ 08-13, 68개 항목)
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
| 4 | 옛 케이스 변환 | 레거시 회귀 케이스를 손볼 때 |

> ⚠️ **공백 구간 있음.** SSOT changelog는 2026-07-27부터 시작한다. **2026-06-12 ~ 07-27 사이 6주의 변경은 changelog에 없다.**

## 지금 무엇을 제공하고 있나

**Enterprise만 제공한다.** 기업이 서버를 사고, 그 안에 CoC를 추가 구매하는 형태다.

- **등급·플랜 기반 테스트를 하지 않는다.** 등급 게이팅이 2026-08-13에 코드에서 제거됐다
- 유일한 게이트는 **Edit Role ≥ Editor**
- Self-serve(유저가 플랜을 사서 쓰는 형태)는 **정식 출시 정책 확정 후** — 2026년 10월 결정 예정

상세: [spec.md §0](spec.md)

---

## 1. 테스트 환경

**모든 조합을 다 하지는 않되**, 결과가 달라질 수 있는 차원을 빠뜨리지 않기 위해 명시한다.

| 차원 | 값 |
|---|---|
| **OS** | macOS, Windows |
| **모드** | Cloud (브라우저), Desktop Cloud-login, Desktop License-key, Embedded (터미널·헤드리스) |
| **네트워크** | LAN only, Cloud Relay, Hybrid |
| **배포** | **Enterprise (B2B silo)만.** Self-serve는 보류 |
| **사용자 권한** | Team Owner/Admin/Member × Edit Role Moderator/Editor/Viewer × Stage owner/editor/viewer |
| **접속 주소** | `127.0.0.1` / `localhost` / **LAN IP** — 주소에 따라 열람 범위가 달라진다 (§2 P0) |
| **하드웨어** | USB, Serial, MQTT 대표 디바이스 1종 이상 (Arduino, G29, Gamepad, MQTT Broker) |
| **외부 클라이언트** | 모바일 iOS·Android, 웹 브라우저 (Chrome·Safari·Edge) |
| **운영 시간** | 단발성(1~2시간), 일상(8시간), 장시간(2~3일 연속 — 이벤트·전시회) |
| **진입 경로** | 공유 링크(토큰), 로그인 후 진입, Desktop 첫 실행, Embedded 터미널 부팅 |

**빠진 차원 2개** — 등급 게이팅 제거로 사라졌다.

- ~~플랜 등급 (Free / Core / Enterprise)~~
- ~~Team 타입 B2C silo~~ (현재 B2B만)

**권한 차원은 특히 조심한다.** 세 축이 독립이라 조합이 많다 → [spec.md §1](spec.md)

---

## 2. 위험 우선순위

### P0 — 실패하면 출시 차단 권고

전부 **격리·인증 우회** 계열이다.

| 항목 | 확인 포인트 |
|---|---|
| Team 간 자원 누출 (RLS 우회) | 다른 Team 자원이 조회되는지 |
| Stage 간 자원 격리 위반 | 다른 Stage의 Pie·플러그인이 노출되는지 |
| URL의 Team ID로 다른 Team 자원 접근 | 인가 우회 |
| Cookie/JWT 위변조 또는 만료 토큰으로 진입 | |
| 변조된 Bridge 빌드가 부팅됨 | 서명 검증 우회 |
| 무서명 자동 업데이트 허용 | |
| 분실 Device 토큰 revoke 지연 | |
| License-only 모드에서 Cloud 자원 접근 | 모드 경계 위반 |
| 장시간(2~3일) 실행 시 메모리 누수·디스크 폭주로 서비스 중단 | |
| **🆕 Local 링크 주소 범위 우회** | `127.0.0.1`/`localhost` 링크가 **다른 기기에서 열리는지**, LAN IP 링크가 **네트워크 밖에서 열리는지** (`useStageShareLink.ts:13-23`) |
| **🆕 공유 토큰 rate limit 우회** | IP당 분당 5회 + 백오프를 넘겨서 토큰 교환이 되는지 (`StageJoinClient.tsx`) |
| **🆕 링크 재설정 후 옛 링크로 접근** | host가 공유 링크를 재설정하면 **발급된 링크가 전부 무효**여야 한다 (`stage.ts:786-900`) |
| **🆕 디바이스 페어링 우회** | 호스트 승인 없이 접근되는지. 제거된 기기의 기존 자격 증명으로 재접근되는지 (`pairing.ts:236,245`) |
| **🆕 Embedded 라이선스 검증 우회** | 없음·읽기 불가·형식 오류·만료·호스트 불일치인데 시작되는지 (`FileLicenseAdapter.ts:87`) |
| **🆕 Web embed URL 차단 우회** | 안전하지 않음·자기 참조·연결 불가·프레이밍 거부 주소가 로드되는지 (`webViewUrl.ts:47,72,91`) |

### P1 — 레거시 동등 보장

**하드웨어·플러그인**
- 하드웨어 통합: Arduino, G29, Gamepad, **MQTT Broker**, Custom Bridge App
- 프리셋 플러그인 **5종**: API, G29, Arduino, Gamepad, MQTT Broker
  - ⚠️ **7종 → 5종으로 줄었다.** IFTTT·Blokdots는 `scopeout` (→ §3). Unity는 플러그인이 아니게 됨
- **Unity는 레이어에서 직접 Send/Receive** — 별도 플러그인 없음 (→ [spec.md](spec.md) Δ-20)
- **G29 메시지 12종** — 자동차 산업 데모에 직결
  - Backstage에서 G29는 **send 전용으로 표시.** `leds` 수신은 라우팅되지만 Receive 점·섹션·edge를 숨김
  - 휠이 LED 값을 거부해도 **오류를 보고하거나 Plugin을 중지하지 않아야** 한다
  - 시작 후 받은 `leds` 메시지만 shift-indicator LED를 변경
- **Arduino**: Baud rate 프리셋 8종, **기본값 9600**. Run 중 Port·Baud rate 변경 불가
- **API plugin**: 요청 시간 제한 **기본 10초**. 잘못된 값에는 기본값 적용
- **🆕 Stage 간 플러그인 배타 실행** — 한 Stage에서 Plugin 시작 → 다른 Stage의 실행 중 Plugin 중지. Stage를 나가면 그 Stage의 Plugin 중지
- **🆕 커스텀 플러그인 import** — **폴더 또는 `.zip`** 둘 다. 무효·안전하지 않음·손상·중복은 설치 거부
- **🆕 미설치 커스텀 플러그인** — Plugins 목록에서 제외 + Backstage 노드에 "Plugin not available". 단 Cloud Stage·owner 세션 없는 게스트·목록 로딩 중/실패 시에는 **판정 보류**
- **Custom Bridge App boilerplate 호환성** — 외부 사용자가 만든 기존 Node.js 앱이 도는지

**Stage View·레이어**
- 기본 미러링, 다중 시청
- **Stage View URL 파라미터**: `pieid` · `stageid` · `group` · bg · hotspotHints · cursorHide · scaleToFit
  - ⚠️ **`fullscreen`은 없어졌다** (→ Δ-22)
- 커스텀 레이어 3종: Web Embed, Camera, Unity — **플랜별 수량 한도는 사라짐**
- Edit Mode 레이어 속성 패널 (Position·Size·Lock·Original·Fit/Fill·Insert)
- **Multi-view broadcast 모델** — 모든 Pie가 모든 메시지를 받는 라우팅
- **🆕 Web embed 권한** — Desktop에서 위치·카메라·마이크 사용 전 확인, **앱 종료까지 오리진×기능별 선택 기억.** 거부·무효 요청은 거절
- **🆕 canvas 자동 Fit to screen** — Group 진입 시, 레이어가 0→1이 되는 배치 직후

**연결·공유**
- Player 연결: **USB**, 모바일 iOS·Android
  - ⚠️ **QR은 현재 미구현** — "공유 수단은 링크뿐". 단 `45-workspace`에 "QR • USB (Desktop app 전용)" 표기가 있어 범위 확인 필요 (→ Q-13)
- **🆕 공유 토큰 모델** — 토큰 무기한, Stage당 1개, 진입 후 6시간 재인증 면제
- **🆕 링크 재설정** — host 동작, 기존 링크 전부 무효화 + 새 링크 발급
- **🆕 호스트 승인 페어링** — 승인 / 거부 / 무응답 2분 타임아웃 3경로. IP당 분당 3개
- **🆕 무효 토큰 화면 분기** — cloud 익명은 로그인 게이트, 로그인된 비멤버·local 전체는 no access
- **🆕 Session expired / login gate 복귀** — 토큰·URL 파라미터를 보존한 채 같은 join 링크로 복귀
- **🆕 Pie 미리보기 링크** — Stage 권한 없는 수신자가 열면 연결된 Stage를 거쳐 입장. 토큰 사용 후 반환 URL에서 제거, 실패해도 리디렉션 재시도 안 함
- **🆕 참가자 상한** — min(운영 실링, host가 정한 max members). 실링 기본 **200**
- Studio 연동: SocketIO 양방향, `.pie` 업로드

**Stage Session 생애 (🆕 전부 신규)**
- 새 Stage는 **Editor가 입장해 실시간 Session을 시작할 때까지 유휴 Workspace**
- **공유 중지** = 현재 Session 종료, Workspace와 배치된 콘텐츠는 유지
- **호스트 연결 끊김 유예 기간** — 그 안에 재접속하면 Session 활성 유지
- Cloud Stage 접근 권한 6분류 — 로그인 크리에이터 / Team space 멤버 / 비멤버 / 게스트 / Session 종료 후 게스트였던 사용자 / 이용 불가 Stage
- **guest = 공유 링크로 들어온 사람**, 표에서 **Editor로 여는 사람 = 현재 Session host**

**Pie·Group·Stage 파일**
- **모든 Pie는 Group 종속 강제** — UI New 비활성, group_id 누락 API 거부, root↔Group 이동 거부 (→ Δ-01)
- Pie 교체 시 **pieId 유지** → 메시지 연결 보존
- **Cloud Pie는 수동 리로드**, Local Pie만 자동 동기화
- **🆕 Local Stage `.stage` 내보내기·가져오기** (Desktop·Embedded)
  - 번들 내용: Stage 그래프 · 로컬 Pie 파일 · Unity 파일 · **글꼴** · 사용자 지정 Plugin 패키지
  - 가져온 Stage 이름 = 파일명. 파일명에 이름 없으면 번들 저장 이름
  - 진행 중 앱 상호작용 차단 + **취소 가능한 하단 진행 표시기**
  - **거부 5종**: 미지원 / 손상 / 불완전 / 이전 버전 / 이후 버전 번들
- **🆕 Local Stage 삭제 cascade**
  - 가져오기·복제가 그 Stage용으로 만든 레이어·Pie·Pie 파일 + **비게 된 그룹까지** 삭제
  - 단 **사용자가 나중에 넣은 Pie는 로컬 라이브러리 자산이라 남고, 그 Pie가 든 그룹도 남는다** ← 여기가 헷갈리는 지점
  - 로컬 Pie 라이브러리 자체는 삭제 불가. Stage 목록에 안 나옴

**권한**
- **Stage Role 자동 부여 룰** — Cloud Edit Role ≥ Editor 유저가 같은 Team 모든 Stage에서 editor로 자동 부여되는지, 강등 시 즉시 박탈되는지. **"Stage editor 멤버 추가 UI"가 없는지 negative test** (→ Δ-04)
- **Cloud Stage 생성이 Desktop에서도 되는지** + cross-mode 동기화 (→ Δ-13)
- **🆕 등급으로 차단되는 지점이 남아 있지 않은지** negative test — 게이팅 제거가 코드 전체에 반영됐는지
- REST API 인증·권한 응답 일관성 — **단 API 잔존 여부 미확인** (→ Q-16)

**Console (구 Debug)**
- **컬럼 4개** — Message는 항상 표시, Time·Value·Source는 **헤더 우클릭으로 토글**
  - ⚠️ **Pie 컬럼은 없다.** 5컬럼이 아니다 (→ Δ-21)
- 모든 컬럼 드래그 리사이즈. 남는 너비를 채우며 늘어나는 건 **하나뿐**
- 한 viewport에서 **가로·세로 모두 스크롤**
- **기록은 현재 Stage 메시지만** — 다른 Stage에서 온 메시지는 넣지 않음
- **CSV Load** — 유효한 CSV를 가져오면 **첫 메시지부터 Play 시작.** 잘못됐거나 비면 오류 알림
  - ⚠️ 버튼 이름은 **Load**다 ("Import"가 아님)
- **Play는 기록된 간격을 그대로 따르고, 10초 넘는 간격만 10초로 축소**
- Terminal 팝오버(커스텀 플러그인): 비모달, 프로세스 출력 + 자동 스크롤 토글, **Clear 버튼 없음**

**Backstage (🆕 전부 신규)**
- **host와 Plugin 노드만** 나타남. 연결된 Player App·Bridge 등 다른 노드는 edge와 함께 숨김
- Pie 노드는 기본 **접힌 상태**, 방향 요약만. 펼치면 Receive·Send 안에 Message Chip을 **Scene 순서로** 나열
- 처음에 접힌 상태로 시작, 브라우저의 마지막 패널 높이 유지
- Plugin에서 못 쓰는 Receive/Send 방향은 section·Handle까지 숨김
- 움직이는 점 + **트래픽 있는 Message Chip만 강조** → 실행 경로와 실제 트래픽 구분
- 미설치 커스텀 플러그인 노드는 연결 유지한 채 "Plugin not available"

**Desktop / Embedded**
- **업데이트 자동 다운로드 기본 OFF.** 저장된 설정을 읽을 수 없을 때도 이 안전한 기본값 유지 ← 안전 기본값이므로 회귀 중요
- 시작 시 저장된 Cloud 세션 검증. **Cloud가 무효라고 확인한 경우에만** 로그아웃
- 프록시 설정은 **로그인 화면 안의 Network proxy settings**
- License 사용자는 계정 메뉴에서 `/login` 게이트 → **Back to Connect** 복귀
- **`PPC_HTTPS=1`** → 자체 서명 인증서로 LAN 브라우저에 HTTPS 제공
- 라이센스 키 단독 로그인: **5분 무료 만료 정책이 폐기됐는지** 확인 (→ Δ-08)

**확인 범위가 불확실한 것 (→ Q-13, Q-14)**
- Wear OS / 스마트워치 — SSOT 4개 페이지에서 못 찾음
- 음성 프로토타이핑 (Voice Command / Speak / Listen) — 못 찾음
- Player IP + 포트 9981 연결 — 못 찾음
- 커스텀 폰트 — `.stage` 번들에 "글꼴"로만 등장. Enterprise 전용이었는데 등급 축이 사라짐
- 메시지 Recording & Playback의 등급 제한 — 기능은 있음(Console), 제한만 불명
- Embedded의 Enterprise 한정 여부

### 데이터 분석 (`50-analytics`) — 🆕 우리 문서에 없던 영역

- `Connect - Launched` 이벤트: 인증·시스템 정보 확정 후 또는 **3초 대기 후**에도 상태 필드 미해결이면 **한 번만** 전송
- 머신 식별자를 확보 못하면 데스크톱 수명 주기 텔레메트리 전송 안 함
- 충돌 텔레메트리: 정상 종료·강제 종료 제외. 그 밖의 반복 종료는 **프로세스 유형 × 종료 사유별 분당 1건**으로 제한
- 이벤트에 platform, stage type, 접속 cloud 서버 URL이 실림
- **수집하지 않아야 하는 것** — 배포 호스트 이름, `hostname` 속성, Cloud 세션의 플러그인 사용 기록 ← 개인정보·보안 관점 negative test

### 미결이 풀리면 바로 케이스화할 것

[spec.md §4](spec.md)를 본다. 우선순위 높은 것:

| 우선 | ID | 질문 | 단계 |
|---|---|---|---|
| 1 | Q-13 | Wear OS·음성·Player IP 9981이 지금 범위인가 | 2 → 3 |
| 2 | Q-16 | REST API가 아직 있나 | 2 |
| 3 | Q-15 | PIN이 완전히 폐기됐나 (SSOT 내부 상충) | 2 |
| 4 | Q-14 | 커스텀 폰트·Recording·Embedded 등급 제한 잔존 | 2 |
| 5 | Q-4·Q-5·Q-9 | Backstage 접근 / 토글 잠금 / 토글 보존 | 2 |
| 6 | Q-1·Q-2·Q-7·Q-8·Q-11 | 나머지 | 2 ~ 3 |

---

## 3. 테스트 제외 범위

### 등급·플랜 관련 — 2026-08-13 제거로 제외

- 등급별 기능 차단 (Free / Core / Enterprise)
- 등급별 수량·시간 한도 (플러그인 동시 실행, 3분 제한, 워터마크 등)
- **Upsell Modal** 및 모든 한도 트리거 지점
- Plan 다운그레이드·업그레이드 시나리오
- **Self-serve 배포** — 정식 출시 정책 확정(2026-10) 후 재검토

정식 출시에 플랜 정책이 다시 붙으면 되살린다 (→ [spec.md](spec.md) Δ-10).

### SSOT `scopeout` 표기 항목

- **IFTTT 플러그인**
- **Blokdots 플러그인**

프리셋 플러그인이 7종 → 5종으로 줄어든 이유다 (→ Δ-19).

### PRD 명시 Non-goals

- AI 기능 (Bridge·Cloud 양쪽)
- 플러그인 마켓플레이스 / 공용 레지스트리. Team별 프라이빗 공유만
- 3rd-party 플러그인 개발자 생태계. 사용자 직접 작성만
- 플러그인 결제·수익 분배
- 플러그인 URL/git import. **폴더 또는 `.zip` 업로드만**
- 플러그인 코드 서명·검수. **사용자 본인 책임 모델**
- On-prem / air-gapped 배포
- Team 간 자원 공유 / 워크스페이스 초대
- 엔터프라이즈 운영 기능 (SSO·SAML·SCIM·CMEK)
- Local DB ↔ Cloud DB 동기화. 모드 전환 시 새 환경으로 인지
- UT (Connect-aware User Testing)
- **Stage view from the Player** — Player 네이티브 web embed/Unity/camera에서 Stage 화면 자체를 띄우는 것
  ⚠️ 단, Player가 단일 Pie를 실행하면서 Stage 메시지에 참여하는 건 **범위에 포함**. 혼동 주의
- Webhook (외부 인터넷 트리거)
- Send/Receive SDK 공개 — 패키징 절차만 노출
- Cross-network 원격 연결의 P2P/VPN/LAN 브리징 대안

### 2026-05-21 회의에서 추가 제외

- Stage 필터·검색 기능
- Stage 정렬 (최근 편집순·Recently Opened)
- **실시간 Sync 보강.** 알려진 한계: 중간 참여자는 이전 상태를 볼 수 없다
- **Kick 기능**

### ACL 반영으로 제외

- **Private Stage / Shared Stage 구분.** 단일 공유 모델 (→ Δ-14)
- **"내 작업실" 자동 생성**

### 범위에 유지 (제외 아님)

- **Embedded Connect** — 포함. 단 등급 제한 잔존 여부 확인 필요 (Q-14)

### 알려진 이슈로 지켜보기만

- 클라우드 파이 편집 시 처리 방안 검토 필요
- 커스텀 폰트가 로컬 환경에 함께 다운로드되지 않는 이슈
  - 참고: `.stage` 번들에는 글꼴이 포함된다 → 해소됐는지 확인 가치 있음

---

## 4. 옛 케이스 변환

### S280 (2.9.0 POR Plan, 309 케이스) — 🗑️ 회귀 시드에서 제외

**2026-08-17 Paige 결정으로 폐기.**

폐기 근거를 남긴다.

- S280은 전체가 **"등급 6종 × 영역 6종" Plan entitlement 매트릭스**다
- 2026-08-13에 등급 게이팅이 코드에서 제거됐다 (`features.ts:6` 외)
- 현재는 **Enterprise만 제공**하고, Enterprise 서버가 CoC를 쓰면 기능 제한이 없다. 유일한 게이트는 Edit Role ≥ Editor
- 즉 매트릭스의 축 자체가 존재하지 않는다

**정식 출시(2026-10 정책 결정) 때 플랜이 다시 붙으면 되살린다.** 원본 CSV는 `testrail/이전_TestCase/connect_feature(2.9.0 POR Plan).csv`에 남아 있고 git 이력에도 있다.

### S503 (Master Regression, 232 케이스) — 유지

레거시 기능 회귀의 1차 시드다. **새로 쓰는 게 아니라 케이스 ID를 살려서 변환**한다 (레거시 PC 화면 → Cloud 브라우저, 단일 사용자 → 멀티 사용자·멀티 디바이스).

`is_converted` 컬럼이 `1`이면 이미 전환됨, `0`이면 검토 후 변환·삭제를 결정.

파일: `testrail/이전_TestCase/connect_regression_test_case.csv`

| S503 영역 | 매핑 | 케이스 ID 범위 | 변환 시 유의 |
|---|---|---|---|
| Plan Login > Free / Connect core (lite) | — | C127812~127828 | **폐기** — 등급 게이팅 제거 |
| New (Upload) > Local Pie / Cloud Pie / Pie Role | F-STG-pie-source, F-STG-stage-role | C127695~127741 | 권한 3축으로 재구성 |
| Open From ProtoPie Cloud 기능 | F-STG-cloud-pie-browser | C127706~ | Q-7(cross-team) 확정 후 |
| Pie List > Local/Cloud/Group/Check box | F-STG-group-1level, F-STG-display-order | C127* | Δ-01(Group 종속) 적용 |
| Web View Player > Group Web Player + Edit Mode 레이어 | F-STG-svw-edit-mode, F-STG-svw-layers | C127833~128665 | 레이어 3종. **플랜별 한도 삭제** |
| Debug > Message / Send-Receive / Record | Console | C127680~127693 | **4컬럼으로 정정.** 버튼 이름 Load |
| Plugin / Blokdots / Arduino / IFTTT / Wear OS 연결 | F-PLG-* | C127748~127767 | **IFTTT·Blokdots 케이스 → 제외 범위.** Wear OS는 Q-13 대기 |
| Bottom menu / Information + Custom Font | F-BRG-bottom-info | C127676~127679<br>C127829~127832 | Custom Font 등급 제한은 Q-14 |
| API > `/api/{pies,groups,players}` | F-API-* (→ [spec.md §7](spec.md)) | C127768~127811 | **Q-16 확인 후** 유지·삭제. Pro plan 실패 케이스는 삭제 |

### 변환 절차

1. **케이스 단위가 아니라 기능 단위로 묶는다** → 중복·obsolete 제거 → §1 환경 차원을 곱해서 케이스 수를 산정
2. `is_converted = 0`인 케이스는 셋 중 하나로 결정
   - 지금도 유효 → 신규 포맷으로 작성
   - 레거시 PC 화면 전용 → Cloud/Desktop으로 대체
   - 비대상 (등급 관련, IFTTT·Blokdots) → 삭제
3. **옛 케이스 ID는 출처 컬럼에 남긴다** — 회귀 결함이 났을 때 레거시 동작과 비교하기 위해
4. 케이스를 지울 때는 **지운 이유를 남긴다.** 나중에 되살릴지 판단하려면 근거가 필요하다

### 변환 전에 반드시 볼 것

[spec.md §5 레거시와 다른 점](spec.md) — Δ 표를 먼저 봐야 "이 케이스가 거부로 뒤집혔나, 그대로인가"를 판단할 수 있다.

**2026-08-17에 Δ가 7개 늘었다** (Δ-17~Δ-23). PIN 폐기·QR 미구현·프리셋 5종·Unity 레이어·Console 4컬럼·URL 파라미터·플러그인 배타 실행. 변환 작업 중이었다면 이 7개를 다시 확인해야 한다.

### TestRail 구조

```
protopie.testrail.io / project 91

메뉴 6개 = suite 6개
  Home 1361 · LeftPanel 1362 · RightPanel 1363
  CanvasStage 1364 · Preview 1365 · ShareRun 1366
```

체크리스트 → TestRail 업로드 절차는 [testrail/README.md](testrail/README.md)와 `.claude/skills/testrail-migrate/SKILL.md`.
