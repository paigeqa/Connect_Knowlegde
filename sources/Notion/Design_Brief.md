# Connect on Cloud (Design Brief)

> Notion 최종본 아카이브 · 원본: https://app.notion.com/p/35945184b5da80318a48ef76a9ce69ca
> Notion view 시점: 2026-07-03T04:07:01.809Z
> CoC 스쿼드 종료(2026-06-30) 인수인계용. 원본 마크다운(표·구조) 보존. 이미지/다이어그램은 `[이미지: Notion 원본 참조]`로 표시(마크다운 미전송).
> Designer: Product Design Team · Status: In progress

---

# 1. Background
## Why?
### Re-discovering Connect's value
**Connect on Cloud aims to lock in existing customers, and it serves as the foundation for advanced features many users have requested.**

## Related features enabled by this concept (tentatively out of scope)
### A. Connect on the cloud environment
> Migrating the entire Connect experience to the cloud so prototypes are reachable from anywhere, not only from inside a LAN
- Today Connect runs on `localhost:9981` and a LAN, which forces remote workflows into ngrok-style workarounds that enterprise IT often blocks (e.g. Zillow Group). Cloud relay removes that barrier.
- Customers including Zillow Group and Disney Streaming want to share API-integrated prototypes via a single link without exposing internal networks.
- Canny request: [Notion 링크]

### B. Stage view from the Player
> Bringing Stage-only capabilities (web embed, Unity, live camera) into the native Player experience
- Customers including Toyota Japan, TomTom, Amazon and Zoox want the web embed layer in the stage supported on the Player.
- Customers including Aston Martin want the Unity embed layer supported on the Player.
- Today Stage View opens in a desktop browser, which fails the moment a tester opens it on a phone: Toyota Japan reports a desktop UI rendered on mobile, TomTom reports browser address bars breaking presentation mode, Amazon reports iPad cannot reach `localhost` Connect at all.

### C. User testing
> Combining Connect-driven prototypes with the existing User Testing product so hardware-aware sessions can run moderated or unmoderated
- Connect-aware UT is the largest concentrated cluster of asks: Johnson & Johnson, Mindray, Inovance, Midea, Hyundai, Google Wearable UX, and Samsung DA all need UT sessions where the prototype is driven through Connect (hardware, multi-device, or API).
- Unmoderated UT requires a public URL participants can open without an app or account — only practical once Connect itself is web-based.
- Unlocks scenarios that fail today: hospital device + mobile companion test (Mindray), simultaneous eye-tracking + Connect telemetry (Inovance), multi-screen home-appliance + companion app (Samsung DA).

### D. UX Enhancements
> Improving the presentation of the current state of connected prototypes
- Today Connect cannot reliably tell the prototype whether `Listen` succeeded, and the prototype cannot reflect connection state back to the user.
- Cloud-grade Connect should let live status (connecting / connected / dropped / version mismatch), member presence, and message-level debugging be redesigned into the surface designers and testers actually look at.
- "Connect debugging UX" appears repeatedly in customer asks, including from automotive and medical OEMs.

### E. Webhook
> Letting external services trigger and observe Connect events over the open internet, not only the LAN
- Today the IFTTT-style webhook plugin runs against `localhost:9981`, restricting triggers to the same machine and network. Once relay lives in the cloud, webhooks become first-class endpoints that any service (IoT cloud, monitoring, AI agent) can call.
- Forms one half of a programmatic surface that, together with G. Send/Receive SDK, lets non-Studio software participate in a stage.

### F. Extending Bridge App ecosystem
> Moving Bridge App from a local-only Enterprise feature toward a cloud-distributable, AI-extensible plugin platform
- Connect's plugin model is a 3-Layer Plugin Framework: Built-in (USB HID, Serial, MQTT), Official (HTTP, IFTTT, Firmata, Gamepad), and Custom Bridge App. New protocols (MIDI, BLE, UDP) have all entered the ecosystem as Bridge Apps without core engine changes.
- Cloud relay enables Bridge Apps to be distributed, signed, and discoverable rather than shipped as ad-hoc executables, and aligns with the AI-agent direction (Claude Agent SDK-based generation, BridgeBuddy).
- Unblocks long-tail enterprise asks (Zoox BLE, Naver Labs robotics) that the core team cannot ship one-by-one but customers can ship for themselves once distribution exists.

