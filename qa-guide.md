---
doc_id: CC-QA
title: Cloud Connect — QA 테스트 기준
purpose: 어떤 환경에서 무엇을 먼저, 어디까지 테스트하는지의 기준. 릴리즈 테스트 계획을 잡을 때 본다.
maintainer: Paige (QA)
ssot: https://ssot.protopie.works/ko/connect/
extracted_from: Cloud_Connect_Spec.md rev16 (2026-06-12)
ssot_reviewed: 2026-08-30 (changelog 2026-08-19 ~ 08-20, 61개 항목)
last_updated: 2026-08-30
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

> ⚠️ **공백 구간 있음.** SSOT changelog는 2026-07-27부터 시작한다. 2026-06-12 ~ 07-27 사이 6주의 변경은 changelog에 없다.

## 지금 무엇을 제공하고 있나

**Enterprise만 제공한다.** 기업이 서버를 사고, 그 안에 CoC를 추가 구매하는 형태다.

- **등급(tier)·플랜 매트릭스 테스트를 하지 않는다.** 등급 게이팅이 2026-08-13에 코드에서 제거됐다
- 주 게이트는 Edit Role ≥ Editor. 단 **플랜 존재 게이트는 별도로 있다** — Stage 생성·Editor 역할 출처 (→ [spec.md §0](spec.md), Q-18)
- Self-serve(유저가 플랜을 사서 쓰는 형태)는 정식 출시 정책 확정 후 — 2026년 10월 결정 예정

상세: [spec.md §0](spec.md)

---

## 1. 테스트 환경

**모든 조합을 다 하지는 않되**, 결과가 달라질 수 있는 차원을 빠뜨리지 않기 위해 명시한다.

| 차원 | 값 |
|---|---|
| OS | macOS, Windows |
| 모드 | Cloud (브라우저), Desktop Cloud-login, Desktop License-key, Embedded (터미널·헤드리스) |
| 네트워크 | LAN only, Cloud Relay, Hybrid |
| 배포 | Enterprise (B2B silo)만. Self-serve는 보류 |
| 사용자 권한 | Team Owner/Admin/Member × Edit Role Moderator/Editor/Viewer × Stage owner/editor/viewer |
| 접속 주소 | `127.0.0.1` / `localhost` / LAN IP — 주소에 따라 열람 범위가 달라진다 (§2 P0) |
| 하드웨어 | USB, Serial, MQTT 대표 디바이스 1종 이상 (Arduino, G29, Gamepad, MQTT Broker) |
| 외부 클라이언트 | 모바일 iOS·Android, 웹 브라우저 (Chrome·Safari·Edge) |
| 운영 시간 | 단발성(1~2시간), 일상(8시간), 장시간(2~3일 연속 — 이벤트·전시회) |
| 진입 경로 | 공유 링크(토큰), 로그인 후 진입, Desktop 첫 실행, Embedded 터미널 부팅 |

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
| Team 간 자원 누출 (RLS 우회) | **비소속** Team 자원이 조회되는지. ⚠️ 격리 경계는 "소속 여부"다 — Stage 목록이 소속 Team 합집합인 것, 같은 Team Viewer의 rename·삭제 API가 200인 것은 스펙이지 버그가 아니다 (→ [spec.md](spec.md) F-IDM-team-root·F-IDM-server-role-gate) |
| Stage 간 자원 격리 위반 | 다른 Stage의 Pie·플러그인이 노출되는지 |
| URL의 Team ID로 다른 Team 자원 접근 | 인가 우회 |
| Cookie/JWT 위변조 또는 만료 토큰으로 진입 | |
| 변조된 Bridge 빌드가 부팅됨 | 서명 검증 우회 |
| 무서명 자동 업데이트 허용 | |
| 분실 Device 토큰 revoke 지연 | |
| License-only 모드에서 Cloud 자원 접근 | 모드 경계 위반 |
| 장시간(2~3일) 실행 시 메모리 누수·디스크 폭주로 서비스 중단 | |
| 🆕 Local 링크 주소 범위 우회 | `127.0.0.1`/`localhost` 링크가 다른 기기에서 열리는지, LAN IP 링크가 네트워크 밖에서 열리는지 (`useStageShareLink.ts:13-23`) |
| 🆕 공유 토큰 rate limit 우회 | 이중 구조다 — 분당 5회 + 백오프는 인스턴스별 인메모리(파드 수만큼 곱해짐), 클러스터 전체는 IP당 5분 창 20회 실패 캡. 캡을 넘겨서 토큰 교환이 되는지 + 캡에 걸리면 올바른 토큰도 거절되는지 (`stage.ts:844` · `env.ts:140`) |
| 🆕 링크 재설정 후 옛 링크로 접근 | host가 공유 링크를 재설정하면 발급된 링크가 전부 무효여야 한다 (`stage.ts:786-900`) |
| 🆕 디바이스 페어링 우회 | 호스트 승인 없이 접근되는지. 제거된 기기의 기존 자격 증명으로 재접근되는지 (`pairing.ts:236,245`). ⚠️ 의도된 예외: **trust-LAN에서는 레거시 v1 bridge 프로토콜(ppBridgeApp/ppMessage)·`POST /api/pp-message`가 페어링 없이 수용**된다 (`pp-client.ts:71` · `bundle-embed.mjs:626`) — 이 경로는 우회 버그가 아니라 스펙. trust-LAN 밖에서도 되는지가 확인 포인트 |
| 🆕 Embedded CLI 무라이선스 경로 | 런처 인자 `stage:list/export/import`는 라이선스 확인 없이 동작한다(스펙 — 만료 장비 구출용). `--no-plugins` 없이 가져오면 플랜·등급 확인 없이 커스텀 Plugin까지 설치된다. 서버 사용 중 폴더는 거절(`--force`로 강행), 종료 코드 0/1/2 (`stage-cli.ts:111-344` · `embed-launcher.mjs:46`) |
| 🆕 Embedded 웹 표면 노출 | `GET /webplayer`는 무인증(음성 토큰 주의). 내부 웹 UI는 3001 포트(`PPC_WEB_PORT`/`PPC_WEB_DIR`, fail-loud 종료). CORS는 자체 origin + `PPC_ALLOWED_WEB_ORIGINS`에 명시한 정확한 origin만 — 그 외 origin이 접근되는지 (`web-player.ts:40` · `cors-policy.ts:79` · `embed-launcher.mjs:74,206`) |
| 🆕 Embedded 라이선스 검증 우회 | 없음·읽기 불가·형식 오류·만료·호스트 불일치인데 시작되는지 (`FileLicenseAdapter.ts:87`) |
| 🆕 Web embed URL 차단 우회 | 안전하지 않음·자기 참조·연결 불가·프레이밍 거부 주소가 로드되는지 (`webViewUrl.ts:47,72,91`) |

