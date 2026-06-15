---
doc_id: CC-SPEC
title: Cloud Connect — QA Feature Spec
purpose: Cloud Connect의 기능을 한 곳에서 추적하고, 테스트 계획·설계의 단일 참조점으로 사용한다.
audience: QA (신입~시니어), PM, Designer, Engineer
maintainer: Paige (QA)
sources:
  - PRD - Draft (Notion, 2026-05-16)
  - Connect on Cloud (Design Brief, Tay Jung, 2026-06-01 갱신본). `Notion 문서/Connect on Cloud (Design Brief) _ Notion_260601.pdf`
  - 2026-05-21 Home 화면 논의 회의
  - protopie_docs_connect.md (Legacy ProtoPie Connect 공식 문서)
  - "Intro to ProtoPie Connect" 강의 영상 자막 8편 (1-1, 1-2, 2, 3, 4, 5, 6, 7)
  - Legacy Connect (User Side) — Ike Sanghoon 작성, 2026-05-22 (사내 Legacy Connect 최고 사용자 기준 정답 문서)
  - TestRail S280 — 2.9.0 POR Plan (Plan entitlement, 309 cases). `이전 TestCase/connect_feature(2.9.0 POR Plan).csv`
  - TestRail S503 — Master Regression Suite (232 cases). `이전 TestCase/connect_regression_test_case.csv`
  - ACL (Notion 직접 확인, 2026-06-09). `Notion 문서/ACL _ Notion.pdf` (로컬 캐시) / Notion 원본: https://app.notion.com/p/36c45184b5da803bb98cd2f62f9f595d — 권한·플랫폼 기능 제약·Node View·Viewer 모드 토글 정의. 미결 사항 5건 잔존(§10 watch). rev10에서 부분 반영(§13 Δ-13~Δ-15), rev11에서 갱신본 반영, rev12에서 Notion 직접 확인 후 §4-8 Node View 접근 규칙·Imported Pie Persistence·WIP Q1/Q3/Q4 추가
release:
  beta_target: 2026-06-30
  dev_window: 2026-05-11 ~ 2026-06-15
  qa_window: 2026-06-16 ~ 2026-06-30
status_legend:
  CONFIRMED: 결정된 사양. 테스트 케이스 작성 가능.
  WIP: dev 5주 중 결정 예정. 결정 시점에 테스트 케이스로 전환.
  DEFERRED: 이번 Beta 범위 아님. 테스트 대상 아님.
last_updated: 2026-06-12 (rev 15)
---

# Cloud Connect — QA Feature Spec

이 문서는 Cloud Connect Beta의 기능을 QA 작업 단위로 정리한 명세다. PRD가 단일 진실 원천이고, 본 문서는 PRD 변경을 추적하며 테스트 계획·설계의 참조점으로 사용한다. 충돌 시 PRD 본문이 우선한다.

신입 QA가 처음 본다면 §1(용어)과 §2(아키텍처)를 먼저 읽고, 시니어가 회귀 범위를 잡는다면 §4(기능 명세)와 §6(에러 카탈로그)에서 시작한다. **레거시 Connect 경험자라면 §13(Legacy ↔ CoC Delta Matrix)을 먼저 본다** — 동작이 갈리는 지점을 한눈에 파악할 수 있다. ACL(Access Control List) 관련 정의는 §1 권한 모델 + §3 Capability Matrix + F-STG-stage-role + §4-8 F-VWR(Viewer 모드 토글) 4곳에 분산되어 있으며, ACL 문서가 WIP 상태라 일부 항목은 WIP로 표시된다(§10 watch).

## 0. 한눈에 보기

Cloud Connect는 레거시 ProtoPie Connect를 신규 앱으로 재작성하면서 클라우드 통신을 새 축으로 추가하는 hybrid 제품이다. 모든 결정의 우선순위는 두 가지로 환원된다.

P1. 레거시 Connect의 사용자 가시 기능을 신규 앱에서 동등 이상으로 보장한다.
P2. 핵심 워크플로가 클라우드 환경에서 동작한다.

판매 모델은 ProtoPie Cloud의 Addon이며, Team이 결제·격리·UI 노출의 root이다. User identity와 Team 멤버십은 ProtoPie Cloud API가 single source of truth이고 Connect는 저장하지 않는다. JWT에는 Cloud user ID만 들어가며, 권한 판정은 매 요청 Connect 서버 미들웨어가 Cloud API를 호출해 처리한다.

Legacy Connect는 사용 등급이 3종으로 분리된다(Legacy Connect (User Side) 문서 기준). **Connect Free**는 기본 제공이고, Connect Core는 Basic/Pro 플랜의 애드온이며, Connect Enterprise는 Enterprise 구독에 기본 포함된다. Beta(Cloud Connect)는 이 3등급 체계를 동등 보장하며, §3-2에 플랜별 정량 한도 매트릭스를 둔다. 본 spec에서 "Pro 구독" 표기는 Core 등급을 가리키고, "Enterprise 구독"은 Enterprise 등급을 가리킨다(혼용 시 Legacy User Side 문서가 정답).

배포 형태는 두 가지이며 **둘 다 Beta 출시 범위**에 포함된다. Self-serve는 `.io` 도메인의 공유 multi-tenant 클라우드(B2C silo, AWS ECS Fargate + RDS Multi-AZ)로, Plan별로 Connect 사용 가능 여부가 다르다. Enterprise는 회사별 전용 서버(B2B silo, EKS namespace + CNPG Postgres)이며, Plan gate 없이 Edit Role이 Editor 이상이면 누구나 Connect를 사용할 수 있다. QA 작성 순서는 Enterprise 기준 케이스를 먼저 정리한 뒤 Self-serve의 Plan entitlement 케이스를 덧붙이는 방식이다(출시 범위와 작성 순서를 혼동하지 않는다).

Beta scope는 클라우드 통신 모드를 기본 축으로 두되, 로컬 서버 단독 모드를 함께 지원한다. 정량 SLA는 약속하지 않는다(레거시 사용 데이터 기반 baseline을 도출한 뒤 §8에서 확정).

## 1. 용어 정의

QA가 테스트 케이스 카피·버그 리포트에 사용하는 용어는 아래 정의를 따른다. UI 노출 가능 여부는 회귀 시 카피 검증의 참조점이다.

| 용어 | 정의 | UI 노출 |
|---|---|---|
| Team | 결제·격리·UI 노출의 root 단위. 한 사용자가 여러 Team에 동시 소속할 수 있다(Slack 워크스페이스 모델). | O |
| Stage | Team 안에서 Pie·플러그인·Relay·stageview를 격리하는 영구 작업 공간. Discord 채널 모델. | O |
| Cloud Stage | Cloud Postgres에 저장된 Stage. Cloud 로그인이 필요하다. **Beta에서 Private/Shared 구분은 scope 제외 — 단일 공유 모델로 운영**(rev10 ACL §6, §13 Δ-14). Cloud Web과 Desktop Cloud-login 두 모드 모두에서 생성 가능(§13 Δ-13). | O |
| Local Stage | Desktop 앱에 임베드된 Postgres에 저장된 Stage. 단일 PC·단일 사용자 한정(외부 공유 개념 부재). 라이센스 키 단독 모드에서도 동작한다. | O |
| Group | Stage 안에서 Pie를 묶는 **필수 컨테이너**. 1 level만 지원한다(Group 안의 Group은 금지). 삭제 시 안의 Pie가 함께 삭제된다. 모든 Pie는 반드시 Group에 종속되어야 하며, Stage root에 Pie를 직접 배치할 수 없다. | O |
| Pie | ProtoPie 프로토타입(.pie). **반드시 Group 안에만 위치한다**(Stage root 배치 금지). 빈 Stage에서는 Group을 먼저 생성한 뒤 그 Group을 선택해야 Pie 추가가 가능하다. | O |
| Stage View (Web) | Stage를 웹 브라우저에서 여는 작업 공간. URL은 `{server}/stages/{stage-id}` 패턴. 한 화면에서 여러 Pie를 동시에 실행하고 **편집까지 가능**. Pie 간 메시지(send/receive)가 이 안에서 라우팅된다 — "Connect"의 어원. F-VWR(외부 게스트 read-only Stageview)와 구분된다. | O |
| Pie View | 단일 Pie를 시청·실행하는 화면. Web(브라우저) 또는 Player(모바일·Wear OS 등 네이티브) 형태. | O |
| PieVersion | 같은 Pie의 업로드/import 단위 버전 row. 진행 중 세션은 자기 버전을 끝까지 사용한다. | 내부 |
| Instance | Stage·Pie preview·Player 등에서 **파이가 열릴 때마다 생성되는 실행 단위**. 인스턴스끼리 단일 상태를 공유하지 않고 메시지로만 인터랙션을 주고받는다. Stage는 열릴 때 생성(Editor↔Preview 전환 시 유지), Pie preview는 열릴 때, Player는 연결될 때 생성(재연결 시 재생성). Embed layer도 인스턴스의 일부(한 유저가 자신의 Stage에서 카메라를 연결해도 다른 유저에게 보이지 않음). 현재는 인스턴스 생성 이후의 메시지만 반영되어 인스턴스 간 상태 불일치가 발생할 수 있다(F-STG-instance-sync watch). 출처: Design Brief 260601 §2 용어 정의. | 내부 |
| Bridge | 사용자 PC에서 동작하는 Connect Desktop 앱. 로컬 에이전트 역할을 한다. | O |
| Device | Bridge가 설치된 PC. Team-scoped이고 Device 단위로 토큰을 발급·차단한다. | O |
| Relay Session | Stage 안에서 생성되는 ephemeral 세션. room_code는 세션 생애 동안만 유효하다. | 내부 |
| ViewerInvite | Stageview 외부 게스트용 토큰. PIN·공유 링크·QR로 표현한다. | O |
| View Mode | Viewer가 Stage에 진입했을 때의 **기본 상태**. Pie 시청만 가능하며 메시지 전송·인터랙션 차단. Node View 편집·Console 로그·Player 연결·하드웨어 등 모든 편집 액션 불가. ACL §3 정의(rev10). | O |
| Interaction Mode | Viewer가 화면 내 **개인 토글**로 View Mode에서 전환한 상태. Pie 실행·메시지 전송 허용. 단 Stage 편집·구조 변경은 어느 상태에서도 불가. 권한 관리가 아니라 mode 전환이며 Role은 viewer로 유지. ACL §3(rev10). | O |
| Participant | **Interaction Mode 토글 ON 상태**의 Viewer를 가리키는 행위자 호칭. 레거시 Connect의 "Guest/Participant" 개념이 mode로 흡수된 명칭이며, Role 전환이 아닌 mode 전환임에 주의(ACL §6 매핑, §13 Δ-15). | O |
| Self-serve | `.io` 도메인의 공유 multi-tenant 클라우드. B2C silo. Plan별로 Connect 사용 가능 여부가 다르다. | O |
| Enterprise | 회사별 전용 서버 배포. B2B silo(EKS namespace + CNPG Postgres). Editor 이상이면 Plan gate 없이 Connect 사용 가능. | O |
| ProtoPi Studio Channel | Pie ↔ Pie / Pie ↔ Plugin 간 메시지 라우팅에 사용되는 채널 식별자. 송신측·수신측이 동일 채널을 선택해야 한다. 채널 불일치 시 메시지는 silent drop된다(레거시 동작). | 내부 |
| Custom Plugin | 사용자가 외부에서 작성·패키징해 Connect에 import한 플러그인. `plugin(.exe)` + `metadata.json` zip 형식. **SDK는 공식 공개하지 않으며**(§7 Non-goals), 패키징·import 절차만 사용자에게 노출된다. Enterprise 구독 한정. | O |
| Bridge App | Node.js 기반의 외부 실행체로, 하드웨어 신호 ↔ Socket.IO 메시지를 양방향 변환·중계한다. API JSON 응답도 메시지로 변환 가능. Custom Plugin과 짝(Enterprise 한정). | O |
| Multi-view Group | 레거시 Connect에서 여러 Pie를 한 화면에 동시 실행·표시하던 그룹. Beta의 Stage View가 동등 이상으로 흡수한다. 단일 브라우저 탭에서 멀티스크린을 구현하며 배경색·크기·레이아웃 커스터마이징을 지원한다. | 내부(레거시) |
| Connect Free | 기본 제공 등급. 워터마크 표시, 동시 프로토타입/Player 2개, 플러그인 동시 1개·실행 3분 제한. | O |
| Connect Core | Basic/Pro 플랜 애드온. 워터마크 없음, 동시 무제한, API 플러그인 3개·플러그인 동시 3개. 본 spec의 "Pro 구독"이 이 등급. | O |
| Connect Enterprise | Enterprise 기본 포함. 모든 제한 해제 + Custom Plugin/Bridge App/Unity 양방향/스마트워치/커스텀 폰트/메시지 Recording & Playback 전용 기능. | O |
| Stage View 커스텀 레이어 | Stage 위에 얹는 외부 콘텐츠 레이어. Web Embed(URL/iframe — Maps·Spline·Rive·Bezi 등), Live Camera(USB 웹캠·노트북 카메라·HLS 스트리밍), Unity(WebGL 빌드) 3종. 플랜별 수량 한도가 다르다(§3-2). | O |
| Voice Prototyping | Voice Command Trigger / Speak Response / Listen Response를 Web Player에서도 사용. Chrome·Edge(Chromium) 최적화. 192.x.x.x IP 구성 시 일회성 브라우저 설정 필요. | O |
| Tenant | v0.7.0 이전 schema 잔재 용어. **UI 노출 금지**. | 금지 |
| Room | v0.8.0 이전 명칭. Stage로 통일했다. **UI 노출 금지**. | 금지 |

권한은 세 축으로 분리된다. **Team Role**은 팀 자체에 대한 관리 권한, Edit Role은 Cloud 콘텐츠(프로젝트·파이·라이브러리) 전반에 대한 권한, Stage Role은 Connect의 Stage 단위 권한이다. 세 Role은 독립이라 한 사용자가 같은 Team에서 `Team Member + Edit Role Editor + Stage A의 owner + Stage B의 viewer` 같은 조합을 가질 수 있다. Team Role·Edit Role은 ProtoPie Cloud가 SoT이고, Stage Role은 Connect가 SoT다.

**Team Role** (Cloud SoT, 3종):

| Role | 권한 |
|---|---|
| Owner | 팀의 주인. 팀 관리·팀원 관리 가능 |
| Admin | 팀 관리·팀원 관리 가능 (Owner와 동등 관리 권한) |
| Member | 초대된 멤버. 팀 관리 권한 없음 |

**Edit Role** (Cloud SoT, UT 권한 모델 기반, 3종):

| Role | 권한 |
|---|---|
| Moderator | Editor가 갖는 모든 권한 + User Testing 기능 사용 가능 |
| Editor | 프로젝트·파이·라이브러리 관리 가능. Studio·Connect 등 프로덕트에 Cloud 계정 인증으로 접근 가능 |
| Viewer | 프로젝트·파이·라이브러리 **조회만** 가능 |

**Stage Role** (Connect SoT, Stage 단위, 3종 — rev10 ACL 반영으로 부여 룰 명문화):

| Role | 권한 | 부여 방식 |
|---|---|---|
| owner | Stage 생성·삭제·멤버 관리 | **Stage를 생성한 사용자 1인**. Stage 단위 unique. Team Owner라고 자동 부여되지 않는다. |
| editor | Stage 내 Pie·Group·Plugin 편집 | **같은 Team에서 Cloud Edit Role이 Editor 이상(Editor 또는 Moderator)인 모든 유저에게 자동 부여**. 별도 명시적 추가 액션 불필요. Edit Role 강등 시 즉시 박탈. |
| viewer | Stage 내 자원 조회만 가능 (기본 View Mode) | **외부 게스트가 ViewerInvite 토큰(URL·QR·PIN)으로 진입한 상태**. Cloud 계정 불필요. Interaction Mode 토글 ON 시 행위자 호칭은 Participant로 전환되나 Role 자체는 viewer 유지(§1 용어 참조). |

신입 QA가 자주 혼동하는 지점: **Stage Role은 Cloud Edit Role과 독립이 아니라 부분적으로 연동**된다. 같은 Team에서 누군가의 Cloud Edit Role이 Editor로 승격되면 그 사람은 해당 Team의 모든 Stage에 editor 권한이 자동으로 생긴다. 반대로 Cloud Edit Role이 Viewer로 강등되면 Connect 진입 자격 자체가 사라져 Stage 진입이 차단된다(F-IDM-connect-entitlement). 즉 Stage editor 멤버를 일일이 부여하는 UI는 없다 — 이건 ACL WIP의 핵심 정정 사항이며 레거시 Connect의 명시적 멤버 관리 모델과 다르다(§13 Δ-04 참조).

Connect 사용 자격은 배포 형태별로 다르다. **Self-serve**는 Team의 Plan이 Connect 사용 가능 Plan인지 + Edit Role이 Editor 이상인지의 AND 조건이고, Enterprise는 Plan gate 없이 Edit Role Editor 이상이면 사용 가능하다. Connect 진입 자격을 통과한 뒤, 각 Stage 안에서의 동작은 Stage Role이 추가로 게이트한다.

## 2. 아키텍처

QA가 알아야 할 만큼만 단순화한 액터 관계다. 버그 분류·재현 환경 구성에 사용한다.

```
User ──[로그인]──▶ ProtoPie Cloud  (인증·결제·Entitlement SoT)
     │
     └─[소속]──▶ Team A / Team B …
                  │
                  ├─ Bridge App (사용자 PC, 로컬 에이전트)
                  │    └─ 하드웨어 (USB·Serial·MQTT: Arduino, MIDI, G29, Gamepad 등)
                  │
                  └─ Connect Cloud (AWS)
                       ├─ B2C silo : 공유 multi-tenant (ECS Fargate + RDS Multi-AZ)
                       └─ B2B silo : 회사별 전용 (EKS namespace + CNPG PostgreSQL pod)
                       │
                       ├─ Cloud API  (Fastify + Prisma 7)
                       ├─ Relay      (Socket.IO + Redis pub/sub)
                       └─ Web Dashboard (브라우저)
```

스택은 Fastify + Socket.IO + Prisma 7 + PostgreSQL + Redis다. `@ppc/local-server` 라이브러리 한 벌이 Desktop child fork, B2C 컨테이너, B2B EKS pod에서 동일하게 부팅된다. B2C와 B2B는 schema·코드·RLS 정책이 같고 호스팅 위치만 다르다. 모든 테이블에 `team_id` 컬럼과 RLS가 적용되어 Team 간 자동 격리가 보장된다.

## 3. 모드별 가용성 (Capability Matrix)

사용자가 어떤 모드로 접속했는지에 따라 가용 기능이 다르다. 모드 전환 시 가용성 변화가 즉시 반영되는지가 회귀 우선이다.

| Capability | Cloud (브라우저) | Desktop, Cloud 로그인 | Desktop, License key | Embedded (터미널) |
|---|---|---|---|---|
| Browse Cloud Stages | O | O (브라우저에서 오픈) | X | — |
| Create Cloud Stage | O | **O** (rev10 ACL 정정) | X | — |
| Browse Local Stages | X | O | O | O |
| Create Local Stage | X | O | O | O |
| Add Cloud Pie to Local Stage | X | O | X | X |
| Local Pie Import (`.pie` 파일 업로드) | X | O | O | O |
| Custom Plugin Import (+버튼, 패키징된 zip) | — | O (Enterprise 구독 한정) | O (Enterprise 구독 한정) | O (Enterprise 구독 한정) |
| Preset Plugins (API/blokdots/Arduino/G29/IFTTT/Gamepad/Unity) | X | O | O | O |
| 하드웨어 연결 (USB·Serial·MQTT 등) | X | O | O | O |
| Cross-network 원격 연결 | O | X | X | X |
| Connect 없이 Studio ↔ Player 직접 통신 (2개 Pie 한정) | — | O | O | — |

**열 명칭과 ACL 매핑**: ACL 문서(§4)는 같은 매트릭스를 3컬럼(Cloud Web / Desktop App 로그인 / Desktop App License key)으로 표현하며 Embedded 컬럼이 부재하다. 본 spec의 4컬럼이 회귀 환경 매트릭스(§9)와 1:1 대응되므로 SoT는 본 spec이고, ACL 표는 Embedded를 후속 추가 대상으로 본다. 2026-05-28 정정 사항 = `Create Cloud Stage`의 Desktop Cloud-login 칸을 X→O로 정정(ACL §4 정합), `Local Pie Import`·`하드웨어 연결` 행 명시(ACL §4 정합·Embedded 컬럼 확장).

라이센스 키 로그인 상태에서 Cloud 로그인을 추가하면 capability가 즉시 확장된다. Cloud 로그아웃 시 라이센스 모드로 복귀하며, 키 값은 로컬에 보존된다.

Embedded Connect는 UI가 없는 환경(예: Windows 미니 PC)에서 터미널로 부팅하며, 라이센스 키 기반으로 디바이스별 관리된다. GUI 의존 동작은 부재하나 호스트 역할은 동일하게 수행한다.

### 3-2. 플랜별 정량 한도 매트릭스

Legacy Connect (User Side) 정답 문서 기준. Beta는 본 매트릭스를 동등 보장하며, Self-serve의 Plan gate가 본 매트릭스를 따라간다. **Pro Plan Before POR 1.5** 컬럼은 POR 1.5 이전 Pro 플랜 기본 포함 상태를 회귀 베이스라인으로 보존한 것이며, Beta 출시 시점의 SoT는 Free/Core/Enterprise 3열이다(Pro Plan은 historical baseline).