### G. Send/Receive SDK
> Opening the Connect protocol so any device, AI agent, or service (not just Studio and Player) can publish and subscribe to a stage
- Today Send/Receive is a closed loop between Studio, Player, and Engine; every external integration is gated on ProtoPie's internal team.
- **Connect ProtoPie prototypes with open spec layer:** Publish the Connect protocol as a public, language-agnostic spec so any tool or device can connect. Support text, image, and voice payloads. The goal is to become the default standard for simulating complex hardware interactions.
- Strategic payoff: customers like Naver Labs, Zoox, and AI-native device makers can build their own integrations, generating reference implementations across robotics, automotive, and AI hardware.

---

# 2. Specification
> 관련: SSOT (Notion `36c45184b5da80788b6ce0e2ee7aedfe`)

## 용어 정의
### Connect on Cloud
- Connect의 클라우드용 환경
- **Bridge App, 플러그인은 최초 스콥에선 대응하지 않음**
- Cloud 진입 시 UT처럼 SNB에서 접근 가능
  - 접근 권한은 클라우드에 로그인한 회원 권한으로 판단

  |  | Viewer | Editor |
  |---|---|---|
  | Add-on 있음 + CBT listing | 접근 권한 없음, 메뉴 미노출 | **접근 권한 있음, 메뉴 노출** |
  | Add-on 없음 or not listed | 접근 권한 없음, 메뉴 미노출 | 접근 권한 없음, 메뉴 미노출 |

- 접근 권한 없는 사용자가 CoC Home으로 접속할 경우 경고 노출

### Connect Desktop (=Desktop app)
- Local stage를 생성/조회/편집할 수 있음
- Cloud stage를 직접 열거나 만들 수 있음
  - 이 경우에도 Stage는 Team space에 종속되며, 동일 Team space 내 파이만 활용 가능
- Bridge App 및 프리셋 플러그인 지원

### Stage
- Stage는 server + Pie 정보 + 그룹별 데이터를 총합한 개념임
- **Legacy Connect의 Group 위 상위 개념 (Project 개념)**
- Stage 하나가 여러 group을 포함할 수 있음

#### Local stage
- Local server(127.0.0.1, 192.168.*.*)를 가진 스테이지
- Desktop app에서만 제작할 수 있음
- 클라우드 파이, 로컬 파이 모두 등재 가능
- 다만 라이선스 키를 통해 로그인할 경우 클라우드 파이 사용 불가
  - 클라우드 인증 정보가 만료되거나, 라이선스 키만 등록된 유저가 클라우드 파이가 포함된 local stage를 열 경우, refresh 시 경고 노출

> **추후 고려 필요**: `.stage` 등 별도 포맷을 통한 export?

#### Cloud stage
- **최초 스펙에선 UT Testing room을 벤치마킹해서 권한 관리 설계**
- 클라우드 파이(같은 Team space에 있는 것만)만 등재 가능
- Desktop app에서 직접 열어 local stage의 일부 기능 사용 가능
  - USB, 로컬 네트워크 통해 플레이어 연결
  - Plugin 지원

#### Instance
- **Stage, Pie preview, Player 등에서 열린 파이는 단일 상태를 공유하지 않고, 인스턴스끼리, 또는 인스턴스 내부에서 인터랙션을 주고 받음**
- **Connect mode, Preview mode에서 Run 액션을 통해 모든 인스턴스를 초기화할 수 있음**
- Stage: 열리는 때에 인스턴스 생성 (Editor ↔ Preview 전환 시엔 상태 유지되어야 함)
  - Embed layer도 인스턴스의 일부처럼 동작
  - 예를 들어 한 유저가 자신의 스테이지에서 카메라를 연결해도 다른 유저에게 보이지 않음