### P1 — 레거시 동등 보장

#### 하드웨어·플러그인
- 하드웨어 통합: Arduino, G29, Gamepad, MQTT Broker, Custom Bridge App
- 프리셋 플러그인 5종: API, G29, Arduino, Gamepad, MQTT Broker
  - ⚠️ **7종 → 5종으로 줄었다.** IFTTT·Blokdots는 `scopeout` (→ §3). Unity는 플러그인이 아니게 됨
  - MQTT Broker는 상세 검증 보류 (→ §3). 지금은 목록에 있는지만 본다
- **Unity는 레이어에서 직접 Send/Receive** — 별도 플러그인 없음 (→ [spec.md](spec.md) Δ-20)
- **G29 메시지 12종** — 자동차 산업 데모에 직결
  - Backstage에서 G29는 send 전용으로 표시. `leds` 수신은 라우팅되지만 Receive 점·섹션·edge를 숨김
  - 휠이 LED 값을 거부해도 오류를 보고하거나 Plugin을 중지하지 않아야 한다
  - 시작 후 받은 `leds` 메시지만 shift-indicator LED를 변경
- **Arduino**: Baud rate 프리셋 8종, 기본값 9600. Run 중 Port·Baud rate 변경 불가
- **API plugin**: 요청 시간 제한 기본 10초. 잘못된 값에는 기본값 적용
- **🆕 Stage 간 플러그인 배타 실행** — 한 Stage에서 Plugin 시작 → 다른 Stage의 실행 중 Plugin 중지. Stage를 나가면 그 Stage의 Plugin 중지
- **🆕 커스텀 플러그인 import** — 폴더 또는 `.zip` 둘 다. 무효·안전하지 않음·손상·중복은 설치 거부. 브라우저 표면은 From folder… 숨김·zip HTTP 업로드만
- **🆕 커스텀 플러그인 단일 인스턴스** — 추가하면 + 메뉴에서 빠지고 행 메뉴엔 Delete plugin만. Replace plugin 메뉴 없음. 다중 인스턴스는 API·IFTTT뿐(→ Q-17) (→ Δ-24)
- **🆕 Embedded도 Run/Stop 노출** — 멈춘 플러그인은 Offline 표시, 실행 중엔 삭제 잠김 (`StagePluginsAccordion.tsx:338`)
- **🆕 다중 Gamepad** — 기기 수 배지(2대 이상, Offline에도 표시) + Backstage 기기별 위성 노드(독립 이동·호스트 선 복제). G29는 단일 기기 유지. 메시지 어휘: G29를 건너뛰는 1부터 번호, `leds`는 5비트 문자열 또는 0~1 소수 (`hardware-device-watcher.ts:13` · `gamepad.ts:20`)
- **🆕 미설치 커스텀 플러그인** — Plugins 목록에서 제외 + Backstage 노드에 "Plugin not available". 단 Cloud Stage·owner 세션 없는 게스트·목록 로딩 중/실패 시에는 판정 보류
- **Custom Bridge App boilerplate 호환성** — 외부 사용자가 만든 기존 Node.js 앱이 도는지

