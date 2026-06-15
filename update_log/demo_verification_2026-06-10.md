# Cloud Connect 데모 구현 현황 점검 (TD 대비)

- 점검일: 2026-06-10
- 데모 URL: https://f1-cloud.protopie.works/connect
- 계정: owner@protopie.works (Team Owner, Edit Role Editor 추정) / password 공용
- TD: Notion "🎿 AI 활용" (https://app.notion.com/p/37b45184b5da8088bc46f6dd00421c4c)
- 점검 방법: Claude in Chrome 실브라우저 조작 + 스크린샷 + DOM 읽기

상태 표기: ✅ 구현 / ⚠️ 부분/차이 / ❌ 미구현 / ❓ 미확인(차단)

---

## 🏠 Connect Home — Editor(owner) 롤

### 접속 / 진입
- ✅ `/connect` 직접 접속 시 owner 계정으로 로그인 상태 진입, Cloud Stage 리스트 표시
- ❓ LNB Connect Menu in Cloud (Cloud 좌측 사이드바의 Connect 진입점) — `/connect` 직접 진입이라 미확인
- ✅ **팀 탭 구현됨** (정정): owner는 소속 팀 1개라 단일 탭으로 보였으나, viewer 계정(2팀 소속)에서 "viewer's Team" / "Connect Cloud/Desktop" 두 탭 확인됨. 탭 전환 동작.
  - ⚠️ "viewer's Team"은 드롭다운상 "No plan"인데 Connect 탭에 노출됨 — TD "Connect Add-on 미보유 팀 미표시"와 충돌 소지(‘No plan’이 add-on 미보유와 동일한지 확인 필요)

### Active Stage 리스트
- ✅ 제목 "Cloud Stages" 표시
- ⚠️ 버튼명 "**+ New stage**" (TD/Figma 기대값: "+ New cloud stage")
- ✅ Stage 카드: 썸네일 영역(플레이스홀더), Stage 이름, "Edited on today" 날짜 표시
  - ✅ `F-HOM-stage-date` "Edited on today" 포맷 일부 확인 (당일 케이스). 절대날짜 포맷 미확인
- ✅ "Archived stages >" 링크 노출 (우측 하단)
- ❓ View more (3개 초과 시) / 정렬 / 개수제한 — 데이터 부족으로 미확인

### Stage 카드 우클릭 메뉴 (Cloud) — ⚠️ 큰 차이
TD/스펙 기대(F-HOM-stage-ctx-cloud): Duplicate / Rename / Handoff to local / Archive stage(destructive)
- ❌ Duplicate group/stage 없음
- ⚠️ Rename stage — 메뉴엔 있으나 **비활성(회색)** 상태
- ❌ Handoff to local 없음
- ❌ Archive stage 없음
- ⚠️ 대신 "**Delete stage**"(빨강) 존재 — 스펙상 Cloud는 Archive, Local만 Delete여야 함. 현재 Cloud/Desktop 통합 탭이라 Local 메뉴 형태에 가까움
- → 결론: 우클릭 메뉴는 초기 단계 (Rename 비활성 + Delete만 동작 가능)

### 계정/설정 (account dropdown → Settings 모달)
- ✅ Settings 모달: General / License / Plugin 탭
  - General: Appearance(System/Light/Dark), Update(Check for updates / Automatically download updates), Snap on canvas 토글
  - License: Account(이름·이메일·Log out), License="Connect Free", Embedded license(Status=Invalid, Device ID=—, Locate a license file)
  - Plugin: "Add new..."(비활성), "No plugins available"
- 참고: Update 자동다운로드·Embedded license·Device ID 등 **데스크톱 앱 공유 셸**이 웹에 그대로 노출됨(공유 코드베이스 정황). TD엔 없는 영역.
- ⚠️ owner 계정인데 License가 "Connect Free"로 표시 — Plan/entitlement 연동 미완성 가능성

---

## ✏️ Edit Mode — Editor(owner) 롤 (Library Stage 진입)

### Stage GNB (상단바) — ✅ 대부분 구현
- ✅ 팀 이름 + 스테이지 이름 표시 ("Team Space / Library")
- ✅ Edit ↔ Preview 토글
- ✅ PIN 표시 ("PIN ------", 미연결 상태)
- ✅ Custom fonts (0) 표시
- ✅ Run 버튼 / Share 버튼
- ❓ 스테이지 이름 인라인 수정(아이콘 클릭) — 미확인

### Canvas — ✅ 구현
- ✅ 빈 그룹 상태 안내 ("Create your first group" / "+ Group")
- ⚠️ **i18n 미완성**: "이 stage 에 아직 group 이 없습니다." 한영 혼용 미번역 문자열 노출 (버그)
- ✅ 줌 컨트롤(100% 드롭다운), 전체화면 아이콘, 패널 토글 아이콘
- ✅ 그룹 선택 시 캔버스 상단 "BACKGROUND" 토글 표시
- ✅ 좌상단 "Layers" 드롭다운 버튼

### Left Panel (Stage / Settings 탭)
- ✅ Groups 섹션: "+" 생성, 생성 시 카드+썸네일 표시
  - ⚠️ 그룹 기본명 "New Group" (TD 기대: "{Group nb}" 예: Group 1), 생성 후 이름 자동 포커스 미확인
  - ⚠️ 캔버스 "+ Group" 빈상태 버튼으로 생성 시 Groups 리스트 즉시 갱신 안 됨(추정 갱신 이슈)
- ✅ Layers 섹션: "+" → 레이어 추가 컨텍스트 메뉴
- ✅ Settings 탭 존재(TD 미정의 영역)

### 레이어 추가 메뉴 — ⚠️ 차이
TD 기대: Browse team space(=Cloud Pie) / Web embed / Camera, **Unity는 메뉴에 없어야 함**
- 데모: **Pie / From Cloud / Web embed / Live Camera / Unity**
- ✅ From Cloud(=Browse team space), Web embed, Live Camera(=Camera) 존재
- ➕ "Pie"(로컬 Pie 추가 추정) 추가 항목
- ⚠️ **Unity가 메뉴에 노출됨** — TD는 노출 안 됨을 기대 (차이)

### Web Embed 레이어 — ⚠️ 부분 + 버그
- ✅ "Add Web Embed" 다이얼로그 (URL 입력, Cancel/Add)
- ✅ 유효 URL 입력 시 Add 활성화 / 빈값 시 비활성
- ❌ **버그**: `wikipedia.org`(프로토콜 없이) → Add 버튼 활성화되나 클릭 시 무반응(무음 실패). TD는 `wikipedia.org` 성공 기대. `https://www.wikipedia.org` 전체 URL로는 정상 추가됨
- ⚠️ 추가된 레이어명이 "Web embed"(고정) — TD 기대: 입력 URL이 레이어 이름
- ✅ 레이어 속성 패널: Layer명, Web embed URL, Position(X/Y), Size(W/H) 입력
- ⚠️ 기본 Size 0,0 → 캔버스에 시각적으로 표시 안 됨
- ❓ "Supported types" 버튼(→docs) 미확인(미노출 추정)

### Right Panel (Console) — ✅ 구현 양호
- ✅ Console 타이틀, Record 버튼, Record play 불러오기(폴더 아이콘)
- ✅ Filter (+, 새로고침)
- ✅ Message 테이블 (Time / Message / VALUE ... Source는 가로 스크롤)
- ✅ 빈 상태 안내 "No messages yet — interact with a connected player to see traffic."
- ✅ Send Message: Message / Value(Optional) 필드, "⌘+↵ to send", Send 버튼(내용 입력 시 활성화)
- ✅ Send 동작: 테이블에 Time(HH:MM:SS:MMM ✅)/Message/VALUE(empty) 기록됨
- ✅ Preview 모드에서도 Send Message 동작

---

## 🖇️ Share & Run — Editor 롤 ✅ 구조 우수
- ✅ Share 다이얼로그: 
  - "Copy link to editor" — "Only members of {Team Space} can access the editor." (팀명 표시 ✅)
  - "Copy link to stage viewer" (> 상세 다이얼로그)
  - "Pie previews" 섹션 — "No pies to preview yet" (Pie 레이어 없을 때 빈상태 ✅)
- ✅ "Link to stage" 상세 다이얼로그 (TD와 일치):
  - viewer URL (`/connect/join...`) + Copy 버튼
  - Background color(Default), Hide hotspot hints, Hide cursors, Hide UI, Scale to fit(ON 기본) 토글
- ❓ 설정값 변경 시 링크 업데이트 / 권한별 링크 접근(Editor/Viewer/비소속/비로그인) — 미검증(계정 전환 필요)
- ✅ Run 버튼 존재 (연결 대상 없어 동작 결과는 미검증)

---

## 🖼️ Preview Mode — Editor 롤 ⚠️ 부분
- ✅ Edit ↔ Preview 토글 동작
- ⚠️ TD 기대 Preview 전용 레이아웃 미흡: 좌측 패널(Groups/Layers)이 **숨겨지지 않고 그대로 유지** (TD: Left Panel 숨김 → Layers 드롭다운 노출)
- ⚠️ View settings(기어) 드롭다운·Preview용 비율 드롭다운 뚜렷이 미노출 (Edit과 캔버스 컨트롤 동일)
- ✅ Console/Send Message는 Preview에서도 유지·동작
- ❓ cmd+\ UI Hide, Fullscreen, Background None/Light/Dark 등 세부 미검증

---

## Codex 추가 확인 — 2026-06-10 18:50 KST

점검 방법: Notion TD + `Cloud_Connect_Spec.md` 대조, 별도 브라우저 세션에서 `owner@protopie.works` 로그인 후 DOM/visible tree 확인. Chrome Owner 프로필은 `Profile 11`로 식별했고, 기본 `protopie.io` 프로필은 건드리지 않음.

### Home / LNB
- ✅ Cloud LNB에 `Connect Cloud/Desktop` 버튼 노출.
- ⚠️ LNB 버튼 클릭 시 팀 드롭다운(`Connect Cloud/Desktop Active Editor (Owner)`, `Create new team`)은 열리지만, 팀 항목 선택은 `/t/51166d84` 프로젝트 홈으로 이동함. TD의 “Connect Menu에서 Connect Home 진입” 기대와 다름.
- ⚠️ 로그인 직후 `/connect` 직접 접근은 한 번 `Where is my pie?` 화면으로 떨어짐. `/t/51166d84` 팀 컨텍스트를 거친 뒤 `/connect` 재접근 시 정상적으로 Connect Home 표시. 직접 URL 진입이 세션/팀 컨텍스트에 의존하는 것으로 보임.
- ✅ Connect Home 표시 항목: 계정 버튼, 단일 탭 `Connect Cloud/Desktop`, `New stage`, Stage 2개(`Library`, `01KTRBQYHSMQSMR99JYWPKYEPX`), `Edited on today`.
- ⚠️ `Archived stages`는 버튼이 보이나 disabled + title `Archived stages — coming soon`. 기존 로그의 “링크 노출”보다 후퇴/정정: 현재는 기능 미구현 placeholder.
- ⚠️ Home Stage 카드 우클릭 메뉴: `Rename stage` 비활성, `Delete stage`만 활성. TD/Spec 기대(`Duplicate / Rename / Handoff to local / Archive stage`) 대비 대부분 미구현이며 Cloud에서 Delete가 보이는 점도 불일치.

### Stage Edit
- ✅ `Library` Stage 진입 시 `/connect/stages/default-stage-b26d59640c50ce28a2d44c4f54c44a7d/groups/01KTRE4M3R28HGKFA1H5EBMEF2`로 열림.
- ✅ GNB: stage menu, stage name `Library`, `Edit`/`Preview`, `PIN ------`, `Custom fonts 0`, `Run`, `Share`.
- ⚠️ PIN 영역이 `PIN ------` + `Reconnecting...` 상태로 유지되어 PIN 기반 viewer 참여 검증이 차단됨.
- ⚠️ Stage menu 항목: `Go to Cloud`, `Open desktop app`, `Preferences`, `Leave Stage…`, `Archive Stage…`. TD의 `Go to home`, `Open in editor` 명칭/구성과 다름.
- ✅ Left panel: `Stage`/`Settings`, `Groups`, `New Group`, `Layers`, 기존 `Web embed` layer, Copy/Open URL 버튼 확인.
- ⚠️ Layer add 메뉴: `Pie`, `From Cloud`, `Web embed`, `Live Camera`, `Unity`. TD 기대와 달리 `Unity`가 노출되고 `Pie`가 별도 노출됨.
- ⚠️ `From Cloud`는 Cloud Finder 모달까지 열림: `Search pies...`, space selector(`My pies`, `Connect Cloud/Desktop`), `Cancel`, disabled `Open`. 목록 선택 전까지 Open 불가.

### Preview / Share / Viewer
- ⚠️ Preview 탭 전환 후에도 좌측 `Stage/Settings`, `Groups`, `Layers`와 우측 Console이 유지됨. 일부 Add 버튼만 사라지는 수준이라 TD의 Preview 전용 레이아웃과 차이.
- ✅ Share dialog: `Copy link to editor`, `Copy link to stage viewer Open` 노출.
- ✅ Stage viewer 상세: URL `/connect/join/default-stage-b26d59640c50ce28a2d44c4f54c44a7d`, Copy, 문구 `Stage viewer is accessible to anyone with the link.`
- ✅ Share 옵션: `Background color: Default`, `Hide hotspot hints`, `Hide cursors`, `Hide UI`, `Scale to fit` 토글 모두 on.
- ⚠️ Viewer link는 display name + 6-digit PIN 입력 화면으로 열리고 Join은 disabled. Editor PIN이 로딩 상태라 Viewer 권한/Preview Mode 세부 동작은 미확인.

### Edit Mode Nav Menu (로고/스테이지 메뉴) — ✅ 구현
- ✅ Go to Cloud / Open desktop app / Preferences(> 서브메뉴) / Leave Stage… / Archive Stage…(빨강)
- TD 기대(Go to home/Open desktop app/Preferences/Archive Stage)와 부합 (+Leave Stage 추가)
- ✅ "Rename stage" 버튼 별도 존재(GNB), Stage 이름 인라인 수정 진입점 확인됨
- 참고: **Archive Stage는 Edit Nav 메뉴엔 존재**하나 Home 카드 우클릭엔 없음(Home은 Delete만)

---

## Codex 추가 재확인 — 2026-06-10 19:05 KST (3회 시도 룰)

원칙: 막히는 항목은 최대 3회까지 다른 방법으로 시도하고, 3회 실패 시 차단으로 넘김. 모르는 항목은 로컬 spec + 공개 문서 검색으로 근거 확인.

### PIN / Reconnecting — ❌ 차단 확정
- 시도 1: Editor stage를 새 탭에서 열고 12초 대기 → `PIN ------` 유지, 콘솔 error/warn 없음.
- 시도 2: `Run` 클릭 후 15초 대기 → `PIN ------` 유지. 로그는 `[PPBridge] Environment` 일반 로그만 확인.
- 시도 3: PIN 영역 클릭 후 reload + 15초 대기 → `PIN ------` 유지.
- 결론: viewer join을 위한 PIN이 발급되지 않아 PIN 기반 viewer 참여/권한 검증 차단.
- spec 근거: PIN + 24h token, ViewerInvite(PIN/share link/QR), relay 자동 reconnect가 기대 동작. steady `Reconnecting...`/`PIN ------`은 기대 동작이 아님.

### Viewer Join Link — ⚠️ PIN 전까지 차단
- 시도 1: 기존 탭 상태 확인 → join 탭이 Editor stage 탭으로 바뀌어 있어 탭 상태 불일치.
- 시도 2: `/connect/join/default-stage-b26d59640c50ce28a2d44c4f54c44a7d` 새 탭 직접 진입 → display name + 6자리 PIN 입력 화면 표시.
- 시도 3: display name `Codex Viewer` 입력 → Join 버튼은 계속 disabled. PIN 6자리가 필수.
- 결론: viewer link 자체는 구현되어 있으나 PIN 미발급 때문에 실제 join/Viewer Preview Mode 검증 불가.

### Home Stage Context Menu / View More — ❌ 주요 미구현
- 시도 1: 기존 `Library` href 우클릭 → 첫 화면에 Library가 없어 locator 0개. 대신 stage 4개 초과 시 `View more` 노출 확인.
- 시도 2: 첫 번째 visible stage 카드 우클릭 → `Rename stage` 비활성 + `Delete stage`만 표시.
- 시도 3: `View more` 클릭 후 6개 stage 전체 노출, Library 카드 우클릭 → 동일하게 `Rename stage` 비활성 + `Delete stage`만 표시.
- 결론: `View more`는 구현됨. Cloud Home 카드 메뉴는 spec/TD 기대(`Duplicate / Rename / Handoff to local / Archive stage`) 대비 대부분 미구현이며, Cloud stage에 `Delete stage`가 노출되는 것도 불일치.

### Viewer Account / Team-Stage 권한 — 🚨 P0 의심
- 시도 1: owner 세션에서 account button → Settings/License의 `Log out` 경로 확인.
- 시도 2: `viewer@protopie.works` 로그인 성공. 홈은 `viewer's Team` (`b0b374e7`) / Free plan으로 표시됨.
- 시도 3: viewer 계정으로 `/connect` 진입 시 `viewer's Team`만 보이고 active stage 없음. 그러나 원래 owner 팀 stage URL(`/connect/stages/default-stage-b26d59640c50ce28a2d44c4f54c44a7d`) 직접 접근 시 **Edit UI가 열림**.
- clean session sanity check: 새 Playwright 브라우저에서 viewer 계정으로만 로그인해도 동일하게 owner 팀 `Library` stage가 열리고 `Edit`, `Preview`, `Run`, `Share`, `Add group`, `Add layer`, `Send Message`가 노출됨.
- 결론: viewer 계정이 원래 team `51166d84`에 보이지 않는데도 직접 stage URL로 Editor UI 접근 가능. Team/Stage 권한 격리 P0 버그 의심.
- 증거 스크린샷:
  - `/Users/paige/Desktop/Boost/Connect Knowlege/update_log/screenshots/viewer-connect-home-2026-06-10.png`
  - `/Users/paige/Desktop/Boost/Connect Knowlege/update_log/screenshots/viewer-direct-owner-stage-edit-ui-clean-2026-06-10.png`

### 공개 문서/Spec 검색 결과
- 로컬 spec은 PIN + 24h token, ViewerInvite(PIN/link/QR), reconnect 복구 기대 동작을 명시.
- 공개 ProtoPie docs에서는 legacy Connect/Stage View/layer 개념은 확인되나, 신규 Cloud LNB route 또는 `/connect/join/{stageId}` 상세 Cloud flow는 찾지 못함.

---

## 🔐 로그인 / 인증 (F-IDM) — Claude 세션 추가
- ✅ 로그아웃 → 로그인 페이지: **"Log in" + General | Secure Enterprise 토글** (F-IDM-login-entrypoint 부합: Self-serve / Enterprise 진입 분리)
- ✅ Continue with Google / Apple, Email+Password, Forgot password, Create account, Terms/Privacy
- ✅ 멀티 팀 소속: viewer 계정이 "viewer's Team"(Editor) + "Connect Cloud/Desktop"(Viewer) 동시 소속 (F-IDM-nm-team)
- ✅ Cloud 로그인 세션이 /connect에 적용 (F-IDM-cookie-jwt 정황)
- 비고(Codex 보완): Cloud LNB에 `Connect Cloud/Desktop` 진입 버튼은 owner에서 보였으나 클릭 시 Connect Home이 아닌 `/t/{teamid}` 프로젝트 홈으로 이동 → 진입 라우팅 미완성. (Claude 세션의 viewer LNB에서는 Connect 항목 미확인 — 재확인 필요)

---

## 🏠🖼️ Viewer(Edit Role Viewer) 롤 — ⚠️⚠️ 권한 게이팅 미구현 (핵심 이슈, Claude 세션 직접 검증)

테스트: viewer@protopie.works (테스트팀 "Connect Cloud/Desktop"에서 Edit Role = **Viewer**, 헤더 "You are a Viewer" 확인)

- ✅ Cloud 대시보드에서 Viewer는 LNB에 Team settings 미노출(Editor와 차이)
- ⚠️ **Viewer가 Connect Home 진입 가능** — spec(F-IDM-edit-role/connect-entitlement)은 "Viewer Connect 진입 차단" 기대, 실제는 차단 없이 진입(단 TD는 Viewer Home 시나리오 정의 → spec↔TD 충돌; 데모는 TD쪽)
- ✅ Viewer Home에서 팀 탭 2개 정상 표시·전환
- ❌ **Viewer Home에 "+ New cloud stage" 버튼 노출됨** — TD는 Viewer에게 숨김 명시 → 게이팅 누락
- ⚠️ (정정됨 — 아래 "🔁 2차 심화 검증" 참조) 이 시점엔 `default-stage` URL 직접 접근 시 풀 Edit Mode가 열려 "RBAC 전무"로 판단했으나, **2차 검증에서 이는 default-stage(특수 비보호 stage) 한정 현상**으로 확인. 실 Cloud Stage는 viewer 접근 시 읽기전용 View/Interact로 게이팅됨. **진짜 갭은 "Viewer가 본인 stage를 생성·편집 가능"(entitlement 게이트 누락).**
- ❓ Viewer Preview View↔Interact / 권한별 링크 → 2차 심화 검증에서 모두 확인 완료(아래 참조)

---

## 📌 종합 요약 (Claude + Codex 세션 통합)

### 잘 구현된 영역 (구조·핵심 플로우)
- Connect Home: 팀 탭(멀티팀), Stage 리스트/카드, New stage, Edited 날짜
- Edit Mode: GNB(팀/스테이지명·PIN·Custom fonts·Run·Share), Canvas(빈상태·줌·전체화면·BACKGROUND), Groups/Layers 패널, 레이어 추가(From Cloud→Cloud Finder 모달/Web embed/Live Camera), 레이어 속성(이름·URL·Position·Size)
- Console: Message 테이블(Time HH:MM:SS:MMM)·Send Message(Message/Value/⌘+↵ 동작)·Filter·Record 진입점
- Share: Copy link to editor / stage viewer / Pie previews, Link to stage 설정(Background/Hide hotspot/cursors/UI/Scale to fit), join URL
- Nav 메뉴, 로그인 진입점(General/Enterprise)

### 미구현·차이·버그 (우선순위순)
1. ⚠️(정정) **RBAC는 부분 동작** — 타인 stage 접근은 차단(viewer→404/읽기전용 View/Interact, Run·Share 없음). 단 **Viewer가 본인 cloud stage를 생성·풀편집 가능**(Connect entitlement 게이트 누락, P1) + **default-stage는 권한 우회 가능성**(P0 의심, 보안 확인 필요). ※ 상세는 "🔁 2차 심화 검증" 참조
2. ❌ Web embed가 프로토콜 없는 URL(`wikipedia.org`)에서 무음 실패 — `https://` 필수 (TD 정상 기대값)
3. ⚠️ Home 카드 우클릭 메뉴 빈약(Rename 비활성 + Delete만); Duplicate/Handoff/Archive 없음(Cloud는 Archive여야)
4. ⚠️ `Archived stages` = disabled "coming soon" placeholder (미구현)
5. ⚠️ Cloud LNB→Connect 진입 라우팅 미완성(/t/ 프로젝트홈으로 이동), /connect 직접 접근이 팀 컨텍스트 의존(첫 진입 시 "Where is my pie?")
6. ⚠️ Preview Mode 전용 레이아웃 미흡(좌측 패널 미숨김, View settings 불명확)
7. ⚠️ 레이어 추가 메뉴에 Unity 노출(TD 미노출 기대), Pie 별도 항목, 그룹 기본명 "New Group"(TD: Group n)
8. ⚠️ Web embed 레이어명이 URL 아닌 "Web embed" 고정, 기본 Size 0,0
9. ⚠️ PIN "Reconnecting…" 고착으로 PIN/Player 연결 검증 차단; i18n 미완성(한영 혼용); owner License "Connect Free" 표기; default-stage 비영속 정황

### 점검 한계
- owner 단일 팀·local(default)성 stage만 보유 → Cloud 영속 stage 시나리오(Pie 레이어 실동작, 권한별 공유, 썸네일, View more/정렬) 미검증
- viewer 열람 가능 cloud stage 부재 → Viewer Preview(View/Interact) 정상 경로 미검증
- PIN/Player·하드웨어·Custom Plugin(Enterprise)은 환경상 범위 외

---

## 🔁 2차 심화 검증 — 2026-06-10 (Claude, owner 새 Cloud Stage 생성 + viewer 교차) ‼️ 앞선 RBAC 결론 정정

owner로 **새 Cloud Stage(영속, ULID `01KTREVH…`)를 직접 생성**하고 실제 Pie를 올린 뒤, 로그아웃/viewer로 교차 접근하여 앞선 "default-stage" 기반 결론을 재검증함. **결과: 앞선 "RBAC 전무 P0" 결론은 default-stage(특수 비보호 stage)에 한정된 현상이었고, 실 Cloud Stage에는 권한 게이팅이 동작함.**

### Cloud Stage 영속성 / View more / 생성 — ✅ (이전 "비영속" 정정)
- ✅ "+ New stage"로 생성한 stage는 **ULID로 영속 저장**됨(재진입·새로고침 후 유지). 이전에 "비영속"으로 본 건 `default-stage-…`라는 **특수 stage** 한정 현상.
- ✅ Stage 3개 초과 시 **View more** 노출, 클릭 시 전체 표시.
- ⚠️ 새 stage 기본 이름 = ULID(친화적 기본명 없음). TD "생성 기본값 TBD".
- ⚠️ 새 stage 진입 시 **기본 Group 자동 생성 안 됨**("Create your first group" 빈 상태) — TD "기본 Group 1개 선택 상태로 열림"과 차이.

### PIN / Relay — ✅ 실 Cloud Stage에선 동작 (이전 "고착" 정정)
- ✅ 새 Cloud Stage는 **PIN 정상 발급**(예: `BQH252`, `FJT667`) + 초록 연결점. 세션마다 PIN이 **회전**함.
- ⚠️ 이전 세션들이 본 `PIN ------`/`Reconnecting…`은 **`default-stage`에 한정**. 실 Cloud Stage에선 재현 안 됨.

### Cloud Pie 레이어 추가 (From Cloud) — ✅ 동작
- ✅ Cloud Finder 모달: 스페이스 드롭다운(My pies / 팀), 팀 선택 시 **프로젝트 리스트**(Movie/Pi Burger Kiosk/Automotive Demo/Connect Cloud) + "+ New project".
- ✅ 프로젝트 진입 → **Pie 리스트(섬네일·이름·Updated 날짜)**(PhoneKey_CIIE/G29 Tester/Dashboard_CIIE/Cluster_CIIE). 뒤로가기 화살표.
- ✅ Pie 선택 → Open 활성화 → **Pie 레이어 추가 성공**, 캔버스에 **실제 Pie 화면 렌더**(잠금/사람 UI), Web embed는 example.com 실제 페이지 렌더.
- ✅ 여러 레이어 타입(Pie/Web embed/Camera/Unity) 공존.
- ⚠️ **렌더링 글리치**: 좌측 Groups/Layers 패널과 캔버스 Pie 콘텐츠가 겹쳐 보임(z-index/레이아웃 버그).

### 실시간 멀티세션 동기화 — ✅ (Connect 핵심)
- ✅ 같은 Cloud Stage를 다른 세션(병행 Codex)이 편집하자 **stage 이름·레이어가 내 화면에 실시간 반영**됨. 클라우드 통신/동기화의 핵심 동작 정황.

### Share Pie previews — ✅
- ✅ Pie 레이어를 올리자 Share 다이얼로그 **Pie previews에 Pie만 리스트업**(Cluster_CIIE/Dashboard_CIIE/PhoneKey_CIIE). Web embed/Camera/Unity 제외 — TD 부합.
- ✅ stage viewer 링크 = `/connect/join/{stageId}?pin={PIN}` (PIN이 쿼리에 포함).

### 권한별 링크 접근 (TD 4계정 상태) — 핵심 정정
1. ✅ **로그아웃 + editor 링크**(`/connect/stages/{id}`) → **로그인 페이지로 리다이렉트**(`?retUrl=…` 보존). spec F-IDM-cookie-jwt 부합.
2. ✅ **로그아웃 + viewer(join) 링크** → **"Join Stage"** 화면(이름 입력 + STAGE PIN 자동입력 + JOIN). Cloud 로그인 불필요(게스트 진입). 단 **Join 시 "This PIN has expired or the stage is no longer available."** → PIN 회전/호스트 세션 종료로 링크 PIN이 무효화됨.
3. ✅✅ **Viewer 로그인 + editor 링크** → stage가 **View/Interact(읽기전용) 모드로 오픈**. **Run/Share 버튼 미제공**. Edit/Preview 탭·편집 진입점 없음. **= Edit Role 기반 RBAC 동작!** (TD "Viewer 권한 Stage Preview Mode: View↔Interact" 부합)
   - ⚠️ 단 **첫 접근(로그인 리다이렉트 직후)엔 404 "Where is my pie?"** → reload 시 정상 Viewer 모드. 로그인 직후 타이밍/캐시 이슈 의심(재현성 있음).
   - ⚠️ TD가 기대한 viewer의 "접근 불가 안내 + Go to ProtoPie Cloud" 화면은 (편집 불가 케이스에서) 일반 404로 대체됨 — 카피/화면 차이.
4. ✅ **View ↔ Interact 토글** 정상 전환 동작.

### ‼️ RBAC 결론 정정 (이전 §"Viewer 롤" 및 Codex P0 의심 갱신)
- **default-stage(`default-stage-…`)**: 특수/비보호 stage로, viewer·로그아웃 불문 **편집 UI가 열림** → 이전 두 세션이 P0로 본 근거. 실제론 이 default-stage가 권한 예외 케이스(데모/샌드박스성 stage로 추정).
- **실 Cloud Stage(ULID)**: viewer 접근 시 **읽기전용 View/Interact 모드**로 게이팅됨(Run/Share 없음). **RBAC는 실 stage에서 동작**.
- → 남은 진짜 이슈: ① **default-stage가 권한 우회 경로**인지(보안), ② viewer editor-링크 **첫 접근 404→reload 정상**(타이밍 버그), ③ **Viewer가 stage 생성·편집 가능**(아래 확정), ④ **공유 링크가 PIN 회전/호스트 종료로 깨짐**(영속 공유 전제와 충돌).

### ‼️ Viewer의 stage 생성 권한 — 확정된 RBAC 갭 (entitlement 게이트 누락)
- ✅ 확인: Viewer 계정으로 "Connect Cloud/Desktop" 탭 → 팀의 기존 cloud stage 5개는 **viewer에게 미표시**("No active stages"). 즉 **남의 stage 열람/편집은 차단**(404/읽기전용).
- ❌ **그러나 "+ New cloud stage" 클릭 시 새 stage가 실제 생성되고 풀 Edit Mode로 열림**(Edit/Preview·Run·Share·+Group·PIN 발급 모두 가능). 생성자=Stage owner가 되어 자기 stage는 풀 편집.
- → **Connect 사용 자격(Edit Role ≥ Editor, F-IDM-connect-entitlement)이 stage 생성 경로에 미적용**. Viewer가 Connect를 사실상 사용 가능. **Beta QA 전 수정 필요(P1).**
- 정리: 권한 모델이 "타인 stage 접근(✅ 차단)"엔 동작하나 "본인 stage 생성(❌ 허용)"엔 entitlement 게이트가 빠짐.

### 추가 확인된 동작
- ✅ Web embed URL 검증 재확인: `https://` 전체 URL은 정상 추가, 프로토콜 없는 `wikipedia.org`는 Add 눌러도 무반응(2회 재현). → 무프로토콜 입력 처리 버그.
- ✅ 로그인 페이지 General/Secure Enterprise 토글, 멀티팀(viewer=2팀) 재확인.