- Per-pie preview: 열리는 때에 인스턴스 생성
- Player: 연결되는 때에 인스턴스 생성 (연결 해제 후 다시 연결할 경우 인스턴스 다시 생성됨)

> **추후 고려 필요**
> - Cloud stage를 local stage로 duplicate
> - Instance간 동기화: 현재는 각 인스턴스 생성 이후에만 메시지 내역이 반영되므로 인스턴스간 상태 불일치가 자주 발생함
> - 현재 상태의 Snapshot을 인스턴스 생성 시 동기화해주는 기능이 필요할 수도

### Capability matrix

| Capability | CoC | Desktop, Log-in | Desktop, License key |
|---|---|---|---|
| CRUD Cloud stage | O | O | X |
| CRUD Local stage | X | O | O |
| Add pie to stage | Cloud Pie → Cloud Stage만 | O | Local Pie → Local Stage만 |
| Plugin | X | O | O |

### 권한
#### Editor
- Stage 주인: local stage의 경우 desktop app이 열려 있는 컴퓨터, cloud stage의 경우 editor 권한이 주어진 유저(들)
  - Cloud stage의 경우 해당 스테이지가 소속된 Team space의 editor role에 따름
- Participant의 모든 권한 가짐
- Public preview를 publish / unpublish할 수 있음

| | |
|---|---|
| 편집 관련 기능 | 가능 |
| Preview 관련 기능 | 가능 |
| Player 관련 기능 | 가능 |

> **추후 고려 필요** — 권한 관리 (Cloud 한정): Stage에도 Pie 수준의 권한 관리 제공
> - Cloud stage의 editor는 스테이지를 Shared(Team space의 모든 member의 스테이지 리스트에서 노출됨) / Private (링크 통해서만 접속 가능)으로 설정 가능
> - Private stage의 경우, editor가 같은 Team space에 소속된 다른 유저를 editor 혹은 guest로 추가할 수 있음

#### Participant (Guest/Viewer)
- Local 네트워크 혹은 link로 접근 후 Passcode 통과한 유저
- Guest ↔ Viewer 간 전환 가능
  - Public preview의 설명에서 'Interact mode'는 guest, 'View mode'는 viewer에 대응
  - 최초 입장 시 Viewer

| 기능 | Guest | Viewer |
|---|---|---|
| 레이어 CRUD | **불가능** | **불가능** |
| 플러그인 연결 | **불가능** | **불가능** |
| 파이 인터랙션 | 가능 | **불가능** |
| Player 관련 기능 | **불가능** | **불가능** |

### Plugin
- Desktop app에서만 이용 가능
- 플러그인 연결 정보는 앱에 종속됨
  - 즉 모든 Stage에 같은 리스트, 같은 정보 노출
- 기존 legacy에서 지원되던 플러그인 전부 지원

#### Backstage
- Plugin, Pie의 메시지 플로우를 확인할 수 있는 Stage 하위 기능
- Editor, preview 모두에서 확인 가능
- 각 플러그인과 파이는 노드가 되고, Connect hub에 모든 노드가 연결된 형태
- 노드 ↔ Connect hub 사이의 메시지 trigger를 비주얼로 확인 가능

## Artifact diagram
[이미지: Artifact diagram — Notion 원본 참조]

---

# 3. Design spec
> Design audit (Notion `37c45184b5da801b8399d37b259a8b22`) / Events (Notion `38345184b5da80cbab50c0a4c03b149b`)

## a. Log in
[이미지: Log in — Notion 원본 참조]

#### 1. License key
- License key를 발급받아 인증하는 방식
- **인터넷 연결 없이도 로그인 가능하**나 사용상 제약이 있음
  - **Cloud stage 조회 및 복제 불가**
  - **Local stage에 Cloud pie 추가 불가**
- License key로 로그인하더라도 Cloud login 진행할 수 있음
  - 이 경우 Cloud login 유저의 기능 범위를 이용 가능 (2. Log-in via Cloud로 업그레이드된 것)
  - Cloud logout할 경우 license 버전으로 복귀 (기존 키 값 로컬에 저장)