#### Stage View·레이어
- 기본 미러링, 다중 시청
- **🆕 Pie 일괄 배치 20개 한도는 UI 전용 상한** — 등급별 Pie 상한은 클라이언트·서버 모두 폐지 (`useAddLocalPies.ts:93`)
- **Stage View URL 파라미터**: `pieid` · `stageid` · `group` · bg · hotspotHints · cursorHide · scaleToFit
  - ⚠️ **`fullscreen`은 없어졌다** (→ Δ-22)
- Engine 레이어 4종: Web Embed, Camera, Unity, **Map Navigation** — 플랜별 수량 한도는 사라짐. 안내 상태는 공통("Engine 레이어 공통 안내" 절), 크래시는 레이어 단위 격리 (`EngineHost.tsx:241`)
  - ⚠️ **3종이 아니다** — Map Navigation이 2026-08-20에 정식 절로 추가됐다 (아래 전용 절)
- Edit Mode 레이어 속성 패널 (Position·Size·Lock·Original·Fit/Fill·Insert)
- **Multi-view broadcast 모델** — 모든 Pie가 모든 메시지를 받는 라우팅
- **🆕 Web embed 권한** — Desktop에서 위치·카메라·마이크 사용 전 확인, 앱 종료까지 오리진×기능별 선택 기억. 거부·무효 요청은 거절
- **🆕 Web embed 추가 대화상자** — iframe 코드 붙여넣기(src 추출), 16–4096px 크기 시드, allow 허용 목록, URL 전용 임베드의 camera/microphone 기본값 (`webViewUrl.ts:122` · `AddWebViewDialog.tsx:60`)
- **🆕 카메라 레이어** — 소스 3택, 장치 선택은 클라이언트별 저장(Stage 데이터 아님) (`camera-device-preference-store.ts:1`)
- **🆕 canvas 자동 Fit to screen — 3가지** — ① Group 진입 시 ② 레이어가 0→1이 되는 배치 직후 ③ 읽기 전용(Preview/Viewer/guest) 캔버스가 열릴 때·창 크기 변경 시. `?scaleToFit=false`로 끔 (`MultiStageCanvas.tsx:795`)
- **🆕 View settings 실제 항목** — Background color(None/Light/Dark/Custom)·Hide hotspot hints·Hide cursors. Scale to fit·Hide UI는 없다. 옛 `hideUI` 파라미터가 남은 링크는 입장하면서 그 값을 버린다

#### Map Navigation 레이어 (🆕 전부 신규, 2026-08-20)

- 프로바이더 3종: Mapbox(기본), Google Map(Web Service Credential·Map ID), AMap(Gaode — 키 쌍·허용 도메인·중국어 고정·중국 본토 한정)
- 레이어별 쓰기 전용 API 키 슬롯 + Connect/Update 검증 흐름 (`MapNavigationPropertiesForm.tsx:53,286`)
- 기본값: Stage 전역 유일 이름, Mapbox·Vancouver·light·2D·Course·영어·km (`map-navigation.ts:10`)
- 출발 위치 검색: 후보 최대 5개, 좌표 직접 입력 가능, 키 게이트 (`MapNavigationOriginField.tsx:74`)
- 변경 영향: 프로바이더·출발지 = 세션 리셋, Map ID = 지도 재시작, 나머지 = 핫 적용. Advanced setting은 즉시 저장
- 레이어 Run은 전 참여자에게 전파. 컨트롤러/팔로워 정책 — Stage 관리 클라이언트만 조종, Viewer·guest는 보간 위치만 수신(수동 줌 유지·표시 명령 로컬 적용) (`stageRunSync.ts:67` · `runtime-message-policy.ts:17`)
- 주행 시뮬레이션: `pedals-gas`/`pedals-brake`, 최고 속도 150km/h (`navigation.ts:77`)
- 메시지 처리: 위치 검색 디바운스(최근 쿼리만), 속도 제한 시 마지막 성공 후보 유지, 길찾기 1회 재시도, Navigation 도착 후 상태 갱신 시 참가자 지도 화면 유지 (`runtime.js:1251,1260,1219,1708`)
- **상시 인터넷 필수 — Embedded 폐쇄망에서도 예외** (음성과 함께 오프라인 예외 2건). 사용 가능 환경: Cloud·Desktop Cloud-login은 Editor만, Desktop 라이선스·Embedded 가능
- 연쇄 노출: Preview 레이어 목록, Console Combobox(Map Navigation 메시지 포함), + 메뉴 행, Backstage 노드(레이어당 1개·삭제 불가·Stage 동기화)