| 카테고리 | 기능 | Connect Free | Connect Core (lite) | Connect Enterprise (full) | Pro Plan Before POR 1.5 |
|---|---|---|---|---|---|
| Pricing | 가격 | Free | $20/month, $200/year | Enterprise 구독 기본 포함 | Pro Plan 기본 포함 |
| Core | 동시 실행 프로토타입 (Pies loaded) | 2개 | 무제한 | 무제한 | 무제한 |
| Core | Cloud Pies 추가 | ✓ | ✓ | ✓ | ✗ |
| Core | 로컬 Pie 사용 (Add Local Pies) | ✗ | ✓ | ✓ | ✓ |
| Core | 워터마크 | 있음 | 없음 | 없음 | 없음 |
| Core | 동시 Player 연결 (Mobile, Web/Stage) | 2개 | 무제한 | 무제한 | 무제한 |
| Core | Stage Views 수 (Multiview/Staging) | 1개 | 무제한 | 무제한 | 무제한 |
| Core | Available plugins | All Public | All Public | All Public + Custom | All Public |
| Core | API 플러그인 설정 수 | 1개 | 3개 | 무제한 | 무제한 (API plugin 1 instance만) |
| Core | 플러그인 동시 실행 | 1개 | 3개 (API plugin 최대 3) | 무제한 | 무제한 (API plugin 1 instance만) |
| Core | 플러그인 실행 시간 | 3분/activation | 무제한 | 무제한 | 무제한 |
| Core | Web Embed / Live Camera 레이어 | 각 1개 | 무제한 | 무제한 | 무제한 |
| Enterprise Diff. | Unity 레이어 (Embed Unity Layer) | ✗ | 1개 | 무제한 | ✗ |
| Enterprise Diff. | Custom Plugin & Bridge App | ✗ | ✗ | ✓ | ✗ |
| Enterprise Diff. | Unity Plugin (양방향 통신, Data binding) | ✗ | ✗ | ✓ | ✗ |
| Enterprise Diff. | 스마트워치 프로토타이핑 | ✗ | ✗ | ✓ | ✗ |
| Enterprise Diff. | 커스텀 폰트 지원 (user's plan 조건) | ✗ | ✗ | ✓ | ✗ |
| Enterprise Diff. | 메시지 Recording & Playback (CSV) | ✗ | ✗ | ✓ | ✗ |
| Enterprise Diff. | Connect Embedded (Raspberry Pi 등, 별도 라이선스) | ✗ | ✗ | ✓ | ✗ |

회귀 우선순위: ① 워터마크 노출/비노출이 결제 상태와 일치, ② Free 플러그인 3분 만료 후 동작 정의, ③ Core 동시 3개 초과 시 차단(API plugin은 최대 3 instance), ④ Unity 레이어 등 Enterprise 전용 기능이 Pro 구독자에게 비노출 또는 비활성, ⑤ Plan 다운그레이드 시 기존 import한 Custom Plugin 처리(WIP, F-IDM-plan-feature-matrix), ⑥ POR 1.5 마이그레이션 시 기존 Pro Plan 사용자의 Cloud Pies 불가 → Free/Core 전환 후 가용 검증.

**카피·노출 충돌 이력 (해소됨)**: Free 플랜의 `Web Embed / Live Camera 레이어`는 한글 자료에 `각 1개`(각 종류 1개씩 = 동시 2개 가능)로, 영문 자료에 `1 layer of either`(둘 중 하나만 1개 = 동시 1개)로 표기되어 있었다. 2026-05-27 Paige 결정으로 한글 기준 "각 1개"를 SoT로 확정. 영문 자료는 한글 SoT에 맞춰 후속 정정 대상이며, 회귀 케이스는 Web Embed 1 + Live Camera 1 동시 활성을 Free 플랜에서 허용한다.

## 4. 기능 명세 (F-* ID)

PRD §6의 prefix 체계 + 회의 결과로 추가된 F-HOM. 각 항목은 ID, 상태, 요구사항, 검증 포인트로 구성한다.

### 4-1. F-HOM — Home 화면·진입점

Cloud 홈화면과 Desktop 앱 첫 실행 화면은 동일 레이아웃·동일 소스 코드를 사용하고 데이터만 다르게 표시한다.

| ID | 상태 | 요구사항 | 검증 포인트 |
|---|---|---|---|
| F-HOM-shared-layout | CONFIRMED | Cloud 홈화면 + Local 첫 실행 화면 동일 레이아웃·소스 코드, 데이터만 차이 | 두 모드 UI diff가 데이터 표시 외에는 없어야 한다. 한쪽 수정 시 다른쪽 회귀 필수. |
| F-HOM-local-all-teams | CONFIRMED | 로컬에서는 Team 선택 없이 모든 Team space 표시 | Cloud 모드는 Team 선택 화면을 거치고, Local 모드는 거치지 않는다. |
| F-HOM-section-split | CONFIRMED | Local Stage와 Cloud Stage는 같은 화면에서 섹션으로 분리 | 섹션 헤더·구분선이 일관되게 표시된다. |
| F-HOM-url-teamid | CONFIRMED | URL에 Team ID를 포함한다 | URL 직접 입력·북마크·새로고침 시 컨텍스트가 유지된다. 권한 없는 Team ID 접근은 거부된다. |
| F-HOM-public-pie-only | CONFIRMED | Pie 목록은 Public Pie만 표시한다(Private/Public 구분 없이 Public만) | Private Pie는 절대 목록에 노출되지 않는다. |
| F-HOM-archive-tab | CONFIRMED | Archive는 soft delete이며 별도 탭으로 분리 | 메인 탭과 Archive 탭 전환·필터링이 정상 동작한다. |
| F-HOM-delete-no-restore | CONFIRMED | Delete는 존재하나 Restore는 제공하지 않는다 | 삭제 직후 복구 불가가 사용자에게 명확히 안내된다. |
| F-HOM-pagination | CONFIRMED (rev15, Design Brief 2026-06-12) | Stage 목록 로딩 방식 = **"View more" pagination**. 최초 로드 수는 **3개**, "View more" 클릭 시마다 **4개** 추가 로드. | 최초 진입 시 최대 3개 카드 표시 + View more 버튼 노출. 클릭당 4개 추가. 전체 목록 소진 시 View more 미노출. Cloud/Local 섹션 각각 독립 카운트 적용. |
| F-HOM-start-button | WIP | Start 버튼 도입 여부 검토 중. 브라우저 refresh와 역할 분리가 필요하며, 현재 상태 보존이 없어 의미가 제한적이다 | 결정 시 동작과 회귀 기준을 정의한다. |
| F-HOM-stage-date | CONFIRMED (rev13, Figma) | Stage 카드에 표시되는 수정 날짜 포맷 규칙. **당일**이면 `Edited on today`, 이전 날짜이면 `Edited on DD Month YYYY` (예: `Edited on 19 May 2026`) 형식으로 표시한다. | 당일 저장 후 "today" 표시, 하루 이상 지난 Stage는 절대 날짜(DD Month YYYY) 형식 표시, 자정 경과 시 today → 날짜 전환 회귀. Cloud/Local 섹션 양쪽 동일 포맷 적용. |
| F-HOM-stage-ctx-cloud | CONFIRMED (rev13, Figma) | Home의 **Cloud Stage 카드 컨텍스트 메뉴** 항목(오른쪽 클릭 또는 `···`). 순서: Duplicate / Rename / Handoff to local / Archive stage (destructive, 빨간색). 에디터 role이 아닌 경우 메뉴 자체를 노출하지 않는다 (Stage Role viewer 포함). | (1) Editor 이상: 4개 항목 모두 표시, Archive 선택 시 확인 다이얼로그. (2) Viewer 또는 비editor role: 컨텍스트 메뉴 진입점(버튼/우클릭) 비노출. (3) Handoff to local 선택 시 F-STG-handoff 플로우 진입. |
| F-HOM-stage-ctx-local | CONFIRMED (rev13, Figma) | Home의 **Local Stage 카드 컨텍스트 메뉴** 항목. 순서: Duplicate / Rename / Delete stage (destructive, 빨간색). Archive stage 없음(Local Stage는 archive 미지원). 에디터 role이 아닌 경우 메뉴 자체 미노출 — F-HOM-stage-ctx-cloud와 동일 게이트. | (1) Duplicate/Rename 정상 동작. (2) Delete 선택 시 복구 불가 안내 후 삭제(F-HOM-delete-no-restore 연동). (3) Cloud Stage 메뉴와 항목 수/종류 차이가 의도적임을 회귀 케이스로 명시: Local에 Archive stage 미노출, Cloud에 Delete stage 미노출. |
| F-HOM-stage-sort | CONFIRMED (rev15, Design Brief 2026-06-12) | Stage 목록은 **최근에 업데이트된 순**으로 정렬된다(사용자 변경 불가 — 정렬 컨트롤 UI 없음). | Stage 생성·업데이트 후 해당 Stage가 목록 상단으로 이동하는지 확인. Cloud/Local 섹션 각각 독립 정렬. 정렬 컨트롤 UI가 화면에 노출되지 않는지 회귀(2026-05-21 scope-out 결정 유지 — 정렬 UI 없이 고정 순서). |
| F-HOM-default-names | CONFIRMED (rev15, Design Brief 2026-06-12) | 최초 생성 시 기본 이름 — Stage: **`Untitled Stage`**, Group: **`Group N`** (N은 그룹 생성 순서 번호, 1부터 시작). | Stage 생성 직후 기본 이름 'Untitled Stage' 표시. Group 생성 시 'Group 1', 'Group 2' 순차 부여. Rename 후 다음 Group의 번호 증가 방식(이미 사용된 번호 재사용 여부) 정책 확인 필요(WIP). |

검증 우선순위: ① URL Team ID로 다른 Team 자원 접근 차단, ② Public Pie 정책 우회로 Private Pie 노출 차단, ③ Cloud/Local 두 모드의 레이아웃 회귀.

**레거시 v2.10.2 메인 화면 구성요소 (회귀 베이스라인)** — Beta 재작성 시 동등 보장 대상:

| 영역 | 구성요소 |
|---|---|
| 상단 좌측 | New, Group (생성 액션) |
| 상단 우측 | Run, Plugin |
| 좌측 패널 | Pie 목록(Group 폴더링, Pie 썸네일·이름·Updated·Connect 버튼·Multiview 모니터 아이콘) |
| 우측 패널 | 메시지 디버깅(Message·Value·Send 입력, Time·Message·Value·Pie·Source 로그 테이블) — F-BRG-16(Debugger 모드)의 베이스 |
| 우측 하단 | Import, Record(메시지 녹화), Clear |
| 하단 상태바 | 로컬 서버 주소(예: `127.0.0.1:9981`), Custom fonts 가용 상태, Connected Player 수(Multiview 포함), Connected Plugin 수 |

### 4-2. F-IDM — 정체성·인증·권한

| ID | 상태 | 요구사항 | 검증 포인트 |
|---|---|---|---|
| F-IDM-team-root | CONFIRMED | Team이 결제·격리·UI 노출의 root | Team 간 자원 누출 0건. |
| F-IDM-device-2tier | CONFIRMED | Team → Device 2계층. User identity는 Cloud SoT | JWT에 Team role이 들어가지 않는다. |
| F-IDM-nm-team | CONFIRMED | 한 사용자가 여러 Team에 동시 소속 | Team 전환 시 컨텍스트가 완전히 분리된다. |
| F-IDM-persisted-auth | CONFIRMED | 인증 상태는 DB/Redis에 영속 저장 | 서버 재시작 후에도 로그인 상태가 유지된다. |
| F-IDM-device-token | CONFIRMED | Device 단위 토큰 발급·revoke | 분실 신고된 Device만 차단되고 사용자 전체가 차단되지 않는다. |
| F-IDM-pin-24h | CONFIRMED | PIN + 24시간 토큰 인증 (레거시 동등, 저장소만 영속화) | 토큰 만료 후 자동 로그아웃. |
| F-IDM-pin-method | CONFIRMED | 게스트 진입은 PIN 방식으로 결정. 호스트 승인(30초 제한, UT 방식)도 검토했으나 PIN 유지. 추후 변경 여지 있음 | Unity 환경 등 typing 불가 환경에서의 UX 이슈는 알려진 한계로 인지한다. |
| F-IDM-cookie-jwt | CONFIRMED | Connect 주소 접속 시 Cloud와 동일한 로그인 확인 로직을 적용. Cookie는 항상 발급되며 JWT로 판별. 실패 시 로그인 페이지로 리다이렉트되고, Cloud 로그인 후 Connect로 재리다이렉트된다 | Cookie 미발급·JWT 만료·서명 위변조 시 모두 차단되는지. |
| F-IDM-license-then-cloud | CONFIRMED | 라이센스 로그인 상태에서 Cloud 로그인을 추가하면 화면이 즉시 업데이트되어 Cloud 모드 기능 범위로 확장. Cloud 로그아웃 시 라이센스 모드로 복귀하며 키 값은 로컬에 보존 | 모드 업그레이드/다운그레이드가 즉시 반영된다. |
| F-IDM-login-entrypoint | CONFIRMED | 로그인 진입점은 두 갈래로 분리한다. (a) **Log in** = Self-serve 진입(`.io` 공유 클라우드). (b) Log in with Secure Enterprise = Enterprise 진입, 전용 서버 주소 입력 필요. 레거시 v2.10.2 패턴을 Beta에서도 유지 | Enterprise 버튼이 서버 주소 입력 화면으로 이동한다. 잘못된 주소·도달 불가·인증서 오류 시 명확한 에러 카피가 표시된다. Self-serve 자격으로 Enterprise 주소에 로그인 시도 시 거부된다(반대도 동일). |
| F-IDM-team-role-cloud-sot | CONFIRMED | Team Role 3종(Owner/Admin/Member) enum만 spec. 권한 매트릭스 detail은 Cloud team-management API SoT | Cloud API 응답이 바뀌면 Connect 권한 판정이 따라가는지. |
| F-IDM-edit-role | CONFIRMED | Edit Role 3종(Moderator/Editor/Viewer) enum. UT(User Testing) 권한 모델 기반. Connect 사용 자격은 Editor 이상 | Editor 미만(Viewer) 계정이 Connect 진입·편집을 시도하면 차단된다. |
| F-IDM-connect-entitlement | CONFIRMED | Connect 사용 자격 = Self-serve: 사용 가능 Plan AND Edit Role ≥ Editor / Enterprise: Edit Role ≥ Editor (Plan gate 없음) | Self-serve의 Plan 다운그레이드, Enterprise의 Edit Role 강등 시 즉시 차단되는지. |
| F-IDM-perm-ut-base | CONFIRMED | 대부분의 권한은 UT(User Testing) 권한 모델을 베이스로 구현. Edit Role이 UT enum과 동일 | UT 권한 정책이 변경되면 Connect에 영향이 있는지 추적. |
| F-IDM-team-switch-ux | WIP | Team 전환 UI 패턴(모달/토스트/인라인) 미결정 | 결정 후 회귀 케이스 정의. |
| F-IDM-cross-team-pie | WIP (2026-05-28 등재) | Cloud Pie 라이브러리에 대한 cross-team 접근 정책 미결정. **레거시 베이스라인**(Paige 제공): Enterprise·Self-serve 둘 다 사용자가 Cloud Edit Role Viewer로 보이는 다른 Team의 Pie도 Connect에 업로드 가능했다. CoC는 §10 P0 "Team 간 자원 누출 0건"과 텐션이 있어 명문화 필요. 3안 검토 중 — A(레거시 동등 유지) / B(현재 Team Pie만 허용) / C(cross-team 표시 + import 시 현재 Team으로 복사). Paige가 PM/Tay 컨펌 후 결정. | 결정 후 회귀 케이스: ① Cloud Pie 모달이 cross-team 폴더를 노출하는지, ② Edit Role Viewer 자격으로 import 시도 시 허용/거부, ③ import된 Pie의 team_id가 어디로 귀속되는지(원본 Team vs 현재 Team), ④ PieVersion에 source_team_id 메타가 보존되는지(C안 채택 시), ⑤ §10 P0 Team 격리와의 정합성. F-STG-cloud-pie-browser·F-API-pies-uploadCloud와 1:1 연동. |
| F-IDM-plan-feature-matrix | CONFIRMED | Connect 진입 자격 통과 후, **Custom Plugin Import(+버튼)는 Enterprise 구독에서만 동작**한다. Pro 구독은 +버튼 자체가 비노출(레거시 동등). Self-serve의 경우 Plan에 따라 Enterprise 등급일 때만 노출 | Pro 구독자에게 +버튼 비노출 회귀(P0), Enterprise 구독자가 import 가능 회귀, Plan 다운그레이드 시 기존 import한 플러그인 처리 정책(즉시 비활성/유예 기간 결정 필요, WIP). 출처: 강의 영상 7, L819-823. |
| F-IDM-upsell-modal | CONFIRMED | Plan 한도 초과·비가용 기능 트리거 시 표시되는 **공통 Upsell Modal**. 3 액션 = (a) [X] Modal Close, (b) [Upgrade] `https://checkout.protopie.io/{unique url}` 이동, (c) [Chat with us] `https://www.protopie.io/form/request-demo` 이동. Enterprise 등급 비가용 기능(Custom Plugin·Wear OS·Custom Font·Unity 등)은 별도 Enterprise Upsell variant (타이틀 문구만 상이) | Free·Core 양쪽 모든 한도 트리거 지점에서 동일 modal 노출(레거시 S280에 21개 지점 케이스화됨). 3 버튼 URL·Close 동작·외부 링크 새 탭 여부 회귀 P1. 다운그레이드 직후 기존 자원에 접근 시도 시 modal 노출 일관성. 출처: TestRail S280 (Free `[Local Pie] Disable` 외 다수). |

검증 우선순위: ① 토큰 lifecycle(만료·revoke·24h grace), ② License → Cloud 로그인 전환 시 capability 즉시 반영, ③ Cookie/JWT 위변조 차단, ④ 결제 → Bridge 가시성 latency(폴링 15초).

라이센스/Cloud 인증 상태 매트릭스: (License 유무) × (Cloud 로그인 유무) × (Cloud entitlement 유효성)의 8개 조합을 명시적으로 케이스화하면 회귀 누락을 막을 수 있다.

### 4-3. F-STG — Stage·Group·Pie

| ID | 상태 | 요구사항 | 검증 포인트 |
|---|---|---|---|
| F-STG-cloud-vs-local | CONFIRMED | Cloud Stage / Local Stage는 생성 시점에 선택하며 변환 불가. **Cloud Stage는 Cloud Web과 Desktop Cloud-login 두 모드 모두에서 생성 가능**(rev10 ACL 정정). | 라이센스 단독 모드에서 Cloud Stage 옵션이 비활성된다. Desktop Cloud-login에서 Cloud Stage 생성 진입점이 정상 노출되고 생성 후 Cloud 브라우저에서도 동일 Stage가 보인다(B2C/B2B 양쪽 회귀). |
| F-STG-private-shared | PARTIAL DEFERRED (rev10) | **Cloud Stage의 Private/Shared 구분은 Beta scope 제외**(ACL §6 결정). Beta Cloud Stage는 단일 공유 모델로 운영. Local Stage는 본질적으로 1 PC·1 Postgres이므로 외부 공유 개념 자체가 부재(여전히 단일 사용자 한정으로 유지). Post-Beta에서 Cloud Stage의 Private 옵션 재도입 검토. | Beta 기간 동안 Cloud Stage 생성 UI에 Private/Shared 토글이 노출되지 않는지, API 레이어에서 `private` 플래그를 받아도 거부 또는 무시되는지. Local Stage 생성·열람이 단일 PC 안에서만 정상 동작하는지(레거시 동등). Legacy Private Stage 데이터 마이그레이션 정책 watch. |
| F-STG-auto-personal | DEFERRED (rev10) | ~~가입 시 "내 작업실" Private Stage가 자동 생성된다~~ → **Beta에서 자동 생성 제외**(F-STG-private-shared와 함께 DEFERRED). 가입 직후 빈 화면 처리는 별도 UX로 해결(F-HOM 영역). | 가입 직후 "내 작업실" Stage가 생성되지 않는지, 대신 빈 상태 가이드(예: "첫 Stage를 만들어보세요" CTA)가 노출되는지. F-HOM-shared-layout 회귀와 연동. |
| F-STG-group-1level | CONFIRMED | 계층은 Stage → Group → Pie까지 1 level만. **Pie는 반드시 Group에 종속**된다(Stage root 직속 Pie 불가) | Group 안 Group은 거부된다. Pie를 Stage root에 직접 추가하려는 모든 경로(UI New 버튼·드래그&드롭·API)가 거부된다. |
| F-STG-cascade-delete | CONFIRMED | Group 삭제 시 안의 Pie가 함께 삭제(Notion 폴더 스타일) | 사용자에게 cascade 안내가 표시된다. |
| F-STG-pie-in-group | CONFIRMED (rev6에서 F-STG-pie-mutex 대체) | **모든 Pie는 정확히 하나의 Group에 종속된다**. Stage root 직속 배치 금지. 빈 Stage에서는 Group을 먼저 생성한 뒤, 해당 Group을 선택한 상태에서만 Pie 추가 진입점(New)이 활성화된다 | (a) Group 0개 상태에서 New(Pie 추가) 버튼·드롭다운 비활성 또는 "Group을 먼저 생성하세요" 카피, (b) Group 미선택 상태에서 Pie 업로드/드래그&드롭 시도 거부, (c) API 레이어에서 group_id 누락 요청 400 응답, (d) 모든 Pie는 정확히 1개 Group에 속함(0개·2개 이상 불가) RLS·DB 제약. |
| F-STG-display-order | CONFIRMED | **각 Group 내부가 독립 정렬 namespace**(Stage root는 Pie를 보유하지 않으므로 Group 목록 자체의 정렬만 root namespace로 유지) | Group 목록 정렬과 Group 내부 Pie 정렬이 분리되어 drag-drop 시 충돌이 발생하지 않는다. |
| F-STG-pieversion | CONFIRMED | 같은 Pie의 업로드/import마다 PieVersion 1 row씩 누적. 활성 버전 1개를 강제한다 | 새 버전 업로드가 진행 중 세션에 영향을 주지 않는다. |
| F-STG-stage-asset | CONFIRMED | Unity build, web embed HTML, camera feed metadata 등은 StageAsset에 저장. binary는 S3에 보관 | 레거시 SUnityLayer / SCameraLayer 흡수 회귀. |
| F-STG-svw-layers | CONFIRMED | Stage View 커스텀 레이어 3종 지원: (a) **Web Embed** — URL 또는 iframe 코드로 외부 웹 콘텐츠 삽입. Maps·Spline·Rive·Bezi 등 다양한 포맷. Stage에서 배치·크기 조정 자유. (b) Live Camera — USB 웹캠, 노트북 카메라, HLS 라이브 스트리밍 URL을 Stage 레이어로 삽입. 카메라 속성 패널에서 설정. (c) Unity — Unity WebGL 빌드를 Stage 레이어로 삽입. 플랜별 수량 한도는 §3-2 매트릭스 따름 | Web Embed: 다양한 URL/iframe 렌더링 정확성, 잘못된 URL fallback, 권한 없는 도메인 차단. Live Camera: USB 디바이스 분리 시 동작, HLS 스트리밍 끊김 처리. Unity: WebGL 빌드 로딩, 키보드 입력 충돌(Enterprise Unity Plugin 미설치 환경). **개선 요구(Design Brief 260601 §2 Features d, Extension layer)**: 현재는 Stage View에서만 레이어 상세를 볼 수 있으나 Pie list와 같은 depth의 레이어 리스트 제공 필요(도입 시 리스트 진입점·상세 회귀 추가, WIP). 출처: Legacy Connect (User Side) §Stage View. |
| F-STG-svw-edit-mode | CONFIRMED | Stage View의 **Edit Mode** UI 규격(레거시 S503 베이스라인). 좌측 [Edit] 버튼으로 진입하면 (a) 상단 타이틀 영역 + 대시보드 Group 영역에 레이어 종류·개수 아이콘 표시, (b) Add 메뉴에서 4종 레이어 추가 가능: Pie(Cloud/Local upload), Web Embed, Live Camera, Unity, (c) 레이어 클릭 시 우측에 공통 속성 패널 노출. 공통 속성 = Position(X·Y, 양수·0·음수 정수 허용, 소수점·비숫자 거부), Size(W·H, 양수만 허용, 0·음수·소수점·비숫자 거부 — 레거시 검증 기반), Size Lock(자동 비율 유지 토글), Original Size 버튼. 레이어 타입별 추가 속성: Web Embed = URL 입력 필드 + Supported Types 링크 / Camera = None·Fit·Fill 모드, Live Streaming URL, 카메라 권한 허용 흐름 / Unity = Insert(파일 삽입) + Unity Build Settings 링크 + View Mode에서 Unity↔Pie 양방향 통신 | 4종 레이어 Add·삭제 시 상단 아이콘·개수 즉시 반영. **Position 입력**: 양수·0·음수 정수 → 해당 좌표 이동(음수=캔버스 밖 허용), 소수점·비숫자 거부(C127892·C127893 등). Size 입력: 양수만 적용, 0·음수·소수점·비숫자 거부(C127894·C127895 등). 입력 검증은 4종 레이어(Pie·Web Embed·Camera·Unity) 동일. Size Lock 토글 시 비율 보존, Original Size 복원 정확성. Camera 권한 거부 시 fallback, Live Streaming URL 입력 무효 처리. Unity Insert 후 View Mode 전환 시 즉시 양방향 통신 가능. 개선 요구(Design Brief 260601 §2 Features e): Snapping 등 더 정교한 편집 지원 요청 있음 — 도입 시 정렬 가이드·스냅 동작 회귀 추가(WIP). 출처: TestRail S503 `Web View Player > Group Web Player > Edit Mode` (C127847~C127921, C128659~C128665). |
| F-STG-teamfont | CONFIRMED | Team 전용 폰트 라이브러리. **Enterprise 등급 전용 기능**(Legacy User Side 정정). 폰트 라이센스 검증은 사용자 책임. Bottom menu / Information 영역의 "custom fonts unavailable" 영역 클릭 시 Custom Fonts modal이 노출되어 폰트 리스트·스크롤·[X] close 동작 회귀 | 폰트 미존재 시 fallback이 정상 동작한다. Free/Core 등급에서 커스텀 폰트 사용 시도 시 비활성화 또는 무시. modal 폰트 리스트 정렬·스크롤·close 동작 일관성. 알려진 이슈: 커스텀 폰트가 로컬 환경으로 함께 다운로드되지 않는 이슈(§7 알려진 이슈 watch). 출처: TestRail S503 `Bottom menu / Information > [Enterprise] Custom Font` (C127829~C127832). |
| F-STG-pie-replace | CONFIRMED | 프로토타입 추가/제거/교체 동작. New 버튼 클릭 또는 드래그&드롭으로 Pie 파일 추가. **교체 시 동일 pieId 유지 → 기존 메시지 연결(send/receive 라우팅)이 보존된다**. Pie 그룹 단위로 Stage View 링크 복사, reload, delete, Stage View open 액션 제공. 드래그&드롭으로 그룹 간 이동, 그룹명 더블클릭으로 이름 변경 | 교체 후 메시지 연결 끊김 0건, 동일 pieId 유지 회귀 P1. 출처: Legacy Connect (User Side) §프로토타입 관리. |
| F-STG-studio-autosync | CONFIRMED | **Studio 변경사항 자동 동기화는 로컬 저장 Pie파일에 한해 동작**한다. Connect에 로드된 Local Pie가 Studio에서 수정되면 변경사항이 자동 반영. Cloud Pie의 경우 편집 후 수동 리로드 필요(자동 동기화 비대상) | Local Pie 자동 반영 latency, Cloud Pie 수동 리로드 UX(reload 버튼 위치·동작 명확성). Pie 교체 중 Studio 저장 race condition. 출처: Legacy Connect (User Side) §프로토타입 관리. |
| F-STG-stage-role | CONFIRMED (rev10 부여 룰 명문화) | Stage 단위 권한은 Connect SoT인 Stage Role(owner / editor / viewer)을 별도로 적용한다. Cloud의 Edit Role이 Connect 진입 자격을 게이트하고, Stage Role이 Stage 안 동작을 게이트한다. **부여 룰**: owner = Stage 생성자 1인. editor = 같은 Team의 Cloud Edit Role ≥ Editor(Editor 또는 Moderator) 유저에게 자동 부여(별도 멤버 추가 액션 없음). viewer = ViewerInvite 토큰으로 진입한 외부 게스트(계정 불필요). ACL §1·§2 반영. | (1) Team Owner라도 자동으로 모든 Stage의 owner가 되지 않는다 — 본인이 만든 Stage만 owner. (2) Cloud Edit Role을 Viewer→Editor로 승격하면 해당 Team의 **모든 Stage에 editor 권한이 즉시 부여**된다(폴링 latency 허용). 강등 시 즉시 박탈. (3) ViewerInvite 토큰 보유자가 Cloud 계정 없이 URL/QR로 진입하면 viewer 상태로 시작한다(F-VWR 연동). (4) Edit Role Viewer 계정은 Connect 진입 자체가 차단되어 Stage editor 자동 부여 룰이 적용되지 않는다(F-IDM-connect-entitlement). |
| F-STG-svw-entry | CONFIRMED | Stage View 웹 진입점. **Group hover 시 "View" 버튼이 노출**되고(F-STG-pie-in-group에 따라 Pie는 Group에만 존재하므로 진입점도 Group 단위), 클릭하면 브라우저에서 `{server}/stages/{stage-id}` URL로 Stage가 열린다 | View 버튼은 적절한 Stage Role 보유 시에만 활성화. URL 직접 입력·북마크·새로고침 시 컨텍스트 유지. 권한 없는 stage-id 접근은 거부. |
| F-STG-svw-multipie | CONFIRMED | Stage View는 Stage에 포함된 여러 Pie를 한 화면에서 동시에 실행·표시하는 작업 공간이다 | 다중 Pie 동시 렌더링 정확성, Pie 추가·삭제·순서 변경 시 화면 반영, 한 Pie 크래시가 다른 Pie에 전파되지 않음. |
| F-STG-svw-edit | CONFIRMED | Stage View는 시청 전용이 아니라 **편집까지 가능**한 작업 공간이다(외부 게스트 read-only인 F-VWR과 명확히 구분된다) | Stage Role editor 이상은 편집 가능, viewer는 진입 후에도 편집 액션이 차단된다. 두 사용자가 동시에 편집할 때의 동작 정의. |
| F-STG-svw-pie-routing | CONFIRMED | 같은 Stage View 안의 Pie들은 send/receive 메시지로 서로 연결된다. "Connect"의 어원이 여기서 나온다 — Pie ↔ Pie 메시지 라우팅이 핵심 가치 | 한 Pie의 send 메시지가 같은 Stage 안 다른 Pie의 receive 트리거를 발화한다. 변수 값이 Pie 간 일관되게 전달된다(예: `Button_nb_variable`). 외부 Stage Pie로는 라우팅되지 않는다. |
| F-STG-pie-source | CONFIRMED | Pie 추가는 상단 **New** 버튼의 드롭다운으로 두 갈래 진입. (a) Cloud Pie: ProtoPie Cloud의 Pie 라이브러리에서 import. (b) Local Pie: 로컬 `.pie` 파일 업로드. Group이 선택된 상태에서만 New(Pie 추가) 진입점이 활성되며, 추가된 Pie는 해당 Group에 종속된다(F-STG-pie-in-group) | 라이센스 단독 모드에서는 Cloud Pie 옵션이 비활성된다. Cloud 로그인 후 즉시 활성화된다. Group 미선택·Group 0개 상태에서 New 비활성 또는 가이드 카피("Group을 먼저 생성하세요") 노출. |
| F-STG-cloud-pie-browser | CONFIRMED (rev13 모달명 보강) | Cloud Pie 추가 플로우: **"Browse Team space asset"** 모달 먼저 열림 → "Pie Gallery" 진입. Pie Gallery에서 검색·폴더 탐색(breadcrumb·뒤로가기), Pie 썸네일·이름·최종 수정 시점 표시, 선택 후 Add 버튼으로 Stage에 추가. Cancel 시 플로우 종료. | 폴더 진입·이탈, 빈 폴더, 다국어 폴더명, 썸네일 fallback, 권한 없는 Pie 노출 차단. "Browse Team space asset" → Pie Gallery 모달 전환 시 Stage 컨텍스트 보존. |
| F-STG-cloud-pie-cross | CONFIRMED | Cloud Pie 모달 하단 좌측에 **Open Local Pie** 진입점이 있어 모달 안에서 Local Pie 모드로 즉시 전환 가능 | 모달 컨텍스트 전환 시 대상 Stage 정보가 보존된다. |
| F-STG-cloud-pie-to-local | CONFIRMED | Cloud Pie를 Local Stage에 추가하는 시나리오 지원(Capability Matrix §3 일치). Cloud 로그인 + Desktop 모드 조합에서만 가능 | 라이센스 단독 모드에서는 Cloud Pie를 Local Stage에 추가하는 액션이 차단된다. |
| F-STG-group-ctx | CONFIRMED (rev13, Figma) | Stage 편집기 좌측 패널 **Groups 섹션 컨텍스트 메뉴** 항목. 순서: Rename group / Duplicate group / Refresh all pies / Preview group / Copy link to preview / Delete group (destructive, 빨간색). | (1) Rename group: 인라인 rename 또는 모달, 빈 이름 거부. (2) Duplicate group: Pie 포함하여 복제, 새 group 이름 기본값 결정. (3) Refresh all pies: group 내 Cloud Pie 전체 최신 버전 reload. (4) Preview group: F-STG-svw-entry의 Group 단위 View와 동일 진입점. (5) Copy link to preview: 클립보드 복사 성공 피드백(토스트 등). (6) Delete group: F-STG-cascade-delete 안내 후 삭제. |
| F-STG-layer-ctx | CONFIRMED (rev13, Figma) | Stage 편집기 좌측 패널 **Layers 섹션 컨텍스트 메뉴** 항목. 순서: Refresh Pie / Copy link to preview / Open preview / Locate Pie in Cloud / Replace Pie → 서브메뉴(From Cloud… / From local space…) / Delete layer (destructive, 빨간색). 레이어 타입별 인라인 퀵액션(목록 hover 시 노출): Cloud Pie = Refresh 아이콘 + "Open Pie" 버튼 / Local Pie = "Player" 버튼 / Web Embed = "Copy URL" + "Open URL" 버튼 / Camera·Unity = 타입 고유 버튼. | (1) Refresh Pie: Cloud Pie 한정, 새 버전 반영 후 세션 영향 없음(F-STG-studio-autosync 연동). (2) Locate Pie in Cloud: ProtoPie Cloud에서 해당 Pie 위치 열기, Cloud 미로그인 시 처리. (3) Replace Pie → From Cloud: Pie Gallery 모달(F-STG-cloud-pie-browser), From local space: 로컬 파일 선택 — 교체 후 pieId 보존(F-STG-pie-replace 연동). (4) 인라인 퀵액션: 레이어 타입에 따라 노출 버튼이 다름 — Cloud Pie에 "Player" 버튼 미노출, Local Pie에 "Open Pie" 버튼 미노출. (5) Delete layer: 확인 없이 즉시 삭제 vs. 안내 포함 정책 결정 필요(WIP). |
| F-STG-navbar-menu | CONFIRMED (rev13, Figma) | Stage 편집기 **상단 navbar 햄버거·설정 드롭다운** 항목. 플랫폼·Stage 타입별로 항목이 다르다. (a) Cloud Web + Cloud Stage: Go to home / Download desktop app / Snap to objects / Theme(System·Light·Dark) / Duplicate / Rename / Archive Stage… (red). (b) Desktop App + Local Stage: Go to home / Settings… / Network(IP 주소 목록) / Duplicate / Rename / Delete Stage… (red) / Restart server. (c) Desktop App + Cloud Stage: (a)와 동일하되 Copy to local 항목 추가(= F-STG-handoff "Handoff to local"과 동일 기능, 진입점 위치만 다름). Navbar 우측 버튼: Edit / Preview 탭, Custom fonts 수, ▶ Run, Share (파란색 버튼). | (1) Cloud Web에서는 "Archive Stage…"만 노출, "Delete Stage…" 미노출 — 반대도 마찬가지. (2) Desktop App Local Stage에서 "Network"는 현재 LAN IP 주소 목록을 표시한다(F-BRG-hybrid-mode 연동). (3) "Restart server" 항목은 Local Stage Desktop 전용. (4) Edit/Preview 탭 전환이 F-STG-svw-edit·F-STG-backstage와 연동되는지 확인. (5) Share 버튼 동작·권한 게이트는 F-VWR 영역(WIP). |
| F-STG-svw-multiview-baseline | CONFIRMED | 레거시 Multi-view Group 동작은 Beta Stage View가 동등 이상으로 보장한다. 레거시 베이스라인 = (a) "New → Group"으로 Multi-view 그룹 생성, (b) Pie 추가는 drag-drop 또는 "New → Pie → Browse" 2가지 진입점, (c) 우클릭 → 기어 아이콘으로 Pie 크기·배치·배경색 변경, (d) Multi-view 안에서 Pie 추가/제거 동적 반영, (e) Studio에서 .pie 저장 시 Multi-view 자동 업데이트(live link) | 레거시 동등 보장. P1. 출처: 강의 영상 1-2, L23-50, L62-72, L122-128. |
| F-STG-svw-broadcast-model | CONFIRMED | 같은 Stage View 안의 Pie들은 **broadcast 모델**로 동작한다. 한 Pie의 send 메시지는 같은 Stage View의 모든 다른 Pie에 전달되며, 라우팅을 의도한 Pie만 반응시키려면 Pie 측 조건 분기가 필요(사용자 책임). 같은 컴포넌트 인스턴스가 여러 개일 때 메시지 폭주 가능성 인지 필요 | 모든 Pie가 모든 메시지를 수신하는지 회귀. Beta에서 라우팅 모델 변경 시 마이그레이션 가이드 필요. 출처: 강의 영상 1-2, L256-282. |
| F-STG-svw-view-settings | CONFIRMED | Stage View **View Mode**의 우측 마우스 클릭 시 상단 Settings 영역 노출. 6 옵션: Fit to Screen(default) ↔ Original Size, Show Cursor On/Off, Show Hotspots Hint On/Off, Background Color 변경, 음성 인터랙션(Speak/Listen) 동작. F-BRG-multiview-url의 URL 파라미터(fullscreen/bg/hotspotHints/cursorHide/scaleToFit)와 1:1 대응 | Single Pie View와 Group Web Player 두 컨텍스트 모두에서 동일 옵션 노출(레거시 S503 C127833~C127846 대응). Fit↔Original 전환 시 레이어 정렬 보존, Hotspots Hint Off 시 UI 클린, Background Color 다양한 값 입력. Speak/Listen은 F-BRG-voice-proto 브라우저 매트릭스에 의존. 출처: TestRail S503 `Web View Player`. |
| F-STG-pie-list-multiselect | CONFIRMED | Pie List 다중 선택(Check box) 동작. 개별 체크·전체 체크·전체 해제·다중 선택 후 일괄 삭제 액션 지원 | 체크 상태 유지(스크롤·필터 후), 일괄 삭제 시 cascade 안내, 권한 없는 Pie 체크 시도 차단. 출처: TestRail S503 `Pie List > Check box 동작 확인` (C127* 6 cases). |
| F-STG-external-guest | WIP | Team 비-멤버를 Stage에 초대 가능 여부 | 정책 확정 후 모델 변경 회귀. |
| F-STG-pie-move | WIP | Beta는 Stage 간 Pie 이동 불가로 한정할지 검토 중 | |
| F-STG-archived | WIP | archived 정책 미결정 | |
| F-STG-pie-imported-persist | CONFIRMED (ACL §3, rev12) | Stage에 추가된 Pie는 이후 **Stage 리소스로 관리**된다. Connect Cloud에서 원본 Pie가 삭제되더라도 이미 Stage에 연결된 Pie는 유지되고 정상 동작해야 한다. 레거시 Connect와 동일한 동작. | 원본 Pie 삭제 후 Stage에서 해당 Pie가 여전히 실행되는지. Stage에서 Pie 재로드/교체 시 동작 정확성. |
| F-STG-pie-no-personal-space | CONFIRMED (ACL §3, rev12) | Pie 조회·선택 범위는 **현재 선택된 Team 범위로 제한**된다. Personal Space에 저장된 Pie, 다른 Team의 Pie(Viewer 권한 포함), Team 간 Pie 교차 참조는 지원하지 않는다. | Personal Space Pie를 Stage에 추가하려는 시도 차단. 다른 Team Pie 선택 시도 차단. Team 전환 시 이전 Team Pie가 목록에 노출되지 않음. |
| F-STG-backstage | WIP (rev13 디자인 구조 보강) | Stage 편집기 **하단 접이식 패널(Backstage)**. Design Brief 260601 + Figma 디자인(564:102822) 기반. 구성: (a) IP 주소 표시 (LAN IP, Local Stage Desktop 전용), (b) Connect Cloud 버튼 (Cloud Relay 연결 진입점), (c) 노드 캔버스 — 각 Plugin·Pie가 노드로 표시되고 Connect hub에 연결된 형태로 메시지 trigger 흐름 비주얼 확인. Navbar의 Edit/Preview 탭과 별개 영역(탭이 아니라 하단 패널)으로 디자인에 등장 — 탭 vs 패널 구조는 PM/Designer 최종 확인 필요. Console 패널은 우측 별도 패널로 공존(Backstage와 분리). Stage Role 접근 정책 미확정. | 결정 후 회귀 포인트: ① Backstage 접기/펼치기 동작, ② IP 주소 표시가 Local Stage Desktop 전용인지 확인, ③ "Connect Cloud" 버튼이 Cloud Relay 연결 플로우 정상 진입, ④ 노드↔Connect hub 메시지 trigger 비주얼 정확성(F-BRG-16 Debugger와 중복 범위 정리), ⑤ Stage Role viewer의 Backstage 접근 허용/차단 확정. 출처: Design Brief 260601 §2 Backstage + Figma 564:102822. |
| F-STG-handoff | CONFIRMED (rev12 신설, Scope: Desktop App) | **Stage 목록에서 Cloud ↔ Local Stage 양방향 복제(handoff/duplicate)**. (a) Handoff to local: Cloud Stage를 복제하여 Local Stage 생성 — Cloud relay 대신 LAN relay에 연결해야 할 경우 대비. (b) Upload to Cloud: Local Stage를 복제하여 Cloud Stage 생성. 제약: local pie가 추가되었거나 Bridge App을 활용하는 Stage는 Upload to Cloud 불가. 복제된 Cloud Stage도 Team space에 종속되며 동일 Team space 내 파이만 활용 가능 | (1) Handoff to local: Cloud Stage 선택 → Local 복제본 생성, 원본 보존, LAN relay 동작 회귀. (2) Upload to Cloud: Local Stage → Cloud 복제, Team space 귀속·동일 Team 파이 제약 검증. (3) **제약 negative test**: local pie 포함·Bridge App 활용 Stage에서 Upload to Cloud 액션 비활성/거부 + 명확한 카피. (4) 라이센스 단독 모드에서 Cloud 관련 복제 차단(§3 Capability Matrix 일치). 출처: Design Brief 260601 §2 Features h, Connect Desktop. |
| F-STG-download-config | CONFIRMED (rev12 신설, Scope: Desktop App) | **Stage를 단일 파일로 저장(Download as a project file)**. 레거시 "Save & Load Connect Configs" 동등. Stage 구성(server + pie 정보 + API/Hardware 연동 정보)을 별도 포맷(예: `.stage`)으로 export/import. `.stage` 등 별도 포맷 export 세부는 추가 고려 대상(Design Brief 미확정) | 단일 파일 저장·로드 라운드트립 정합성(Pie·embed layer·플러그인 설정 보존), 잘못된/손상 파일 import 거부, Cloud pie 포함 Stage의 export 시 참조 처리(다운로드 vs 링크). 출처: Design Brief 260601 §2 Features i + 용어 정의(추가 고려). |
| F-STG-instance-sync | WIP (rev12 신설) | **인스턴스 간 상태 동기화**. 현재는 각 인스턴스(§1 용어 Instance) 생성 이후의 메시지만 반영되어 Stage·Pie preview·Player 간 상태 불일치가 자주 발생. 인스턴스 생성 시 현재 상태의 Snapshot을 동기화해주는 기능 필요 여부 검토 중(Design Brief "추가 고려 필요") | 결정 후 회귀: 늦게 진입한 인스턴스가 현재 상태 Snapshot을 받는지, Snapshot 미적용 시 허용되는 상태 차이 범위, Embed layer(카메라 등) 비공유 동작 유지. §7 "실시간 Sync 보강 scope out"과의 경계 명문화 필요. 출처: Design Brief 260601 §2 Instance 추가 고려. |
| F-STG-nodeview | WIP (rev10 신설, rev11 TBD 완화, ACL §4) | Node View 접근 규칙. **Editor의 Player 내 진입 가능 여부는 TBD** — rev11 ACL §4가 "플레이어 진입 경로에서 노드 뷰 이동을 비활성화할지" 및 "Player 내 접근이 Editor에게도 차단되는지"를 미결로 표기(표 비고: "노드 뷰는 플레이어를 통해 접근할 수 없다"와 접근방법 "Player/URL" 표기가 상충). 확정 전까지 Editor의 Player 내 Node View 접근은 가능으로 단정하지 않는다. URL 경로 진입·확인·편집은 Editor 가능으로 유지. Viewer는 URL 직접 공유로만 진입 가능하며 확인만 가능, 편집 차단. Stage Player 내부에서 Viewer가 Node View로 진입하는 경로는 부재(레거시 동일). ACL §4 TBD + 미결 Q-4(URL 공유 시 인증/PIN 여부) 확정 후 CONFIRMED 승격. | (1) Editor: URL 경로 진입·확인·편집 정상. **Player 내 Node View 진입점 노출 여부는 ACL §4 TBD 확정 후 케이스화**(현재는 양방향 모두 회귀 대상으로 열어둠). (2) Viewer: URL 진입 시 read-only로 노출, 편집 시도(저장·노드 추가·삭제) 차단. (3) Viewer가 Stage Player 화면에서 Node View 진입점이 노출되지 않는지 — Player UI에 Node View 버튼·메뉴 부재 회귀. (4) Console 로그도 Viewer에게 차단되는지(ACL §3 표). (5) Q-4 확정 시: Node View URL 무인증 접근 허용 여부·PIN 게이트 유무에 따른 진입 회귀(§10 watch). |

검증 우선순위: ① 다른 Stage 자원이 의도치 않게 노출되는 경우(정성 0-tolerance), ② License-only ↔ Cloud login 전환 시 사용자가 새 환경으로 명확히 인지하는지(작업물 자동 이전 없음), ③ PieVersion 활성 1개 제약 위반.

### 4-4. F-PLG — 플러그인 시스템

| ID | 상태 | 요구사항 | 검증 포인트 |
|---|---|---|---|
| F-PLG-bridge-only | CONFIRMED | Beta에서 플러그인은 Bridge 안에서만 보고·실행. Web Dashboard 미노출 | Cloud Stage 뷰에 플러그인 실행 UI가 없다. |
| F-PLG-builtin-ide | CONFIRMED | Bridge 내장 IDE에서 작성·실행 | 외부 ZIP 빌드 후 업로드 방식이 폐기되었다. |
| F-PLG-team-library | CONFIRMED | Team 라이브러리 + Stage 단위 인스턴스 모델 | 다른 Team의 플러그인이 보이지 않는다. |
| F-PLG-manifest-perm | CONFIRMED | Manifest 기반 권한 선언 | manifest 손상 시 Import가 거부된다(E-PLG-2). |
| F-PLG-crash-restart | CONFIRMED | 플러그인 크래시 시 자동 1회 재시작 후 실패 시 정지 | E-PLG-1 동작 일치. |
| F-PLG-zip-upload-only | CONFIRMED | 파일 업로드만 허용. URL/git import는 거부 | |
| F-PLG-preset-list | CONFIRMED | 프리셋 플러그인 **7종** = API, IFTTT, G29, Arduino, Gamepad, Blokdots, Unity (Stage view 양방향 메시지 통신). Bridge 내 Plugin 패널에서 노출. Unity Plugin은 Stage view에 삽입된 Unity 씬과의 양방향 통신 전용으로 Enterprise 등급에서 무제한 활성화 가능 | 7종이 모두 표시되고 각 아이콘·이름·상태가 정상 렌더링. Unity 플러그인이 Free 등급에서 비노출/비활성화 회귀. 출처: Legacy Connect (User Side) §내장 플러그인. |
| F-PLG-tier-limits | CONFIRMED | 플러그인 동시 실행/실행 시간은 플랜별로 제한된다(§3-2 매트릭스). Free: 1개 동시 / 3분 실행 후 만료, Core: 3개 동시 / 무제한, Enterprise: 무제한 / 무제한. API 플러그인 설정 수 한도도 동일 매트릭스 적용 | Free 3분 만료 후 동작 정의(silent stop / 경고 모달 / 자동 재시작 제안 중 정책 확정 필요, WIP). Core 4번째 플러그인 활성화 시도 시 차단 메시지. Plan 다운그레이드 직후 기존 활성 플러그인 처리. |
| F-PLG-states | CONFIRMED | 플러그인 상태 3종: **Run**(실행 가능, 클릭 시 활성화) / Deactivated(비활성, 빨간 점) / Disconnected(외부 디바이스·서비스 연결 끊김, 빨간 점) | 상태 전이가 실제 연결 상태와 일치한다. Blokdots처럼 외부 하드웨어 의존 플러그인은 디바이스 분리 시 Disconnected로 전환. |
| F-PLG-api-bridge | CONFIRMED | API 플러그인은 HTTP 요청과 Pie 메시지를 **양방향 라우팅**한다. (a) Method(GET/POST/...)·URL·Header·Body 정적 설정. (b) `Message from Pie`로 트리거 메시지 지정. (c) Override 옵션으로 URL/Header/Body를 Pie의 메시지 값으로 동적 치환. (d) API 응답을 `Message to Pie`로 지정된 메시지명으로 Pie에 회신. Activate 시 활성화 | 동적 override 정확성(escape·인코딩 포함), 응답 매핑 정확성, 실패 응답·타임아웃 처리, 여러 API 인스턴스 동시 활성. |
| F-PLG-test-request | CONFIRMED | API 플러그인 설정 화면에 Activate 전 단발성 호출용 **Test Request** 버튼이 있다 | Activate 전이라도 Test Request가 동작하고, Pie 메시지에 영향을 주지 않는다(드라이런). 에러 응답 가시화. |
| F-PLG-concurrent | CONFIRMED | 여러 플러그인이 동시 실행 가능하다(예: Arduino + G29 + IFTTT 동시 활성). 한 Pie의 send 메시지는 활성 모든 플러그인에 dispatch된다. 같은 종류 다중 인스턴스도 허용(예: Arduino 2대를 Arduino 플러그인 + Blokdots 플러그인으로 각각 제어) | 멀티 플러그인 메시지 라우팅 충돌·우선순위 정책 정의 필요(WIP). 출처: 강의 영상 5, L1146-1180. |
| F-PLG-states-external-dep | CONFIRMED | 외부 디바이스 분리(USB 빼기) 또는 외부 앱 종료(Blokdots 앱 종료, Arduino IDE 점유 등) 시 즉시 Disconnected로 전이. 재연결 시 큐잉된 메시지 처리 정책 미정(WIP) | latency 측정, silent drop vs queue 정책 결정. F-PLG-states 보강. |
| F-PLG-disp-multi-route | WIP | 다중 플러그인 동시 활성 시 dispatch 충돌·우선순위 정책 | F-PLG-concurrent와 짝. dev 기간 중 결정. |
| F-PLG-perm-enforce | WIP | 권한 강제 메커니즘·격리 환경·의존성 설치 정책 detail | dev 기간 중 결정. |
| F-PLG-lifecycle-baseline | CONFIRMED | 외부 디바이스 의존 플러그인(Arduino/Blokdots/IFTTT/Wear OS)의 **공통 라이프사이클 4단계** 회귀 시퀀스 = (1) 디바이스 정상 연결, (2) Run(활성화), (3) Stop(비활성화), (4) Send/Receive 통신. 각 단계 사이 상태 전이가 F-PLG-states 3종(Run/Deactivated/Disconnected)과 일치 | 4단계 시퀀스를 Arduino/Blokdots/IFTTT/Wear OS에서 각각 회귀(레거시 S503에 plug당 4 case로 명시화됨). Connect Core 등급 Wear OS 시도 시 **연결 실패**가 명시적으로 노출되어야 한다(Enterprise 전용). 출처: TestRail S503 `Blokdots/Arduino/IFTTT/Wear OS 연결 확인` 각 4 case. |
| F-PLG-plugin-mgmt | CONFIRMED | Plugin 패널 관리 액션 4종 회귀: **추가(Import)**, 삭제, Run, [Open in Terminal] | Custom Plugin Import 시 Enterprise 게이트(F-IDM-plan-feature-matrix)와 일관. Open in Terminal은 macOS·Windows 양 OS에서 기본 터미널 앱 호출. 출처: TestRail S503 `Plugin` (C127764~C127767). |

검증 우선순위: 레거시는 플러그인이 무제한 권한을 가졌으나 Beta는 격리 환경에서 실행된다. 보안 표면(파일 시스템·네트워크·자식 프로세스) 검증과 변조된 ZIP 거부가 회귀의 핵심이다.

**프리셋 플러그인 4종 상세 검증 포인트** (레거시 동등 보장, P1) — 출처: 강의 영상 2/3/4/5

#### F-PLG-preset-ifttt — IFTTT 플러그인

| 검증 포인트 | 근거 |
|---|---|
| Webhook Key 입력 필수. 빈 값/잘못된 형식 거부 | 영상 2, L165-178 |
| Test 기능: 플러그인 Run 상태일 때만 활성. Pie 메시지에 영향 없음(드라이런). 응답·에러 가시화 | 영상 2, L181-208 |
| Events 매핑: Pie 메시지 명 ↔ IFTTT 이벤트 명 1:1 매핑 | 영상 2, L211-224 |
| 이벤트 명 제약(IFTTT 측): 영문자/숫자/언더스코어만 허용. 공백·특수문자 거부 시 사용자 가이드 카피 일관성 | 영상 2, L21-25 |
| Pie → Connect → IFTTT 메시지 흐름의 Source 표기가 메시지 로그에서 정확 | 영상 2, L139-160 |
| JSON 페이로드 packing: Pie에서 value1/2/3 키로 escape 처리 (`\"` 사용) | 영상 2, L99-145 |

#### F-PLG-preset-blokdots — Blokdots 플러그인

| 검증 포인트 | 근거 |
|---|---|
| Blokdots 앱에서 "Add Integration → ProtoPie Connect" 선택 시 양측 상태가 즉시 "connected"로 전이 | 영상 3, L126-133 |
| Blokdots 앱 종료 시 Connect 플러그인이 Disconnected로 전이 (F-PLG-states-external-dep 회귀) | 영상 3 전체 + F-PLG-states |
| 첫 연결 시 Arduino 보드에 펌웨어 자동 설치 — Blokdots 책임 영역. Connect는 무관심 | 영상 3, L42-45 |
| 인코더는 디지털 핀 2개를 sequential로 점유(D3+D4 등). 인접 핀 충돌 시 동작 정의 | 영상 3, L62-71 |
| 알려진 한계(QA 무관): 인코더 + 일반 버튼 혼합 배선 시 버튼 동작이 반전될 수 있음. 사용자 배선 책임 | 영상 3, L86-124 |

#### F-PLG-preset-arduino — Arduino 플러그인 (코드 직접 작성)

| 검증 포인트 | 근거 |
|---|---|
| Baud rate 설정 일치 필수(코드 ↔ 플러그인). 불일치 시 메시지 수신 불가하며 에러 미표시 → E-PLG-BAUD-MISMATCH 후보 | 영상 4, L46-51, L130-139 |
| 시리얼 포트 자동 식별 + 라벨 표시("Arduino Uno R3" 등). 미식별 디바이스 처리 정의 | 영상 4, L136-139 |
| Arduino IDE 또는 다른 시리얼 점유 앱과 동시 사용 불가 → E-PLG-PORT-BUSY 후보 | 영상 4, L120-125 |
| 메시지 값 전달 프로토콜: `messageName\|\|value` 형식 (파이프 2개 구분자) | 영상 4, L201-213 |
| 한 줄에 `Serial.println(msg + "\|\|" + value)`가 동작하지 않음 — `Serial.print(msg + "\|\|"); Serial.println(value);` 2단 구성 필요. **레거시 동작상 제약** | 영상 4, L210-228 |
| Beta envelope 변경 시 `\|\|` 구분자 호환성 검토 필요 (F-REL-envelope WIP와 연결) | 본 스펙 §4-7 |

#### F-PLG-preset-g29 — Logitech G29 플러그인

| 검증 포인트 | 근거 |
|---|---|
| 스티어링 휠 PS3 호환 모드 권장. PS4 모드는 동작 보장 안 됨 | 영상 5, L9-13 |
| 메시지 카탈로그 12종 회귀 (아래 표) — 자동차 산업 데모 영향 큼, P1 | 영상 5 전체 |

**G29 메시지 카탈로그** (레거시 베이스라인, 회귀 필수):

| 메시지 명 | 값 범위 | 의미 |
|---|---|---|
| `wheel turn` | 0.00 ~ 100.00 (소수 2자리) | 0=좌 풀락, 50=중립, 100=우 풀락 |
| `pedals gas` | 0.00 ~ 1.00 (소수 2자리) | 가속 페달 압력 |
| `shifter gear` | -1, 1~6 | -1=후진, 1~6=전진단 |
| `wheel button r3` | 0 또는 1 | R3 버튼 |
| `wheel button l3` | 0 또는 1 | L3 버튼 |
| `wheel button triangle` | 0 또는 1 | 삼각형 버튼 |
| `wheel button plus` | 0 또는 1 | + 버튼 |
| `wheel button minus` | 0 또는 1 | - 버튼 |
| `wheel button spinner` | 0 또는 1 | 휠 스피너 중앙 버튼 |
| `wheel shift right` | 0 또는 1 | 우측 패들 |
| `wheel shift left` | 0 또는 1 | 좌측 패들 |
| `wheel spinner` | -1 또는 1 | 휠 스피너 회전 (1=시계, -1=반시계) |

#### 플러그인 설정 UI 회귀 베이스라인

| 플러그인 | 설정 UI 구성요소 |
|---|---|
| API | (F-PLG-api-bridge 참조: Method·URL·Header·Body 정적 + Override + Test Request 버튼) |
| IFTTT | Webhook Key 입력 + Events 매핑 표 + Test 영역(Event Name + JSON Payload + Send) |
| Arduino | Baud rate 드롭다운 + Port 드롭다운 + Run/Stop 토글 |
| G29 | Run/Stop 토글만 (자동 페어링) |
| Blokdots | Run/Stop 토글만 (외부 앱이 페어링 담당) |
| Gamepad | 게임패드 컨트롤러 입력 연동. Run/Stop 토글 + 디바이스 선택(연결된 컨트롤러 목록). 출처: Legacy User Side §내장 플러그인. |
| Unity (Stage view) | Run/Stop 토글 + 대상 Stage view 선택. Unity 씬과 양방향 메시지 통신. Enterprise 한정 무제한 활성화. 출처: Legacy User Side §내장 플러그인 + §커스텀 플러그인. |

### 4-5. F-BRG — Bridge 앱

레거시 동등 보장이 우선이며, Beta에서 명시적으로 확정된 신규 기능은 3개(F-BRG-15·16·17)다.

| ID | 상태 | 요구사항 | 검증 포인트 |
|---|---|---|---|
| F-BRG-hardware-legacy | CONFIRMED | USB/Serial/MQTT 하드웨어 통합 — 레거시 동등 보장 | Arduino, G29, MIDI, Gamepad, blokdots 모두 회귀. |
| F-BRG-hybrid-mode | CONFIRMED | 로컬 서버 + Cloud Relay 양쪽 동시 지원 | 두 모드 전환·동시 사용이 정상 동작한다. |
| F-BRG-build-protect | CONFIRMED | 코드 난독화 + 라이센스 우회 차단 + 변조 빌드 부팅 거부 | 변조된 빌드가 부팅되지 않는다. |
| F-BRG-auto-update | CONFIRMED | 자동 업데이트는 디지털 서명을 검증한다 | 무서명 update가 거부된다. |
| F-BRG-15 | CONFIRMED | 레거시 Studio 연동 동등 보장. STU-1: Studio SocketIO 연결(IP/port/sessionToken 입력 → Server가 Studio로 SocketIO 열고 양방향 라우팅). STU-2: .pie 파일 multipart POST 업로드 → 저장 → 즉시 실행 | 신규 동작(자동 발견·페어링 승인 UX)은 추가하지 않는다 — 레거시 그대로. |
| F-BRG-16 | CONFIRMED | Debugger 모드 (Beta 신규). Bridge UI에서 실시간으로 (a) 하드웨어 → 플러그인 → 프로토타입 메시지 흐름 시각화, (b) Pie 안 노드 기반 인터랙션 트리거 시퀀스 시각화. 정지·재생·step-through·이벤트 타임라인 기록 | Scania, 내부 피드백 출처. |
| F-BRG-17 | CONFIRMED (실험적) | Socket 기반 HTML 프로토타입 import. 외부 HTML(WebSocket/Socket.IO 클라이언트 코드 포함)을 Bridge에서 import해 ProtoPie 메시지 프로토콜에 연결 | 보안 정책(샌드박스·CORS·permission scope)이 미확정 상태로 release되지 않도록 차단. 파일 업로드만 허용. Beta 진행 중 deferral 가능. |
| F-BRG-license-login | CONFIRMED | Desktop 앱에서도 라이센스 키로 로그인 가능. 기존 5분 무료 사용 후 Cloud 로그인 강제 정책은 폐기. Embedded와 동일한 키를 사용 | 라이센스 키 검증·만료·재발급. Cloud 의존성 없이 작동한다. |
| F-BRG-studio-autodl | CONFIRMED | Studio 미설치 환경에서는 몇 초 후 다운로드 페이지로 자동 이동. Studio의 Connect 연결 기능은 별도 dependency 없이 진행 | 자동 이동 타이밍과 사용자 취소 가능 여부. |
| F-BRG-cloud-addr | CONFIRMED | Enterprise 로그인 진입 시 전용 서버 주소를 입력받는다(레거시 v2.10.2의 "Log in with Secure Enterprise" 패턴 유지). 주소 형식 검증, 도달 가능성 체크, TLS 인증서 검증 후 로그인 화면으로 이동 | 잘못된 주소·DNS 실패·인증서 오류·타임아웃 시 명확한 에러 카피. 주소 기억 옵션과 초기화 동작이 일관. |
| F-BRG-plugin-packaging | CONFIRMED | Custom Plugin Import용 패키징 절차: (1) `pkg`로 3 아키텍처(node16-macos-arm64/x64, win-x64) 빌드, (2) Mac 바이너리 `chmod +x`, (3) `metadata.json`을 `{"name":"<plugin name>"}`으로 작성, (4) 실행 파일을 `plugin`(Mac)/`plugin.exe`(Win)로 rename, (5) zip 압축 후 Connect Plugin 패널 +버튼으로 import. **SDK 자체는 비공개**(§7 Non-goals)이며, 패키징 절차만 사용자에게 노출 | Beta에서 지원 아키텍처 결정 필요(Linux 추가?), metadata 필드 확장 검토. F-IDM-plan-feature-matrix와 짝(Enterprise 한정 import). 출처: 강의 영상 7, L661-806. |
| F-BRG-debugger-baseline | CONFIRMED | Connect 메시지 디버거 패널 회귀 베이스라인: 5컬럼(Time·Message·Value·Pie·Source) + Clear 버튼 + 실시간 스트림. Source 컬럼은 메시지를 보낸 주체(Pie 이름 또는 Bridge App 이름)를 표시. F-BRG-16 Debugger 모드의 베이스이며 Beta에서 동등 이상 보장 | 5컬럼 회귀, Source 컬럼 정확성(Bridge App ppConnectAppName 반영), Multi-pie 환경에서 Pie 컬럼 구별, Clear 후 즉시 빈 상태. 출처: 강의 영상 1-2, L226-258; 영상 2, L139-160; 영상 6, L156-172. |
| F-BRG-bridge-app-detail | CONFIRMED | Bridge App = **Node.js 기반** 외부 실행체. 하드웨어 신호 ↔ Socket.IO 메시지 양방향 변환·중계. API JSON 응답도 ProtoPie 메시지로 변환 가능. Custom Plugin과 별개 개념이며 Enterprise 한정 | Bridge App import/실행, JSON → 메시지 변환 정확성, 인증 실패 시 동작(E-BRG-API-AUTH). 출처: Legacy Connect (User Side) §커스텀 플러그인 & Bridge App. |
| F-BRG-player-connect | CONFIRMED | ProtoPie Player 연결 3경로 회귀 베이스라인: (a) **QR 코드** — Connect에서 QR 표시, Player 앱 스캔으로 즉시 실행. iOS·Android·iPadOS 지원. (b) IP 주소 — 동일 WiFi 네트워크에서 Connect IP(포트 9981)를 Player에 직접 입력. (c) USB 케이블 — WiFi 없이도 USB 케이블로 기기 직접 연결해 테스트 가능 | 3경로 모두 동등 보장. iPadOS QR 스캔 회귀(레거시 명시 지원). 포트 9981 변경 시 영향 추적. USB 케이블 연결 시 OS별(macOS/Windows) 권한 흐름. 출처: Legacy Connect (User Side) §다기기 테스트. |
| F-BRG-wear-os | CONFIRMED | ProtoPie Player for Wear OS 페어링. Connect와 Wear OS 앱이 자동 페어링. **화면 두 번 탭으로 재시작/종료** UX. Apple Watch는 미지원. Enterprise 등급 Smartwatch Solution 패키지에 포함 | 페어링 자동성, 두 번 탭 인터랙션 인식, Apple Watch 시도 시 명확한 안내. F-VWR-mobile-bg(백그라운드 절전)와 짝. 출처: Legacy Connect (User Side) §다기기 테스트 + §Enterprise 전용. |
| F-BRG-multiview-url | CONFIRMED | MultiView(Stage View) URL 파라미터로 표시 방식 제어: `fullscreen`, `bg`(배경색), `hotspotHints`, `cursorHide`, `scaleToFit` 등. 같은 그룹의 여러 프로토타입을 단일 브라우저 탭에서 멀티스크린으로 실행하며 배경색·크기·레이아웃 커스터마이징 가능 | 각 URL 파라미터 동작 정확성 회귀(P1), 잘못된 값 입력 시 무시/에러 정책. 출처: Legacy Connect (User Side) §웹 브라우저 플레이어. |
| F-BRG-voice-proto | CONFIRMED | Web Player 음성 프로토타이핑: Voice Command Trigger, Speak Response, Listen Response를 Web Player에서 사용 가능. **Chrome·Edge(Chromium) 최적화**. 192.x.x.x IP 구성 시 일회성 브라우저 설정 필요(보안 컨텍스트) | Chrome/Edge 동작 회귀, Safari/Firefox 동작 정의, 192.x.x.x 구성 시 1회성 설정 가이드 UX, 마이크 권한 거부 시 fallback. 출처: Legacy Connect (User Side) §웹 브라우저 플레이어. |
| F-BRG-remote-browser | CONFIRMED | 동일 LAN 내 다른 기기 브라우저에서 Connect IP 주소로 접속해 프로토타입 원격 실행 (`http://[IP]:9981`). **PIN code 입력 필요** (F-IDM-pin-method와 연결). 별도 LAN 환경(Cross-network)은 Cloud Relay 경유(§3 Capability Matrix) | LAN 내 원격 접속 회귀, PIN 발급/입력/만료 흐름, 잘못된 PIN 차단, Cross-LAN 시도는 Cloud 모드로 유도. 출처: Legacy Connect (User Side) §웹 브라우저 플레이어. |
| F-BRG-network-otp | WIP | Local app 열린 포트 브라우저 접속 시 OTP 입력 플로우(XR·Unity 내부 플러그인 needs). Design Brief 260601 §2 Features g(Network settings)에서 동일 니즈 재확인 | |
| F-BRG-ota-update | WIP (rev12 신설, Scope: Desktop App) | **OTA(앱 업데이트) 방식**. 현재는 업데이트 항목이 있을 경우 Connect 앱이 업데이트 알림만 표시하고 `.dmg` 수동 다운로드를 유도. Studio와 같은 방식의 자동 업데이트 도입 여부 검토 중(Design Brief "가능할지?"). F-BRG-auto-update(디지털 서명 검증)와는 별개 — 본 항목은 업데이트 전달·설치 플로우 | 결정 후 회귀: 자동 업데이트 채택 시 업데이트 감지·다운로드·재시작 플로우, 사용자 취소/연기 처리, 서명 검증(F-BRG-auto-update)과의 연계, 수동 `.dmg` 폴백. 출처: Design Brief 260601 §2 Features j (OTA Update). |
| F-BRG-bottom-info | CONFIRMED | Bridge 하단 **Bottom menu / Information** 영역: (a) 로그인 유저 정보 표시 + Logout 액션, (b) Player 연결 정보 노출(연결 개수·종류), (c) Plugin 연결 정보 노출(활성 플러그인 수·상태), (d) Custom Fonts 진입점(F-STG-teamfont 참조) | Logout 클릭 후 즉시 로그인 화면으로 전환되고 라이센스 키 보존 여부가 정책과 일치(F-IDM-license-then-cloud). Player·Plugin 카운트가 F-PLG-states 전이와 실시간 동기화. 출처: TestRail S503 `Bottom menu / Information` (C127676~C127679). |

### 4-6. F-CLD — Cloud 서버·silo·배포

| ID | 상태 | 요구사항 | 검증 포인트 |
|---|---|---|---|
| F-CLD-dual-silo | CONFIRMED | **둘 다 Beta 출시.** Self-serve(B2C silo): `.io` 공유 multi-tenant, AWS ECS Fargate(task ≥2 Multi-AZ) + RDS Multi-AZ. Plan별 Connect 사용 자격 다름. Enterprise(B2B silo): 회사별 전용 EKS namespace + CNPG PostgreSQL pod. Plan gate 없이 Editor 이상이면 사용 가능 | schema·코드 동일, 호스팅 위치와 entitlement gate만 다르다. QA 작성 순서는 Enterprise 우선 → Self-serve Plan 케이스 보강. |
| F-CLD-stateless | CONFIRMED | 무상태 서비스 + Redis 메시지 동기화. 메모리 저장 금지 | 다중 인스턴스에서 일관된 응답을 반환한다. |
| F-CLD-team-rls | CONFIRMED | 모든 테이블에 team_id 컬럼 + RLS ON | 잘못된 Team 조회 시 자동 차단된다. |
| F-CLD-migration | CONFIRMED | DB 마이그레이션 도구 사용. 강제 초기화 금지 | |
| F-CLD-secrets | CONFIRMED | AWS Secrets Manager / External Secrets Operator 사용 | 하드코딩된 비밀 키가 거부된다. |
| F-CLD-cors-whitelist | CONFIRMED | CORS는 화이트리스트로 운영(와일드카드 금지) | 허용 origin 외 요청이 거부된다. |
| F-CLD-failover | CONFIRMED | AZ 단일 outage 시 RDS Multi-AZ failover로 분 단위 회복(NDA에 명시) | 운영 회복성 시나리오. |
| F-CLD-ws-cap | CONFIRMED | 동시 WebSocket 연결 ≤ 100명(Beta 단일 클러스터) | 한계 초과 시 동작 정의를 따라가는지. |
| F-CLD-region | CONFIRMED | us-west-2 단일 리전 | 멀티 리전은 Post-Beta. |
| F-CLD-embedded-included | CONFIRMED | Embedded Connect는 Beta scope에 포함된다(2026-05-21 회의 정정). 터미널 실행, 라이센스 키 기반, UI 없는 환경에서도 호스트 사용 가능. Windows 미니 PC 사용이 증가하는 흐름을 반영 | Headless 모드 부팅·라이센스 검증·터미널 로깅 회귀. |
| F-CLD-long-run | CONFIRMED | 이벤트·전시회에서 2~3일 연속 실행하는 시나리오가 존재. 데이터가 수 GB까지 증가할 수 있다 | 장시간 안정성·메모리 누수·로그 회전·디스크 사용량 테스트. |
| F-CLD-enterprise-cost | WIP | Cloud 사용 시 서버 비용 발생(현재의 2배). Enterprise 추가 청구 정책 논의 중. B2C는 현행 유지, B2B는 별도 판매 검토 | 정책 확정 후 entitlement gate 동작 검증. |
| F-CLD-fan-out | WIP | B2B silo N개에 대한 마이그레이션 fan-out 메커니즘 | ARCH §8-1 D-FanOut ADR. |

### 4-7. F-REL — Relay (실시간 통신)

| ID | 상태 | 요구사항 | 검증 포인트 |
|---|---|---|---|
| F-REL-stage-context | CONFIRMED | Relay 방은 Stage 컨텍스트 안에서 생성·관리한다. Team 격리가 자동 상속된다. **단 예외**: Connect 없이 Studio ↔ Player 1:1 직접 통신(F-REL-direct-channel) 시에는 Stage·Relay·Team 컨텍스트 모두 부재 — 별도 경로 | Stage 외부에서 Relay 시작이 차단된다. 직접 통신 경로와 Stage 경로가 명확히 구분되는지(메시지 디버거 Source 표기 차이). |
| F-REL-direct-channel | CONFIRMED | Connect를 거치지 않는 Studio ↔ Player 1:1 직접 통신을 지원한다(레거시 동등). 채널은 동일하게 `ProtoPi Studio`, Pie 2개 한정. 3개 이상은 Connect 경유 필수 | 2개 Pie 한정 동작 회귀, 3번째 Pie 추가 시도 차단 또는 Connect로 유도 카피, Team·Cloud 미연결 상태에서도 동작. 출처: 강의 영상 1-1, L201-209. |
| F-REL-room-ephemeral | CONFIRMED | Stage는 영구, RelaySession은 ephemeral(room_code는 세션 생애만 유효) | 방 만료 후 재진입이 차단된다(E-RELAY-1). |
| F-REL-viewer-invite | CONFIRMED | ViewerInvite(PIN·공유 링크·QR) + ViewerSession으로 외부 게스트 진입. Bridge↔Device 페어링용 Pin과는 별도 도메인 | 토큰 lifecycle 검증. |
| F-REL-pubsub | CONFIRMED | 다중 Cloud 인스턴스 간 메시지 동기화는 Redis pub/sub | 인스턴스 간 메시지 일관성. |
| F-REL-auto-reconnect | CONFIRMED | 서버 종료 시 클라이언트가 자동 재연결한다 | E-NET-2 동작(5초 후 자동 재입장). |
| F-REL-local-relay | CONFIRMED | Bridge 로컬 모드도 동일 Relay 프로토콜을 사용한다 | Cloud 연결 없이도 시연이 가능하다. |
| F-REL-unified-dispatch | CONFIRMED | 분산 하드웨어 이벤트와 stageview 미러링은 같은 dispatch 메커니즘을 공유 | |
| F-REL-channel-id | CONFIRMED | Pie ↔ Pie / Pie ↔ Plugin / Pie ↔ Bridge App 메시지 라우팅의 단일 채널 식별자는 **`ProtoPi Studio`**다. 송신측 send 트리거와 수신측 receive 트리거 모두 동일 채널을 선택해야 한다. 채널 불일치 시 메시지는 silent drop된다(레거시 동작) | 채널 미일치 시 silent drop 회귀, Beta에서 디버거에 경고 표시 여부 결정 필요(E-MSG-CHANNEL-MISMATCH 후보). 출처: 강의 영상 1-1, L43-46, L94-96. |
| F-REL-msg-value-var | CONFIRMED | 메시지는 **이름 + 선택적 값 1개**로 구성된다. 수신측에서 값을 사용하려면 변수에 assign 필수. 변수 타입(Number/Text)이 값과 불일치 시 동작 정책 미정(WIP) | 타입 불일치 시 silent drop / 에러 / 자동 캐스팅 중 정책 확정 필요. 출처: 강의 영상 1-1, L104-130. |
| F-REL-simultaneous-receive | CONFIRMED | 한 트리거 안에서 연속 호출된 다수 send는 수신측에서 **동시(simultaneous) 도착**으로 처리된다. 따라서 수신 로직은 그룹 중 한 메시지의 receive 트리거 내에서 다른 메시지 값(이미 변수에 들어와 있음)을 사용해 작성 가능 | 분산 환경(Cloud Relay 경유)에서도 동시 도착 보장이 유지되는지 — **F-REL-envelope 설계 핵심**. 출처: 강의 영상 1-1, L135-142. |
| F-REL-msg-naming | CONFIRMED (가이드 영역) | 메시지 명명 컨벤션(강제 아님, 학습 자료 표준): 외부(Pie 간) 메시지는 UPPERCASE, 내부(Scene/Component 안) 메시지는 lowercase | 카피·튜토리얼 산출물 일관성 검증 시 참조. 출처: 강의 영상 1-1, L50-61. |
| F-REL-flood-prevention | WIP | 연속 변경값(slider width 등)의 detect 트리거 + 다중 컴포넌트 인스턴스 조합은 메시지 폭주를 일으킨다. 레거시는 silent 처리하나 Beta Cloud Relay 환경에서는 네트워크·Redis 부하로 직접 전이. **rate limiting / backpressure 정책 필요** | E-PLG-MSG-FLOOD 후보. dev 5주 결정. 출처: 강의 영상 1-2, L286-306. |
| F-REL-envelope | WIP (우선 처리 권고) | 메시지 envelope과 idempotency(per-Bridge monotonic seq + Redis dedupe window). **F-REL-channel-id / msg-value-var / simultaneous-receive / flood-prevention 5개 항목이 envelope 설계에 의존하므로 dev 5주 중 우선 처리 권고**. **레거시 Arduino `\|\|` 구분자는 입력 계층에서 계속 지원**(기존 사용자 스케치 무수정 동작 보장) — Beta envelope는 내부 표현이며 외부 입력은 호환 파싱 | ARCH §8-1 D2/D12 ADR. 기존 Arduino 스케치 무수정 회귀 케이스 필수. |
| F-REL-hw-conflict | WIP | 둘 이상의 사용자가 동시에 같은 입력 채널을 사용할 때 충돌 처리 정책 | S10 시나리오에서 검증. |
| F-REL-multi-bridge | WIP | 여러 Bridge가 동시 활성일 때 마스터 결정 정책 | |

검증 우선순위: idempotency 미정 상태에서의 중복 메시지 dispatch, 분산 하드웨어 입력 latency p95, 채널 미일치 silent drop, 다중 컴포넌트 인스턴스의 메시지 폭주.

### 4-8. F-VWR — Stageview / Viewer

레거시 사용자 가시 기능이며, Beta는 동등 보장 + 단순 개선만 수행한다.

| ID | 상태 | 요구사항 | 검증 포인트 |
|---|---|---|---|
| F-VWR-selective-pie | CONFIRMED | 시청자가 시청할 Pie를 선택할 수 있다(레거시: 모든 Pie 강제 시청) | Pie 목록 표시·전환이 정상 동작한다. |
| F-VWR-cloud-relay | CONFIRMED | Cloud Relay를 경유한 분산 시청(레거시: LAN 한정) | LAN 외에서도 시청이 가능하다. |
| F-VWR-auto-reconnect | CONFIRMED | 자동 재연결 + 마지막 상태 복구(레거시: 수동 재접속) | 끊김 → 자동 복구율 측정. |
| F-VWR-browser-only | CONFIRMED | URL/QR 한 번으로 즉시 시청. Connect 설치가 필요하지 않다 | 브라우저만으로 진입이 완료된다. |
| F-VWR-quality | CONFIRMED | 화질은 레거시 수준을 유지한다. 적응형 화질은 scope 외 | |
| F-VWR-readonly | CONFIRMED (rev10 표현 정정) | Viewer 기본 상태는 **View Mode = 시청 전용**. Pie 실행·메시지 전송 불가. 단 Interaction Mode 토글 ON 시는 예외(F-VWR-interaction-toggle 참조). Stage 편집·구조 변경은 어느 모드에서도 불가. | View Mode 기본 진입 시 인터랙션 거부, 메시지 전송 시도 차단. 토글 ON 시 인터랙션 허용으로 즉시 전환(F-VWR-interaction-toggle 검증과 연동). Node View 편집·Console 로그·Player QR/USB 연결·하드웨어 액션은 어느 모드에서도 차단(ACL §3 표 기반). |
| F-VWR-interaction-toggle | WIP (rev10 신설, ACL §3) | Viewer는 화면 내 **개인 토글로 View Mode ↔ Interaction Mode 전환** 가능. Interaction Mode = Pie 실행·메시지 전송 허용. Role 전환이 아니라 mode 전환이며 Stage Role은 viewer로 유지. 토글 ON 상태의 행위자를 Participant로 칭한다(§1 용어). 같은 Pie에서 다수 Viewer가 동시에 Interaction Mode를 켤 수 있다. ACL 확정 후 CONFIRMED 승격. | (1) View Mode → Interaction Mode 전환 시 즉시 Pie 인터랙션 가능, 다시 View Mode 복귀 시 인터랙션 차단. (2) Stage 편집 액션(레이어 추가·삭제·구조 변경)은 두 모드 모두 차단. (3) ACL 미결: Q-1 Editor 알림 정책(WIP, §10 watch). (4) ACL 미결: Q-2 다수 Participant 동시 인터랙션 충돌 처리(E-PLG-MSG-FLOOD §6과 매핑 검토, §10 watch). (5) 토글 상태가 페이지 새로고침·재진입 시 어떻게 보존되는지 정책 확정 필요(WIP). (6) ACL 미결: Q-5 **Editor가 Viewer의 Interaction Mode 토글을 비활성화(잠금)할 수 있는가** — 잠금 가능 시 Viewer 토글 UI 비노출/disabled 처리, 잠금 Stage에서 토글 시도 차단 회귀(rev11 ACL §6 신규, §10 watch). |
| F-VWR-acl-mapping | CONFIRMED (rev10 신설, ACL §6) | 레거시 명칭 → CoC 명칭 매핑을 본 spec의 정답으로 둔다. **Host → Editor**(Stage 생성자/편집자에 흡수). Editor → Editor. Participant(Guest) → Viewer + Interaction Mode ON(토글로 흡수). Viewer → Viewer(기본 View Mode). Guest ↔ Viewer는 Role 전환이 아니라 mode 전환이다. | 회귀 케이스 변환 시 레거시 카피("Host", "Guest", "Participant")가 UI에 잔존하지 않는지 검출. §13 Δ-15 회귀 변환 컬럼과 1:1. |
| F-VWR-nodeview-access | WIP (ACL §4, rev12) | **Node View 접근 경로 규칙.** Editor: Player/URL로 접근 가능, 편집 가능. 단 Player를 통해서는 Node View 접근 불가(TBD — Player 내 Editor도 차단인지 확인 필요). Viewer: URL 직접 공유만 가능, 확인은 가능하나 편집 불가. Viewer는 Player/Stage 화면 내에서 Node View 진입 경로 없음. Q4 미결: Node View URL Viewer 접근 시 인증 요구 여부(PIN 등). | Editor: Stage 내에서 Node View 접근 가능, Player 탭 내에서는 Node View 진입 불가. Viewer: URL로만 접근, Stage/Player 화면 내 직접 진입 차단. Viewer의 Node View URL 접근 시 인증 정책 확정 후 보안 케이스 추가. |
| F-VWR-editor-notify | WIP (ACL §6 Q1, rev12) | Viewer가 Interaction Mode ON 시 **Editor에게 알림이 가는가** 여부. UI 및 실시간 상태 표시에 영향. 정책 미결. | 알림 있는 경우: Editor 화면에 Viewer 상태 변경 표시 회귀. 알림 없는 경우: 변경 없음. 결정 후 케이스화. |
| F-VWR-link-expiry | WIP (ACL §6 Q3, rev12) | Viewer 공유 링크(URL/QR/PIN) **만료 정책**. 시간 제한 vs 무기한. 보안 및 운영 정책 미결. | 시간 제한 시: 만료 후 접근 차단, 에러 처리. 무기한 시: 링크 revoke 수단 확인. |
| F-VWR-interaction-isolation | WIP | **다수 Viewer가 동시에 Interaction Mode일 때 인터랙션 상태 격리 모델**. 같은 Stage를 열어도 각 사용자는 개별 instance를 가지며, 한 Viewer의 Pie 인터랙션으로 생긴 화면/변수 상태가 다른 Viewer 화면에 실시간 동기화되지 않는 것이 현재 합의된 기본값. 예외: Pie 추가/삭제 같은 Stage 구성 변경은 브로드캐스트될 수 있음. 다수 Participant 동시 인터랙션 충돌 처리 설계는 미결(F-VWR-interaction-toggle Q-4 참조). 출처: User Flow Discussion 미팅, 2026-06-09. | Viewer A 인터랙션 결과(화면·변수 상태)가 Viewer B에게 미반영됨을 확인. Stage 구성 변경(Pie 추가/삭제)은 전체 반영되는지 확인. 충돌 처리 정책 확정 후 케이스 보강. |
| F-VWR-auth-policy | WIP | 시청자 인증 정책(공개 URL vs Team 한정 vs 토큰 게스트) | |
| F-VWR-mobile-bg | WIP | 모바일 OS 백그라운드 절전 모드 처리(자동 일시정지·복귀) | |
| F-VWR-selective-ux | WIP | 선택적 Pie 시청 UX(목록·전환·다중 선택) | |
| F-VWR-player-participant | CONFIRMED | **Player가 시청자(viewer)가 아니라 참여자(participant)로 진입하는 시나리오**. Stage View 안의 각 Pie는 QR 코드를 노출하고, Player 앱에서 QR을 스캔하면 해당 Pie 1개를 실행하며 같은 Stage 컨텍스트의 메시지를 양방향 송수신한다. F-VWR-readonly(외부 게스트 시청 전용)와 명확히 구분된다. Non-goals "Stage view from the Player"는 별개 개념(Player에서 Stage 화면 자체를 보는 것 = 제외) | 데스크탑 브라우저 + 실제 모바일·태블릿 다수가 동일 Stage View 안의 Pie를 각자 실행하면서 메시지를 주고받는지 회귀. Player 측 send가 다른 디바이스로 전파되는지. 출처: 강의 영상 1-2, L341-376; 영상 5, L1162-1180. |

### 4-9. F-AUD — 감사·관찰성

| ID | 상태 | 요구사항 | 검증 포인트 |
|---|---|---|---|
| F-AUD-change-log | CONFIRMED | 모든 변경 작업을 기록한다. 보존 기간 90일 | Team 생성·삭제·멤버 변경이 기록되는지. |
| F-AUD-error-metrics | CONFIRMED | 에러 카탈로그(§6)의 모든 에러를 운영 메트릭에 기록 | Beta 평가 시 빈도·영향 분석에 사용된다. |
| F-AUD-msg-record | CONFIRMED | **메시지 Recording (Enterprise)**: 프로토타입 실행 중 주고받은 모든 메시지를 CSV 파일로 저장. 디버거 패널 우측 하단의 Record 버튼이 진입점(F-HOM 레거시 베이스라인의 "Record" 항목) | CSV 컬럼 스키마(Time/Message/Value/Pie/Source) 일관성, 장시간 레코딩 시 파일 크기 관리, 레코딩 중 메시지 누락 0건. Enterprise 미만 등급에서 Record 버튼 비활성화. 출처: Legacy Connect (User Side) §디버깅 & 메시지 모니터링. |
| F-AUD-msg-playback | CONFIRMED | **CSV Import & Playback (Enterprise)**: 진입점은 Debug 패널 우측 하단 Import 버튼(Record와는 별개의 독립 버튼). Import 클릭 → CSV 파일 선택 → Import 세팅 모드로 화면 전환. 모드 안에서 (a) 불러온 메시지 목록 표시, (b) 재생, (c) 정지, (d) 반복재생 설정, (e) 재생 속도 설정, (f) 나가기(모드 종료) 액션 제공. Import 세팅 모드 활성 동안 Record·Clear 버튼은 비활성. 메시지가 없는 인터랙션은 재현 불가(터치/탭 등 직접 입력은 대응하지 않음) | Import 버튼 진입점 가시성, CSV 형식 검증(잘못된 형식 거부 + 카피), Import 세팅 모드 진입·이탈 시 화면 전환 정확성. 모드 안 액션: 재생 timing(원본 timestamp 또는 상대 시간), 정지 후 재개·정지 후 재생 처리, 반복재생 끊김 없음, 재생 속도 0.5x/1x/2x 등 정확성, 나가기 시 진행 상태 처리(저장 X). 모드 활성 중 Record·Clear 비활성(disabled UI). 비-메시지 인터랙션이 재현 대상 아님을 사용자에게 명확히 안내. 시연 자동화·데모 자동화에 핵심. 출처: Legacy Connect (User Side) §디버깅 & 메시지 모니터링 + §Enterprise 전용 + Paige 실 동작 확인(2026-05-27). |
| F-AUD-record-ui-sequence | CONFIRMED | Debug 패널 UI 구성(레거시 S503 베이스라인 + Paige 실 동작 확인 2026-05-27). **메인 액션 3 버튼**(우측 하단, 각자 독립): Record(녹화 시작/중지) / Import(CSV 불러오기 → Import 세팅 모드 진입, F-AUD-msg-playback) / Clear(메시지 로그 초기화). Import 세팅 모드 내부 5 액션: 재생 / 정지 / 반복재생 설정 / 재생 속도 설정 / 나가기. 모드 활성 동안 Record·Clear는 비활성. 또한 Debug Message 영역에서 Send 단발성 전송(동일·다른 내용 반복 회귀), 필수 값 미입력 시 차단 | 메인 3 버튼 독립 동작(Record 중 Import 시도 차단/허용 정책 명문화 필요, WIP). Import 세팅 모드 진입 시 Record·Clear 비활성(disabled UI) 즉시 반영, 모드 이탈 시 비활성 해제. Send 필수 값 검증·Clear 즉시 빈 상태. Send/Receive 통신은 Pie↔Pie / Pie↔Player 양방향 모두 회귀. 출처: TestRail S503 `Debug > Message 동작 확인` (C127680~C127685), `Debug > Send/Receive 통신` (C127686~C127687), `Debug > Record` (C127689~C127693) + Paige 실 동작 확인. |

### 4-10. F-API — REST API 엔드포인트 (Bridge ↔ Server)

레거시 S503 회귀 케이스에서 직접 검증되는 Bridge ↔ Server REST API 표면이다. Beta에서 동등 보장 + 인증·권한 게이트(F-IDM-connect-entitlement, F-STG-stage-role) 일관 적용이 회귀 우선순위다. 모든 엔드포인트는 인증 실패·권한 부족·잘못된 ID 입력 시 명확한 4xx 응답을 반환해야 한다.

| ID | 상태 | 요구사항 | 검증 포인트 |
|---|---|---|---|
| F-API-pies | CONFIRMED | `GET /api/pies` — Pie List information 조회. 빈 상태·존재 상태 모두 정상 응답 | 빈 리스트 시 200 + `[]`, 존재 시 권한 필터링된 목록만 반환. 출처: S503 C127794~C127795. |
| F-API-pies-upload | CONFIRMED | `POST /api/pies/upload` — Local Pie 업로드. 인증 필수 | Connect 미로그인·Connect 종료 상태에서 차단, 잘못된 파일 거부. 출처: S503 C127808~C127811. |
| F-API-pies-uploadCloud | CONFIRMED | `POST /api/pies/uploadCloud` — Cloud Pie 업로드. Cloud login + Pie/Project 권한 필요. **Pro plan 계정에서는 실패** 정의됨 | Cloud 미로그인·Connect 미로그인·Pro plan·Pie/Project 권한 없음·Pie id 불일치 6 실패 케이스 회귀. 출처: S503 C127800~C127807. |
| F-API-pies-delete | CONFIRMED | `POST /api/pies/delete` — 1개·다수 Pie 삭제. 잘못된 ID 혼합 시 부분 실패 정책 | 정상 1건·다중 삭제, 무효 ID 단독·혼합 4 케이스. 출처: S503 C127796~C127799. |
| F-API-groups | CONFIRMED | `GET /api/groups`, `POST /api/groups/add`, `POST /api/groups/remove` — Group 조회·생성·삭제. F-STG-group-1level 강제 | 빈/존재 조회, add 후 정렬 namespace 유지, remove 시 cascade(F-STG-cascade-delete) 동작. 무효 ID 단독·혼합 회귀. 출처: S503 C127785~C127788, C127791~C127793. |
| F-API-groups-updatePie | CONFIRMED | `POST /api/groups/updatePie` — Pie를 **Group↔Group 이동 한정**. F-STG-pie-in-group(모든 Pie는 Group에 종속) 강제 — root를 source/target으로 지정한 요청은 거부 | 정상 1 패턴(Group→Group) + **root를 source/target으로 지정한 요청 400 거부**(rev6 정책 변경) + 무효 Pie ID·무효 Group ID·group_id 누락 실패 케이스. 출처: S503 C127777~C127784(Beta 변환 시 root 이동 케이스는 거부 케이스로 전환). |
| F-API-players | CONFIRMED | `GET /api/players` — Player 연결 정보 조회. 미연결·연결 상태 모두 정상 응답 | 빈 상태 200 + 빈 목록, 연결 상태 목록 정확성. 출처: S503 C127775~C127776. |
| F-API-players-run | CONFIRMED | `POST /api/players/run` — 특정 Player에서 Pie 실행. 이미 실행 중·미연결 시 명확한 에러 | 정상 실행, 중복 실행, 미연결 에러 회귀. 출처: S503 C127770~C127772, C127789~C127790. |
| F-API-players-runAll | CONFIRMED | `POST /api/players/runAll` — 전체 연결 Player에서 일괄 실행 | 전체 실행 정확성, Player 0개일 때 에러 응답. 출처: S503 C127773~C127774. |
| F-API-players-loadPie | CONFIRMED | `POST /api/players/loadPie` — 특정 Player에 특정 Pie 로드 | 정상·실패 케이스. 출처: S503 C127768~C127769. |
| F-API-auth-uniform | CONFIRMED | 모든 API 공통: **인증·권한 실패 응답 카피·코드 일관**. Connect 미로그인 / Cloud 미로그인 / 권한 없음 / 무효 ID 4 카테고리를 동일 패턴으로 처리 | 카피 일관성, HTTP status 코드 일관(401/403/404 구분), 멤버·Stage role별 거부 응답이 §6 에러 카탈로그와 매핑되는지. F-IDM-connect-entitlement·F-STG-stage-role 게이트와 1:1 일치. |

검증 우선순위: ① RLS·권한 우회를 차단하는 인증·권한 응답 일관성(P0), ② Pie/Group 이동·삭제 시 cascade 및 **F-STG-pie-in-group**(모든 Pie는 Group 종속) 강제(P1), ③ 잘못된 ID 혼합 시 부분 실패 정책 명문화.

## 5. 핵심 시나리오

각 시나리오는 user story 수준의 high-level 의도다. 상세 step·success criteria는 dev 5주 중 user research와 디자인 산출물로 정제된다. QA는 시나리오 ID를 테스트 케이스의 출처로 사용한다.

| ID | 시나리오 | 검증 대상 |
|---|---|---|
| S1 | 개인 사용자 온보딩 (B2C) | 가입 → Pie·플러그인 자력 작성 |
| S1-2 | B2C 멤버 초대 | Team 멤버십 + 역할 기반 권한 |
| S3 | 원격 시연 + Viewer 게스트 | 빠른 파이 공유, 외부 클라이언트 시연 |
| S8 | 디바이스 분실 (최소 revoke) | Device 단위 토큰 차단, 사용자 전체는 차단되지 않음 |
| S10 | 분산 하드웨어 협업 | P2 검증 (클라우드 환경에서 핵심 워크플로 작동) |
| S11 | Stageview 미러링 | 레거시 동등 + 단순 개선 |
| S12 | Stage 생성·초대·격리 | Discord 채널 모델, 회사 워크플로우 정착 |
| S13 | 원격 UX 리서치 (Design Brief i) | 서울 리서처(Host)가 Cloud Stage 생성·녹화, 베를린 참가자(Participant)가 초대 링크로 폰에서 프로토타입 구동 → POS 디바이스 반응. 디자이너·PM은 view-only 링크로 시청(Viewer). Host/Participant/Viewer 3역할 + 연결 디바이스 |
| S14 | 내부 디자인 리뷰 (Design Brief ii) | 디자이너(Host)가 단일 Cloud Stage에서 스티어링 휠 등 하드웨어 설정 + pie 구동, 이해관계자(Viewer)는 sharable link로 직접 테스트. Cloud Stage preview가 하드웨어 입력에 반응 |
| S15 | 자동차 HMI + Unity/Unreal 런타임 (Design Brief iii) | 디자이너가 pie + Unity 차량 인테리어 모델로 스티어링 휠 인포테인먼트 인터랙션 프로토타이핑. **Unreal 런타임 언급은 신규**(기존 spec은 Unity 한정) — Unreal 지원 범위는 확인 필요(WIP watch) |

### S10 — 분산 하드웨어 협업

2명 팀이 자동차 대시보드 프로토타입을 함께 시연하는 흐름이다.

1. 멤버 A가 Bridge A에 Arduino(회전 다이얼)를 연결한다.
2. 멤버 B가 Bridge B에 MIDI(페이더)를 연결한다.
3. 두 사람이 같은 Team에 소속되어 있고, 한 명이 Relay 방을 생성한 뒤 다른 한 명을 초대한다.
4. A의 Arduino 회전 → Cloud Relay → B의 화면에 즉시 반영된다. 동시에 B의 MIDI 페이더 입력이 A의 화면에 반영된다.
5. 양쪽 하드웨어 입력이 하나의 프로토타입 상태에 통합된다.

검증 지표: 한 Team 안에서 동시 활성 Device ≥2인 세션 카운트, 분산 하드웨어 세션 평균 지속 시간·끊김률, latency 허용 범위(레거시 baseline 도출 후 정의).

### S11 — Stageview 레거시 vs Beta 개선점

| 측면 | Legacy | Beta | 측정 |
|---|---|---|---|
| 시청 대상 | 모든 Pie 강제 시청 | 시청자가 Pie 선택 | 세션당 평균 선택 Pie 수 |
| 반응성 | LAN 한정 | Cloud Relay | p50/p95 latency |
| 다중 디바이스 동기화 | 화면별 드리프트 | 단일 상태 소스 + 동시 dispatch | 동기화 드리프트(ms) |
| 연결 안정성 | 수동 재접속 | 자동 재연결 + 상태 복구 | 자동 복구율 |
| 온보딩 | Connect 설치 필요 | URL/QR 한 번 | 첫 화면 도달 시간 |
| 시청 인원 | 같은 LAN 소수 | Cloud Relay 통해 분산 다수 | 동시 시청자 수 |

## 6. 에러 카탈로그 (S-ERR)

모든 에러는 운영 메트릭에 기록되며 Beta 평가 자료가 된다. 카피·복구 흐름의 상세 detail은 dev 5주 중 정제된다.

| 코드 | 상황 | 사용자 화면 | 시스템 동작 | 복구 |
|---|---|---|---|---|
| E-AUTH-1 | ProtoPie Cloud 로그인 실패 | "로그인 실패. 다시 시도" 모달 | Bridge 시작 화면 유지 | 사용자 재시도 |
| E-AUTH-2 | Device 토큰 만료 | "세션이 만료되었습니다. 다시 로그인" | 자동 로그아웃 + 로그인 화면 | 재로그인 |
| E-AUTH-3 | Device 토큰 차단(분실 신고 등) | "이 디바이스는 차단되었습니다" | Bridge 잠금 | 관리자가 차단 해제 |
| E-ENT-1 | Team Entitlement 만료·결제 실패 | "Connect 사용 기간이 끝났습니다" 차단 | 즉시 읽기 전용 모드 | 결제 갱신 시 즉시 복구 |
| E-ENT-2 | Cloud 장애로 Entitlement 검증 불가 | (무음) | 캐시 토큰으로 24h 읽기 전용 grace | Cloud 복구 시 자동 |
| E-NET-1 | Cloud 연결 끊김 | "Cloud 연결 끊김. 재연결 시도 중…" 토스트 | 자동 재연결(지수 백오프) | 네트워크 복구 |
| E-NET-2 | Relay 방 연결 끊김 | "방에서 끊어졌습니다. 재입장" | 5초 후 자동 재입장 시도 | 자동 또는 수동 |
| E-DEV-1 | Device 등록 실패(네트워크·시계 오차) | "디바이스 등록 실패: [이유]" + 재시도 | 등록 화면 유지 | 사용자 재시도 |
| E-PLG-1 | 플러그인 실행 크래시 | 카드에 빨간색 + "재시작" | 자동 1회 재시작 후 실패 시 정지 | 사용자 재시작 또는 코드 수정 |
| E-PLG-2 | manifest 잘못됨(Import 시) | "플러그인 형식 오류: [상세]" | Import 거부 | 사용자가 zip 수정 후 재업로드 |
| E-USB-1 | USB 디바이스 권한 없음(macOS) | "Arduino 사용 권한 필요" + 시스템 설정 deep-link | 디바이스 미인식 유지 | 사용자가 권한 부여 |
| E-PAY-1 | 결제 → Bridge 가시성 latency | "결제 처리 중. 1~2분 후 새로고침" + 버튼 | 폴링(15초 간격) | 1~2분 내 자동 또는 수동 새로고침 |
| E-TEAM-1 | Connect 사용 가능 Team 없음 | "Connect Addon 구매하기" + Cloud 결제 링크 | Bridge 잠금 | 결제 후 자동 |
| E-RELAY-1 | Relay 방 만료·종료 | "이 방은 종료되었습니다" + 새 방 생성 | 방 목록으로 복귀 | 새 방 생성 |
| E-OS-1 | macOS Gatekeeper / Windows SmartScreen 경고 | OS 기본 경고 화면 | (Bridge가 직접 안내 불가) | OS 신뢰 후 재실행 또는 코드 서명 정상화 |
| E-MSG-CHANNEL-MISMATCH | Pie의 send/receive 채널이 ProtoPi Studio가 아니거나 양측 불일치 | (레거시 무음. Beta에서 디버거 경고 표시 검토) | 메시지 silent drop | 사용자가 채널을 ProtoPi Studio로 일치시킴 |
| E-PLG-BAUD-MISMATCH | Arduino 플러그인 baud rate와 보드 코드 baud rate 불일치 | 메시지 미수신, 에러 미표시 | 시리얼 통신 무응답 | 사용자가 baud rate 일치(예: 115200) |
| E-PLG-PORT-BUSY | Arduino IDE 또는 다른 앱이 시리얼 포트 점유 | 플러그인 실행 실패 또는 무응답 | 포트 open 실패 | 점유 앱 종료 후 플러그인 재실행 |
| E-BRG-API-AUTH | Custom Bridge App이 외부 API 인증 실패(token 만료·잘못된 키 등) | 앱 stdout에 에러, Connect 메시지 로그는 무음 | 앱 종료 또는 idle | 사용자가 토큰 갱신 후 Bridge App 재시작. **F-CLD-secrets 정책과 사용자 책임 경계 명확화 필요** |
| E-PLG-MSG-FLOOD | 다중 컴포넌트 인스턴스의 연속 send로 메시지 폭주 (F-REL-flood-prevention 미적용 상태) | (현재 무음) | 메시지 큐 적체·Cloud Relay 부하 | rate limit 트리거 후 dispatch 제한, Pie 측 detect 트리거 재설계 가이드 |

## 7. 테스트 범위에서 제외 (Non-goals)

이번 Beta에서 테스트하지 않는 항목이다. Post-Beta 진입 시 재검토한다.

PRD에 명시된 Non-goals:
- AI 기능 (Bridge·Cloud 양쪽). 별도 정책 결정 대기.
- 플러그인 마켓플레이스 / 공용 레지스트리. Team 별 프라이빗 공유만 지원.
- 3rd-party 플러그인 개발자 생태계. 사용자 직접 작성만 허용.
- 플러그인 결제·수익 분배.
- 플러그인 URL/git import. 파일 업로드만 허용.
- 플러그인 코드 서명·검수. 사용자 본인 책임 모델.
- On-prem / air-gapped 배포. Beta는 Connect-managed만 지원하며, B2B EKS silo 구조로 Post-Beta 진입 비용을 낮춰둔다.
- Team 간 자원 공유 / 워크스페이스 초대.
- 엔터프라이즈 운영 기능(SSO·SAML·SCIM·CMEK).
- Local DB ↔ Cloud DB 동기화. 모드 전환 시 새 환경으로 인지(자동 이전 없음).
- UT(Connect-aware User Testing). Post-Beta candidate.
- Stage view from the Player(Player 네이티브 web embed/Unity/camera에서 Stage 화면 자체를 띄우는 것). Post-Beta. **단 Player가 QR 스캔으로 단일 Pie를 실행하면서 Stage 메시지에 참여하는 시나리오는 F-VWR-player-participant로 scope-in.**
- Webhook(외부 인터넷 트리거).
- Send/Receive SDK 공개. **Custom Plugin Import는 Enterprise 한정으로 지원(F-IDM-plan-feature-matrix)되나, SDK 명세·boilerplate·공식 문서는 공개하지 않는다.** 사용자가 socket.io-client 등으로 자체 구현 → 패키징 절차(F-BRG-plugin-packaging)만 노출.
- Cross-network 원격 연결의 P2P/VPN/LAN 브리징 대안.

2026-05-21 회의에서 추가로 scope-out된 항목:
- Stage 필터·검색 기능.
- Stage 정렬(최근 편집순·Recently Opened). 회의 마지막 정정에 따라 scope-out 확정.
- 실시간 Sync 보강. 알려진 한계: 중간 참여자는 이전 상태를 볼 수 없으며, 새 참여자 진입 시 전체 리셋 대신 사용자 간 차이를 허용하는 방향을 검토. UT 통합 시 추가 고려.
- Kick 기능. 검토된 안은 호스트가 Editor 권한자로서 플레이어(디바이스) 단위로 Kick하는 모델이었으나 이번 Beta에서는 미포함.

2026-05-28 ACL WIP 반영(rev10)으로 추가 scope-out된 항목:
- **Private Stage / Shared Stage 구분**(ACL §6). Beta Cloud Stage는 단일 공유 모델로 운영. F-STG-private-shared·F-STG-auto-personal DEFERRED. Post-Beta에서 재도입 검토.
- **"내 작업실" 자동 생성**(F-STG-auto-personal DEFERRED). 가입 직후 빈 상태는 별도 UX로 처리(F-HOM watch).

회의에서 검토 후 scope에 포함으로 유지된 항목:
- Embedded Connect는 F-CLD-embedded-included로 포함된다(제외 후보에서 정정).
- 게스트 인증은 F-IDM-pin-method로 PIN 방식을 유지한다(호스트 승인 방식은 추후 검토 여지).

알려진 이슈로 watch만 하는 항목:
- 클라우드 파이 편집 시 처리 방안 검토 필요.
- 커스텀 폰트가 로컬 환경에서 함께 다운로드되지 않는 이슈 존재.

## 8. 정량 목표 (Beta)

Beta는 외부 SLA를 약속하지 않는다. 임계값은 레거시 Connect 사용 데이터로부터 baseline을 도출한 뒤 본 섹션에 추가한다.

| 영역 | 측정 항목 |
|---|---|
| Go/No-Go | S10 동시 활성 Device ≥2 세션 누적 카운트 |
| 온보딩 (S1 / S1-2) | 가입자 Pie 생성률, 첫 N일 retention |
| 분산 하드웨어 (S10) | 동시 활성 Device 세션 수, 세션당 Device 수 |
| Stageview (S11) | 세션 누적, 동시 시청자, latency p50/p95, 재연결 성공률, 선택적 Pie 시청 비율 |
| Stage (S12) | 생성률, Shared 비율, 초대 → 수락 → 첫 진입 시간, 데이터 누출 0건(정성 0-tolerance) |
| API 운영 | API p95 응답 지연 |
| Relay 운영 | Relay 메시지 지연 p95 |

운영 제약(Beta scope): 동시 WebSocket ≤ 100명(단일 클러스터), 멀티 리전 1개(us-west-2). RDS Multi-AZ failover로 분 단위 회복.

## 9. 테스트 환경 매트릭스

회귀·통합 테스트에서 다뤄야 할 차원이다. 모든 조합을 수행하지 않더라도, 결정에 영향을 주는 차원을 명시한다.

| 차원 | 값 |
|---|---|
| OS | macOS, Windows |
| 모드 | Cloud (브라우저), Desktop Cloud-login, Desktop License-key, Embedded (터미널·헤드리스) |
| 네트워크 | LAN only, Cloud Relay, Hybrid |
| Team 타입 | B2C silo, B2B silo |
| 사용자 권한 | Team Owner/Admin/Member/Viewer × Stage owner/editor/viewer |
| 하드웨어 | USB, Serial, MQTT 대표 디바이스 1종 이상(Arduino, G29, MIDI, Gamepad, blokdots) |
| 외부 클라이언트 | 모바일 iOS·Android, 웹 브라우저(Chrome·Safari·Edge) |
| 운영 시간 | 단발성(1~2시간), 일상(8시간), 장시간(2~3일 연속, 이벤트·전시회) |
| 진입 경로 | URL 직접 입력, 북마크, Cloud 로그인 후 redirect, Desktop 첫 실행, Embedded 터미널 부팅 |

### 9-2. 레거시 회귀 시드 (TestRail Suite 매핑)

이전 ProtoPie Connect의 TestRail 2개 suite를 Beta 회귀 시드로 사용한다. **신규 작성이 아니라 케이스 ID를 출발점으로 Beta 환경에 맞게 변환**한다(레거시 PC 화면 → Cloud 브라우저, 단일 사용자 → 멀티 사용자/멀티 디바이스 등). `is_converted` 컬럼이 1인 케이스는 이미 신규 포맷으로 전환된 것이며, 0인 케이스는 검토 후 변환·삭제 결정이 필요하다.

**Suite 개요**:

| Suite ID | 명칭 | 케이스 수 | 초점 | 사용 시점 |
|---|---|---|---|---|
| **S280** | 2.9.0 POR Plan | 309 | Plan entitlement 매트릭스(Free / Basic-Core / Pro-Core / Pro Plus-Core / Pro Plus-Enterprise / Enterprise) | F-IDM-plan-feature-matrix·F-PLG-tier-limits·F-IDM-upsell-modal 변환 시 |
| **S503** | Master Regression | 232 | Pie List·Stage View·Plugin 연결·Debug·API·Custom Font 등 기능 회귀 전반 | 각 F-* 별 케이스 변환 시. Plan gate 외 영역의 1차 시드 |

**S280 → F-* 매핑** (Plan 등급 6종 × 영역 6종 매트릭스):

| S280 Section 영역 | 매핑 F-* | Beta 변환 시 유의점 |
|---|---|---|
| Account plan 표시 확인 | F-HOM, F-IDM-edit-role | Plan 라벨 카피만 변경(Free → Connect Free 등). Cloud SoT 의존 |
| [Local Pie] Disable / Cloud Pie Upload 한도 | F-PLG-tier-limits, F-STG-pie-source | 한도 수치는 §3-2 매트릭스 따라 재확정 |
| Players Connected 제한 | F-PLG-tier-limits, F-BRG-player-connect | Web/iOS/Android/USB 4 채널 모두 회귀 |
| Plugins (API/IFTTT/Arduino/Blokdots/Gamepad) | F-PLG-tier-limits, F-PLG-preset-* | Free 3분 만료·동시 실행 한도 강제 |
| Stage View (Pie/Web Embed/Camera/Smart Watch) | F-STG-svw-layers, F-STG-svw-edit-mode, F-BRG-wear-os | Plan별 레이어 수량 한도 + 비가용 시 Upsell |
| Dashboard / Pie upload / Players Connect | F-HOM, F-STG-pie-source, F-PLG-tier-limits | 등급 상승 시 한도 해제 즉시 반영 |
| 모든 Upsell 트리거 | F-IDM-upsell-modal | 3 버튼 URL·카피 variant(Enterprise vs Core) 회귀 |

**S503 → F-* 매핑** (기능 회귀 전반):

| S503 Section 영역 | 매핑 F-* | 케이스 ID 범위(샘플) |
|---|---|---|
| Plan Login > Free / Connect core (lite) | F-IDM-connect-entitlement, F-IDM-upsell-modal | C127812~C127828 |
| New (Upload) > Loacl Pie / Cloud Pie / Pie Role | F-STG-pie-source, F-STG-cloud-pie-browser, F-STG-stage-role | C127695~C127741 |
| Open From ProtoPie Cloud 기능 | F-STG-cloud-pie-browser, F-STG-cloud-pie-cross | C127706~ |
| Pie List > Local/Cloud/Group/Check box | F-STG-group-1level, F-STG-pie-list-multiselect, F-STG-display-order | C127* |
| Web View Player > Group Web Player + Edit Mode 4종 레이어 | F-STG-svw-view-settings, F-STG-svw-edit-mode, F-STG-svw-layers | C127833~C128665 |
| Debug > Message / Send-Receive / Record | F-BRG-debugger-baseline, F-AUD-msg-record, F-AUD-record-ui-sequence | C127680~C127693 |
| Plugin / Blokdots / Arduino / IFTTT / Wear OS 연결 | F-PLG-plugin-mgmt, F-PLG-lifecycle-baseline, F-PLG-preset-*, F-BRG-wear-os | C127748~C127767 |
| Bottom menu / Information + [Enterprise] Custom Font | F-BRG-bottom-info, F-STG-teamfont | C127676~C127679, C127829~C127832 |
| API > /api/{pies,groups,players,...} | F-API-* (§4-10 신설) | C127768~C127811 |

**변환 절차 (QA Senior 표준)**:
1. 케이스 단위가 아니라 **F-* 단위**로 그룹화 → 중복·obsolete 제거 후 Beta 환경 차원(§9)을 곱해 케이스 수를 산정.
2. `is_converted = 0`인 케이스는 (a) Beta에서도 유효 → 신규 포맷으로 작성, (b) 레거시 PC 화면 전용 → Cloud/Bridge로 대체, (c) Beta 비대상(예: Free·Core·Enterprise 6분할 매트릭스 중 Basic plan 단종 영역) → 삭제 결정.
3. 케이스 ID는 **출처(traceability)** 컬럼에 보존한다 — 회귀 결함 발생 시 레거시 동작과 비교하기 위함.
4. Plan entitlement 영역(S280)은 **자동화 우선 후보**. UI 한도 트리거 → Upsell modal 노출은 데이터 주도 테스트(데이터: 등급 × 한도)로 회귀량 절감.

## 10. 검증 우선순위 (Risk-based)

각 카테고리의 검증 우선순위는 §4 표 아래에 명시한다. 여기서는 Beta 출시 차단을 권고할 만한 P0 항목과 P1 회귀 우선 항목을 모아둔다.

P0 (실패 시 Beta 출시 차단 권고)
- Team 간 자원 누출 (F-CLD-team-rls의 RLS 우회).
- Stage 간 자원 격리 위반 (다른 Stage의 Pie·플러그인 노출).
- 변조된 Bridge 빌드가 부팅됨 (F-BRG-build-protect 우회).
- 무서명 자동 업데이트 허용 (F-BRG-auto-update 우회).
- 분실 Device 토큰 revoke 지연 (S8).
- License-only 모드에서 Cloud 자원 접근 (Capability Matrix 위반).
- URL Team ID로 다른 Team 자원 접근 (F-HOM-url-teamid 인가 우회).
- Cookie/JWT 위변조 또는 만료 토큰으로 진입 (F-IDM-cookie-jwt).
- Public Pie 정책 우회로 Private Pie 노출 (F-HOM-public-pie-only).
- 장시간(2~3일) 실행 시 메모리 누수·디스크 폭주로 서비스 중단 (F-CLD-long-run).

P1 (레거시 동등 보장)
- 하드웨어 통합: Arduino, G29, MIDI, Gamepad, blokdots, Unity, Custom Bridge App(.zip).
- 플러그인: API, IFTTT, **Unity (Stage view 양방향)**, Custom.
- 플러그인 동시 실행/시간 제한 매트릭스(F-PLG-tier-limits, §3-2).
- Studio 연동: STU-1(SocketIO 양방향), STU-2(.pie 업로드).
- Stageview: 기본 미러링, QR 진입, 다중 시청, **MultiView URL 파라미터**(fullscreen/bg/hotspotHints/cursorHide/scaleToFit).
- Stage View 커스텀 레이어 3종: Web Embed, Live Camera, Unity (플랜별 한도).
- 모바일/웹 Player 연결: QR(iOS·Android·**iPadOS**)·IP(9981)·USB·Wear OS(두 번 탭, Apple Watch 미지원).
- 웹 원격 접속: `http://[IP]:9981` + PIN code 입력.
- 음성 프로토타이핑(Voice Command/Speak/Listen): Chrome·Edge(Chromium) 최적화.
- Embedded Connect: 터미널 부팅·라이센스 키 검증·헤드리스 호스트 동작 (Enterprise 한정).
- 라이센스 키 단독 로그인: 5분 무료 만료 정책 폐기 확인.
- Home 화면 일관성: Cloud 모드 vs Desktop 첫 실행 화면 동일 레이아웃.
- Pie 교체 시 **pieId 유지** → 메시지 연결 보존 (F-STG-pie-replace).
- **Cloud Pie 수동 리로드**, Local Pie만 자동 동기화 (F-STG-studio-autosync).
- **메시지 디버거 5컬럼**(Time·Message·Value·Pie·Source) + Clear 동작 (F-BRG-debugger-baseline).
- **메시지 Recording & Playback (CSV)** — Enterprise 전용, 데모 자동화 핵심 (F-AUD-msg-record, F-AUD-msg-playback).
- **커스텀 폰트 = Enterprise 전용** 명시 (F-STG-teamfont).
- **G29 메시지 12종** 회귀 — 자동차 산업 데모 영향 (F-PLG-preset-g29).
- **Custom Bridge App boilerplate 호환성** — 외부 사용자가 만든 기존 Node.js 앱이 Beta에서 동작하는지 (마이그레이션).
- **Multi-view broadcast 모델** — 모든 Pie가 모든 메시지 수신하는 라우팅 (F-STG-svw-broadcast-model).
- **공통 Upsell Modal 3 버튼 URL·카피** 일관성 — Plan 한도 모든 트리거 지점에서 (F-IDM-upsell-modal, S280 21개 지점).
- **Stage View Edit Mode 4종 레이어 속성 패널**(Position·Size·Lock·Original·Fit/Fill·Insert) — F-STG-svw-edit-mode.
- **외부 디바이스 플러그인 라이프사이클 4단계**(연결·Run·Stop·Send/Receive) — Arduino·Blokdots·IFTTT·Wear OS 4종 (F-PLG-lifecycle-baseline).
- **REST API 엔드포인트 인증·권한 응답 일관성** — `/api/pies` `/api/groups` `/api/players` (F-API-*, P0 후보).
- **모든 Pie는 Group 종속 강제** (F-STG-pie-in-group, rev6 정책 변경) — UI New 비활성 동작, group_id 누락 API 거부, root↔Group 이동 케이스 거부 전환.
- **Stage Role 자동 부여 룰** (F-STG-stage-role, rev10 ACL 정합) — Cloud Edit Role ≥ Editor 유저가 같은 Team의 모든 Stage에서 editor로 자동 부여되는지, 강등 시 즉시 박탈되는지. "Stage editor 멤버 추가 UI"가 부재한지 negative test.
- **Cloud Stage 생성 Desktop 가능** (F-STG-cloud-vs-local, rev10 ACL 정정) — Desktop Cloud-login 모드에서 Cloud Stage 생성 진입점 노출 + cross-mode 동기화 회귀.

WIP watch (결정 시점에 즉시 케이스화)
- F-IDM-team-switch-ux, F-IDM-plan-feature-matrix, F-STG-external-guest, F-STG-pie-move, F-PLG-perm-enforce, F-PLG-disp-multi-route.
- F-REL-envelope (우선 처리 권고), F-REL-flood-prevention, F-REL-hw-conflict, F-VWR-auth-policy.
- F-VWR-nodeview-access (Player 내 Editor 접근 차단 여부 TBD), F-VWR-editor-notify (Interaction mode ON 시 Editor 알림), F-VWR-link-expiry (공유 링크 만료 정책), F-VWR-interaction-isolation (다수 Viewer 동시 인터랙션 상태 격리).
- F-BRG-17 (HTML import 보안 정책).
- F-HOM-start-button.
- F-CLD-enterprise-cost.
- 클라우드 파이 편집 처리, 커스텀 폰트 로컬 다운로드 누락.
- ~~충돌 5건~~ 모두 2026-05-22 (rev3) Paige 결정 완료: (1) Custom Plugin Import = Enterprise 한정 / (2) Connect 없이 직접 통신 = 유지 / (3) SDK = 비공개, 패키징 절차만 노출 / (4) Arduino `\|\|` 구분자 = 호환 유지 / (5) Player-participant vs Stage view from Player = 별개 개념 명문화.
- **ACL WIP 추가 watch (rev10 등재 → rev11 확장)**: F-STG-nodeview(Node View 접근 규칙), F-VWR-interaction-toggle(View↔Interaction Mode 토글). ACL 미결 5건(rev11 ACL §6에서 2건→5건 증가) — (Q-1) Viewer가 Interaction Mode ON 시 Editor 알림 필요 여부(UI·실시간 상태 표시), (Q-2) 동일 Pie 다수 Participant 동시 인터랙션 충돌 처리(Engine·인스턴스 설계, E-PLG-MSG-FLOOD §6과 매핑 검토), (Q-3, rev11 신규) Viewer용 공유 링크 만료 정책(시간 제한 vs 무기한 — 보안·운영, F-REL-viewer-invite 토큰 lifecycle과 연동), (Q-4, rev11 신규) Node View URL 공유 시 Viewer 인증 여부(무인증 접근 허용 여부·PIN 게이트 — 보안, F-STG-nodeview와 연동), (Q-5, rev11 신규) Interaction Mode 토글을 Editor가 비활성화(잠금)할 수 있는가(권한 설계, F-VWR-interaction-toggle와 연동). 미결 5건 해소 시 WIP→CONFIRMED 일괄 승격. (참고: rev11 ACL §4는 Editor의 Player 내 Node View 접근 차단 여부도 TBD로 표기 — F-STG-nodeview 완화 반영.)
- **F-IDM-cross-team-pie** (2026-05-28 Paige 질문에서 식별): Cloud Pie 라이브러리 cross-team 접근 정책. 레거시는 Viewer 자격 Pie도 업로드 허용 — CoC 정책 미결, PM/Tay 컨펌 대기.
- **F-STG-backstage** (2026-05-28 디자인 산출물에서 식별): Stage 편집기 상단 탭(Edit/Preview/Backstage) 중 Backstage 영역 정의 미문서화. 디자인 단독 개념, PM/Designer 컨펌 대기.

## 11. 변경 추적 (Decision Log)

QA에 영향 큰 결정만 기록한다. 본인이 갱신한다.

| 날짜 | 결정 | 영향 영역 | 출처 |
|---|---|---|---|
| 2026-04-26 | PRD 초안 작성 | 전체 | PRD §0 |
| 2026-05-16 | PRD v0.7.0: Tenant 표 제거, Team이 root entity | F-IDM, F-STG | PRD §1-4, §6-1 |
| v0.8.0 | Room → Stage 명칭 통일. Room UI 노출 금지 | F-STG, F-REL | PRD §6-2 |
| v0.9.0 | Group(Stage 안 Pie 폴더) 신설. 1 level only | F-STG-group-1level | PRD §6-2 |
| 2026-05-21 | Home 화면: Cloud/Local 동일 레이아웃·동일 소스 코드, 데이터만 차이. URL에 Team ID 포함 | F-HOM 신설 | 회의 |
| 2026-05-21 | Public Pie만 fetch. Archive = soft delete + 별도 탭. Restore 없음 | F-HOM-public-pie-only, F-HOM-archive-tab, F-HOM-delete-no-restore | 회의 |
| 2026-05-21 | Stage 필터·검색·정렬(최근 편집·Recently Opened) 모두 scope out | Non-goals | 회의(마지막 정정 반영) |
| 2026-05-21 | 게스트 인증 PIN 방식 유지. 호스트 승인 방식은 추후 검토 | F-IDM-pin-method | 회의 |
| 2026-05-21 | 인증 = Cookie + JWT. Cloud와 동일 로직. 실패 시 Cloud 로그인 후 Connect 재리다이렉트 | F-IDM-cookie-jwt | 회의 |
| 2026-05-21 | License → Cloud 로그인 추가 시 화면 즉시 업데이트. Cloud logout 시 license 모드 복귀 | F-IDM-license-then-cloud | 회의 |
| 2026-05-21 | Desktop 앱 라이센스 키 로그인 가능. 5분 무료 정책 폐기. Embedded와 동일 키 | F-BRG-license-login | 회의 |
| 2026-05-21 | Studio 미설치 시 자동 다운로드 페이지 이동. Studio의 Connect 연결은 dependency 없음 | F-BRG-studio-autodl | 회의 |
| 2026-05-21 | Embedded Connect는 Beta scope 포함(제외 후보에서 정정). 라이센스 키 기반 headless | F-CLD-embedded-included | 회의 |
| 2026-05-21 | Enterprise 클라우드 비용 정책 WIP. B2C 현행 유지, B2B 별도 판매 검토 | F-CLD-enterprise-cost | 회의 |
| 2026-05-21 | 장시간(2~3일) 실행·수 GB 데이터 증가 시나리오 인지 | F-CLD-long-run | 회의 |
| 2026-05-21 | 실시간 Sync 보강 scope out. Kick 기능 scope out | Non-goals | 회의(마지막 정정 반영) |
| 2026-05-21 | 권한은 대부분 UT 모델을 베이스로 구현 | F-IDM-perm-ut-base | 회의 |
| 2026-05-21 (rev2) | Team Role 3종(Owner/Admin/Member)·Edit Role 3종(Moderator/Editor/Viewer)로 권한 모델 정정. 기존 Stage role(owner/editor/viewer)은 Edit Role로 통합 | F-IDM-team-role-cloud-sot, F-IDM-edit-role, F-STG-stage-role | Paige 정정 |
| 2026-05-21 (rev2) | 배포 형태를 Self-serve(B2C, `.io`, Plan gate) / Enterprise(B2B, Editor 이상) 두 갈래로 명시. **둘 다 Beta 출시**. QA 작성 순서만 Enterprise 우선 | F-CLD-dual-silo, F-IDM-connect-entitlement | Paige 정정 |
| 2026-05-21 (rev2) | 권한 3축 모델 확정: Team Role(Cloud SoT) + Edit Role(Cloud SoT, 콘텐츠 전반) + Stage Role(Connect SoT, Stage 단위). Stage Role은 owner/editor/viewer 그대로 유지 | F-IDM-edit-role, F-STG-stage-role | Paige 정정 |
| 2026-05-21 (rev2) | 로그인 진입 UI 분리(Self-serve "Log in" / Enterprise "Log in with Secure Enterprise" + 서버 주소). F-BRG-cloud-addr를 WIP → CONFIRMED로 승격. 레거시 v2.10.2 메인 화면 구성요소를 F-HOM 회귀 베이스라인으로 기록 | F-IDM-login-entrypoint, F-BRG-cloud-addr, F-HOM | Paige 이미지 제공 |
| 2026-05-22 (rev3) | "Intro to ProtoPie Connect" 강의 영상 8편 분석 → 레거시 동작 베이스라인 추가 + 충돌 5건 식별(후속 결정 라인 참조). 신규 용어 3종 추가(ProtoPi Studio Channel, Custom Plugin, Multi-view Group) | §1 용어, §3 Capability Matrix, F-STG-svw-multiview-baseline, F-STG-svw-broadcast-model, F-PLG-concurrent, F-PLG-states-external-dep, F-PLG-disp-multi-route(WIP), F-PLG-preset-{ifttt,blokdots,arduino,g29}, F-BRG-plugin-packaging, F-BRG-debugger-baseline, F-REL-channel-id, F-REL-msg-value-var, F-REL-simultaneous-receive, F-REL-msg-naming, F-REL-flood-prevention(WIP), F-VWR-player-participant, §6 에러 5종 추가 | 강의 영상 자막 8편 (Connect_Video_Change_Proposal.md 참조) |
| 2026-05-22 (rev3) | 충돌 5건 식별 후 Paige 결정: (1) **Custom Plugin Import = Enterprise 구독 한정** (레거시 동등 유지). Pro 구독은 +버튼 비노출. (2) Connect 없이 Studio ↔ Player 직접 통신 = 유지 (2개 Pie 한정, F-REL-direct-channel 신설). (3) Custom Bridge App SDK = 비공개 유지. SDK 명세 삭제, 패키징 절차(F-BRG-plugin-packaging)만 노출. (4) **Arduino `\|\|` 구분자 = 호환 유지**. Beta envelope는 내부 표현, 외부 입력은 호환 파싱. (5) **F-VWR-player-participant vs Non-goals "Stage view from Player" = 별개 개념** 명문화 | F-IDM-plan-feature-matrix(CONFIRMED), F-REL-direct-channel(신설 CONFIRMED), F-BRG-custom-bridge-sdk(삭제), F-REL-envelope(`\|\|` 호환 명시), F-VWR-player-participant, §7 Non-goals 보강, §1 용어 정리 | Paige 결정 + 강의 영상 자막 |
| 2026-05-26 (rev4) | **Legacy Connect (User Side) — Ike Sanghoon 정답 문서 반영**: ① 플랜 등급 체계 3종(Free/Core/Enterprise) 명시 + §3-2 플랜별 정량 한도 매트릭스 신설. ② 프리셋 플러그인 6종 → 7종(Unity Stage view 양방향 통신 추가). ③ Stage View 커스텀 레이어 3종(Web Embed/Live Camera/Unity) 구체 spec. ④ Pie 교체 시 pieId 유지로 메시지 연결 보존 명문화. ⑤ Studio 자동 동기화는 Local Pie 한정, Cloud Pie 수동 리로드. ⑥ Player 연결 3경로(QR-iPadOS 포함·IP 포트 9981·USB) + Wear OS(Apple Watch 미지원, 두 번 탭). ⑦ MultiView URL 파라미터(fullscreen/bg/hotspotHints/cursorHide/scaleToFit). ⑧ Web Player 음성 프로토타이핑(Chrome·Edge, 192.x.x.x 일회성 설정). ⑨ 동일 LAN 다른 기기 브라우저 원격 실행 + PIN code 입력. ⑩ Bridge App = Node.js, API JSON 응답도 메시지로 변환 가능. ⑪ 메시지 Recording (CSV) & Playback detail (반복재생·재생속도, 비-메시지 인터랙션은 재현 불가) — Enterprise 전용. ⑫ 커스텀 폰트 = Enterprise 전용 정정. ⑬ 플러그인 동시 실행/시간 제한 정량화(F-PLG-tier-limits) | §0 한눈에 보기, §1 용어(8종 신규/보강), §3-2 매트릭스(신설), F-STG-svw-layers·pie-replace·studio-autosync(신설), F-STG-teamfont(Enterprise 정정), F-PLG-preset-list(7종), F-PLG-tier-limits(신설), F-BRG-bridge-app-detail·player-connect·wear-os·multiview-url·voice-proto·remote-browser(신설), F-AUD-msg-record·msg-playback(신설), §10 P1 보강, §12 출처 | Legacy Connect (User Side) — Ike Sanghoon (정답 문서) |
| 2026-05-27 (rev8) | **F-AUD-msg-playback·F-AUD-record-ui-sequence 표현 정정** (Paige 실 UI 동작 확인). 기존 spec은 "Record 액션 5종 시퀀스(Record/Import/Play&Stop/Setting/Exit)"로 압축해 적었으나 실제 동작은: Debug 패널 우측 하단에 Record·Import·Clear 3개 독립 버튼이 있고, Import 클릭 시 별도 'Import 세팅 모드'로 화면 전환되어 모드 내부에 재생/정지/반복재생 설정/속도 설정/나가기 5 액션이 있다. Import 세팅 모드 활성 동안 Record·Clear는 비활성. Record 중 Import 동시 호출 정책은 WIP로 두고 dev 기간 중 확정. 레거시↔CoC 동작 차이가 아닌 spec 표현 결함 수정이므로 §13 Delta에는 추가하지 않음 | F-AUD-msg-playback, F-AUD-record-ui-sequence | Paige 실 동작 확인 |
| 2026-05-27 (rev7) | **§13 Legacy ↔ CoC Delta Matrix 신설**. 레거시와 CoC 동작이 갈리는 지점을 Δ-NN 행으로 관리. 초기 12건(Δ-01~Δ-12) 등록: Pie-Group 관계, Stage·Tenant 용어, 권한 3축, 듀얼 배포, Multi-view→Stage View 흡수, 인증 영속성, License 5분 폐기, Studio 의존성 제거, Plan 3등급 정량화, Custom Bridge SDK 비공개, Stageview 선택 시청. 갱신 절차(§14)에 "delta 발생 시 §13 행 추가" 단계 명시 | §13(신설), §14(갱신 절차), §11 자체 | Paige 지시 |
| 2026-05-27 (rev6) | **Pie ↔ Group 관계 정책 변경**: 이전에는 Pie가 Stage root 또는 Group 한쪽에 위치(mutex)했으나, 앞으로 모든 Pie는 반드시 Group에 종속된다. Stage root 직속 Pie 금지. 빈 Stage에서는 Group을 먼저 생성한 뒤 해당 Group을 선택한 상태에서만 Pie 추가 가능. ① F-STG-pie-mutex 폐기 → F-STG-pie-in-group 신설(CONFIRMED). ② F-STG-group-1level 요구사항·검증 포인트에 root 직속 Pie 거부 명문화. ③ F-STG-display-order의 정렬 namespace 정의에서 root는 Group 목록 정렬만 담당하도록 정정. ④ F-STG-pie-source에 "Group 선택 상태에서만 New 활성" 조건 추가. ⑤ F-STG-svw-entry의 View 버튼 진입점을 Group hover 단위로 정정. ⑥ F-API-groups-updatePie의 정상 패턴을 Group↔Group 1종으로 축소, root를 source/target으로 지정한 요청은 거부 케이스로 전환. ⑦ §10 P1에 정책 추가. 마이그레이션은 본 Beta 범위 외(Paige 확인) — 신규 schema 기준으로만 적용. | F-STG-pie-in-group(신설 CONFIRMED, F-STG-pie-mutex 대체), F-STG-group-1level, F-STG-display-order, F-STG-pie-source, F-STG-svw-entry, F-API-groups-updatePie, §1 용어(Group·Pie), §10 P1 보강 | Paige 결정 |
| 2026-06-12 (rev15) | **Design Brief 2026-06-12 갱신본 반영**. 신규/미반영 항목 3건 추가: ① F-HOM-pagination(WIP → CONFIRMED) — "View more" pagination 확정(최초 3개, 클릭당 4개 추가 로드). ② F-HOM-stage-sort(신설 CONFIRMED) — Stage 목록 최근 업데이트 순 고정 정렬(사용자 변경 불가). ③ F-HOM-default-names(신설 CONFIRMED) — Stage 기본 이름 'Untitled Stage', Group 기본 이름 'Group N'. §10 WIP watch에서 F-HOM-pagination 제거. | F-HOM-pagination(CONFIRMED 승격), F-HOM-stage-sort(신설), F-HOM-default-names(신설), §10 WIP watch, §12 출처 갱신 | Connect on Cloud (Design Brief, Tay Jung) — Notion 2026-06-12 갱신본 |
| 2026-06-09 (rev14) | **Notion ACL 직접 접근 후 신규 항목 반영** (ACL §3·§4·§6 기준). ① F-VWR-nodeview-access(신설 WIP) — Node View 접근 경로 규칙: Viewer는 URL 직접 공유만 가능, Player/Stage 내 진입 없음. Editor의 Player 내 Node View 접근 차단 여부 TBD. ② F-VWR-editor-notify(신설 WIP) — Viewer Interaction Mode ON 시 Editor 알림 여부(ACL Q1). ③ F-VWR-link-expiry(신설 WIP) — Viewer 공유 링크 만료 정책: 시간 제한 vs 무기한(ACL Q3). ④ F-STG-pie-imported-persist(신설 CONFIRMED) — Stage에 추가된 Pie는 Stage 리소스로 관리, 원본 삭제 후에도 유지(레거시 동등). ⑤ F-STG-pie-no-personal-space(신설 CONFIRMED) — Personal Space Pie 및 다른 Team Pie는 Connect에서 조회/선택 불가. ⑥ §10 WIP watch에 4건 추가(F-VWR-nodeview-access, F-VWR-editor-notify, F-VWR-link-expiry, F-VWR-interaction-isolation). ⑦ ACL 출처 Notion 직접 URL 추가 | F-VWR-nodeview-access·editor-notify·link-expiry(신설 WIP), F-STG-pie-imported-persist·pie-no-personal-space(신설 CONFIRMED), §10 WIP watch, §1 ACL 출처 | ACL Notion 직접 확인(https://app.notion.com/p/36c45184b5da803bb98cd2f62f9f595d, 2026-06-09) |
| 2026-06-09 (rev14) | **F-VWR-interaction-isolation(신설 WIP)** — 다수 Viewer 동시 Interaction Mode 시 Pie 상태 격리 모델. 각 사용자 개별 인스턴스, 상태 비공유가 기본값. Stage 구성 변경(Pie 추가/삭제)은 브로드캐스트 가능. 충돌 처리 설계 미결. 출처: User Flow Discussion 미팅 합의 | F-VWR-interaction-isolation(신설 WIP) | User Flow Discussion 미팅, 2026-06-09 |
| 2026-06-08 (rev13) | **Figma 디자인 3개 페이지 반영** (Home `446:111421`, Stage+Plugin `446:111422`). 신규/보강 항목: ① F-HOM-stage-date(신설 CONFIRMED) — Stage 카드 날짜 표시 포맷 확정(`Edited on today` / `Edited on DD Month YYYY`). ② F-HOM-stage-ctx-cloud(신설 CONFIRMED) — Cloud Stage 컨텍스트 메뉴(Duplicate/Rename/Handoff to local/Archive stage), 에디터 role 아닌 경우 메뉴 미노출. ③ F-HOM-stage-ctx-local(신설 CONFIRMED) — Local Stage 컨텍스트 메뉴(Duplicate/Rename/Delete stage), 동일 role gate. ④ F-STG-cloud-pie-browser 모달명 정정 — "Open From ProtoPie Cloud" → "Browse Team space asset" + "Pie Gallery" 2단계 모달 플로우. ⑤ F-STG-group-ctx(신설 CONFIRMED) — Groups 패널 컨텍스트 메뉴 6종(Rename/Duplicate/Refresh all/Preview/Copy link/Delete). ⑥ F-STG-layer-ctx(신설 CONFIRMED) — Layers 패널 컨텍스트 메뉴(Refresh/Copy link/Open preview/Locate in Cloud/Replace→서브메뉴/Delete) + 레이어 타입별 인라인 퀵액션. ⑦ F-STG-navbar-menu(신설 CONFIRMED) — Stage 편집기 navbar 드롭다운 항목(Cloud Web·Desktop Local·Desktop Cloud 3 variants + Edit/Preview 탭·Run·Share 버튼). ⑧ F-STG-backstage 구조 보강 — 탭이 아닌 하단 패널로 확인, IP 주소·Connect Cloud 버튼·노드 캔버스 구성 명시. | 위 모든 항목 | Figma Connect-v3 (`A9BgGUCeTzAzYg9ghokqz1`) 노드 446:111421·111422, 섹션 968:93639·93640·549:75049·554:107247·564:102822·100480·100481 |
| 2026-06-01 (rev12) | **Connect on Cloud (Design Brief) 260601 갱신본 반영**(`Notion 문서/Connect on Cloud (Design Brief) _ Notion_260601.pdf`). rev11까지 capability matrix·Stage Role·Private Stage 제외·Node View 등은 이미 반영된 상태였고, 본 갱신본에서 신규/미반영 항목만 추가: ① §1 용어 Instance 신설 — Stage/Pie preview/Player 각각 인스턴스 생성, 상태 비공유·메시지로만 인터랙션, Embed layer도 인스턴스 일부. ② F-STG-handoff 신설(CONFIRMED) — Cloud↔Local Stage 양방향 복제(Handoff to local / Upload to Cloud), local pie·Bridge App Stage는 Upload 제약. ③ F-STG-download-config 신설(CONFIRMED) — Stage 단일 파일(.stage) 저장(Save & Load Connect Configs). ④ F-STG-instance-sync 신설(WIP) — 인스턴스 간 Snapshot 동기화 검토. ⑤ F-STG-backstage 정의 보강 — Design Brief가 처음으로 Backstage 정의 제공(노드↔Connect hub 메시지 플로우 비주얼, non-modal). ⑥ F-BRG-ota-update 신설(WIP) — `.dmg` 수동 다운로드 → Studio식 자동 업데이트 검토. ⑦ Snapping·Extension layer 리스트 depth 개선 요구를 F-STG-svw-edit-mode·svw-layers 검증 포인트에 보강(WIP). ⑧ §5 시나리오 S13~S15 추가 — 원격 UX 리서치/내부 디자인 리뷰/자동차 HMI + Unity·Unreal(Unreal은 신규, 지원 범위 WIP watch). ⑨ §13 Δ-16 신설 — Cloud↔Local 핸드오프. Background의 out-of-scope 후보(Webhook·SDK·UT·Stage view from Player 등)는 기존 §7 Non-goals와 일치(고객 근거만 보강, 결정 변경 없음). 충돌 사항 없음(Design Brief는 "Status quo + 로컬→클라우드 확장"이라 기존 CoC 결정과 모순 없음) | §1 용어(Instance), F-STG-handoff·download-config·instance-sync·backstage·svw-edit-mode·svw-layers, F-BRG-ota-update·network-otp, §5 S13~S15, §13 Δ-16, §12 출처 | Connect on Cloud (Design Brief) 260601 갱신본 |
| 2026-06-01 (rev11) | **ACL 갱신본(Notion) 반영**. 새 ACL은 표지의 "WIP, 확정 아님" 문구가 제거되고 파일명도 `ACL - WIP` → `ACL`로 변경. 단 §6 미결 사항이 2건→5건으로 증가하여 QA spec은 관련 항목을 WIP 상태로 유지(2026-06-01 Paige 결정). 결정 사항: ① 신규 미결 3건 §10 watch 등재 — Q-3 Viewer 공유 링크 만료 정책(시간 제한/무기한), Q-4 Node View URL 공유 시 Viewer 인증 여부(무인증/PIN), Q-5 Editor가 Interaction Mode 토글을 비활성화(잠금)할 수 있는가. ② F-STG-nodeview TBD 완화(Paige 결정) — rev11 ACL §4가 "Editor의 Player 내 Node View 접근 차단 여부"를 미결로 표기(표 비고와 접근방법 표기 상충)함에 따라, 기존 "Editor는 Player·URL 두 경로 모두 접근 가능" 단정을 철회하고 Player 내 접근은 TBD로 표시. URL 경로는 Editor 접근 가능 유지. ③ F-VWR-interaction-toggle에 Q-5 회귀 포인트 추가. ④ §0 watch·§12 출처의 ACL 파일 경로·설명 갱신. 권한 모델·Stage Role 부여 룰·Platform 매트릭스·레거시 매핑 등 rev10 반영 내용은 새 ACL과 일치하여 변경 없음 | §0 watch(파일 경로·WIP 유지 근거), §10 watch(미결 2→5건), F-STG-nodeview(Player 접근 TBD 완화), F-VWR-interaction-toggle(Q-5 추가), §12 출처(파일 경로·설명) | ACL 갱신본 Notion(`ACL _ Notion.pdf`) + Paige 결정(2026-06-01) |
| 2026-05-28 (rev10) | **ACL - WIP (Notion) 부분 반영**. ACL 문서는 표지에 "WIP, 확정 아님" 명시 상태이므로 (a) 충돌 결정 4건 = Paige 컨펌 후 본문 반영, (b) ACL 신규 항목 = WIP 상태로 신설. 결정 사항: ① Stage Role 부여 룰 명문화 — owner = Stage 생성자 1인, editor = 같은 Team의 Cloud Edit Role ≥ Editor(Editor/Moderator) 유저 자동 부여(별도 멤버 추가 액션 없음), viewer = ViewerInvite 토큰 외부 게스트(계정 불필요). ② Cloud Stage 생성 모드 정정 — §3 L139 `Create Cloud Stage = Desktop Cloud-login`을 X→O로 정정(ACL §4 정합). ③ Private Stage Beta scope 제외 — F-STG-private-shared·F-STG-auto-personal DEFERRED. Beta Cloud Stage는 단일 공유 모델. ④ Viewer 모드 토글 모델 명문화 — 신규 용어 View Mode / Interaction Mode / Participant 추가. F-VWR-readonly 표현 정정(토글 ON 시 예외). 신규 WIP: F-STG-nodeview(Node View 접근 규칙), F-VWR-interaction-toggle(모드 토글), F-VWR-acl-mapping(레거시→CoC 명칭 매핑 CONFIRMED). §3 신규 행: `Local Pie Import`, `하드웨어 연결` 추가(ACL §4 정합, Embedded 컬럼까지 확장). §13 Δ 신규 3건: Δ-13(Cloud Stage 생성 모드), Δ-14(Private Stage 정책), Δ-15(Stageview 시청 모델 = View↔Interaction 토글). Δ-04(권한 모델) 갱신. ACL 미결 Q-1·Q-2는 §10 watch 등재 | §1 용어(Stage Role 표·신규 3종), §3 Capability Matrix(2행 정정·2행 신설), F-STG-cloud-vs-local·private-shared(DEFERRED)·auto-personal(DEFERRED)·stage-role(부여 룰), F-STG-nodeview(신설 WIP), F-VWR-readonly(표현 정정)·interaction-toggle(신설 WIP)·acl-mapping(신설 CONFIRMED), §7 Non-goals 보강, §10 WIP watch, §13 Δ-04·Δ-13~Δ-15 | ACL - WIP Notion + Paige 결정(2026-05-28) |
| 2026-05-26 (rev5) | **이전 TestCase TestRail 2 suite(S280·S503) 반영**: ① F-IDM-upsell-modal 신설 — 공통 Upsell Modal 3 버튼 URL/카피 spec. ② F-STG-svw-edit-mode 신설 — Stage View Edit Mode 4종 레이어(Pie/Web Embed/Live Camera/Unity) 공통 속성 패널(Position/Size/Lock/Original) + 타입별 추가 속성(Camera Fit/Fill, Unity Insert 등). ③ F-STG-svw-view-settings 신설 — View Mode Settings 6옵션(Fit↔Original, Show Cursor, Hotspots Hint, BG Color, Speak/Listen). ④ F-STG-pie-list-multiselect 신설 — Pie List Check box 다중 선택. ⑤ F-PLG-lifecycle-baseline 신설 — 외부 디바이스 플러그인 4단계(연결·Run·Stop·Send/Receive) 회귀 시퀀스. ⑥ F-PLG-plugin-mgmt 신설 — Plugin 패널 4 액션(Import/삭제/Run/Open in Terminal). ⑦ F-AUD-record-ui-sequence 신설 — Debug Record 5종 UI 시퀀스. ⑧ F-BRG-bottom-info 신설 — Bottom menu / Information(유저·Player·Plugin 정보 + Logout). ⑨ §4-10 F-API 신설 — Bridge↔Server REST API 11개 엔드포인트(`/api/pies` `/api/groups` `/api/players`) 카탈로그. ⑩ §9-2 신설 — TestRail S280·S503 suite 매핑 + Beta 변환 절차(QA Senior 표준). ⑪ §10 P1 5건 보강 | F-IDM-upsell-modal, F-STG-svw-edit-mode·view-settings·pie-list-multiselect, F-PLG-lifecycle-baseline·plugin-mgmt, F-AUD-record-ui-sequence, F-BRG-bottom-info, §4-10 F-API(11 ID 신설), §9-2 신설, §10 P1 보강, §12 출처 보강 | TestRail S280 (2.9.0 POR Plan, 309 cases), S503 (Master Regression, 232 cases) — `이전 TestCase/` |

## 12. 출처

본 문서의 모든 spec은 다음 원본의 발췌·구조화다. 충돌 시 원본이 우선한다.

- PRD - Draft (Notion `protopie/PRD-Draft-35745184b5da80398889cad96345e77c`, 2026-05-16).
- **Connect on Cloud (Design Brief, Tay Jung)** — Notion `protopie/Connect-on-Cloud-Design-Brief-35945184b5da80318a48ef76a9ce69ca`. 2026-06-01 갱신본 PDF: `Notion 문서/Connect on Cloud (Design Brief) _ Notion_260601.pdf`. Background(고객 요구·out-of-scope 후보 A~G), Tech Spec(용어 정의 — Stage/Instance/Editor/Participant/Backstage/Local·Cloud stage, Services, Capability matrix, Features a~j), Scenario 3종, Timeline, Discussion. rev12 갱신 근거. **2026-06-12 Notion 추가 갱신**: Stage 목록 UX 세부(정렬·로딩·기본 이름) 추가 — rev15 반영.
- 2026-05-21 Home 화면 논의 회의록.
- protopie_docs_connect.md — 레거시 ProtoPie Connect 공식 문서 15페이지.
- STRATEGY - WIP 부록 A — 글로벌 고객 요구사항 + 2026 China Customer Visit Report.
- DB_SCHEMA - Draft / DB_SCHEMA_LOCAL - Draft.
- **Figma Connect-v3** (`A9BgGUCeTzAzYg9ghokqz1`) — Home(`446:111421`) / Stage, Plugin(`446:111422`). rev13 UI spec 근거.
- ARCH §8-1 — D-항목 ADR(D2, D4, D7, D12, D-silo, D-FanOut).
- "Intro to ProtoPie Connect" 강의 영상 자막 8편 — 1-1(Studio Send/Receive), 1-2(Connect Send/Receive), 2(IFTTT), 3(Blokdots), 4(Arduino), 5(G29), 6(Custom Bridge App: Date/Time/Weather), 7(Custom Bridge App: Home Assistant + Plugin Packaging). 자막은 `/Connect 강의 영상 자막 추출/` 디렉토리에 보관.
- Connect_Video_Change_Proposal.md — 영상 자막 분석 후 도출된 변경 제안 리포트 (2026-05-22, Claude 작성).
- **Legacy Connect (User Side) _ Notion.pdf** — Ike Sanghoon 작성, 2026-05-22. 사내 Legacy Connect 최고 사용자 기준 정답 문서. 공식 문서(protopie.io/learn/docs/ko/connect) + 실 사용 경험 기반. 모호한 동작에 대한 first-call source. rev4 갱신 전반의 근거.
- **TestRail S280** — 2.9.0 POR Plan suite (309 cases). `이전 TestCase/connect_feature(2.9.0 POR Plan).csv`. Plan entitlement 매트릭스 6등급(Free/Basic-Core/Pro-Core/Pro Plus-Core/Pro Plus-Enterprise/Enterprise) × 영역 6종(Dashboard/Pie upload/Stage View/Players/Plugin/Smart Watch)의 Plan gate 회귀 시드. rev5 §9-2 매핑.
- **TestRail S503** — Master Regression suite (232 cases). `이전 TestCase/connect_regression_test_case.csv`. Pie List·Stage View(Edit Mode)·Plugin 연결·Debug(Record)·Custom Font·REST API 등 기능 회귀 전반. `is_converted` 컬럼이 변환 상태를 표시. rev5 §9-2 매핑 + §4-10 F-API의 근거.
- **ACL (Notion)** — 2026-06-01 갱신본 PDF 캡처. `Notion 문서/ACL _ Notion.pdf`. 이전(2026-05-28) 표지의 "확정 아님, 업데이트 많이 될 예정" 문구 제거됨. 단 §6 미결 사항이 2건→5건으로 증가(공유 링크 만료·Node View 인증/PIN·Editor 토글 잠금 신규)했고, §4 Node View는 Editor의 Player 내 접근 차단 여부를 TBD로 표기. 권한 모델(Editor/Viewer 2-Role), Role 정의, Interaction Mode 토글, Platform별 ACL 매트릭스, Node View 접근 규칙, 레거시 명칭 매핑(Host/Participant/Guest→CoC) 정의. rev10·rev11 갱신 근거. 미결 5건 해소 시 WIP 항목 일괄 재검토.

## 13. Legacy ↔ CoC Delta Matrix

레거시 ProtoPie Connect와 신규 CoC(Connect Cloud) 동작이 갈리는 지점을 한 표로 관리한다. **회귀 시드(S280·S503) 변환 시 이 표를 먼저 본다** — "이 케이스가 거부로 뒤집혔는지 / 그대로인지"를 한눈에 판단해 변환 누락을 막는 게 목적이다.

읽는 법: **CoC 컬럼이 정답**. 레거시 컬럼은 회귀 베이스라인. 회귀 변환 컬럼은 dev 5주 중 케이스 변환 시의 처리 방침.

| ID | 항목 | 레거시 | CoC | 영향 F-* | 회귀 변환 |
|---|---|---|---|---|---|
| Δ-01 | Pie ↔ Group 관계 | Pie는 root 또는 Group(둘 중 하나) | 모든 Pie는 Group 종속 (root 직속 금지) | F-STG-pie-in-group, F-STG-group-1level, F-STG-display-order, F-STG-pie-source, F-API-groups-updatePie | root 관련 정상 케이스는 ID 보존하고 expected를 "거부"로 뒤집기 |
| Δ-02 | Stage 명칭 | Room | Stage (UI 노출 금지) | §1 용어, F-STG-*, F-REL-* | "Room" 카피 잔존 검출 케이스 추가 |
| Δ-03 | Tenant 용어 | v0.7.0 이전 사용 | UI 노출 금지 | §1 용어 | "Tenant" 카피 잔존 검출 케이스 추가 |
| Δ-04 | 권한 모델 | Stage role 단일축 (명시적 멤버 부여) | Team Role + Edit Role + Stage Role 3축. **Stage editor는 Cloud Edit Role ≥ Editor 유저에게 자동 부여**(rev10 ACL 정합) | F-IDM-team-role-cloud-sot, F-IDM-edit-role, F-STG-stage-role | 권한 케이스에 3축 조합 매트릭스 적용. **"Stage editor 멤버 추가 UI"가 부재한지 negative test 추가**(rev10). Cloud Edit Role 승격·강등 시 모든 Stage에 즉시 반영되는 케이스 신규. |
| Δ-05 | 배포 형태 | 단일 배포 | Self-serve(`.io`, Plan gate) / Enterprise(전용 서버, Editor 이상) 듀얼 | F-CLD-dual-silo, F-IDM-connect-entitlement, F-IDM-login-entrypoint | 모든 entitlement 케이스에 배포 차원 분리 |
| Δ-06 | Multi-view Group | 별도 그룹 모델 | Stage View가 동등 이상으로 흡수 | F-STG-svw-multiview-baseline, F-STG-svw-broadcast-model | 레거시 multi-view 케이스 → Stage View 케이스로 ID 매핑 |
| Δ-07 | 인증 영속성 | 메모리 only | DB/Redis 영속 (서버 재시작 후에도 로그인 유지) | F-IDM-persisted-auth | 서버 재시작 시나리오 신규 |
| Δ-08 | License 5분 무료 | 5분 무료 후 만료 | 정책 폐기, 라이센스 키 단독 모드로 통일 | F-BRG-license-login | "5분 만료" 케이스 삭제 |
| Δ-09 | Studio 의존성 | Studio 설치 필수 | 의존성 없음, 미설치 시 자동 다운로드 페이지로 이동 | F-BRG-studio-autodl | "Studio 미설치 거부" 케이스 → "자동 다운로드" 케이스로 변환 |
| Δ-10 | Plan 정량 한도 | 비명문화 또는 등급 2종 | 3등급(Free/Core/Enterprise) × 영역별 정량 매트릭스 명문화 | §3-2, F-PLG-tier-limits, F-IDM-upsell-modal | S280 6등급 표기 → 3등급으로 재맵핑, 공통 Upsell Modal 회귀 추가 |
| Δ-11 | Custom Bridge SDK | 공식 공개 검토 이력 | **비공개**, 패키징 절차만 노출 | F-BRG-plugin-packaging | SDK 문서 케이스 삭제, 패키징 케이스 유지 |
| Δ-12 | Stageview 시청 모델 | 모든 Pie 강제 시청 | 시청자가 Pie 선택 가능 | F-VWR-selective-pie | 선택 UX 신규 케이스 추가 |
| Δ-13 | Cloud Stage 생성 모드 | 단일 진입(데스크탑 한정) | **Cloud Web과 Desktop Cloud-login 두 모드 모두에서 생성 가능**(rev10 ACL §4) | §3 Capability Matrix L139, F-STG-cloud-vs-local | 데스크탑에서 Cloud Stage 생성 진입점 노출 회귀 추가. 생성 후 Cloud Web에서 동일 Stage 확인 cross-mode 회귀. |
| Δ-14 | Private Stage 정책 | Cloud Stage = Private/Shared 구분 + 가입 시 "내 작업실" 자동 생성 | **Beta scope에서 Private/Shared 구분 제외, 자동 생성 제외**(rev10 ACL §6) | F-STG-private-shared(DEFERRED), F-STG-auto-personal(DEFERRED), F-HOM | 레거시 Private 케이스 → "거부 또는 옵션 부재"로 전환. 가입 직후 빈 상태 가이드 UX 회귀 신규. Post-Beta 재도입 시 별도 Δ 추가 예정. |
| Δ-15 | Stageview 행위자 모델 (View↔Interaction) | Host/Editor/Participant(Guest)/Viewer 4종 Role | **2-Role(Editor/Viewer) + 개인 토글(View Mode↔Interaction Mode)**. Participant = Interaction Mode ON 상태의 행위자 호칭(rev10 ACL §3·§6). Role 전환이 아니라 mode 전환. | F-VWR-readonly(표현 정정), F-VWR-interaction-toggle(WIP), F-VWR-acl-mapping, §1 용어 | "Host"·"Guest"·"Participant" 카피 잔존 검출 케이스 신규. View↔Interaction Mode 전환 토글 UI 회귀(ACL 확정 후 본격 케이스화). 다수 Participant 동시 인터랙션 충돌 처리는 §10 Q-2 watch. |
| Δ-16 | Cloud ↔ Local Stage 핸드오프 | 단일 환경(로컬 LAN), Cloud↔Local 복제 개념 부재 | **양방향 복제 제공**: Handoff to local(Cloud→Local, LAN relay 대비) + Upload to Cloud(Local→Cloud). 단 local pie 포함·Bridge App 활용 Stage는 Upload to Cloud 불가(rev12 Design Brief §2 Features h) | F-STG-handoff(신설), §3 Capability Matrix | 신규 복제 정상 케이스 + 제약 negative test(local pie·Bridge App Stage Upload 거부). 라이센스 단독 모드 차단 회귀. |

운영 규칙
- 새 충돌이 결정될 때마다 **Δ-NN 한 행을 추가**하고, §11 Decision Log rev에 "delta Δ-NN 추가"를 명시한다.
- "회귀 변환" 컬럼은 dev 5주 중 케이스 변환 작업의 체크리스트로 사용한다. 변환 완료 후 케이스 ID와 변환 결과(유지/거부/삭제/신규)를 별도 변환 로그에 기록한다.
- Paige 결정이 아직 없는 충돌은 행으로 만들지 않고 §10 WIP watch에 둔다.

## 14. 본 문서 갱신 절차

1. PRD·Design Brief·회의록·Paige 결정에서 변경 부분을 식별한다.
2. 영향받는 F-* ID 섹션을 갱신한다(CONFIRMED ↔ WIP 상태 변경 포함).
3. **레거시와 동작이 갈리면 §13 Delta Matrix에 Δ-NN 행을 추가**한다.
4. §11 Decision Log에 한 줄을 추가한다(영향 F-* + delta ID 명시).
5. frontmatter의 `last_updated`를 갱신한다.