#### 2. Log-in via Cloud
- 브라우저로 연결해서 로그인 후 앱으로 리디렉팅되는 방식
- General cloud / Enterprise 선택하여 로그인 가능
- 현재 Connect app에서 제공하는 방식과 같음

## b. Home
[이미지: Home — Notion 원본 참조]

### Nav bar
[이미지: Nav bar — Notion 원본 참조]

| CoC | Desktop, Log-in | Desktop, License key |
|---|---|---|
| **앱 메뉴 (커넥트 심볼)**<br>• Go back to Cloud: 현재 로그인된 계정의 클라우드 홈으로 이동<br>• Documentation<br>• Download desktop app<br><br>**유저 메뉴 없음** | **앱 메뉴 (커넥트 심볼)**<br>• Settings<br>• Documentation<br>• Visit homepage<br><br>**유저 메뉴 (계정명)**<br>• License type (Connect core, etc)<br>• URL to Cloud<br>• License settings<br>• Log out | **앱 메뉴 (커넥트 심볼)**<br>• Settings<br>• Documentation<br>• Visit homepage<br><br>**유저 메뉴 (계정명)**<br>• License settings<br>• Log in |

### Cloud stages

| CoC | Desktop, Log-in | Desktop, License key |
|---|---|---|
| O | O | X |