#### 연결·공유
- Player 연결: USB, 모바일 iOS·Android
  - ⚠️ **QR은 현재 미구현** — "공유 수단은 링크뿐". 단 `45-workspace`에 "QR • USB (Desktop app 전용)" 표기가 있어 범위 확인 필요 (→ Q-13)
- **🆕 공유 토큰 모델** — 토큰 무기한, Stage당 1개, 진입 후 6시간 재인증 면제
- **🆕 링크 재설정** — host 동작, 기존 링크 전부 무효화 + 새 링크 발급
- **🆕 호스트 승인 페어링** — 승인 / 거부 / 무응답 2분 타임아웃 3경로. IP당 분당 3개
- **🆕 무효 토큰 화면 분기** — cloud 익명은 로그인 게이트, 로그인된 비멤버·local 전체는 no access
- **🆕 Session expired / login gate 복귀** — 토큰·URL 파라미터를 보존한 채 같은 join 링크로 복귀
- **🆕 Pie 미리보기 링크** — Stage 권한 없는 수신자가 열면 연결된 Stage를 거쳐 입장. 토큰 사용 후 반환 URL에서 제거, 실패해도 리디렉션 재시도 안 함
- **🆕 참가자 상한** — min(운영 실링, host가 정한 max members). 실링 기본 200. 만석 시 "This stage is full"(전용 화면 없음), **Editor는 예외로 입장**
- **🆕 게스트 재입장** — 쿠키로 재입장, 동명 게스트는 번호 부여. 망가진 쿠키는 무오류 처리
- **🆕 Session expired 자동 재입장** — 팀 Viewer는 3초→60초 백오프로 자동 재입장. guest는 Back to join, Viewer는 Go to Cloud 버튼
- **🆕 Stop sharing** — 세션만 종료(Workspace 유지). guest·Viewer 즉시 Session expired, Editor는 유지
- **🆕 버전 핸드셰이크** — 클라이언트·서버 버전 불일치 시 거절 + 서버 상세 문구 (`handshake.ts:84`)
- Studio 연동: SocketIO 양방향, `.pie` 업로드

#### Stage Session 생애 (🆕 전부 신규)
- 새 Stage는 Editor가 입장해 실시간 Session을 시작할 때까지 유휴 Workspace
- **공유 중지** = 현재 Session 종료, Workspace와 배치된 콘텐츠는 유지
- **호스트 연결 끊김 유예 기간 = 1분** — 그 안에 재접속하면 Session 활성 유지. Viewer 입장 → Editor 퇴장 → 1분 후 만료 (→ [spec.md](spec.md) F-VWR-session-grace)
- Cloud Stage 접근 권한 6분류 — 로그인 크리에이터 / Team space 멤버 / 비멤버 / 게스트 / Session 종료 후 게스트였던 사용자 / 이용 불가 Stage
- **guest = 공유 링크로 들어온 사람**, 표에서 Editor로 여는 사람 = 현재 Session host

#### Pie·Group·Stage 파일
- **모든 Pie는 Group 종속 강제** — UI New 비활성, group_id 누락 API 거부, root↔Group 이동 거부 (→ Δ-01)
- Pie 교체 시 pieId 유지 → 메시지 연결 보존
- **Cloud Pie는 수동 리로드**, Local Pie만 자동 동기화
- **🆕 Local Stage `.stage` 내보내기·가져오기** (Desktop·Embedded)
  - 번들 내용: Stage 그래프 · 로컬 Pie 파일 · Unity 파일 · 글꼴 · 사용자 지정 Plugin 패키지
  - 내보내기 진입: Local Stage의 Connect 메뉴 "Export local stage" (호스트 전용, 설정 구역과 Delete stage 사이) (`StageNavMenu.tsx:444`)
  - 가져온 Stage 이름 = 파일명. 파일명에 이름 없으면 번들 저장 이름
  - 진행 중 앱 상호작용 차단 + 취소 가능한 하단 진행 표시기. 차단 알약의 Cancel은 1회성, 99%에서 대기
  - **거부 목록 확대 (2026-08-30)**: 미지원 / 손상 / 불완전 / 이전 버전 / 이후 버전 / 비`.stage` 즉시 거절 / **암호 오답**(손상과 동일 문구)
  - 여러 파일을 주면 첫 개만 가져오기. 암호 잠금 번들은 드롭 폴더 거절. 미완 Pie는 무경고 제외 (`stage-bundle-crypto.ts:100` · `useStageImportRunner.ts:30`)
  - Embedded는 CLI 경로도 있다 — `stage:list/export/import` 런처 인자, **라이선스 확인 없음** (→ §2 P0)
- **🆕 Local Stage 삭제 cascade**
  - 가져오기·복제가 그 Stage용으로 만든 레이어·Pie·Pie 파일 + 비게 된 그룹까지 삭제
  - 단 사용자가 나중에 넣은 Pie는 로컬 라이브러리 자산이라 남고, 그 Pie가 든 그룹도 남는다 ← 여기가 헷갈리는 지점
  - 로컬 Pie 라이브러리 자체는 삭제 불가. Stage 목록에 안 나옴

#### 권한
- **Stage Role 자동 부여 룰** — Cloud Edit Role ≥ Editor 유저가 같은 Team 모든 Stage에서 editor로 자동 부여되는지, 강등 시 즉시 박탈되는지. "Stage editor 멤버 추가 UI"가 없는지 negative test (→ Δ-04)
- **🆕 서버 검증 경계** — rename·보관·복원·삭제는 서버가 팀 소속만 검증(Viewer 요청도 200 — 스펙), Viewer 차단은 FE 몫. `/stop`은 같은 Team Editor 누구나 가능. 기대결과를 여기에 맞춘다 (→ [spec.md](spec.md) F-IDM-server-role-gate)
- **🆕 Cloud 로그인 7일 상한** — 만료 시 강등 (`cloud-auth-service.ts:14`)
- **Cloud Stage 생성이 Desktop에서도 되는지** + cross-mode 동기화 (→ Δ-13)
- **🆕 등급으로 차단되는 지점이 남아 있지 않은지** negative test — 게이팅 제거가 코드 전체에 반영됐는지
- REST API 인증·권한 응답 일관성 — 단 API 잔존 여부 미확인 (→ Q-16)

#### Console (구 Debug)
- **컬럼 4개** — Message는 항상 표시, Time·Value·Source는 헤더 우클릭으로 토글
  - ⚠️ **Pie 컬럼은 없다.** 5컬럼이 아니다 (→ Δ-21)
- 모든 컬럼 드래그 리사이즈. Source는 왼쪽 가장자리 손잡이로 100~250px(기본 240px, 더블클릭 복귀). 남는 너비를 채우며 늘어나는 건 Value(숨기면 Source)
- 줄 펼침은 줄 단위 누적 토글(클릭 또는 Enter/Space, Esc로 전체 접기). **헤더 전체 펼침 토글은 없다**
- 한 viewport에서 가로·세로 모두 스크롤. hover·선택 시 자동 따라가기 정지 + 화면 고정
- 라이브 버퍼 5,000개 상한 (`debug-messages-store.ts:26`). Map 소스 라벨, 미상 출처 `—`, 빈 값 `(empty)`
- **기록은 현재 Stage 메시지만** — 다른 Stage에서 온 메시지는 넣지 않음
- **CSV Load** — 유효한 CSV를 가져오면 첫 메시지부터 Play 시작. 잘못됐거나 비면 오류 알림
  - ⚠️ CSV 재생 버튼 이름은 Load다. 단 헤더에는 별도의 **Import 버튼**이 있다 — 녹화 중 사라지는 건 Import 버튼과 필터 영역뿐, Clear는 Send Message 푸터에 있어 계속 쓸 수 있다 (`StageEditorConsole.tsx:254`)