#### Team space tab strip
[이미지: Team space tab strip — Notion 원본 참조]
- 로그인한 유저가 커넥트 접근 권한(팀이 Add on 구매 및 유저가 editor role)을 갖고 있는 팀들을 횡방향 나열
  - 접근 권한 있는 팀이 없고 embedded license 등록되지 않았을 경우 라이선스 없음 케이스로 fallback ([Figma node 968-75957](https://www.figma.com/design/A9BgGUCeTzAzYg9ghokqz1/Connect-v3?node-id=968-75957))
  - Self-serve의 경우 Tab strip 노출하지 않음
- Width overflow시 pagination
- 팀 나열 순서는 클라우드의 팀 나열 순서와 동일함

#### Stage list
- 최근에 업데이트된 순으로 정렬됨
- 최초 로드되는 스테이지 수는 3개, 이후 View more 클릭 시마다 4개 추가로 로드
- 스테이지 카드에 우클릭할 경우 Context menu 노출
  - Desktop app, Cloud stage / Cloud stage on Cloud (각 Context menu — Notion 원본 이미지 참조)

#### Renaming
- 기존 스테이지 이름과 똑같은 입력값 입력할 경우 Confirm button deactivate

#### Archived stages
[이미지: Archived stages — Notion 원본 참조]

### Local stages 리스트

| CoC | Desktop, Log-in | Desktop, License key |
|---|---|---|
| X | O | O |

#### Cloud stage와 차이
- Archive 대신 delete할 수 있음

## c. Stage
- Default names: 최초 생성 시 아래 이름으로 만들어짐
  - Stage: "Untitled Stage"
  - Group: "Group N"

### View modes
#### Connect mode
- Pie, embed layer를 추가하고 배치할 수 있는 view
- Player 또는 Pie preview에서 인터랙션이 일어나면 화면에도 반영됨

| 분류 | 편집 관련 기능 | Preview 관련 기능 | Player 관련 기능 |
|---|---|---|---|
| Pie | • Add<br>• Remove<br>• Replace<br>• Reload (Update) | • Per-pie preview | • QR<br>• USB<br>• Replace source |
| Embed | • Add<br>• Configure: Web URL, Camera (Source, Fill/Fit, Stage)<br>• Remove | • Preview on Stage instance | - |
| Plugin **(Desktop app)** | • Plugin 연결<br>• Bridge app 추가 | • Backstage | - |
| Canvas | • Resize<br>• Move | • Preview on Stage instance | - |
| Console | - | • View log<br>• Record log<br>• Import: playback settings | - |

#### Preview mode
- Stage editor에서 편집 관련 기능이 비활성화된 view

| 분류 | 편집 관련 기능 | Preview 관련 기능 | Player 관련 기능 |
|---|---|---|---|
| Pie | N/A | • Per-pie preview | • QR<br>• USB<br>• Replace source |
| Embed | N/A | • Preview on Stage instance | - |
| Plugin **(Desktop app)** | N/A | • Backstage | - |
| Canvas | N/A | • Preview on Stage instance | - |
| Console | - | • View log<br>• Record log<br>• Import: playback settings | - |

#### Guest/Viewer
- Stage link를 edit 권한 없는 사람이 접속할 경우 viewer로 접속됨
- 접속하기 위해서 PIN 입력 필요
  - PIN은 일정 시간마다 갱신됨
- View / Interact 모드 선택 가능
  - View mode: 파이 인터랙션 불가능, 메시지를 통한 상태 변경만 확인할 수 있음
  - Interact mode: 파이 인터랙션 가능

| 분류 | Preview 관련 기능 | Player 관련 기능 |
|---|---|---|
| Pie | • Per-pie preview | N/A |
| Embed | • Preview on Stage instance | - |
| Plugin **(Desktop app)** | N/A | - |
| Canvas | • Preview on Stage instance | - |
| Console | • View log<br>• Record log<br>• Import: playback settings | - |

#### ~~Public preview~~ `Not in this scope`
- 공개 링크로 공유되어 제삼자가 접속 가능한 view
- Editor가 publish, unpublish 가능

**Published**
- 로그인 여부, Team space member 여부와 관계없이 접근할 수 있음
- 파이별 프리뷰도 마찬가지

**Not published**
- Editor role만 접근할 수 있음 (Connect, Preview mode 접근 권한과 동일)
- Nav bar에 `Not published` 정보 표시
- 파이별 프리뷰도 마찬가지

---

# 4. Scenario
## i. Remote UX research
> **Context**: A UX researcher in Seoul runs a 1:1 usability test with a participant in Berlin on a new mobile payment flow. If the participant triggers the pay button in the prototype in the phone, than the POS machine in the hand of the researcher reacts.
- Host: Researcher creates the Cloud stage from her workspace, loads the banking Pie, and starts recording.
- Participant: Tester opens the invite link on their phone and drives the prototype.
- Viewer: Two product designers and a PM open the view-only link to watch live without affecting the session.
- Connected device: The participant's phone is paired with the POS machine.

## ii. Internal design review
> **Context**: Designer presents a pie working with a steering wheel in a review session.
- Host: Designer drives the pie and configure hardware settings from a single Cloud stage.
- Viewer: Stakeholders get a sharable link to test it by themselves.
- Connected device: Cloud stage preview reacts to the steering wheel in the review session.

## iii. Automotive HMI with Unity/Unreal runtime
> **Context**: Designer prototypes a steering-wheel infotainment interaction using a pie and a car interior model from Unity.
- Host: Designer creates a Cloud stage, loads the HMI Pie, and configures the Unity/Unreal embed layer.
- Viewer: Stakeholders open the view-only link to observe and review.
- Connected device: A steering wheel or other input hardware is connected to drive the runtime and prototype.

# 4. Timeline
## 1주차 2026-05-11 - 2026-05-15
**Design Handoff ETA: 2026-05-15 오후**
- 디자인 시스템 구축 + 클라우드 환경에서 기존 커넥트 기능 rework
  - Cloud 진입점
  - Stage, API & Hardware settings, Log 1단계
- 전체 Flow + Spec 초안

## 2주차 2026-05-18 - 2026-05-22
- Desktop app용 기능
- Bridge app, Local pie 추가
- 추가 기능
- Stage view 뷰어 모드 대응

## 3주차 2026-05-25 - 2026-05-29
- Advanced 기능 대응
- Log 2단계 (디버깅)
- 1/2주차 follow up

## 4주차 2026-06-01 - 2026-06-05
- 온보딩
- 유저별 권한 메트릭
- 기타

# 5. Discussion
- 2026-05-26 User flow (Notion `36c45184b5da80d692a1c44b39915122`)