- **Play는 기록된 간격을 그대로 따르고, 10초 넘는 간격만 10초로 축소.** 재생 상세: 정순·경과 시간·Exit 재생 헤더·푸터 숨김·속도 6단계. join 재생은 빈 Console일 때만 — 재연결 갭 미보충·Pie 미전달 (`StageReplayPanel.tsx:47`)
- **필터 바** — 기준별 값 제안(Source는 이 Console에 실제 나타난 라벨), 접힘 바·배지·칩·Refresh (`MessageFilterBar.tsx:106`)
- **Message Combobox는 클릭 시 전체 제안 목록**(Stage Pie + Map Navigation 레이어 메시지, 방향 배지, Pie별 그룹)을 열고, 입력은 필터만 한다 (`MessageCombobox.tsx:104`)
- Terminal 팝오버(커스텀 플러그인): 비모달, 프로세스 출력 + 자동 스크롤(기본 ON), 타임스탬프·빨간 오류 줄·버퍼 상한. ⚠️ "Clear 버튼 없음"은 2026-08-20 터미널 상세화(푸터 구성, `StagePluginTerminalPopover.tsx:196`)와 대조 안 됨 — 47-layers-plugins 본문 재확인 필요

#### Backstage (🆕 전부 신규)
- 나타나는 노드 (2026-08-30 정정): host · Pie · Plugin + **Map Navigation 노드**(레이어당 1개·평평한 칩·삭제 불가·Stage 동기화) + **게임패드 위성 노드**(기기별 펼침·독립 이동·호스트 선 복제). 연결된 Player App·Bridge 노드는 edge와 함께 숨김
- Pie 노드는 기본 접힌 상태, 방향 요약만. 펼치면 Receive·Send 안에 Message Chip을 Scene 순서로 나열
- 처음에 접힌 상태로 시작, 브라우저의 마지막 패널 높이 유지
- Plugin에서 못 쓰는 Receive/Send 방향은 section·Handle까지 숨김
- 움직이는 점 + 트래픽 있는 Message Chip만 강조 → 실행 경로와 실제 트래픽 구분
- 미설치 커스텀 플러그인 노드는 연결 유지한 채 "Plugin not available" + 오류 행·툴팁
- **🆕 브라우저 Connect on Cloud는 구조 편집(놓기·잇기·지우기) 차단, 노드 이동만** (`BackstageCanvas.tsx:785` · `cloud-adapter.ts:52`)
- **🆕 실행 중·원격 잠금 플러그인 노드는 Delete/Backspace 무시** — 먼저 Stop해야 지워짐
- Local Stage 호스트 노드는 LAN 주소 없으면 127.0.0.1 폴백. Cloud 호스트 노드 라벨은 "Connect on Cloud" (구 "Connect Cloud" — 옛 카피 검출 목록에 추가)
- 캔버스 어포던스: Fit to view·열 때 자동 맞춤·최소 10%, 키보드 이동 5/20px, No plugins yet 빈 화면

#### Desktop / Embedded
- **업데이트 자동 다운로드 기본 OFF.** 저장된 설정을 읽을 수 없을 때도 이 안전한 기본값 유지 ← 안전 기본값이므로 회귀 중요. ⚠️ SSOT에 "자동 내려받기 체크박스"가 신설 서술됨 — 기본값 유지 여부 확인 (Q-19)
- **🆕 강제 업데이트 다이얼로그** + 업데이트 상태 카드 전 상태 (`updater.ts:283` · `UpdateSection.tsx:13`)
- 시작 시 저장된 Cloud 세션 검증. Cloud가 무효라고 확인한 경우에만 로그아웃. **Cloud 로그인은 7일 상한 — 만료 시 강등**
- 프록시 설정은 로그인 화면 안의 Network proxy settings
- License 경로 (2026-08-30 정정): Settings › License의 Log-in은 Cloud/Enterprise 선택 다이얼로그 중첩(Settings 유지). 홈 계정 메뉴의 Log-in이 `/login` 게이트 → Back to Connect 복귀
- **🆕 Remove license** — 버튼·확인·게이트 복귀. Valid until 행 (`SettingsLicenseTab.tsx:134`)
- **🆕 Embedded 라이선스 상태 3값** — 파일 미등록 = N/A(outline 배지), Invalid는 등록된 파일이 신뢰 상실·만료·회수된 경우에만 (`SettingsLicenseTab.tsx:272`)
- **🆕 로그인 게이트 오류 분류** — 원인 코드 폴백, 접근 거부 화면 2종과 복구 경로 (`openLoginErrorMessage.ts:10` · `NoPlanScreen.tsx:35`)
- **`PPC_HTTPS=1`** → 자체 서명 인증서로 LAN 브라우저에 HTTPS 제공
- 라이센스 키 단독 로그인: 5분 무료 만료 정책이 폐기됐는지 확인 (→ Δ-08)
- **🆕 macOS 번들 런처** — `start.command`(더블클릭용) 생성, 브라우저로 받은 zip은 `xattr -dr com.apple.quarantine .` 1회 필요 (`bundle-embed.mjs:562,695`)

#### 음성 기능 (Voice trigger / Speak) — 🆕 범위 확정 (Q-13 부분 해결)
- 음성 기능을 쓰는 Pie는 인터넷 위 음성 서비스로 동작(자동 인증) — **인터넷·마이크 권한 필수**
- 자격 준비 전 비활성(준비 후 재마운트), 듣기 중 오류 상태 목록 있음 (`voice-interface.ts:23` · `useVoiceConfig.ts:42`)
- **Embedded 폐쇄망에서도 바깥 인터넷 필요** (Map Navigation과 함께 오프라인 예외 2건)

#### 확인 범위가 불확실한 것 (→ Q-13, Q-14)
- Wear OS / 스마트워치 — 2026-08-30 대조(61개)에서도 언급 0
- Player IP + 포트 9981 연결 — 언급 0
- 커스텀 폰트 — 사실상 범위 확정: Custom fonts 버튼·배지가 SSOT에 등급 조건 없이 등장 (`StageCustomFontButton.tsx:41`). "조건 미달 시 미표시"의 조건만 확인 (Q-14 잔여)
- 메시지 Recording & Playback의 등급 제한 — 기능은 있음(Console), 제한만 불명
- Embedded의 Enterprise 한정 여부

~~음성 프로토타이핑~~ → 범위 확정, 위 "음성 기능" 절로 승격 (2026-08-30)

### 데이터 분석 (`50-analytics`) — 🆕 우리 문서에 없던 영역

- `Connect - Launched` 이벤트: 인증·시스템 정보 확정 후 또는 3초 대기 후에도 상태 필드 미해결이면 한 번만 전송
- 머신 식별자를 확보 못하면 데스크톱 수명 주기 텔레메트리 전송 안 함
- 충돌 텔레메트리: 정상 종료·강제 종료 제외. 그 밖의 반복 종료는 프로세스 유형 × 종료 사유별 분당 1건으로 제한
- 이벤트에 platform, stage type, 접속 cloud 서버 URL이 실림
- **🆕 opt-out 없음** — 수집 여부는 빌드 키가 결정. 세션 시작·종료 자동 수집 ON. Sentry는 DSN 게이트, 미니덤프는 로컬 상시 (`client.ts:12` · `observability.ts:20`)
- **🆕 신원 식별 (2026-08-30)** — 해시는 enterprise cloud 한정. **team cloud(SaaS)는 UUID·이메일 원문을 user_id/email로 전송**(Studio와 동일 규칙), 라이선스 전용 Desktop은 `license:<deviceId>` (`properties.ts:340`) ← "이메일을 안 남긴다"고 잡으면 오검출
- **🆕 이벤트군 추가** — 로그인·라이선스·페어링·초대 링크·오류 토스트(종류별 스로틀) (`events.ts:50` · `useErrorToast.ts:44`)
- **수집하지 않아야 하는 것** — 배포 호스트 이름, `hostname` 속성, Cloud 세션의 플러그인 사용 기록 ← 개인정보·보안 관점 negative test

### 미결이 풀리면 바로 케이스화할 것

[spec.md §4](spec.md)를 본다. 우선순위 높은 것:

| 우선 | ID | 질문 | 단계 |
|---|---|---|---|
| 1 | Q-18 | 플랜 게이트(Stage 생성·Editor 역할 출처)가 Enterprise-only 배포에서 실효가 있나 | 3 |
| 2 | Q-17 | IFTTT 다중 인스턴스 언급 vs scopeout 상충 | 2 → 3 |
| 3 | Q-13 | Wear OS·Player IP 9981이 지금 범위인가 (음성은 해결) | 2 → 3 |
| 4 | Q-16 | REST API가 아직 있나 | 2 |
| 5 | Q-15 | PIN 폐기 잔여 확인 (40-product-overview 상충·pin-store 코드) | 1 ~ 2 |
| 6 | Q-19 | 업데이트 자동 내려받기 기본값 OFF 유지 여부 | 1 |
| 7 | Q-14 | Recording·Embedded 등급 제한 잔존 (커스텀 폰트는 사실상 해결) | 2 |
| 8 | Q-4·Q-5·Q-9 | Backstage 접근 / 토글 잠금 / 토글 보존 | 2 |
| 9 | Q-1·Q-2·Q-7·Q-8·Q-11 | 나머지 | 2 ~ 3 |

**1단계(페이지 재확인) 거리 2건 추가**: Terminal 팝오버 Clear 버튼·푸터 구성(47-layers-plugins), Q-19 자동 내려받기 기본값(42-desktop).

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

### 다음으로 미룬 것

- **MQTT Broker 플러그인 상세 검증.** 오토모티브 고객 요청으로 들어간 기능이다. 급하지 않다고 판단해 Sprint #3에서 넘겼다(2026-08-04 Paige). 지금은 플러그인 목록에 존재하는지만 확인한다. 상세 동작(브로커 연결·토픽 구독·메시지 변환)은 다음 차례.

### PRD 명시 Non-goals

- AI 기능 (Bridge·Cloud 양쪽)
- 플러그인 마켓플레이스 / 공용 레지스트리. Team별 프라이빗 공유만
- 3rd-party 플러그인 개발자 생태계. 사용자 직접 작성만
- 플러그인 결제·수익 분배
- 플러그인 URL/git import. 폴더 또는 `.zip` 업로드만
- 플러그인 코드 서명·검수. 사용자 본인 책임 모델
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

- S280은 전체가 "등급 6종 × 영역 6종" Plan entitlement 매트릭스다
- 2026-08-13에 등급 게이팅이 코드에서 제거됐다 (`features.ts:6` 외)
- 현재는 Enterprise만 제공하고, Enterprise 서버가 CoC를 쓰면 기능 제한이 없다. 유일한 게이트는 Edit Role ≥ Editor
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
| Web View Player > Group Web Player + Edit Mode 레이어 | F-STG-svw-edit-mode, F-STG-svw-layers | C127833~128665 | 레이어 3종. 플랜별 한도 삭제 |
| Debug > Message / Send-Receive / Record | Console | C127680~127693 | 4컬럼으로 정정. 버튼 이름 Load |
| Plugin / Blokdots / Arduino / IFTTT / Wear OS 연결 | F-PLG-* | C127748~127767 | IFTTT·Blokdots 케이스 → 제외 범위. Wear OS는 Q-13 대기 |
| Bottom menu / Information + Custom Font | F-BRG-bottom-info | C127676~127679<br>C127829~127832 | Custom Font 등급 제한은 Q-14 |
| API > `/api/{pies,groups,players}` | F-API-* (→ [spec.md §7](spec.md)) | C127768~127811 | Q-16 확인 후 유지·삭제. Pro plan 실패 케이스는 삭제 |

### 변환 절차

1. **케이스 단위가 아니라 기능 단위로 묶는다** → 중복·obsolete 제거 → §1 환경 차원을 곱해서 케이스 수를 산정
2. `is_converted = 0`인 케이스는 셋 중 하나로 결정
   - 지금도 유효 → 신규 포맷으로 작성
   - 레거시 PC 화면 전용 → Cloud/Desktop으로 대체
   - 비대상 (등급 관련, IFTTT·Blokdots) → 삭제
3. **옛 케이스 ID는 출처 컬럼에 남긴다** — 회귀 결함이 났을 때 레거시 동작과 비교하기 위해
4. 케이스를 지울 때는 지운 이유를 남긴다. 나중에 되살릴지 판단하려면 근거가 필요하다

### 변환 전에 반드시 볼 것

[spec.md §5 레거시와 다른 점](spec.md) — Δ 표를 먼저 봐야 "이 케이스가 거부로 뒤집혔나, 그대로인가"를 판단할 수 있다.

**2026-08-17에 Δ가 7개 늘었다** (Δ-17~Δ-23). PIN 폐기·QR 미구현·프리셋 5종·Unity 레이어·Console 4컬럼·URL 파라미터·플러그인 배타 실행. **2026-08-30에 Δ-24 추가** — 커스텀 플러그인 단일 인스턴스·Replace plugin 제거. 변환 작업 중이었다면 이 8개를 다시 확인해야 한다.

### TestRail 구조

```
protopie.testrail.io / project 91

메뉴 6개 = suite 6개
  Home 1361 · LeftPanel 1362 · RightPanel 1363
  CanvasStage 1364 · Preview 1365 · ShareRun 1366
```

체크리스트 → TestRail 업로드 절차는 [testrail/README.md](testrail/README.md)와 `.claude/skills/testrail-migrate/SKILL.md`.
