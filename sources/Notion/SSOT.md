# SSOT

> Notion 최종본 아카이브 · 원본: https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe
> Notion view 시점: 2026-07-02T06:26:24.251Z
> CoC 스쿼드 종료(2026-06-30) 인수인계용. 원본 마크다운(표 포함) 그대로 보존.

---

<table_of_contents color="gray"/>
---
# Overview
<tabs>
	<tab>
		Executive Summary
		## 1. What is New Connect? {color="green_bg"}
		### Connect on Cloud: Web-based Connect
		<columns>
			<column>
				**EN**
				Connect on Cloud extends the existing Connect into a web-based environment.
				Legacy Connect operated around a single PC and its local network. In the long term, Connect on Cloud aims to enable multiple users to connect and run devices, prototypes, and plugins from different locations within a single shared workspace.
			</column>
			<column>
				**KO**
				Connect on Cloud는 기존 Connect를 웹 환경으로 확장한 제품이다.
				기존 Connect는 하나의 PC와 로컬 네트워크 중심으로 동작했다. Connect on Cloud는 장기적으로 여러 사용자가 서로 다른 위치의 디바이스, 프로토타입, 플러그인을 하나의 공유 워크스페이스에서 연결하고 운영할 수 있도록 하는 것이 목표이다.
			</column>
		</columns>
		### Desktop app also gets the new UX
		<columns>
			<column>
				**EN**
				Core experience of legacy Connect focused on connecting Pie ↔ Plugins (hardware, APIs, etc). In the new UX, Stage is brought to the surface (instead of being buried in a deep navigation path) so users can visually see multiple layers and understand the message flow more intuitively.
			</column>
			<column>
				**KO**
				기존 Connect의 핵심 경험은 Pie ↔ Plugin (Hardware, API 등) 간 연결에 집중되어 있었는데, 접근 경로가 깊숙이 위치해 있던 Stage를 표면에 배치해 사용자가 여러 레이어를 시각적으로 확인하고, 메시지 흐름을 직관적으로 확인할 수 있게 한다.
			</column>
		</columns>
		### Cloud Stage and Local Stage
		<columns>
			<column>
				**EN**
				In New Connect, users can use two types of stages.
				A **Cloud Stage** is a new concept introduced in New Connect. It runs in a cloud environment, allowing multiple users on different networks to author and view the Stage. Like the User Testing Test Room, it is tied to a Team space, so it can only include Pies within the same Team space.
				A **Local Stage** connects over a local network, like legacy Connect. Unlike a Cloud Stage, it can include local Pies and is not tied to a Team space. It also has the advantage of being usable in a fully isolated offline environment via an Embedded license.
			</column>
			<column>
				**KO**
				New Connect에서는 두 종류의 Stage를 활용할 수 있다.
				**Cloud Stage**는 New Connect에서 새롭게 도입되는 개념으로, 클라우드 환경에서 작동하며, 여러 사용자가 서로 다른 네트워크에서 Stage를 저작하고 확인할 수 있다. User testing의 Test room과 같이 Team space에 종속되어 같은 Team space의 파이만 활용할 수 있다.
				**Local Stage**는 기존 Connect처럼 로컬 네트워크를 통해 연결된다. Cloud Stage와 달리 Local Pie를 추가할 수 있고, Team space에 종속되지 않는다. 또한 Embedded license를 통해 완전 격리된 오프라인 환경에서도 활용할 수 있다는 장점이 있다.
			</column>
		</columns>
		## 2. Why are we building this?: Re-discovering Connect’s value {color="green_bg"}
		<columns>
			<column>
				**EN**
				Connect is currently the strongest driver of renewals for our customers. However, the product was designed around individual use on a single computer, which limits Enterprise customers from scaling it across an organization.
				Connect on Cloud aims to address these constraints by 1) locking in existing Enterprise revenue, 2) expanding team-based usage, and in the long term 3) enabling remote collaboration, and 4) establishing a foundation for the AI strategy.
			</column>
			<column>
				**KO**
				Connect는 현재 ProtoPie 고객의 가장 높은 재계약 유인이다. 하지만 현재 제품이 개인, 하나의 컴퓨터를 사용하도록 설계되어 있어 Enterprise 고객이 조직 단위로 확장하는 데 한계가 있다.
				Connect on Cloud는 이러한 제약을 해결하여 1) 기존 Enterprise 매출 보호, 2) 팀 단위 사용 확대, 3) \[향후\] 원격 협업 지원, 4) \[향후\] AI 전략의 기반 확보를 목표로 한다.
			</column>
		</columns>
		## 3. What's Changing? {color="green_bg"}
		<columns>
			<column>
				**EN**
				**Newly introduces**
				- Cloud Relay: Integrate hardware devices from different PCs **(Cloud Stage only)**
				- Team space-scoped Stage: Access via URL, preserve team assets in the cloud **(Cloud Stage only)**
				- Remote sharing: Viewer access via link/QR without an account, same flow for internal and external use **(Cloud Stage only)**
				**UX improvements**
				- Stage: Position Pies, add custom layers on the canvas
				- Backstage: Visually inspect the message flow between added Plugins and Pies
				- Console: Real-time message timeline, filters, and test sending
			</column>
			<column>
				**KO**
				**신규 도입**
				- Cloud Relay: 서로 다른 PC의 하드웨어 장비를 하나의 Stage에 통합 **(Cloud Stage 한정)**
				- Team space에 종속된 Stage: URL을 통한 접근, 팀 자산을 클라우드에 보존 **(Cloud Stage 한정)**
				- 원격 공유: 계정 없이 링크/QR만으로 Viewer 접근 (기업 내부, 외부 동일 플로우) **(Cloud Stage 한정)**
				**공통 UX 개선**
				- Stage: 캔버스 상에서 각 파이의 위치 설정, Custom layer 추가
				- Backstage: 추가한 Plugin과 Pie의 메시지 플로우를 시각적으로 확인
				- Console: 실시간 메시지 타임라인, 필터, 테스트 전송
			</column>
		</columns>
		<table header-row="true">
		<colgroup>
		<col width="235.66666666666666">
		<col width="235.66666666666666">
		<col width="235.66666666666666">
		</colgroup>
<tr>
<td>**Dimension**</td>
<td>**Legacy Connect**</td>
<td>**Connect on Cloud**</td>
</tr>
<tr>
<td>Access scope</td>
<td>On the same network only</td>
<td>Anywhere on the internet</td>
</tr>
<tr>
<td>Collaboration unit</td>
<td>Single user (1 Host)</td>
<td>Whole team (Editor + Viewer)</td>
</tr>
<tr>
<td>External sharing</td>
<td>Requires workarounds</td>
<td>Instant link sharing</td>
</tr>
<tr>
<td>Asset persistence</td>
<td>Stored on individual PCs only (lost on team turnover)</td>
<td>Persisted in the cloud</td>
</tr>
		</table>
		## 4. Success Definition {color="green_bg"}
		<columns>
			<column>
				**EN**
				- Phase 1: Retain existing Connect customers
				- Phase 2: Expand team-based usage, improve the collaboration experience
				- Phase 3: Validate new business ideas (e.g., Connect SDK)
			</column>
			<column>
				**KO**
				- Phase 1: 기존 Connect 고객 유지
				- Phase 2: 팀 단위 사용 확대, 협업 경험 증진
				- Phase 3: 신규 사업 (Connect SDK 등) 검증
			</column>
		</columns>
	</tab>
	<tab>
		Section A - MKT / Sales / OR
		## 1. Positioning (one-liner) {color="green_bg"}
		<columns>
			<column>
				**EN**
				> Connect on Cloud lets teams **prototype, connect, and validate with real devices; together, remotely, in a shared Stage.**
			</column>
			<column>
				**KO**
				> Connect on Cloud는 **프로토타입을 팀 단위로 저작, 연결, 검증하는 협업 플랫폼**이다.
			</column>
		</columns>
		### Key Benefits
		<columns>
			<column>
				**EN**
				- Accessibility: Removes dependency on LAN and specific PCs
				- Collaboration: Integrates hardware connected to different computers
				- Shareability: URL-based sharing
				- Governance: Team asset management and permission control
			</column>
			<column>
				**KO**
				- Accessibility: LAN과 특정 PC 의존 제거
				- Collaboration: 서로 다른 컴퓨터에 연결된 하드웨어 통합
				- Shareability: URL 기반 공유
				- Governance: 팀 자산 관리 및 권한 제어
			</column>
		</columns>
		### Example Scenarios
		<columns>
			<column>
				**EN**
				1. **Gaming**
				<callout color="gray_bg">
					**Context**
					UX designer who works on console games presents a pie working with a gamepad in a review session.
				</callout>
				- Host: Designer drives the pie and configure hardware settings from a single Cloud stage.
				- Viewer: Stakeholders get a sharable link to watch the interactions and message flows by themselves.
				- Connected device: Cloud stage preview reacts to the gamepad in real-time.
				<empty-block/>
				1. **Automotive HMI**
				<callout color="gray_bg">
					**Context**
					Designer prototypes a steering-wheel infotainment interaction using a pie and a car interior model from Unity.
				</callout>
				- Host: Designer creates a Cloud stage, loads the HMI Pie, and configures the Unity embed layer + plugin.
				- Viewer: Stakeholders open the view-only link to observe and review.
				- Connected device: A steering wheel or other input hardware is connected to drive the runtime and prototype.
			</column>
			<column>
				**KO**
				1. **게이밍 디자인**
				<callout color="gray_bg">
					**Context**
					콘솔 게임을 다루는 UX 디자이너가 리뷰 세션에서 게임패드와 연동된 Pie를 시연한다.
				</callout>
				- Host: 디자이너가 하나의 Cloud Stage에서 Pie를 구동하고 하드웨어 설정을 구성한다.
				- Viewer: 이해관계자는 공유 링크로 인터랙션과 메시지 플로우를 직접 확인한다.
				- 연결 기기: Cloud Stage 프리뷰가 게임패드 입력에 실시간으로 반응한다.
				<empty-block/>
				1. **자동차 HMI**
				<callout color="gray_bg">
					**Context**
					디자이너가 Pie와 Unity 차량 인테리어 모델로 스티어링 휠 인포테인먼트 인터랙션을 프로토타이핑한다.
				</callout>
				- Host: 디자이너가 Cloud Stage를 만들고 HMI Pie를 로드한 뒤 Unity 임베드 레이어, 플러그인을 설정한다.
				- Viewer: 이해관계자는 View-only 링크로 관찰 및 리뷰한다.
				- 연결 기기: 스티어링 휠 등 입력 하드웨어가 런타임과 프로토타입을 구동한다.
			</column>
		</columns>
		### Competitive Differentiators
		<columns>
			<column>
				**EN**
				Connect Cloud’s competitive edge comes from having all three in a single product: **hardware and API integration, multi-screen prototyping, and hybrid (web + local app) deployment**. Each can be replaced by a different tool on its own, but ProtoPie Connect is the only product on the market that delivers all three at once.
				Competing tools largely fall into two categories. Web-based collaboration tools like Figma and Framer are strong at real-time collaboration and sharing, but they cannot handle hardware such as USB or MQTT. Hardware-oriented tools like TouchDesigner, Unity, or a custom Arduino setup can control hardware, but they lack or are weak in designer-friendly prototyping, team-level isolation, and cloud sharing.
			</column>
			<column>
				**KO**
				Connect Cloud의 경쟁력은 **하드웨어/API 통합, Multi-screen prototyping, 혼합형 (Web+Local app) 배포** 세 가지가 한 제품 안에 동시에 존재한다는 데서 나온다. 하나씩 떼어보면 대체할 만한 도구가 있지만, 셋을 동시에 충족하는 제품은 시장에 ProtoPie Connect뿐이다.
				경쟁 도구는 크게 두 갈래로 나뉜다. Figma, Framer 같은 웹 기반 협업 도구는 실시간 협업과 클라우드 공유는 강하지만 USB, MQTT 등 하드웨어를 다루지 못한다. TouchDesigner, Unity, 직접 구성한 Arduino 셋업 같은 하드웨어 코딩 도구는 하드웨어 제어는 되지만 디자이너가 바로 쓸 수 있는 프로토타이핑 경험이나 팀 단위 격리, 클라우드 공유가 없거나 약하다.
				<empty-block/>
			</column>
		</columns>
		<table header-row="true">
		<colgroup>
		<col width="235.66666666666666">
		<col width="235.66666666666666">
		<col width="235.66666666666666">
		</colgroup>
<tr>
<td>**Alternatives**</td>
<td>**Limitation**</td>
<td>**Connect Cloud advantage**</td>
</tr>
<tr>
<td>Figma Prototype + Web API</td>
<td>Cannot connect physical hardware; one-way interaction</td>
<td>Real-device connections via USB HID, Serial, MIDI, etc.</td>
</tr>
<tr>
<td>Figma / Framer (web collaboration tools)</td>
<td>No support for USB, Serial, MQTT, or physical hardware</td>
<td>Distributed hardware unified via Cloud Relay</td>
</tr>
<tr>
<td>TouchDesigner / Unity / Arduino</td>
<td>High barrier for designers; no team isolation or cloud sharing</td>
<td>Designer-first no-code interface + team governance</td>
</tr>
<tr>
<td>Legacy Connect + ngrok</td>
<td>Blocked by enterprise IT firewalls; unstable, security risk</td>
<td>Official cloud relay, dedicated Enterprise infrastructure</td>
</tr>
<tr>
<td>Self-built WebSocket server</td>
<td>Requires engineering resources; no ProtoPie integration</td>
<td>Native ProtoPie Studio integration, no coding required</td>
</tr>
		</table>
		## 2. Business Impact {color="green_bg"}
		### Enterprise Retention
		<columns>
			<column>
				**EN**
				- Customers using Connect show a higher renewal rate than non-users.
				- Connect on Cloud is a key retention lever for our core customers.
			</column>
			<column>
				**KO**
				- Connect 사용 고객은 미사용 고객 대비 높은 재계약률을 보인다.
				- Connect on Cloud는 핵심 고객의 유지 수단이다.
			</column>
		</columns>
		### Seat Expansion
		<columns>
			<column>
				**EN**
				- Legacy Connect is focused on individual use.
				- Connect on Cloud transitions Connect into a collaboration product used by the entire team.
			</column>
			<column>
				**KO**
				- 기존 Connect는 개인 사용 중심이다.
				- Connect on Cloud는 팀 전체가 사용하는 협업 제품으로 전환한다.
			</column>
		</columns>
		### New Revenue Foundation
		<columns>
			<column>
				**EN**
				- It will serve as the shared foundation for future new businesses such as Connect SDK, AI Connect, and Validation Workspace.
			</column>
			<column>
				**KO**
				- 향후 Connect SDK, AI Connect, Validation Workspace 등 신규 사업의 공통 기반이 된다.
			</column>
		</columns>
	</tab>
	<tab>
		Section B - CD / Sales
		## 1. BM {color="green_bg"}
		### 현재 구조
		<table header-row="true">
		<colgroup>
		<col width="176.75">
		<col width="176.75">
		<col width="176.75">
		<col width="176.75">
		</colgroup>
<tr>
<td>**채널**</td>
<td>**현황 가격**</td>
<td>**판매 단위**</td>
<td>**비고**</td>
</tr>
<tr>
<td>Self-Serve</td>
<td>월 \$20 / 연 \$240</td>
<td>Team 단위 Addon</td>
<td>클라우드 포함 여부 미결</td>
</tr>
<tr>
<td>Enterprise</td>
<td>Sales 계약 (개별 협의)</td>
<td>Org 단위</td>
<td>전용 EKS 추가 \~\$8/월/고객</td>
</tr>
<tr>
<td>Embedded</td>
<td>License key 별도</td>
<td>기기 단위</td>
<td>현행 유지</td>
</tr>
		</table>
		## 2. Pricing & Packaging Considerations {color="green_bg"}
		<callout color="gray_bg">
			**Pricing Consideration (Future)**
			Cloud 환경에서는 고객 가치가 클라우드 세션, 디바이스 연결, 원격 협업 등 실제 사용 패턴과 연관될 가능성이 있습니다.
			다만 현재 단계에서 Usage 기반 과금 전환을 검토하는 것은 아니며, 기존 Seat 기반 모델을 유지하는 것을 전제로 합니다.
			향후 Pricing 옵션을 열어두기 위해 Cloud 사용량 관련 지표를 수집하고, 실제 고객 가치 및 비용 구조와의 상관관계를 확인할 필요가 있습니다.
		</callout>
		### 인프라 비용 구조
		현재 Enterprise 고객사 약 250사 기준, Connect on Cloud 전면 적용 시 월 추가 인프라 비용 약 \$2,000/월 발생 (고객당 \$8/월). 사용량 증가, 서버 증설, 네트워크 트래픽에 따라 변동 가능 (UT와 동일한 인프라 구조 채택 시).
		Enterprise 과금 설계 시 전용 인프라 비용(\$8/월)과 운영 오버헤드를 ACV에 반영해야 함.
		온프레미스 고객의 경우, 인프라 비용을 고객이 담당하지만, License 관리 기능 추가 필요.
		<table header-row="true">
		<colgroup>
		<col width="235.66666666666666">
		<col width="235.66666666666666">
		<col width="235.66666666666666">
		</colgroup>
<tr>
<td>**환경**</td>
<td>**배포 형태**</td>
<td>**비용 구조**</td>
</tr>
<tr>
<td>일반 (Self-Serve)</td>
<td>AWS ECS (공유 멀티테넌트)</td>
<td>공유 구조로 규모의 경제. 고객당 단가 낮음</td>
</tr>
<tr>
<td>Enterprise</td>
<td>EKS + PostgreSQL (전용 격리)</td>
<td>**고객당 \~\$8/월 추가 인프라 비용 발생**</td>
</tr>
		</table>
		#### Monetization options {toggle="true"}
			<synced_block url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#37a45184b5da8062b4ddd47145a4652d">
				<table>
				<colgroup>
				<col width="353.5">
				<col width="353.5">
				</colgroup>
<tr>
<td>**\[Option A: Add-on 별도 과금\]**<br>  • 기존 Connect 가격 유지<br>  • Cloud 기능 별도 과금<br><br>**장점 (유연한 수익화)**<br>**  •** 수익화 유연성 높음 - 클라우드 사용 고객만 비용 전가 가능<br>  • 기존 고객 반발 최소화<br>  • 시장 확대 가능(self-serve부터 enterprise까지 폭넓게)<br>  • 향후 Usage 기반 과금으로 확장 용이 (Storage, 프로젝트 수, 사용자 수 등과 연계 가능)<br><br>**단점 (가격 단순성)**<br>  • 가격 체계가 복잡해짐<br>  • 도입 장벽 상승 (추가 비용에 대한 심리적 저항)<br>  • 영업 및 운영 부담 증가<br><br>**개발 작업량**<br>  • mid</td>
<td>**\[Option B: 플랜 가격 인상\]**<br>  • Connect on Cloud를 기본 포함하여 전체 플랜 가격 인상<br>  • 기존 고객에게 전환 가격 정책(grandfathering) 제공??<br><br>**장점 (운영 단순성)**<br>  • 패키징이 가장 단순<br>  • 매출 확대 효과 즉각적<br>  • 운영 및 영업 복잡도 낮음<br><br>**단점 (기존 고객 전환)**<br>  • 기존 고객 전환 리스크<br>      ◦ 기존 고객들에게 가격 리스크 발생 ( legacy PG )<br>  • Cloud 미사용 고객의 반발 가능성<br>  • 가격 경쟁력 저하 가능성<br><br>**개발 작업량**<br>  • mid</td>
</tr>
<tr>
<td>**\[Option C: 현황유지, Beta 후 결정\]<br>**  • 일단 출시<br>  • Usage 및 운영 비용 데이터 확보 후 결정<br><br>**장점 (학습 및 검증)**<br>  • 실제 데이터를 기반으로 의사결정 가능<br>  • 출시 일정 영향 최소화<br>  • Cloud 운영 비용 구조 검증 가능<br>  • 사용자 가치 검증 가능<br>  • 여러 추가 가격 정책 논의 가능<br><br>**단점 (즉시 수익화 부족)**<br>  • 수익화 시점 지연<br>  • 향후 가격 인상 난이도 증가<br>  • 초기 가격 기준점 형성</td>
<td>**\[Option D: Enterprise 전용\]<br>  • **Enterprise 전용 기능으로 묶어서 더 높은 가격 받기 <br>  • Self-Serve는 Legacy Connect (Local 전용) 유지<br><br>**장점 (Enterprise ARPU)**<br>  • Enterprise 패키지 차별화 가능<br>  • ARPU 확대 가능<br>  • 영업 중심 판매에 유리<br><br>**단점 (시장 확장성 포기)**<br>  • 시장 확장성 제한<br>  • PLG 경로 차단<br>  • Cloud를 성장 제품으로 활용하기 어려움<br><br>개발 작업량<br>  • low</td>
</tr>
				</table>
			</synced_block>
		### Closed Beta Release
		- 마크가 전달주시는 Enterprise 리스트에 한정하여 Closed Beta 제공 (10개사 미만일 것)
		- Pricing 및 Packaging은 Closed Beta 종료 후 별도 결정
	</tab>
</tabs>
# Section C - Product Specification
## 1. Product overview {color="green_bg"}
<columns>
	<column>
		**EN**
		The legacy Connect app ties collaboration to a single machine and a local relay. Sharing a running Stage across people, devices, and locations is fragile, and there is no durable cloud home for Stages. Teams running distributed hardware demos, for example in automotive cockpits and physical AI scenarios, need a Stage that persists in the cloud, can be opened by the right people with the right permissions, and can relay messages reliably between prototypes, screens, and hardware.
		Connect v3 extends ProtoPie Connect (a device/prototype/plugin message-relay tool that legacy ran on a single PC at `localhost:9981` over LAN) into a web-based, team-scoped, cloud environment, while also reworking the desktop app’s UX around a new top-level **Stage** concept.
	</column>
	<column>
		**KO**
		기존 Connect 앱은 단일 기기와 로컬 네트워크에 묶여있다. 여러 사람, 디바이스, 위치에 걸쳐 실행 중인 Stage를 공유하기 어렵고, Stage가 지속적으로 저장될 수 있는 확실한 클라우드 공간도 없다. 예를 들어 자동차 cockpit이나 physical AI처럼 분산된 하드웨어 데모를 운영하는 팀에게는, 클라우드에 지속적으로 저장되고 적절한 사용자에게 적절한 권한으로 열릴 수 있으며, 프로토타입, 스크린, 하드웨어 간 메시지를 신뢰성 있게 중계할 수 있는 Stage가 필요하다.
		Connect v3는 기존에 단일 PC에서 `localhost:9981`로 LAN을 통해 동작하던 ProtoPie Connect(디바이스/프로토타입/플러그인 메시지 릴레이 도구)를 웹 기반의 팀 범위(Team-scoped) 클라우드 환경으로 확장하는 동시에, 데스크톱 앱 UX를 새로운 최상위 개념인 **Stage** 중심으로 재구성한다.
		<empty-block/>
	</column>
</columns>
### 1.1 Entry surfaces
The product runs in three modes.
<table header-row="true">
<colgroup>
<col>
<col>
<col width="167.3984375">
<col>
</colgroup>
<tr>
<td>Capability</td>
<td>Connect Cloud (web, CoC)</td>
<td>Desktop: Cloud login</td>
<td>Desktop: License key</td>
</tr>
<tr>
<td>Create/read/update/delete **Cloud** stage</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>Create/read/update/delete **Local** stage</td>
<td>❌</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Add pie to stage</td>
<td>**Cloud Pie → Cloud Stage only**</td>
<td>✅</td>
<td>**Local Pie → Local Stage only**</td>
</tr>
<tr>
<td>Local Pie import</td>
<td>❌</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Plugins / Bridge App / built-in plugins / Hardware</td>
<td>❌</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Remote (cross-network) connection</td>
<td>✅</td>
<td>**Cloud Stage only**</td>
<td>❌</td>
</tr>
<tr>
<td>Unity Layer</td>
<td>❌</td>
<td>**Local Stage only**</td>
<td>✅</td>
</tr>
<tr>
<td>Other custom layers</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>
<columns>
	<column>
		**EN**
		- **Connect on Cloud (CoC)** runs in the cloud; multiple users on different networks author/view a Stage. Entered via the ProtoPie Cloud side-nav (SNB), positioned under “User Testing”. A Cloud Stage is tied to a **Team space** and may include only Cloud Pies from the same Team space.
		- **Desktop authenticated via ProtoPie Cloud SSO** can CRUD both Local and Cloud stages; supports plugins/hardware/Backstage.
		- **Desktop app is offline-capable via Embedded license;** <span color="red">**cannot**</span> view/duplicate Cloud stages and <span color="red">**cannot**</span> add Cloud pies to Local stages; a Cloud login can be layered on top to temporarily gain cloud features, reverting to the license version on logout.
			- The desktop-vs-embed split is auto-detected by **license-file presence**, not a flag.
			- On the login screen, select the **Use embedded license** option, then attach and register a valid `.lic` file.
	</column>
	<column>
		**KO**
		- **Connect on Cloud (CoC)**는 클라우드에서 실행되며, 서로 다른 네트워크의 여러 사용자가 하나의 Stage를 저작/뷰할 수 있다. ProtoPie Cloud 사이드 내비게이션(SNB)에서 진입하며 “User Testing” 아래에 진입점이 위치한다. Cloud Stage는 **Team space**에 종속되며, 같은 Team space의 Cloud Pie만 포함할 수 있다.
		- **ProtoPie Cloud SSO로 인증된 Desktop 앱**은 Local/Cloud stage를 모두 생성·조회·수정·삭제(CRUD)할 수 있으며, 플러그인/하드웨어/Backstage를 지원한다.
		- **Desktop 앱은 Embedded license로 오프라인 사용이 가능**하지만, 이 경우 <span color="red">**Cloud stage를 조회/복제할 수 없고**</span> <span color="red">**Cloud pie를 Local stage에 추가할 수 없다.**</span> 다만 Cloud login을 위에 덧씌워 일시적으로 클라우드 기능을 사용할 수 있으며, 로그아웃하면 라이선스 버전으로 되돌아간다.
			- Desktop vs. Embed 분기는 플래그가 아니라 **license-file 존재 여부**로 자동 감지
			- Login 화면에서 **Use embedded license** 옵션을 선택하고, 유효한 `.lic` 파일을 첨부해 등록
	</column>
</columns>
### 1.2 Core terminologies
<columns>
	<column>
		**EN**
		<table header-row="true">
		<colgroup>
		<col>
		<col width="722">
		</colgroup>
<tr>
<td>Term</td>
<td>Definition</td>
</tr>
<tr>
<td>**Team space**</td>
<td>= Cloud’s team space. One Team can have **multiple Stages**.</td>
</tr>
<tr>
<td>**Stage**</td>
<td>Top-level workspace (“Project-level” concept, above legacy’s Group). A persistent workspace = server + Pie info + per-group data + layer placement + wiring. A Cloud Stage is bound to a Team space; a Local Stage is not.</td>
</tr>
<tr>
<td>**Group**</td>
<td>A folder segmenting a Stage’s layers. **1-level only** (no nested groups). Default name `Group N`.</td>
</tr>
<tr>
<td>**Layer**</td>
<td>An item on the canvas: Pie (cloud/local), Web embed, Camera, Unity (Local stage only).</td>
</tr>
<tr>
<td>**Pie**</td>
<td>A Pie added to a Stage. In a Cloud Stage, Cloud Pies only; in Local, local or Cloud. After adding, the Pie is a **Stage resource** that persists even if the original is removed or gone.</td>
</tr>
<tr>
<td>**Instance**</td>
<td>A running pies and stage. Pies in Stage / per-pie preview / Player **do not share a single state**. The **Run** action resets all instances. A Stage instance is created on open and preserves state across Connect↔︎Preview switching.</td>
</tr>
<tr>
<td>**Session**</td>
<td>The ephemeral runtime that a Stage runs under while any Editor remains the stage opened. ≤1 open session per Stage. Stopping sharing ends the session; the Stage (content) persists.</td>
</tr>
		</table>
	</column>
	<column>
		**KO**
		<table header-row="true">
		<colgroup>
		<col>
		<col width="722">
		</colgroup>
<tr>
<td>용어</td>
<td>정의</td>
</tr>
<tr>
<td>**Team space**</td>
<td>= Cloud의 Team space. 하나의 Team은 **여러 개의 Stage**를 포함한다.</td>
</tr>
<tr>
<td>**Stage**</td>
<td>최상위 워크스페이스(레거시의 Group보다 상위인 “Project 레벨” 개념). 지속적으로 저장되는 워크스페이스 = 서버 + Pie 정보 + 그룹별 데이터 + 레이어 배치 + 연결(wiring)을 모두 포함한 개념. Cloud Stage는 Team space에 종속되며, Local Stage는 그렇지 않다.</td>
</tr>
<tr>
<td>**Group**</td>
<td>Stage의 레이어를 구분하는 폴더. **1단계만 지원**(중첩 그룹 불가). 기본 이름은 `Group N`.</td>
</tr>
<tr>
<td>**Layer**</td>
<td>캔버스 상의 항목: Pie(Cloud/Local), Web embed, Camera, Unity(Local stage 전용).</td>
</tr>
<tr>
<td>**Pie**</td>
<td>Stage에 추가된 Pie. Cloud Stage에서는 Cloud Pie만, Local Stage에서는 Local 또는 Cloud Pie를 사용할 수 있다. 추가된 이후 Pie는 원본이 삭제되거나 사라져도 유지되는 **Stage에 종속된 리소스가** 된다.</td>
</tr>
<tr>
<td>**Instance**</td>
<td>실행 중인 Pie와 Stage. Stage 내 Pie / 개별 Pie 프리뷰 / Player는 **단일 상태를 공유하지 않는다**. **Run** 액션은 모든 인스턴스를 초기화한다. Stage 인스턴스는 Stage를 열 때 생성되며 Connect↔︎Preview 전환 시에도 상태를 유지한다.</td>
</tr>
<tr>
<td>**Session**</td>
<td>Editor가 Stage를 열어 둔 동안 Stage가 구동되는 임시 런타임. Stage당 열린 세션은 최대 1개. 공유를 중단하면 세션이 종료되며, Stage(콘텐츠)는 유지된다.</td>
</tr>
		</table>
	</column>
</columns>
<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38845184b5da8068a2d3d84e9bea8946" alt="external_object_instance"/>
## 1. Connect on Cloud {color="green_bg"}
### 1.1 Role model
<columns>
	<column>
		**EN**
		- **2 roles: Editor / Viewer**
			- Editors have access to all Cloud Stage features. However, in this release they can’t delete a stage, only archive it.
			- Archived stages aren’t editable or viewable, for both editors and viewers, until they’re restored.
			- Viewer has a personal **View / Interact** toggle.
	</column>
	<column>
		**KO**
		- **Editor / Viewer 두가지 권한이 있다.**
			- **Editor**는 Cloud Stage의 모든 기능에 접근할 수 있지만, 이번 릴리즈에선 Stage를 **삭제할 수 없고**, **아카이브만** 가능하다.
			- 아카이브된 Stage는 restore 하지 않는 한 Editor와 Viewer **모두**에게 **편집 및 조회 불가능하다.**
			- **Viewer**는 개인별로 **View / Interact** 토글을 사용해 모드간 전환할 수 있다.
	</column>
</columns>
#### Permission matrix
<table header-row="true">
<colgroup>
<col>
<col>
<col>
<col width="145">
<col>
</colgroup>
<tr>
<td>Category</td>
<td>Function</td>
<td>Editor</td>
<td>Viewer (default)</td>
<td>Viewer (Interaction ON)</td>
</tr>
<tr>
<td>Stage edit</td>
<td>Pie / Embed / Canvas edit</td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
</tr>
<tr>
<td>Preview</td>
<td>View Stage instance</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Preview</td>
<td>Pie run / interaction</td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td>Preview</td>
<td>Send message</td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td>Player</td>
<td>QR/USB connect, replace source **(does NOT show other users’ devices)**</td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
</tr>
<tr>
<td>Log/Debug</td>
<td>Console log</td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td>Log/Debug</td>
<td>Backstage</td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td>Hardware</td>
<td>all</td>
<td>❌ **(Desktop only)**</td>
<td>❌</td>
<td>❌</td>
</tr>
<tr>
<td>Share</td>
<td>Generate Viewer link / QR</td>
<td>✅ **(CoC only)**</td>
<td>❌</td>
<td>❌</td>
</tr>
</table>
#### Access entitlement
<columns>
	<column>
		**EN**
		- The Connect menu (SNB under the Team space submenu) is shown **only to Editor-or-above**.
		- Stage editing requires **same-team member AND Editor-or-above**.
		- A user not logged in reaches CoC directly (e.g. via URL) → warning/“no access” screen.
		- **Editor & Viewer use the SAME share link**; the accessing user’s role branches them into Editor vs Viewer. An Editor previewing a Viewer link is **not possible**.
	</column>
	<column>
		**KO**
		- Connect 메뉴(Cloud SNB에서 Team space 하위에 위치)는 **Editor 이상 권한을 가진 사용자에게만** 표시된다.
		- Stage가 속한 Team space 소속이면서 **Editor 이상 권한**이 있어야 Stage를 편집할 수 있다.
		- CoC에 로그인되지 않은 유저가 직접 접속할 경우 (예: URL로 접속) “no access”로 표시한다.
		- 에디터, 뷰어 링크는 같은 링크, 접속하는 유저 권한에 따라 분기, 에디터가 뷰어 링크를 미리보는 것은 **불가하다.**
	</column>
</columns>
#### Team scope
<columns>
	<column>
		**EN**
		- All Pie browse/select/connect in Cloud Stages is limited to the **currently-selected Team**; no cross-team sharing/reference; cannot browse other teams’ or Personal Space pies even with permission.
		- Stage belongs to a Team; Pie belongs to a Stage.
	</column>
	<column>
		**KO**
		- Cloud Stage에서 모든 Pie 조회/선택/연결은 **현재 선택된 Team**으로 제한된다. Team 간 공유/참조는 불가하며, 권한이 있어도 다른 Team이나 Personal Space의 Pie는 조회할 수 없다.
		- Stage는 Team에 종속되고, Pie는 Stage에 종속된다.
	</column>
</columns>
### 1.2 Closed beta scope
#### Tentative future scope (Out of scope for Closed Beta)
<columns>
	<column>
		**EN**
		- **IFTTT, blokdots Plugin**
		- Unity Plugin
		- Supporting On-Prem environment
		- Connect SDK
		- IDE for custom plugins and AI integration
		- Validation Workspace
	</column>
	<column>
		**KO**
		- **IFTTT, blokdots 플러그인**
		- Unity 플러그인
		- 온프레미스 서포트
		- Connect SDK
		- Custom plugin용 IDE, AI 통합
		- 데이터를 활용한 검증 워크스페이스
	</column>
</columns>
## 2. Connect Desktop (App) {color="green_bg"}
<callout>
	#### Worth considering in the next phase
	- Multi-tab interface like ProtoPie Studio, Figma, Notion, etc
</callout>
### 2.1 Log-in
<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38745184b5da80f2a095fdfcfc05375a" alt="external_object_instance"/>
#### i. License key
<columns>
	<column>
		**EN**
		- Authentication method using an issued license key.
		- **Works without an internet connection,** but has functional limitations:
			- **Cannot view or duplicate Cloud Stages**
			- **Cannot add Cloud Pies to Local Stages**
		- Even when signed in with a license key, the user can still proceed with Cloud login.
			- In that case, the user can access the feature set available to the Cloud-logged-in account.
			- Logging out from Cloud returns the app to the license-key version. (The existing key value is stored locally.)
	</column>
	<column>
		**KO**
		- License key를 발급받아 인증하는 방식
		- **인터넷 연결 없이도 사용 가능하**나 사용상 제약이 있다.
			- **Cloud stage 조회 및 복제 불가**
			- **Local stage에 Cloud pie 추가 불가**
		- License key로 로그인하더라도 Cloud login 진행할 수 있음
			- 이 경우 Cloud login 유저의 기능 범위를 이용 가능하다.
			- Cloud logout할 경우 license 버전으로 복귀된다. (기존 키 값은 로컬에 저장)
	</column>
</columns>
#### ii. Log-in via Cloud (SSO)
<columns>
	<column>
		**EN**
		- Login flow that opens a browser for authentication, then redirects back to the app.
		- Users can choose between General Cloud and Enterprise during login.
		- This is the same method provided in the current Connect app.
		- If the logged-in user does not belong to any Team Space that has the Connect Add-on enabled **and** where they have Editor permissions, they cannot use Connect.
	</column>
	<column>
		**KO**
		- 브라우저로 연결해서 로그인 후 앱으로 리디렉팅되는 방식
		- General cloud / Enterprise 선택하여 로그인 가능하다.
		- 현재 Connect app에서 제공하는 방식과 같다.
		- 로그인한 유저가 Connect Add-on이 추가된 + Editor 권한을 가진 Team Space가 없을 경우 커넥트 이용 불가
	</column>
</columns>
### 2.2 Settings
#### General
<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38945184b5da8099b8c3e740a1c47d7d" alt="external_object_instance"/>
<columns>
	<column>
		**EN**
		- Appearance: Defaults to the system setting.
		- Update: Provides OTA updates (Electron).
			- Auto update: When an update is available, a toast informs the user and prompts whether to download/install automatically.
			- Check for updates.
		- Network: Different from the existing Connect offering.
			- Provides explanations for network options.
			- **Removed 0.0.0.0** to address a security vulnerability.
			- **Users can manually choose the port** to use.
	</column>
	<column>
		**KO**
		- Appearance: 기본값은 시스템 세팅을 따른다.
		- Update: OTA update를 제공한다. (Electron)
			- Auto update: 업데이트 있을 때 자동으로 다운로드 및 설치 여부를 토스트로 안내
			- Check for updates
		- Network: 기존 Connect에서 제공하는 것과 차이
			- 네트워크 옵션에 대한 설명 제공
			- **0.0.0.0 제거: Security 취약점 해소를 위함**
			- **이용할 Port를 유저가 직접 선택 가능**
	</column>
</columns>
#### License
<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38a45184b5da8084adfee77d8e755868" alt="external_object_instance"/>
<columns>
	<column>
		**EN**
		- Account
			- Enterprise: Shows the currently logged-in account info, Enterprise URL, and license.
			- Basic/Pro: Shows the currently logged-in account info and license.
			- If not logged in: Shows a Log-in button and links to <mention-page url="https://app.notion.com/p/38745184b5da80b88d47c289958fb767">2.1 Log-in</mention-page>.
		- Embedded license
			- Allows using Embedded licenses (previously issued per device) by attaching them to the app.
			- See <mention-page url="https://app.notion.com/p/1c945184b5da8011b879c67e4631d0a0"/>.
			- Device ID: Required when issuing an Embedded license.
			- Use “Locate a license file” to open a .zip-format license file.
			- License status: Valid (valid license), N/A (no license file registered), Invalid (license file error or expired).
	</column>
	<column>
		**KO**
		- Account
			- Enterprise: 현재 로그인된 계정 정보, Enterprise URL, License
			- Basic/Pro: 현재 로그인된 계정 정보, License
			- 로그인되지 않았을 경우: Log-in 버튼 제공, <mention-page url="https://app.notion.com/p/38745184b5da80b88d47c289958fb767">2.1 Log-in</mention-page> 로 연결
		- Embedded license
			- 기존 디바이스별로 발급되던 Embedded license를 앱에 연결해서 사용 가능
			- <mention-page url="https://app.notion.com/p/1c945184b5da8011b879c67e4631d0a0"/> 
			- Device ID: Embedded license를 발급할 때 필요함
			- Locate a license file 버튼을 통해 .zip 형태의 라이선스 파일 열기
			- 라이선스 상태: Valid (유효한 라이선스), N/A (라이선스 파일 등록하지 않았을 경우), Invalid (라이선스 파일 오류/유효기간 지남)
	</column>
</columns>
#### Plugin
<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38a45184b5da8002af1bc1d411f7b014" alt="external_object_instance"/>
<columns>
	<column>
		**EN**
		- Shows the list of custom plugins.
			- Clicking the location path (/Users/…) copies the path to the clipboard.
			- On row hover, a Delete button appears. Deleting a plugin means **unlisting** it; the original plugin file is not deleted.
			- Plugins can be added as a folder or as a .zip file.
		- Plugins added here appear in each Stage’s Plugin panel \> Add plugin menu.
	</column>
	<column>
		**KO**
		- Custom plugin 목록을 확인할 수 있다.
			- 위치(/Users/…)를 클릭할 경우 path를 클립보드에 복사
			- 각 row 호버 시 삭제 버튼 노출, 플러그인을 삭제 → Unlist 개념, 실제 원본 플러그인은 삭제되지 않음
			- 플러그인은 folder, zip 형태로 추가 가능
		- 여기서 추가한 플러그인은 각 스테이지의 Plugin panel \> Add plugin 메뉴에 노출된다.
	</column>
</columns>
## 3. Core Features {color="green_bg"}
<callout icon="💡" color="yellow_bg">
	- **Flagged with **$`^\mathtt{arbitrary}`$<span color="gray">*:*</span> the number in the specification is defined arbitrarily and may change in later phases.
		$`^\mathtt{arbitrary}`$**로 표시된 설명**의 경우 스펙의 숫자는 임의로 정해진 값이며, 이후 단계에선 변경될 수 있습니다.
	- **Flagged with **$`^\mathtt{legacy}`$: the feature is already supported in the legacy app and has been carried over to the new Connect.
		$`^\mathtt{legacy}`$**로 표시된 설명**의 경우 해당 기능은 기존 앱에서 지원되는 기능입니다.
	- **Flagged with **$`^\mathtt{scopeout}`$: the feature is currently (as of June 30th) scoped out, but still specified.
		$`^\mathtt{scopeout}`$**로 표시된 설명**의 경우 스펙화했으나 6월 30일 릴리즈에서 스콥 아웃된 기능입니다.
</callout>
### 1. Stage
#### Stage
<callout>
	#### Worth considering in the next phase
	- `.stage` : a local copy that enables export/import in the app <mention-page url="https://app.notion.com/p/1c945184b5da80559768ee6855ce79e3"/> 
	- Handoff to local/Cloud: duplicate cloud stage as a local stage, or vice versa
	- Sorting, searching, filtering from the stage list
	- Undo-ing, Redo-ing, multi layer select from the Connect mode canvas
</callout>
<columns>
	<column>
		**EN**
		- A unit that bundles server info + Pie + group data
		- A concept one level above legacy Connect's Group (Project level)
		- A single Stage can contain multiple Groups.
		- **Layers and plugins that belong to different Stages do not share a message stream.**
		- Groups that belong to the same Stage share a message stream.
		- A Stage name can be up to 120 characters. $`^\mathtt{arbitrary}`$
		- **A Stage is auto-saved without an explicit save action, and the most recently changed value is the one stored.**
			- **Data that belongs to a Stage:**
			>
				- Layer list
				- Layer order
				- Layer properties
					- Layer name, dimensions (x/y coordinates, size)
					- Pie layers: Pie location, name, revision
					- Web embed layers: URL
					- Camera layers: Camera type, HLS URL, Run in Connect mode option
					- Unity layers: Unity wasm location
				- Plugin list
				- Plugin order
				- Plugin properties
					- Plugin name
					- REST API: Method, URL, Message from Pie, Override, Message to Pie, Header, Body
					- Arduino: Port, Baud rate
	</column>
	<column>
		**KO**
		- Server 정보 + Pie + 그룹 데이터를 묶은 단위
		- Legacy Connect의 Group 상위 개념(Project)
		- Stage 1개가 여러 Group을 포함할 수 있다.
		- **서로 다른 Stage에 속해 있는 레이어 및 플러그인은 메시지 스트림을 공유하지 않는다.**
		- 하나의 Stage에 속해 있는 Group들은 메시지 스트림을 공유한다.
		- Stage의 이름은 최대 120자이다. $`^\mathtt{arbitrary}`$
		- **Stage는 명시적인 저장 액션 없이 자동 저장되며, 가장 최후에 변경된 값이 저장된다.**
			- **Stage에 속하는 데이터들:**
			>
				- Layer list
				- Layer order
				- Layer properties
					- Layer name, dimensions (x/y coordinates, size)
					- Pie layers: Pie location, name, revision
					- Web embed layers: URL
					- Camera layers: Camera type, HLS URL, Run in Connect mode option
					- Unity layers: Unity wasm location
				- Plugin list
				- Plugin order
				- Plugin properties
					- Plugin name
					- REST API: Method, URL, Message from Pie, Override, Message to Pie, Header, Body
					- Arduino: Port, Baud rate
	</column>
</columns>
#### Instance
<callout>
	#### Worth considering in the next phase
	- Instance synchronization: For now, reaction to message is only applied after each instance is created, so state inconsistencies between instances occur frequently.
</callout>
<columns>
	<column>
		**EN**
		- Pies opened in a Stage, a Pie preview, and the Player do not share a single state.
		- An instance is created per session, and after an instance is created, only interactions between instances / within an instance are applied to each instance.
		- Instances are created when:
			- Opening a Stage (not created or reset when switching Connect ↔ Preview)
			- Opening a Stage preview (not created or reset when switching View ↔ Interaction)
		- An Editor can reset all instances connected to a stage with the Run action.
	</column>
	<column>
		**KO**
		- Stage, Pie preview, Player에서 열린 파이는 단일 상태를 공유하지 않는다.
		- 개별 세션에 인스턴스가 생성되고, 인스턴스 생성 이후에 인스턴스끼리/인스턴스 내부에서의 인터랙션만 각 인스턴스에 적용된다.
		- 인스턴스가 생성되는 경우
			- Stage를 열 때 (Connect ↔ Preview 전환 시엔 생성 또는 초기화하지 않음)
			- Stage preview를 열 때 (View ↔ Interaction 전환 시엔 생성 또는 초기화하지 않음)
		- Editor는 Run 액션으로 stage에 연결된 전체 instance를 초기화할 수 있다.
	</column>
</columns>
#### Cloud Stage
<table header-row="true" header-column="false">
<colgroup>
<col width="148.25">
<col width="151.25">
<col width="166.25">
</colgroup>
<tr>
<td>Connect on Cloud</td>
<td>Desktop (SSO)</td>
<td>Desktop (License)</td>
</tr>
<tr>
<td>✅</td>
<td>✅</td>
<td>❌</td>
</tr>
</table>
<callout>
	#### Worth considering in the next phase
	- **Permission management (Cloud only): Provide Pie-level permission management on the Stage as well.**
	- E.g.,
		- A Cloud Stage editor can set the stage to **Shared** (visible in the stage list for all members of the Team space) or **Private** (accessible only via a link).
		- In the case of a private stage, the editor can add other users who belong to the same Team space as either an editor or a guest.
	- **"A layer suddenly moved" reflects another user editing it. Awareness UI is planned later.**
	- Show the session’s status from the Stage list.
	- Sorting / Filtering in the Stage list: (Current) recently updated, session alive, alphabetical order, etc
</callout>
<columns>
	<column>
		**EN**
		**List:**
		1. **A Cloud Stage belongs under a Team space and cannot be transferred between Team spaces.**
		2. **When adding a Pie layer to a Cloud Stage, only Cloud Pies belonging to the owning Team space can be loaded.**
		3. Team space tab strip: shows only teams where the currently logged-in user is Editor-or-above.
			1. If the user has Editor permission on only one team, or is a Self-serve user, the strip is hidden and only the team name is shown.
		4. Stage list: sorted by most recently updated; loads 3 initially, then 4$`^\mathtt{arbitrary}`$ at a time.
			1. Date format: (i) for the same calendar day, time only `Edited at 02:00 PM` (ii) from the next day up to under 1 year, month, day and time `Edited at May 25, 02:00 PM` (iii) after 1 year, year, month, day and time `Edited at May 25, 2025, 02:00 PM`
			2. If the Team space has no Stages, an empty state is shown.
			3. If the Team space has one or more Stages, a New stage button is shown at the front.
		5. Archive: an archived stage cannot be viewed or edited, even by an Editor.
			1. Archived stages are shown per Team space in a separate list.
			2. An archived stage can be restored via right click \> restore in the Archived list.
			3. A restore action is also treated as an update, so it appears first in the list.
			4. If a Stage is archived while open, the user's screen shows "no access".
			<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38b45184b5da80a4b793c9f4d67906c3" alt="external_object_instance"/>
		6. Thumbnail: shows the thumbnail of the first group contained in the stage.
	</column>
	<column>
		**KO**
		**List:**
		1. **Cloud Stage는 Team space 산하에 소속되며, Team space 간 이전은 불가능하다.**
		2. **Cloud Stage에 Pie layer를 추가할 때, 소속된 Team space에 속한 Cloud Pie만 불러올 수 있다.**
		3. Team space 탭 strip: 현재 로그인한 유저가 Editor 이상인 팀만 노출한다.
			1. Editor 권한을 가진 팀이 하나이거나, Self-serve 유저의 경우 strip은 노출하지 않고 팀 이름만 노출한다.
		4. Stage 리스트: 최근 업데이트순으로 정렬, 초기 3개 후 4개$`^\mathtt{arbitrary}`$씩 로드된다.
			1. 날짜 표기는 (i) Calendar 기준 당일의 경우 시간만 표기 `Edited at 02:00 PM` (ii) 다음날\~1년 미만일 경우 월, 일과 시간 표기 `Edited at May 25, 02:00 PM` (iii) 1년 이후일 경우 연, 월, 일과 시간 표기 `Edited at May 25, 2025, 02:00 PM` 
			2. Team space에 아무 Stage도 없을 경우 empty state로 표시
			3. Team space에 Stage 하나 이상일 경우 맨 앞에 New stage 버튼 표시
		5. Archive: Archive된 stage의 경우 Editor더라도 조회 및 수정 불가하다.
			1. Archive된 stage는 Team space별로, 별도 리스트로 표시
			2. Archive된 stage를 Archived list에서 right click \>restore해 다시 원래대로 사용 가능
			3. Restore 동작도 업데이트로 보아 리스트에서 가장 먼저 표시됨
			4. Stage를 연 상태에서 아카이브할 경우, 유저 화면에서 ‘권한 없음’ 표시됨
			<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38a45184b5da804b8715e4572cdcefe4" alt="external_object_instance"/>
		6. Thumbnail: 스테이지에 포함된 첫번째 그룹의 썸네일을 표시한다.
		<empty-block/>
	</column>
</columns>
#### Local Stage
<table header-row="true" header-column="false">
<colgroup>
<col width="148.25">
<col width="151.25">
<col width="166.25">
</colgroup>
<tr>
<td>Connect on Cloud</td>
<td>Desktop (SSO)</td>
<td>Desktop (License)</td>
</tr>
<tr>
<td>❌</td>
<td>✅</td>
<td>✅</td>
</tr>
</table>
<columns>
	<column>
		**EN**
		**List:**
		1. **A Local Stage is saved on the user's computer.**
		2. **When adding a Pie layer to a Local Stage, there is no restriction on the Cloud Pie's location.**
			1. Pies in the Personal space can be used.
			2. Pies from any Team space where the user has Editor permission can be used.
		3. **Local Pies can be added to a Local Stage.**
		4. Stage list: sorted by most recently updated; loads 3 initially, then 4$`^\mathtt{arbitrary}`$ at a time.
			1. Date format: (i) for the same calendar day, time only `Edited at 02:00 PM` (ii) from the next day up to under 1 year, month, day and time `Edited at May 25, 02:00 PM` (iii) after 1 year, year, month, day and time `Edited at May 25, 2025, 02:00 PM`
			2. If the currently connected device has no Stages, an empty state is shown.
			3. If there is one or more Stages, a New stage button is shown at the front.
		5. Unlike a Cloud Stage, a Local Stage provides Delete instead of Archive.
			1. A deleted Stage cannot be restored or accessed again.
			2. If a stage is deleted while open, it returns to the home screen.
		6. Thumbnail: shows the thumbnail of the first group contained in the stage.
	</column>
	<column>
		**KO**
		**List:**
		1. **Local Stage는 유저의 컴퓨터에 저장된다.**
		2. **Local Stage에 Pie layer를 추가할 때, Cloud Pie의 위치에 제한을 받지 않는다.**
			1. Personal space에 포함된 파이 이용 가능
			2. 유저가 Editor 권한을 갖는 모든 Team space의 파이 이용 가능
		3. **Local Stage에 Local Pie를 추가할 수 있다.**
		4. Stage 리스트: 최근 업데이트순으로 정렬, 초기 3개 후 4개$`^\mathtt{arbitrary}`$씩 로드된다.
			1. 날짜 표기는 (i) Calendar 기준 당일의 경우 시간만 표기 `Edited at 02:00 PM` (ii) 다음날\~1년 미만일 경우 월, 일과 시간 표기 `Edited at May 25, 02:00 PM` (iii) 1년 이후일 경우 연, 월, 일과 시간 표기 `Edited at May 25, 2025, 02:00 PM` 
			2. 현재 접속한 기기에 아무 Stage도 없을 경우 empty state로 표시
			3. Stage 하나 이상일 경우 맨 앞에 New stage 버튼 표시
		5. Cloud Stage와 달리, Local Stage는 Archive 대신 Delete를 제공한다.
			1. Delete한 Stage는 다시 복구 또는 접근할 수 없음
			2. 스테이지를 연 상태에서 delete할 경우, 홈 화면으로 돌아감
		6. Thumbnail: 스테이지에 포함된 첫번째 그룹의 썸네일을 표시한다.
	</column>
</columns>
### 2. Workspace
#### Navigation, Canvas
<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38945184b5da80fb945fc991ecdea6a8" alt="external_object_instance"/>
<columns>
	<column>
		**EN**
		- The GNB provides menu (click the Connect symbol), mode switch, custom fonts, run, and share features.
		- The Stage name is shown as `Team Space / Stage name` (for a Cloud Stage) or `🗄️ / Stage name` (for a Local Stage).
			- Clicking the Stage name area or the local storage icon switches to the renaming state, where the stage name can be changed.
			- If the user leaves during renaming: if there is no newly entered content, only whitespace, or everything was cleared, the name is not changed; if the newly entered content is valid, the change is applied.
			- Clicking the Team space name or the 🗄️ icon goes to home.
		- The Menu items vary depending on the Stage type and whether it is CoC or App.
			<table header-row="true" header-column="true">
			<colgroup>
			<col width="159.25">
			<col width="147.25">
			<col width="151.25">
			<col width="166.25">
			</colgroup>
<tr>
<td>Menu items</td>
<td>Connect on Cloud</td>
<td>Desktop (SSO)</td>
<td>Desktop (License)</td>
</tr>
<tr>
<td>Cloud Stage, Editor</td>
<td>  • Go to home<br>  • Download desktop app<br>  • Appearance<br>  • Archive stage</td>
<td>  • Go to home<br>  • Settings<br>  • Archive stage</td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Cloud Stage, Viewer</td>
<td>  • Copy link to preview<br>  • Appearance</td>
<td><span color="gray">N/A</span></td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Local Stage</td>
<td><span color="gray">N/A</span></td>
<td>  • Go to home<br>  • Settings<br>  • Delete stage</td>
<td>  • Go to home<br>  • Settings<br>  • Delete stage</td>
</tr>
			</table>
			- Go to home: moves to the Connect home (CoC home for CoC, app home for the app)
			- Download desktop app: moves to the app download page, link TBD
			- Appearance: choose among System, Light, Dark. Default is System
			- Settings: <mention-page url="https://app.notion.com/p/38845184b5da800e9b12c32677366507">2.2 Settings</mention-page> 
			- Archive stage: <mention-page url="https://app.notion.com/p/38745184b5da8034bf18d1060c34d526">Archive: Archive된 stage의 경우 Editor더라도 조회 및 수정 불가하다.</mention-page> 
			- Delete stage: <mention-page url="https://app.notion.com/p/38345184b5da80ceb342dafdacd3b7d8">Cloud Stage와 달리, Local Stage는 Archive 대신 Delete를 제공한다.</mention-page> 
		- The Mode switch has different features depending on the user's role.
			- Editor: Connect / Preview
				- Connect: editor mode. Users can place layers on the Stage and connect plugins <mention-page url="https://app.notion.com/p/38345184b5da80c5b1a6cdb41d2c02f8"/> 
				- Preview: users can operate the Pies within the Stage. View-related options such as Hide hotspot hints and Hide UI are available <mention-page url="https://app.notion.com/p/38345184b5da80fcb1dcf6891f6e4fa9"/> 
			- Viewer, Guest: View / Interact
				- View: the user cannot operate Pies; only other users' message receives are reflected in the current instance
				- Interact: the user can operate Pies and send/receive messages
		- Custom fonts
			<table header-row="true" header-column="false">
			<colgroup>
			<col width="148.25">
			<col width="151.25">
			<col width="166.25">
			</colgroup>
<tr>
<td>Connect on Cloud</td>
<td>Desktop (SSO)</td>
<td>Desktop (License)</td>
</tr>
<tr>
<td>❌</td>
<td>✅</td>
<td>❌</td>
</tr>
			</table>
			- When logged in with a Cloud account, this downloads the Custom fonts included in that tenant so that Pies are displayed correctly
			- Fonts are not downloaded automatically; when the user Reloads, the fonts are loaded and shown after download
			- Even if a font download fails, already-downloaded fonts can still be used
		- Run: a Run action resets all instances connected to a stage, along with the previews and players connected to those instances
		- Share: <mention-page url="https://app.notion.com/p/38945184b5da80b78039c32778345141">Share</mention-page> 
	</column>
	<column>
		**KO**
		- GNB에서는 menu (Connect symbol 클릭), mode switch, custom fonts, run, share 기능을 제공한다.
		- Stage의 이름은 (Cloud Stage의 경우) `Team Space / Stage name`, (Local Stage의 경우) `🗄️ / Stage name` 으로 표시된다.
			- Stage 이름 영역 또는 로컬 스토리지 아이콘을 클릭할 경우 renaming 상태로 전환되고 stage 이름을 변경할 수 있다.
			- Renaming 도중 이탈할 경우: 새로 입력한 내용이 없거나 공백만 있을 경우, 모두 지웠을 경우에는 이름을 변경하지 않고, 새로 입력한 내용이 유효할 경우에는 변경이 반영된다.
			- Team space 이름 또는 🗄️ 아이콘을 누를 경우 홈으로 이동한다.
		- Menu item은 Stage 종류, CoC/App 여부에 따라 달라진다.
			<table header-row="true" header-column="true">
			<colgroup>
			<col width="159.25">
			<col width="147.25">
			<col width="151.25">
			<col width="166.25">
			</colgroup>
<tr>
<td>Menu items</td>
<td>Connect on Cloud</td>
<td>Desktop (SSO)</td>
<td>Desktop (License)</td>
</tr>
<tr>
<td>Cloud Stage, Editor</td>
<td>  • Go to home<br>  • Download desktop app<br>  • Appearance<br>  • Archive stage</td>
<td>  • Go to home<br>  • Settings<br>  • Archive stage</td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Cloud Stage, Viewer</td>
<td>  • Copy link to preview<br>  • Appearance</td>
<td><span color="gray">N/A</span></td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Local Stage</td>
<td><span color="gray">N/A</span></td>
<td>  • Go to home<br>  • Settings<br>  • Delete stage</td>
<td>  • Go to home<br>  • Settings<br>  • Delete stage</td>
</tr>
			</table>
			- Go to home: Connect 홈으로 이동 (CoC는 CoC 홈, 앱은 앱 홈)
			- Download desktop app: 앱 다운로드 페이지로 이동, 링크 TBD
			- Appearance: System, Light, Dark 중 선택 가능. 기본값은 System
			- Settings: <mention-page url="https://app.notion.com/p/38845184b5da800e9b12c32677366507">2.2 Settings</mention-page> 
			- Archive stage: <mention-page url="https://app.notion.com/p/38745184b5da8034bf18d1060c34d526">Archive: Archive된 stage의 경우 Editor더라도 조회 및 수정 불가하다.</mention-page> 
			- Delete stage: <mention-page url="https://app.notion.com/p/38345184b5da80ceb342dafdacd3b7d8">Cloud Stage와 달리, Local Stage는 Archive 대신 Delete를 제공한다.</mention-page> 
		- Mode switch는 유저의 role에 따라 다른 기능을 가진다.
			- Editor: Connect / Preview
				- Connect: 에디터 모드. Stage에 레이어를 배치하고 플러그인 연결할 수 있음 <mention-page url="https://app.notion.com/p/38345184b5da80c5b1a6cdb41d2c02f8"/> 
				- Preview: Stage 내의 파이를 조작할 수 있음. Hide hotspot hints, Hide UI 등 뷰 관련 옵션 활용 가능 <mention-page url="https://app.notion.com/p/38345184b5da80fcb1dcf6891f6e4fa9"/> 
			- Viewer, Guest: View / Interact
				- View: 유저는 파이를 조작하지 못하고, 다른 유저들의 메시지 receive만 현재 인스턴스에 반영됨
				- Interact: 유저가 파이 조작 및 메시지 send, receive 가능
		- Custom fonts
			<table header-row="true" header-column="false">
			<colgroup>
			<col width="148.25">
			<col width="151.25">
			<col width="166.25">
			</colgroup>
<tr>
<td>Connect on Cloud</td>
<td>Desktop (SSO)</td>
<td>Desktop (License)</td>
</tr>
<tr>
<td>❌</td>
<td>✅</td>
<td>❌</td>
</tr>
			</table>
			- Cloud 계정으로 로그인했을 경우, 해당 테넌트에 포함된 Custom font를 다운로드해 파이가 정상적으로 보이도록 하는 기능
			- 자동으로 폰트 다운로드하지 않음, 사용자가 Reload하면 폰트 불러오고, 다운로드 후 표시
			- 폰트 다운로드 실패할 경우에도 이미 다운로드된 폰트는 활용할 수 있음
		- Run: Run 동작을 한 스테이지에 연결된 모든 인스턴스, 인스턴스에 연결된 프리뷰 및 플레이어를 초기화
		- Share: <mention-page url="https://app.notion.com/p/38945184b5da80b78039c32778345141">Share</mention-page> 
	</column>
</columns>
#### Connect mode
<callout>
	#### Worth considering in the next phase
	- Snapping on the canvas
	- Show the session’s status from the Stage editor
</callout>
<table header-row="true" header-column="true">
<colgroup>
<col width="159.25">
<col width="147.25">
<col width="151.25">
<col width="166.25">
</colgroup>
<tr>
<td>**Availability matrix**</td>
<td>Connect on Cloud</td>
<td>Desktop (SSO)</td>
<td>Desktop (License)</td>
</tr>
<tr>
<td>Cloud Stage, Editor</td>
<td>✅</td>
<td>✅</td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Cloud Stage, Viewer</td>
<td>❌</td>
<td><span color="gray">N/A</span></td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Local Stage</td>
<td><span color="gray">N/A</span></td>
<td>✅</td>
<td>✅</td>
</tr>
</table>
<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38b45184b5da801391d4e9a452551025" alt="external_object_instance"/>
<table header-row="true">
<colgroup>
<col width="319.5">
<col width="319.5">
<col width="319.5">
<col width="319.5">
</colgroup>
<tr>
<td>Category</td>
<td>Editing features</td>
<td>Preview features</td>
<td>Player-related features</td>
</tr>
<tr>
<td>Pie</td>
<td>  • Add<br>  • Remove<br>  • Replace<br>  • Reload (Update)</td>
<td>  • Per-pie previews<br>  • Preview on canvas</td>
<td>  • QR<br>  • USB (Desktop app only)<br>  • Replace source</td>
</tr>
<tr>
<td>Embed</td>
<td>  • Add<br>  • Configure: Web URL, Camera, Unity (Source, Fill/Fit, Stage)<br>  • Remove</td>
<td>  • Preview on canvas</td>
<td>-</td>
</tr>
<tr>
<td>Plugin** (Desktop app)**</td>
<td>  • Default plugins<br>  • Bridge app = Custom plugins</td>
<td>  • Backstage</td>
<td>-</td>
</tr>
<tr>
<td>Canvas</td>
<td>  • Resize<br>  • Move<br>  • Zoom, Panning</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>Console</td>
<td>-</td>
<td>  • View log<br>  • Record log<br>  • Import and play<br>      ◦ Playback settings</td>
<td>-</td>
</tr>
</table>
<columns>
	<column>
		**EN**
		- Connect mode is a space where the Editor can
			- place layers on the canvas,
			- set up layer Configurations, and
			- debug via the Console and Backstage.
		- In Connect mode, cursor events cannot be triggered on a Pie.
			- However, interactions caused by messages are shown on the Pie instance within the canvas.
		- In Connect mode, a dotted grid is shown, and the view options provided in Preview are not available.
			- Hide hotspot hints: always hidden
			- Hide cursor: always hidden
			- Hide layer names: cannot be hidden
			- Hide UI: cannot be hidden
			- Background option: default only (dotted grid)
		- Layers can be freely resized and moved.
			- However, for a Pie layer the width:height ratio is fixed.
			- For other layers, fixing the width:height ratio is offered as an option.
		- A newly added layer is placed to the right of the most recently added layer without overlapping.
			- However, if the canvas is empty, it is placed at the center of the viewport.
		- Zoom option: enter a number directly or choose from the options.
			- Fit: scales so all layers on the canvas are visible. Selecting Fit moves the viewport so all layers are visible.
			- Original: the layer's actual size (=100%). **No viewport movement**
			- 25%, 50%, 200% **No viewport movement**
	</column>
	<column>
		**KO**
		- Connect mode는 Editor가
			- 캔버스에 레이어를 배치하고
			- 레이어 Configurations를 세팅하고
			- Console 및 Backstage를 통해 디버깅할 수 있는 공간이다.
		- Connect mode에서는 Pie에 커서 이벤트를 트리거할 수 없다.
			- 단, message로 인한 인터랙션은 캔버스 내 Pie instance에 노출된다.
		- Connect mode에서는 dotted grid가 노출되고, Preview에서 제공되는 view options이 제공되지 않는다.
			- Hide hotspot hints: 무조건 숨김
			- Hide cursor: 무조건 숨김
			- Hide layer names: 숨김 불가
			- Hide UI: 숨김 불가
			- Background option: 기본값만 가능 (dotted grid)
		- 레이어를 자유롭게 리사이징, 이동할 수 있다.
			- 단, Pie layer의 경우 가로:세로비가 고정된다.
			- 나머지 레이어의 경우 가로:세로비 고정을 옵션으로 둔다.
		- 새로 추가되는 레이어는 가장 최근에 추가한 레이어의 우측에 겹치지 않게 배치된다.
			- 단, 캔버스가 비어있을 경우 viewport 정중앙에 배치한다.
		- Zoom option: 숫자를 직접 입력하거나 옵션 중 선택할 수 있다.
			- Fit: 캔버스에 배치된 레이어들이 모두 보이는 배율로 조정. Fit 선택할 경우 viewport가 레이어들이 전부 보일 수 있도록 이동함
			- Original: 레이어의 실제 크기대로 (=100%). **Viewport 이동 없음**
			- 25%, 50%, 200% **Viewport 이동 없음**
	</column>
</columns>
#### Preview mode
<table header-row="true" header-column="true">
<colgroup>
<col width="159.25">
<col width="147.25">
<col width="151.25">
<col width="166.25">
</colgroup>
<tr>
<td>**Availability matrix**</td>
<td>Connect on Cloud</td>
<td>Desktop (SSO)</td>
<td>Desktop (License)</td>
</tr>
<tr>
<td>Cloud Stage, Editor</td>
<td>✅</td>
<td>✅</td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Cloud Stage, Viewer</td>
<td>❌</td>
<td><span color="gray">N/A</span></td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Local Stage</td>
<td><span color="gray">N/A</span></td>
<td>✅</td>
<td>✅</td>
</tr>
</table>
<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38b45184b5da8065b087eea0aa0f62d2" alt="external_object_instance"/>
<table header-row="true">
<colgroup>
<col width="319.5">
<col width="319.5">
<col width="319.5">
<col width="319.5">
</colgroup>
<tr>
<td>Category</td>
<td>Editing features</td>
<td>Preview features</td>
<td>Player-related features</td>
</tr>
<tr>
<td>Pie</td>
<td><span color="gray">**N/A**</span></td>
<td>  • Per-pie preview</td>
<td>  • QR<br>  • USB (Desktop app only)<br>  • Replace source</td>
</tr>
<tr>
<td>Embed</td>
<td><span color="gray">**N/A**</span></td>
<td>  • Preview on Stage instance</td>
<td>-</td>
</tr>
<tr>
<td>Plugin** (Desktop app)**</td>
<td><span color="gray">**N/A**</span></td>
<td>  • Backstage</td>
<td>-</td>
</tr>
<tr>
<td>Canvas</td>
<td><span color="gray">**N/A**</span></td>
<td>  • Preview on Stage instance</td>
<td>-</td>
</tr>
<tr>
<td>Console</td>
<td>-</td>
<td>  • View log<br>  • Record log<br>  • Import and play<br>      ◦ Playback settings</td>
<td>-</td>
</tr>
</table>
<columns>
	<column>
		**EN**
		- Preview mode is a space where the Editor can disable editing-related features and operate each Pie.
		- The left panel is shown as an accordion, and the Plugin section is hidden.
			- Only switching between Groups is possible; order and name cannot be changed
			- Layer names, properties, and order cannot be changed
			- Opening a Pie preview and connecting a Player are possible
		- In Preview mode, the dotted grid is not shown, and more extended view options than Connect mode are provided.
			- Hide hotspot hints: can hide each Pie's hotspot hints
			- Hide cursor: can hide the cursor shown on each Pie
			- Hide layer names: can hide the layer names shown on the canvas
			- Hide UI: can hide the UI including the left/right panels and GNB. Shortcut ⌘+\\
			- Background option
				- None: default light/dark color according to the theme set in Settings
				- Light: fixed to the light theme canvas color (does not affect the UI theme)
				- Dark: fixed to the dark theme canvas color (does not affect the UI theme)
				- Custom value
		- Layer resizing and moving are not possible.
		- Zoom option: enter a number directly or choose from the options.
			- Fit: scales so all layers on the canvas are visible. Selecting Fit moves the viewport so all layers are visible.
			- Original: the layer's actual size (=100%). **No viewport movement**
			- 25%, 50%, 200% **No viewport movement**
	</column>
	<column>
		**KO**
		- Preview mode는 Editor가 편집 관련 기능을 비활성화하고 각 파이를 조작할 수 있는 공간이다.
		- Left panel이 아코디언 형태로 표현되고, Plugin 섹션이 숨겨진다.
			- Group 간 전환만 할 수 있고, 순서나 이름 변경 불가
			- Layer 이름이나 property, 순서 변경 불가
			- Pie preview 열기 및 Player 연결은 가능
		- Preview mode에서는 dotted grid가 보이지 않고, Connect mode보다 확장된 view options이 제공된다.
			- Hide hotspot hints: 각 파이의 Hotspot hint를 숨길 수 있음
			- Hide cursor: 각 파이에 노출되는 커서를 숨길 수 있음
			- Hide layer names: 캔버스에 표시되는 레이어 이름을 숨길 수 있음
			- Hide UI: 좌, 우 패널, GNB를 포함한 UI를 숨길 수 있음. 단축키 ⌘+\\
			- Background option
				- None: Setting에서 설정한 theme에 따라 light, dark 기본값 색상
				- Light: light theme의 캔버스 색상으로 고정 (UI theme에는 영향을 미치지 않음)
				- Dark: dark theme의 캔버스 색상으로 고정 (UI theme에는 영향을 미치지 않음)
				- Custom value
		- 레이어 리사이징, 이동이 불가능하다.
		- Zoom option: 숫자를 직접 입력하거나 옵션 중 선택할 수 있다.
			- Fit: 캔버스에 배치된 레이어들이 모두 보이는 배율로 조정. Fit 선택할 경우 viewport가 레이어들이 전부 보일 수 있도록 이동함
			- Original: 레이어의 실제 크기대로 (=100%). **Viewport 이동 없음**
			- 25%, 50%, 200% **Viewport 이동 없음**
	</column>
</columns>
#### Viewer mode
<table header-row="true" header-column="true">
<colgroup>
<col width="159.25">
<col width="147.25">
<col width="151.25">
<col width="166.25">
</colgroup>
<tr>
<td>**Availability matrix**</td>
<td>Connect on Cloud</td>
<td>Desktop (SSO)</td>
<td>Desktop (License)</td>
</tr>
<tr>
<td>Cloud Stage, Editor</td>
<td>❌</td>
<td>❌</td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Cloud Stage, Viewer</td>
<td>✅</td>
<td><span color="gray">N/A</span></td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Local Stage</td>
<td><span color="gray">N/A</span></td>
<td>❌</td>
<td>❌</td>
</tr>
</table>
<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38b45184b5da805da967c4a8185659be" alt="external_object_instance"/>
<table header-row="true">
<colgroup>
<col width="319.5">
<col width="319.5">
<col width="319.5">
</colgroup>
<tr>
<td>Category</td>
<td>Preview features</td>
<td>Player-related features</td>
</tr>
<tr>
<td>Pie</td>
<td>  • Per-pie preview</td>
<td>-</td>
</tr>
<tr>
<td>Embed</td>
<td>  • Preview on Stage instance</td>
<td>-</td>
</tr>
<tr>
<td>Plugin** (Desktop app)**</td>
<td>  • Backstage</td>
<td>-</td>
</tr>
<tr>
<td>Canvas</td>
<td>  • Preview on Stage instance</td>
<td>-</td>
</tr>
<tr>
<td>Console</td>
<td>  • View log<br>  • Record log<br>  • Import and play<br>      ◦ Playback settings</td>
<td>-</td>
</tr>
</table>
<columns>
	<column>
		**EN**
		- Viewer mode is a space where a non-Editor user can observe interactions in a Cloud Stage.
		- Since it shares the same link as Connect mode and Preview mode, a user logged in as an Editor cannot see Viewer mode.
		- The left panel is shown as an accordion, and the Plugin section is hidden.
			- Only switching between Groups is possible; order and name cannot be changed
			- Layer names, properties, and order cannot be changed
			- Opening a Pie preview is possible
		- The view options provided in Preview mode are available.
			- Hide hotspot hints: can hide each Pie's hotspot hints
			- Hide cursor: can hide the cursor shown on each Pie
			- Hide layer names: can hide the layer names shown on the canvas
			- Hide UI: can hide the UI including the left/right panels and GNB. Shortcut ⌘+\\
			- Background option
				- None: default light/dark color according to the theme set in Settings
				- Light: fixed to the light theme canvas color (does not affect the UI theme)
				- Dark: fixed to the dark theme canvas color (does not affect the UI theme)
				- Custom value
		- Users can toggle between View / Interaction modes.
			- View: cannot perform interactions that directly trigger a Pie. Only interaction changes via Receive can be observed.
			- Interaction: all interactions including Send and Receive are possible.
	</column>
	<column>
		**KO**
		- Viewer mode는 Cloud Stage에서 Editor가 아닌 유저가 인터랙션을 확인할 수 있는 공간이다.
		- Connect mode, Preview mode와 같은 링크를 공유하므로, Editor로 로그인된 유저의 경우 Viewer mode를 확인할 수 없다.
		- Left panel이 아코디언 형태로 표현되고, Plugin 섹션이 숨겨진다.
			- Group 간 전환만 할 수 있고, 순서나 이름 변경 불가
			- Layer 이름이나 property, 순서 변경 불가
			- Pie preview 열기는 가능
		- Preview mode에서 제공되는 view options이 제공된다.
			- Hide hotspot hints: 각 파이의 Hotspot hint를 숨길 수 있음
			- Hide cursor: 각 파이에 노출되는 커서를 숨길 수 있음
			- Hide layer names: 캔버스에 표시되는 레이어 이름을 숨길 수 있음
			- Hide UI: 좌, 우 패널, GNB를 포함한 UI를 숨길 수 있음. 단축키 ⌘+\\
			- Background option
				- None: Setting에서 설정한 theme에 따라 light, dark 기본값 색상
				- Light: light theme의 캔버스 색상으로 고정 (UI theme에는 영향을 미치지 않음)
				- Dark: dark theme의 캔버스 색상으로 고정 (UI theme에는 영향을 미치지 않음)
				- Custom value
		- View / Interaction 모드를 토글로 오갈 수 있다.
			- View: 파이에 직접 trigger하는 인터랙션을 할 수 없다. Receive를 통한 인터랙션 변화만 관찰할 수 있다.
			- Interaction: Send, Receive를 포함한 모든 인터랙션이 가능하다.
	</column>
</columns>
#### Share
<callout>
	#### Worth considering in the next phase
	- Show session status from Stage, Stage list, etc
</callout>
<table header-row="true" header-column="true">
<colgroup>
<col width="159.25">
<col width="147.25">
<col width="151.25">
<col width="166.25">
</colgroup>
<tr>
<td>**Availability matrix**</td>
<td>Connect on Cloud</td>
<td>Desktop (SSO)</td>
<td>Desktop (License)</td>
</tr>
<tr>
<td>Cloud Stage, Editor</td>
<td>✅</td>
<td>✅</td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Cloud Stage, Viewer</td>
<td>✅ (via menu)</td>
<td><span color="gray">N/A</span></td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Local Stage</td>
<td><span color="gray">N/A</span></td>
<td>❌</td>
<td>❌</td>
</tr>
</table>
<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38945184b5da8057bb18c99c8b272bbd" alt="external_object_instance"/>
<columns>
	<column>
		**EN**
		- Users can copy the Stage link and individual Pie preview links.
			- For the Stage link, a different screen is shown depending on the user's role
			- An individual Pie preview link shows the same screen to all users (only the Pie, without controls)
		- View options: users can control it using `?param` appended to the URL. $`^\mathtt{legacy}`$
			>
				**pieid: **Pie ID
				- Values: `number`
				- Default Value: `(required)`
				- Example: [**http://localhost:9981/pie?pieid=1**](http://localhost:9981/pie?pieid=1)
				---
				**bg: **Background color
				- Values:
					- CSS color, e.g., `red, black, transparent`
					- HEX, e.g., `#ffffff`
					- rgb, e.g., `rgb(255,255,0)`
					- rgba, e.g., `rgba(200,100,20,0.4)`
				- Default Value: `black`
				- Example: [**http://localhost:9981/pie?pieid=1&bg=#000000**](http://localhost:9981/pie?pieid=1&bg=#000000)
				---
				**hotspotHints: **Show hotspot hints in prototype
				- Values: `true | false`
				- Default Value: `true`
				- Example: [**http://localhost:9981/pie?pieid=1&hotspotHints=true**](http://localhost:9981/pie?pieid=1&hotspotHints=true)
				---
				**cursorHide: **Hide the cursor in prototype
				- Values: `true | false`
				- Default Value: `false`
				- Example: [**http://localhost:9981/pie?pieid=1&cursorHide=true**](http://localhost:9981/pie?pieid=1&cursorHide=true)
				---
				**scaleToFit: **Scale the prototype to fit the screen
				- Values: `true | false`
				- Default Value: `true`
				- Example: [**http://localhost:9981/pie?pieid=1&scaleToFit=false**](http://localhost:9981/pie?pieid=1&scaleToFit=false)
			- When a user selects the Light / Dark option for Background color, the respective primitive values `#F8F8F8` and `#474747` are applied.
			- Clicking each Copy link to this Stage / Pie previews row copies a URL that reflects the current Preview mode view settings.
			- Clicking the Config icon button shown when hovering over each row lets users customize the view settings.
		- **Session**: A Cloud stage has a session time. When the session time has expired, only an Editor can enter the stage.
			- A Session is kept for 1 minute after all Editors leave the Stage, then expires. $`^\mathtt{arbitrary}`$
			- When an Editor reopens the Stage, the Session opens again, and Viewers can connect via the existing link.
		- **Passcode**: A user logged in with an account that does not belong to the Team space, or a user who is not logged in, can enter as a Stage viewer by entering the Passcode.
			- However, when an Editor copies the link, the link includes a token; accessing via a URL that includes the correct token lets users enter as a Stage viewer without entering the Passcode.
			- **The token does not expire (each Stage has one token). When accessing using the token, users can enter without separate authentication for 6 hours (the JWT is stored in the browser cookie and is valid for 6 hours). **$`^\mathtt{arbitrary}`$
			- If the token is invalid or not included in the URL, it moves to the Passcode input screen.
			- When copying the Passcode, it is copied to the clipboard without hyphens. However, **the Passcode is refreshed every 5 minutes, and entering with a previous Passcode is not possible.**
		- **If a user belongs to the Team space and are an Editor, the user enters directly as the Stage editor, and **accessing a stage link whose session has expired starts the session.
		- **If a user belongs to the Team space and are a Viewer, and a Session is active, the user enters as a Stage viewer without authentication such as a Passcode.**
	</column>
	<column>
		**KO**
		- 스테이지 링크 및 개별 파이 프리뷰 링크를 복사할 수 있다.
			- 스테이지 링크의 경우 유저의 role에 따라 다른 화면 표시됨
			- 개별 파이 프리뷰 링크는 모든 유저에게 같은 화면 표시됨 (컨트롤 없이 파이만 표시)
		- View options: URL 뒤에 `?param` 을 활용해서 컨트롤할 수 있다. $`^\mathtt{legacy}`$
			>
				**pieid: **Pie ID
				- Values: `number`
				- Default Value: `(required)`
				- Example: **http://localhost:9981/pie?pieid=1**
				---
				**bg: **Background color
				- Values:
					- CSS color, e.g., `red, black, transparent`
					- HEX, e.g., `#ffffff`
					- rgb, e.g., `rgb(255,255,0)`
					- rgba, e.g., `rgba(200,100,20,0.4)`
				- Default Value: `black`
				- Example: **http://localhost:9981/pie?pieid=1&bg=#000000**
				---
				**hotspotHints: **Show hotspot hints in prototype
				- Values: `true | false`
				- Default Value: `true`
				- Example: **http://localhost:9981/pie?pieid=1&hotspotHints=true**
				---
				**cursorHide: **Hide the cursor in prototype
				- Values: `true | false`
				- Default Value: `false`
				- Example: **http://localhost:9981/pie?pieid=1&cursorHide=true**
				---
				**scaleToFit: **Scale the prototype to fit the screen
				- Values: `true | false`
				- Default Value: `true`
				- Example: **http://localhost:9981/pie?pieid=1&scaleToFit=false**
			- Background color \> Light / Dark 옵션을 선택할 경우 각각의 primitive 값인 `#F8F8F8` , `#474747` 값이 적용된다.
			- Copy link to this Stage, Pie previews 각 row를 클릭하면 현재 Preview mode의 view 세팅이 반영된 URL이 복사됨
			- 각 row에 커서 호버 시 노출되는 Config 아이콘 버튼 클릭 시 view 세팅을 커스터마이징할 수 있음
		- **Session**: Cloud stage는 session time을 가진다. Session time이 만료된 경우 Editor만 스테이지에 진입할 수 있다.
			- Session은 모든 Editor가 Stage를 떠난 이후 1분간 유지, 이후 만료 $`^\mathtt{arbitrary}`$
			- Editor가 다시 Stage를 열 경우 다시 Session이 열리고, 기존 링크로 Viewer가 접속 가능
		- **Passcode**: Team space에 소속되어 있지 않은 계정으로 로그인된 유저, 로그인하지 않은 유저의 경우 Passcode 입력을 통해 Stage viewer로 입장할 수 있다.
			- 단, Editor가 링크를 복사할 때 링크에는 token이 포함되는데, 맞는 token이 포함된 URL로 접속할 경우 Passcode 입력 없이 Stage viewer로 입장
			- **Token은 만료되지 않음 (Stage당 하나의 Token을 가짐). Token을 활용해 접속할 경우 6시간 동안 별도 인증 없이 입장 가능 (JWT가 브라우저 쿠키에 저장되고, 6시간 동안 유효함) **$`^\mathtt{arbitrary}`$
			- Token이 유효하지 않거나 URL에 포함되지 않았을 경우 Passcode 입력 화면으로 넘어감
			- Passcode 복사 시 hypen 없이 클립보드에 복사. 단, **Passcode는 5분마다 갱신되며, 이전 Passcode로 입장 불가능**
		- **Team space에 소속되었으면서 Editor일 경우, Stage editor로 바로 입장하며, **Session이 만료된 스테이지 링크에 접속하면 세션이 시작됨
		- **Team space에 소속되었으면서 Viewer일 경우, Session이 활성화되어 있으면 Passcode 등 인증 없이 Stage viewer로 입장**
	</column>
</columns>
<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38945184b5da80acb3e0d747e2fc1067" alt="external_object_instance"/>
#### Group $`^\mathtt{legacy}`$
<callout>
	#### Worth considering in the next phase
	- Present groups like Figma’s Sections: **one large canvas with optional separate views**
</callout>
<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38a45184b5da80a1ab83fdfc4a1be544" alt="external_object_instance"/>
<columns>
	<column>
		**EN**
		- A Stage can contain multiple groups, and at least one group is required.
		- A newly created group is named `Group N`.
			- `N` = the order in which the group was created
		- Groups are sorted in chronological order, but manually
		- All Pies in a Group can be refreshed at once.
		- A Group's thumbnail shows the thumbnails of all layers in the group in order.
			- Including custom layers (Camera, Web embed, Unity)
		- **Groups that belong to the same Stage share a message stream.**
		- Delete group: deleted when Delete is confirmed after an alert is shown.
			- If there is only one group, the group cannot be deleted.
		- A Group name can be up to 120 characters. $`^\mathtt{arbitrary}`$
	</column>
	<column>
		**KO**
		- 한 Stage가 여러 그룹을 포함할 수 있고, 적어도 하나의 그룹이 필요하다.
		- 새로 생성된 그룹의 이름은 `Group N`이다.
			- `N` = 새로 생성된 그룹의 순서
		- 그룹은 chronical order로 정렬되나, 인위적으로 
		- Group에 포함된 모든 파이를 한번에 refresh할 수 있다.
		- Group의 thumbnail은 그룹에 포함된 모든 레이어의 썸네일을 순차대로 표시한다.
			- Custom layer (Camera, Web embed, Unity) 포함
		- **하나의 Stage에 속해 있는 Group들은 메시지 스트림을 공유한다.**
		- Delete group: 얼럿 표시 후 Delete confirm할 경우 삭제된다.
			- 그룹이 하나밖에 없을 경우, 그룹 삭제 불가능
		- Group의 이름은 최대 120자이다. $`^\mathtt{arbitrary}`$
	</column>
</columns>
#### Pie layer $`^\mathtt{legacy}`$
<callout>
	#### Worth considering in the next phase
	- Improve loading state: Loading a Pie from the dialog currently takes a long time, forcing the user to stare at a spinner with no available actions.
		- One option is to close the dialog and show the loading progress directly on the layer item.
</callout>
**Basic properties**
<columns>
	<column>
		**EN**
		- A Pie layer's size keeps its aspect ratio fixed even when resizing.
		- A layer name can be up to 120 characters. $`^\mathtt{arbitrary}`$
		- Click on the canvas → activate the bounding box to resize and move.
		- For a Pie layer that is being updated, a loading state is shown in the layer list and on the canvas.
	</column>
	<column>
		**KO**
		- Pie layer의 사이즈는 리사이징 시에도 비율이 고정된다.
		- Layer의 이름은 최대 120자이다. $`^\mathtt{arbitrary}`$
		- 캔버스에서 클릭 → Bounding box를 활성화해 리사이징 및 이동 가능하다.
		- 업데이트 중인 파이 레이어의 경우 layer list와 캔버스에 로딩 상태가 표시된다.
	</column>
</columns>
<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38b45184b5da80739c74e41f14c7f6f0" alt="external_object_instance"/>
<empty-block/>
**Preview**
<columns>
	<column>
		<table header-row="true" header-column="true">
		<colgroup>
		<col width="159.25">
		<col width="147.25">
		<col width="151.25">
		<col width="166.25">
		</colgroup>
<tr>
<td>**Availability matrix**</td>
<td>Connect on Cloud</td>
<td>Desktop (SSO)</td>
<td>Desktop (License)</td>
</tr>
<tr>
<td>Cloud Stage, Editor</td>
<td>✅</td>
<td>✅</td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Cloud Stage, Viewer</td>
<td>✅</td>
<td><span color="gray">N/A</span></td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Local Stage</td>
<td><span color="gray">N/A</span></td>
<td>✅</td>
<td>✅</td>
</tr>
		</table>
	</column>
	<column>
		**Availability: Cloud Pie layer**
		<table header-row="true" header-column="false">
		<colgroup>
		<col width="148.25">
		<col width="151.25">
		<col width="166.25">
		</colgroup>
<tr>
<td>Connect on Cloud</td>
<td>Desktop (SSO)</td>
<td>Desktop (License)</td>
</tr>
<tr>
<td>Only from the same team space</td>
<td>✅</td>
<td>❌</td>
</tr>
		</table>
	</column>
	<column>
		**Availability: Local Pie layer**
		<table header-row="true" header-column="false">
		<colgroup>
		<col width="148.25">
		<col width="151.25">
		<col width="166.25">
		</colgroup>
<tr>
<td>Connect on Cloud</td>
<td>Desktop (SSO)</td>
<td>Desktop (License)</td>
</tr>
<tr>
<td>❌</td>
<td>✅</td>
<td>✅</td>
</tr>
		</table>
	</column>
</columns>
<columns>
	<column>
		**EN**
		- Each Pie preview can be opened.
		- **Access paths:**
			- The active bounding box on the canvas → Preview icon button
			- The Preview icon button shown when hovering over each layer item
			- The Preview button shown in the Pie layer's property panel
			- The Preview button shown when hovering over a Pie previews item in the Share modal
		- For supported browsers, a preview using the [Document PIP](https://developer.chrome.com/docs/web-platform/document-picture-in-picture) feature is shown.
			- Supported browsers: Chromium-based browsers (Chrome, Edge, etc), Firefox
			- Unsupported browsers: Safari. In this case the preview opens in a new tab.
			- For the Desktop app, it opens in a new tab in the user's default browser environment.
		- For a Pie preview opened in a tab rather than Document PIP, users can control the background color, whether hotspot hints are shown, etc. using URL parameters, like a Stage preview.
		- A Pie Preview link follows the Share link policy.
	</column>
	<column>
		**KO**
		- 각 파이 프리뷰를 열 수 있다.
		- **접근 경로:**
			- 캔버스상에서 활성화된 bounding box → Preview 아이콘 버튼
			- 각 레이어 아이템에 커서 호버 시 노출되는 Preview 아이콘 버튼
			- Pie layer의 property panel에서 노출되는 Preview 버튼
			- Share modal → Pie previews 아이템에 커서 호버 시 노출되는 Preview 버튼
		- 지원되는 브라우저의 경우, [Document PIP](https://developer.chrome.com/docs/web-platform/document-picture-in-picture) 기능을 활용한 프리뷰를 노출한다.
			- 지원되는 브라우저: Chromium-based browsers (Chrome, Edge, etc), Firefox
			- 지원되지 않는 브라우저: Safari. 이 경우 새 탭에 프리뷰가 열림
			- Desktop app의 경우 유저의 default browser 환경에서 새 탭으로 열림
		- Document PIP가 아니라 탭에서 열린 Pie preview의 경우 Stage preview처럼 URL 파라미터를 활용해 배경 색상, Hotspot hints 노출 여부 등을 컨트롤할 수 있다.
		- Pie Preview 링크의 경우 Share link의 정책을 따른다.
	</column>
</columns>
**Refresh**
<table header-row="true" header-column="true">
<colgroup>
<col width="159.25">
<col width="147.25">
<col width="151.25">
<col width="166.25">
</colgroup>
<tr>
<td>**Availability matrix**</td>
<td>Connect on Cloud</td>
<td>Desktop (SSO)</td>
<td>Desktop (License)</td>
</tr>
<tr>
<td>Cloud Stage, Editor</td>
<td>✅</td>
<td>✅</td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Cloud Stage, Viewer</td>
<td>❌</td>
<td><span color="gray">N/A</span></td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Local Stage</td>
<td><span color="gray">N/A</span></td>
<td>✅</td>
<td>✅</td>
</tr>
</table>
<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38a45184b5da80a38525d03dbdac8101" alt="external_object_instance"/>
<columns>
	<column>
		**EN**
		- Loads the latest Revision of each Pie.
		- See Figma for the success and failure cases.
			- Success: a success toast is shown
			- Already the latest version: a success toast is shown
			- Failure: if it fails due to lack of access permission to the Pie, a dialog is shown; other errors are handled via toast
			- During a bulk refresh (e.g., refreshing the whole group from the group menu), if some succeed and some fail, it reports the number of succeeded/failed Pies
	</column>
	<column>
		**KO**
		- 각 파이의 최신 Revision을 불러온다.
		- 성공, 실패 케이스는 피그마 참조
			- 성공: success 토스트 표출
			- 이미 최신 버전: success 토스트 표출
			- 실패: 파이의 access 권한 없어서 실패할 경우 dialog, 나머지 오류는 토스트로 처리
			- Bulk refresh (e.g., group 메뉴에서 통째로 refresh) 중 일부 성공 일부 실패일 경우 성공/실패한 파이 개수를 알려줌
	</column>
</columns>
**Player**
<table header-row="true" header-column="true">
<colgroup>
<col width="159.25">
<col width="147.25">
<col width="151.25">
<col width="166.25">
</colgroup>
<tr>
<td>**Availability matrix**</td>
<td>Connect on Cloud</td>
<td>Desktop (SSO)</td>
<td>Desktop (License)</td>
</tr>
<tr>
<td>Cloud Stage, Editor</td>
<td>✅</td>
<td>✅</td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Cloud Stage, Viewer</td>
<td>❌</td>
<td><span color="gray">N/A</span></td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Local Stage</td>
<td><span color="gray">N/A</span></td>
<td>✅</td>
<td>✅</td>
</tr>
</table>
<callout>
	#### Worth considering in the next phase
	- Force-disconnect a connected device from the Stage
</callout>
<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38a45184b5da80c78249c7bc1b2282f5" alt="external_object_instance"/>
<columns>
	<column>
		**EN**
		- **Access paths:**
			- The Player icon button shown when hovering over each layer item → for layers with a connected Player, the icon is distinguished with a check mark
			- The Player section shown in the Pie layer's property panel: shows the number of players connected to the current Pie as a badge
		- A Player panel exists per Pie and is shown in Connect mode, Preview mode, and to Viewers.
			- 'View properties' is an option to switch to the Property panel of the layer the Player panel is currently showing
			- The 'View properties' button is not shown in Preview mode or to Viewers
		- Connected to this Pie: shows the device names of currently connected players
			- If no device is connected to the currently selected Pie, this entire section is not shown
		- Connected to others: shows the device names connected to other Pies within the same Stage
			- Pressing Replace switches the player to the currently connected Pie
			- If no device is connected to other Pies, this entire section is not shown
		- Connect new device
			- QR code: shows a QR code and app download badges.
			- USB: uses the player of a device connected via USB cable, **not available in a Cloud stage**
	</column>
	<column>
		**KO**
		- **접근 경로:**
			- 각 레이어 아이템에 커서 호버 시 노출되는 Player 아이콘 버튼 → Player가 연결된 레이어의 경우 아이콘에 체크 표시로 구별 가능
			- Pie layer의 property panel에서 노출되는 Player 섹션: 현재 파이에 연결된 플레이어 수 뱃지로 노출
		- Player panel은 파이별로 존재하고, Connect mode, Preview mode, Viewer에게 모두 노출된다.
			- ‘View properties’는 현재 Player panel이 보여주고 있는 레이어의 Property panel로 전환하는 옵션
			- Preview mode, Viewer에게는 ‘View properties’ 버튼 없음
		- Connected to this Pie: 현재 연결된 플레이어의 디바이스명 노출
			- 현재 선택된 파이에 연결된 디바이스 없을 경우 이 섹션 통째로 보여주지 않음
		- Connected to others: 같은 Stage 내 다른 파이에 연결된 디바이스명 노출
			- Replace 누를 경우 현재 연결된 파이로 플레이어 전환
			- 현재 다른 파이에 연결된 디바이스 없을 경우 이 섹션 통째로 보여주지 않음
		- Connect new device
			- QR code: QR code 및 앱 다운로드 뱃지 노출. 
			- USB: USB 케이블로 연결된 디바이스의 플레이어 활용, **Cloud stage에서 이용 불가**
	</column>
</columns>
**Replace**
<table header-row="true" header-column="true">
<colgroup>
<col width="159.25">
<col width="147.25">
<col width="151.25">
<col width="166.25">
</colgroup>
<tr>
<td>**Availability matrix**</td>
<td>Connect on Cloud</td>
<td>Desktop (SSO)</td>
<td>Desktop (License)</td>
</tr>
<tr>
<td>Cloud Stage, Editor</td>
<td>Only Cloud Pie → Cloud Pie</td>
<td>Only Cloud Pie → Cloud Pie</td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Cloud Stage, Viewer</td>
<td>❌</td>
<td><span color="gray">N/A</span></td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Local Stage</td>
<td><span color="gray">N/A</span></td>
<td>✅</td>
<td>Only Local Pie → Local Pie</td>
</tr>
</table>
<columns>
	<column>
		**EN**
		- The Pie connected to a Pie layer can be replaced.
		- When replacing a Pie
			- Layer name and Position are kept.
			- Size returns to the original size.
		- Access paths:
			- Cloud Pie layer's property panel: only replacement with another Cloud Pie is possible
			- Context menu of the Cloud Pie layer / Local Pie layer list: Cloud → Cloud, Cloud → Local, Local → Local, Local → Cloud are all possible
		- For Cloud Pie → Cloud Pie, users cannot select the same pie to replace.
	</column>
	<column>
		**KO**
		- Pie layer에 연결된 Pie를 교체할 수 있다.
		- Pie 교체 시
			- Layer name, Position은 유지된다.
			- Size는 original size로 돌아간다.
		- 접근 경로:
			- Cloud Pie layer의 property panel: 다른 Cloud Pie로의 교체만 가능
			- Cloud Pie layer, Local Pie layer list의 context menu: Cloud → Cloud, Cloud → Local, Local → Local, Local → Cloud 모두 가능
		- Cloud Pie → Cloud Pie의 경우 자기 자신을 선택해 교체할 수 없다.
	</column>
</columns>
#### Web embed layer $`^\mathtt{legacy}`$
<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38b45184b5da8026b442c7c68db311c9" alt="external_object_instance"/>
<columns>
	<column>
		**EN**
		- Embeds the Web URL entered by the user into the Stage as an iframe.
		- The iframe's viewport size matches the layer size specified on the canvas. (Not affected by the Zoom level)
		- Add layer → enter a URL in the Dialog to add the layer; afterward the URL can be changed in the property panel.
		- A Web embed layer's name follows the specified URL by default.
			- On first creation, the name is set to the URL
			- When the URL is changed, the layer name is updated to the new URL even if the user had manually renamed the layer
			- If the URL exceeds 120 characters, it is truncated at 120 characters
		- Supported URL types: [https://www.protopie.io/learn/docs/connect-custom-layer-integrations#web-embed-supported-url-types](https://www.protopie.io/learn/docs/connect-custom-layer-integrations#web-embed-supported-url-types)
	</column>
	<column>
		**KO**
		- 유저가 입력한 Web URL을 스테이지에 iframe으로 임베딩한다.
		- iframe의 viewport 크기는 캔버스에서 지정한 레이어의 크기와 일치한다. (Zoom 배율에 영향을 받지 않음)
		- Add layer → Dialog에서 URL을 입력하면 레이어가 추가되고, 이후에는 property panel에서 URL 변경이 가능하다.
		- Web embed 레이어의 이름은 기본값으로 지정한 URL을 따른다.
			- 최초 생성 시 URL으로 이름 지정
			- URL을 변경할 경우 유저가 매뉴얼로 레이어 이름 변경했더라도 새로운 URL로 레이어 이름을 적용함
			- URL이 120자를 넘을 경우 120자 선에서 자름
		- Supported URL types: [https://www.protopie.io/learn/docs/connect-custom-layer-integrations#web-embed-supported-url-types](https://www.protopie.io/learn/docs/connect-custom-layer-integrations#web-embed-supported-url-types)
	</column>
</columns>
#### Camera layer $`^\mathtt{legacy}`$
<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38b45184b5da80e7bb28cfb20b9fba9d" alt="external_object_instance"/>
<columns>
	<column>
		**EN**
		- Add a Camera layer to play the user's webcam or a stream on the Stage.
			- If a disconnected camera or an invalid URL is entered, the camera name or `Web Streaming (HLS)` is shown as text on the Stage.
		- **Self-streaming is not supported. Even if a Camera layer is added and plays on user A's Stage, the same view is not shown to user B; each of A and B watches the camera feed connected to their own device.**
		- **Layout:**
			- Fit: default; the camera image is shown in full without cropping, fitted to the layer's size ratio
			- Fill: if the layer size ratio and the camera image ratio do not match, the camera image is cropped to the center to fill the layer
		- When the Run in Connect Mode toggle is on, the camera feed also plays in Connect mode (editor); otherwise the camera name is shown as text.
	</column>
	<column>
		**KO**
		- Camera 레이어를 추가해 유저의 웹 캠 혹은 Streaming을 스테이지에서 재생할 수 있다.
			- 연결되지 않은 카메라나 유효하지 않은 URL을 입력한 경우에는 스테이지에 카메라 이름 혹은 `Web Streaming (HLS)`이 텍스트로 표시된다.
		- **자체 스트리밍을 지원하지 않는다. Camera 레이어를 추가해 A 유저의 스테이지에서 재생되더라도, 같은 화면이 B 유저에게 보이지는 않고, A, B 유저의 기기에 연결된 카메라 화면을 각각 시청한다.**
		- **Layout:**
			- Fit: 기본값, 레이어 사이즈 비율에 맞추어 카메라 화상이 잘리지 않고 전부 표시
			- Fill: 레이어 사이즈 비율과 카메라 화상 비율이 맞지 않으면 카메라 화상 가운데로 크롭해 레이어를 꽉 채우게 표시
		- Run in Connect Mode 토글을 켤 경우 Connect mode (편집기)에서도 카메라 화상이 재생되고, 그렇지 않다면 카메라 이름이 텍스트로 노출된다.
	</column>
</columns>
#### Unity layer $`^\mathtt{legacy}`$
<table header-row="true" header-column="true">
<colgroup>
<col width="159.25">
<col width="147.25">
<col width="151.25">
<col width="166.25">
</colgroup>
<tr>
<td>**Availability matrix**</td>
<td>Connect on Cloud</td>
<td>Desktop (SSO)</td>
<td>Desktop (License)</td>
</tr>
<tr>
<td>Cloud Stage, Editor</td>
<td>❌</td>
<td>✅</td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Cloud Stage, Viewer</td>
<td>❌</td>
<td><span color="gray">N/A</span></td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Local Stage</td>
<td><span color="gray">N/A</span></td>
<td>✅</td>
<td>✅</td>
</tr>
</table>
<columns>
	<column>
		**EN**
		- Users can load a Unity wasm (.zip) and embed it into the Stage.
		- **Adding a Unity layer does not mean the Stage and Unity can exchange messages.**
			- Send / Receive is supported via a separate Unity plugin and bridge app $`^\mathtt{scopeout}`$
	</column>
	<column>
		**KO**
		- Unity wasm (.zip)을 불러와서 스테이지에 임베딩할 수 있다.
		- **Unity layer를 추가한다고 해서 Stage와 Unity가 메시지를 주고받을 수 있는 것은 아니다.**
			- Send / Receive는 별도의 Unity 플러그인 및 bridge app에서 지원 $`^\mathtt{scopeout}`$
	</column>
</columns>
#### Plugin $`^\mathtt{legacy}`$
<callout>
	#### Worth considering in the next phase
	- **Plugins for CoC**: Use API integrations on the web environment and shared previews
	- **IDE for Custom plugins**: Easier debugging and editing
	- **AI generating Custom plugins inside Connect**
</callout>
<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38b45184b5da808dbd86ef8e8122fb18" alt="external_object_instance"/>
<table header-row="true" header-column="true">
<colgroup>
<col width="159.25">
<col width="147.25">
<col width="151.25">
<col width="166.25">
</colgroup>
<tr>
<td>**Availability matrix**</td>
<td>Connect on Cloud</td>
<td>Desktop (SSO)</td>
<td>Desktop (License)</td>
</tr>
<tr>
<td>Cloud Stage, Editor</td>
<td>❌</td>
<td>✅</td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Cloud Stage, Viewer</td>
<td>❌</td>
<td><span color="gray">N/A</span></td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Local Stage</td>
<td><span color="gray">N/A</span></td>
<td>✅</td>
<td>✅</td>
</tr>
</table>
<columns>
	<column>
		**EN**
		- Default built-in plugins: API, G29, Arduino, Gamepad
		**API **$`^\mathtt{legacy}`$
		- Name: defaults to ‘New API’; this is a required value.
		- Method, URL, Message from Pie, Message to Pie: same as the legacy implementation.
		- Override: Message from Pie can be overridden by one of URL, Header, or Body.
			- In this case, the overridden property cannot be edited in API Settings
		- For Header and Body, values can be entered in the code editor.
		- Test request: users can test the configured values. When a response arrives, the call success/failure is shown, and the user can view the full response content.
		- Changes are saved when a user Runs or Updates after changing values.
		- Settings cannot be changed during a Run.
		**IFTTT **$`^\mathtt{scopeout}`$** **$`^\mathtt{legacy}`$
		- Same as the legacy implementation except for the following:
			- **Settings cannot be changed during a Run**
		- In IFTTT Settings, users can save and test values like API.
		- Changes are saved when a user Runs or Updates after changing values.
		**Blokdots **$`^\mathtt{scopeout}`$** **$`^\mathtt{legacy}`$
		- Same as the legacy implementation.
		- Only adding, removing, and Run are possible, without separate Settings.
		**G29, Gamepad **$`^\mathtt{legacy}`$
		- Same as the legacy implementation.
		- Hardware can be connected via a wired connection.
		- Only adding, removing, and Run are possible, without separate Settings.
		**Arduino **$`^\mathtt{legacy}`$
		- Same as the legacy implementation except for the following:
			- **Settings cannot be changed during a Run**
		- In Arduino Settings, users can save the Port and Baud rate values.
		- Changes are saved when a user Runs or Updates after changing values.
		- Help link: [https://www.protopie.io/learn/docs/connect-arduino-plugin](https://www.protopie.io/learn/docs/connect-arduino-plugin)
	</column>
	<column>
		**KO**
		- Default 탑재 플러그인: API, G29, Arduino, Gamepad
		**API **$`^\mathtt{legacy}`$
		- Name: 기본값 ‘New API’, 필수로 입력해야 하는 값이다.
		- Method, URL, Message from Pie, Message to Pie: 레거시 구현과 같다.
		- Override: Message from Pie를 URL, Header, Body 중 하나로 override할 수 있다.
			- 이 경우, override된 속성은 API Settings에서 편집할 수 없음
		- Header, Body의 경우 코드 편집기에서 값을 입력할 수 있다.
		- Test request: 세팅한 값을 테스트해볼 수 있다. 응답이 오면 호출 성공/실패 여부가 노출되며, 전체 response 내용을 확인할 수 있다.
		- 값 변경 후 Run하거나 Update할 경우 변경한 값이 저장된다.
		- Run 도중에는 Settings를 변경할 수 없다.
		**IFTTT **$`^\mathtt{scopeout}`$** **$`^\mathtt{legacy}`$
		- 레거시 구현과 아래 항목을 제외하고 같다.
			- **Run 도중에는 Settings를 변경할 수 없음**
		- IFTTT Settings에서 API와 같이 값을 저장하고 테스트할 수 있다.
		- 값 변경 후 Run하거나 Update할 경우 변경한 값이 저장된다.
		**Blokdots **$`^\mathtt{scopeout}`$** **$`^\mathtt{legacy}`$
		- 레거시 구현과 같다.
		- 별도 Settings 없이 추가, 삭제, Run만 가능하다.
		**G29, Gamepad **$`^\mathtt{legacy}`$
		- 레거시 구현과 같다.
		- 유선으로 하드웨어를 연결할 수 있다.
		- 별도 Settings 없이 추가, 삭제, Run만 가능하다.
		**Arduino **$`^\mathtt{legacy}`$
		- 레거시 구현과 아래 항목을 제외하고 같다.
			- **Run 도중에는 Settings를 변경할 수 없음**
		- Arduino Settings에서 Port, Baud rate 값을 저장할 수 있다.
		- 값 변경 후 Run하거나 Update할 경우 변경한 값이 저장된다.
		- Help 링크: [https://www.protopie.io/learn/docs/connect-arduino-plugin](https://www.protopie.io/learn/docs/connect-arduino-plugin)
	</column>
</columns>
#### Gamepad and G29 message map
<callout>
	#### Worth considering in the next phase
	- Support multiple gamepads: New Connect currently supports multiple gamepads but lacks an indicator showing how many are connected.
</callout>
<columns>
	<column>
		<table header-row="true">
<tr>
<td>**Gamepad name**</td>
<td>**ProtoPie Connect message**</td>
<td>**Value**</td>
</tr>
<tr>
<td>**LT**</td>
<td>1_button6</td>
<td>10,0</td>
</tr>
<tr>
<td>**LB**</td>
<td>1_button4</td>
<td>1,0</td>
</tr>
<tr>
<td>**RT**</td>
<td>1_button7</td>
<td>10,0</td>
</tr>
<tr>
<td>**RB**</td>
<td>1_button5</td>
<td>1,0</td>
</tr>
<tr>
<td>**X**</td>
<td>1_button2</td>
<td>1,0</td>
</tr>
<tr>
<td>**Y**</td>
<td>1_button3</td>
<td>1,0</td>
</tr>
<tr>
<td>**A**</td>
<td>1_button0</td>
<td>1,0</td>
</tr>
<tr>
<td>**B**</td>
<td>1_button1</td>
<td>1,0</td>
</tr>
<tr>
<td>**Start**</td>
<td>1_button9</td>
<td>1,0</td>
</tr>
<tr>
<td>**Back**</td>
<td>1_button8</td>
<td>1,0</td>
</tr>
<tr>
<td>**1**</td>
<td>1_button12</td>
<td>1,0</td>
</tr>
<tr>
<td>**2**</td>
<td>1_button15</td>
<td>1,0</td>
</tr>
<tr>
<td>**3**</td>
<td>1_button13</td>
<td>1,0</td>
</tr>
<tr>
<td>**4**</td>
<td>1_button14</td>
<td>1,0</td>
</tr>
<tr>
<td>**RSB X axis**</td>
<td>1_axe2</td>
<td>10 to -10</td>
</tr>
<tr>
<td>**RSB Y axis**</td>
<td>1_axe3</td>
<td>10 to -10</td>
</tr>
<tr>
<td>**LSB X axis**</td>
<td>1_axe0</td>
<td>10 to -10</td>
</tr>
<tr>
<td>**LSB Y axis**</td>
<td>1_axe1</td>
<td>10 to -10</td>
</tr>
		</table>
		<empty-block/>
	</column>
	<column>
		<table header-row="true">
<tr>
<td>**G29 name**</td>
<td>ProtoPie Connect message</td>
<td>**Values**</td>
<td>**Notes**</td>
</tr>
<tr>
<td>**Wheel**</td>
<td>wheel-turn</td>
<td>0 - 100</td>
<td><span discussion-urls="discussion://36c45184-b5da-8078-8b6c-e0e2ee7aedfe/38b45184-b5da-80fe-9fd1-d5ae970478a2/39145184-b5da-8029-b942-001c5bbc73a0">  • 0 is full right<br>  • 50 is centered<br>  • 100 is full left</span></td>
</tr>
<tr>
<td>**Wheel**</td>
<td>wheel-shift_left</td>
<td>1,0</td>
<td></td>
</tr>
<tr>
<td>**Wheel**</td>
<td>wheel-shift_right</td>
<td>1,0</td>
<td></td>
</tr>
<tr>
<td>**Dpad**</td>
<td>wheel-dpad</td>
<td>0 - 8</td>
<td>  • 0 = neutral<br>  • 1 = north<br>  • 2 = northeast<br>  • 3 = east<br>  • 4 = southeast<br>  • 5 = south<br>  • 6 = southwest<br>  • 7 = west<br>  • 8 = northwest</td>
</tr>
<tr>
<td>**X**</td>
<td>wheel-button_x</td>
<td>1,0</td>
<td></td>
</tr>
<tr>
<td>**□**</td>
<td>wheel-button_square</td>
<td>1,0</td>
<td></td>
</tr>
<tr>
<td>**▵**</td>
<td>wheel-button_triangle</td>
<td>1,0</td>
<td></td>
</tr>
<tr>
<td>**○**</td>
<td>wheel-button_circle</td>
<td>1,0</td>
<td></td>
</tr>
<tr>
<td>**L2**</td>
<td>wheel-button_l2</td>
<td>1,0</td>
<td></td>
</tr>
<tr>
<td>**R2**</td>
<td>wheel-button_r2</td>
<td>1,0</td>
<td></td>
</tr>
<tr>
<td>**L3**</td>
<td>wheel-button_l3</td>
<td>1,0</td>
<td></td>
</tr>
<tr>
<td>**R3**</td>
<td>wheel-button_r3</td>
<td>1,0</td>
<td></td>
</tr>
<tr>
<td>**+**</td>
<td>wheel-button_plus</td>
<td>1,0</td>
<td></td>
</tr>
<tr>
<td>**-**</td>
<td>wheel-button_minus</td>
<td>1,0</td>
<td></td>
</tr>
<tr>
<td>**Spinner**</td>
<td>wheel-spinner</td>
<td>-1, 0, 1</td>
<td>  • -1 = left<br>  • 0 = neutral<br>  • 1 = right</td>
</tr>
<tr>
<td>**⏎**</td>
<td>wheel-button_spinner</td>
<td>1,0</td>
<td></td>
</tr>
<tr>
<td>**Share**</td>
<td>wheel-button_share</td>
<td>1,0</td>
<td></td>
</tr>
<tr>
<td>**Option**</td>
<td>wheel-button_option</td>
<td>1,0</td>
<td></td>
</tr>
<tr>
<td>**PlayStation**</td>
<td>wheel-button_playstation</td>
<td>1,0</td>
<td></td>
</tr>
<tr>
<td>**Gear**</td>
<td>shifter-gear</td>
<td>0 - 6, -1</td>
<td>  • 0 = neutral<br>  • 1-6 = gears<br>  • -1 = reverse</td>
</tr>
<tr>
<td>**Gas**</td>
<td>pedals-gas</td>
<td>0 - 1</td>
<td>  • 0 is no pressure<br>  • 0.25 is quarter pressure<br>  • 1 is fully pressed.</td>
</tr>
<tr>
<td>**Brake**</td>
<td>pedals-brake</td>
<td>0 - 1</td>
<td>  • 0 is no pressure<br>  • 0.25 is quarter pressure<br>  • 1 is fully pressed.</td>
</tr>
<tr>
<td>**Clutch**</td>
<td>pedals-clutch</td>
<td>0 - 1</td>
<td>  • 0 is no pressure<br>  • 0.25 is quarter pressure<br>  • 1 is fully pressed.</td>
</tr>
		</table>
	</column>
</columns>
#### Custom plugin $`^\mathtt{legacy}`$
<table header-row="true" header-column="true">
<colgroup>
<col width="159.25">
<col width="147.25">
<col width="151.25">
<col width="166.25">
</colgroup>
<tr>
<td>**Availability matrix**</td>
<td>Connect on Cloud</td>
<td>Desktop (SSO)</td>
<td>Desktop (License)</td>
</tr>
<tr>
<td>Cloud Stage, Editor</td>
<td>❌</td>
<td>✅</td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Cloud Stage, Viewer</td>
<td>❌</td>
<td><span color="gray">N/A</span></td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Local Stage</td>
<td><span color="gray">N/A</span></td>
<td>✅</td>
<td>✅</td>
</tr>
</table>
<columns>
	<column>
		**EN**
		- The plugin located in <mention-page url="https://app.notion.com/p/38a45184b5da8066ac7ff00bd66d0e25">Plugin</mention-page> appears below the default plugins.
		- Users can go directly to Settings \> Plugin via the Configure custom plugin… menu.
		- Custom plugins can only be used by Connect Enterprise users.
		- The plugin name set in the custom plugin's config is shown, and its first letter is shown in the thumbnail.
		- On hovering over a custom plugin row, a Terminal icon button appears.
			- Pressing the button opens the Terminal in a non-modal form, and logs sent from the Bridge app are shown here.
			- Users can pause or resume the log using the pause/play button.
				<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38b45184b5da80e29ce1c4bcf04dd436" alt="external_object_instance"/>
	</column>
	<column>
		**KO**
		- <mention-page url="https://app.notion.com/p/38a45184b5da8066ac7ff00bd66d0e25">Plugin</mention-page> 에서 locate한 플러그인이 default plugin 하단에 노출된다.
		- Configure custom plugin… 메뉴를 통해 Settings \> Plugin으로 바로 진입할 수 있다.
		- Custom plugin의 경우 Connect Enterprise 유저만 사용 가능하다.
		- Custom plugin의 config에서 설정된 플러그인 이름이 노출되고, 첫 글자가 썸네일에 노출된다.
		- Custom plugin row에 커서 호버 시 Terminal 아이콘 버튼이 노출된다.
			- 버튼을 누르면 Terminal이 non-modal 형태로 열리고, Bridge app에서 전송한 로그가 여기에 남는다.
			- 일시정지/재생 버튼을 통해 로그를 잠시 멈추거나 다시 재개할 수 있다.
			<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38b45184b5da8004986cf6be270667fd" alt="external_object_instance"/>
	</column>
</columns>
#### Console
<table header-row="true" header-column="true">
<colgroup>
<col width="159.25">
<col width="147.25">
<col width="151.25">
<col width="166.25">
</colgroup>
<tr>
<td>**Availability matrix**</td>
<td>Connect on Cloud</td>
<td>Desktop (SSO)</td>
<td>Desktop (License)</td>
</tr>
<tr>
<td>Cloud Stage, Editor</td>
<td>✅</td>
<td>✅</td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Cloud Stage, Viewer</td>
<td>✅</td>
<td><span color="gray">N/A</span></td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Local Stage</td>
<td><span color="gray">N/A</span></td>
<td>✅</td>
<td>✅</td>
</tr>
</table>
<callout>
	#### Worth considering in the next phase
	- Expanding multiple rows
	- Expand / Collapse all rows at once
</callout>
<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38b45184b5da807382b3ddd487179b25" alt="external_object_instance"/>
**Message log **$`^\mathtt{legacy}`$
<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38b45184b5da809b9cbfd49cdbb23bd5" alt="external_object_instance"/>
<columns>
	<column>
		**EN**
		- A record of messages Sent from Pies and Plugins is kept in chronological order.
		- It is stored per session and is volatile afterward.
			- It is not included in the data saved to the Stage.
		- Users can clear the accumulated message log using the Clear icon button.
		- A message row contains the following information:
			- Timecode: the time the message was sent
			- Message: the message name
			- Value: the value the message carries
			- Source
				- For a Plugin, the plugin name (for plugins whose name can be changed, such as API, the changed name is shown)
				- A message sent via the Send Message feature is “Console”
				- For a Pie, a message sent from the Player is “\[Pie name\] - \[Device name\]”; a message sent from a Pie preview or Stage preview is “\[Pie name\] - Web”
		- Clicking a message row selects that row; while selected, all values are shown in full without truncation.
		- New messages stack at the very top.
	</column>
	<column>
		**KO**
		- Pie, Plugin에서 Send한 메시지 기록이 시간 순서대로 남는다.
		- 세션당 저장되고 이후 휘발된다.
			- Stage에 저장되는 데이터에 포함되지 않는다.
		- Clear 아이콘 버튼을 통해 쌓인 메시지 로그를 제거할 수 있다.
		- 메시지 row는 다음 정보를 담고 있다.
			- Timecode: 메시지를 발신한 시간
			- Message: 메시지 이름
			- Value: 메시지가 담고 있는 값
			- Source
				- Plugin의 경우 플러그인 이름 (API 등 이름 변경이 가능한 플러그인은 변경한 이름이 노출)
				- Send Message 기능을 통해 전송한 메시지는 “Console”
				- Pie의 경우 Player에서 발신한 메시지는 “\[파이 이름\] - \[기기 이름\]”, Pie preview 혹은 Stage preview에서 발신한 메시지는 “\[파이 이름\] - Web”
		- 메시지 row를 클릭할 경우 각 row가 선택되며, 선택된 상태에서는 모든 값이 truncate되지 않고 전문이 노출된다.
		- 새로운 메시지가 가장 위에 쌓인다.
	</column>
</columns>
**Filter**
<columns>
	<column>
		**EN**
		- Users can add a Filter to view only the relevant content among Log messages.
		- Filtering is possible using three criteria: Message, Pie, and Source.
			- Message / =(is) or ≠(is not) or ⊇ (contains) / \[enter a value in the Combobox\]
			- Pie / =(is) or ≠(is not) / \[select from the list of added Pies\]
			- Source / =(is) or ≠(is not) / \[select from connected devices, plugins, or Preview\]
		- Multiple filters can be applied at the same time.
	</column>
	<column>
		**KO**
		- Filter를 추가해 Log 메시지 중 관련 있는 내용만 확인할 수 있다.
		- Message, Pie, Source 세가지 기준을 활용해 필터링 가능하다.
			- Message / =(is) or ≠(is not) or ⊇ (contains) / \[입력값을 Combobox에서 입력\]
			- Pie / =(is) or ≠(is not) / \[추가된 Pie 리스트에서 선택\]
			- Source / =(is) or ≠(is not) / \[연결된 device, plugin, Preview 중 선택\]
		- 여러 필터를 동시에 적용할 수 있다.
	</column>
</columns>
**Send Message **$`^\mathtt{legacy}`$
<columns>
	<column>
		**EN**
		- Users can send a message manually by entering a Message and Value.
			- Message: a Combobox appears when a user starts typing, showing the list of messages registered in all Pies and plugins in the Stage
			- Messages not in the list can also be typed and sent directly
		- Users can send it using ⌘+Return (Ctrl+Enter on Windows).
	</column>
	<column>
		**KO**
		- Message, Value를 입력해 강제로 메시지를 발신할 수 있다.
			- Message: 입력 시작 시 Combobox가 나타나고, Stage에 포함된 모든 파이 및 플러그인에 등록된 메시지 목록이 보임
			- 목록에 포함되지 않은 메시지도 직접 타이핑해 전송할 수 있음
		- ⌘+Return (Windows의 경우 Ctrl+Enter)를 활용해 전송할 수 있다.
	</column>
</columns>
**Recording **$`^\mathtt{legacy}`$
<table header-row="true" header-column="true">
<colgroup>
<col width="159.25">
<col width="147.25">
<col width="151.25">
<col width="166.25">
</colgroup>
<tr>
<td>**Availability matrix**</td>
<td>Connect on Cloud</td>
<td>Desktop (SSO)</td>
<td>Desktop (License)</td>
</tr>
<tr>
<td>Cloud Stage, Editor</td>
<td>✅</td>
<td>✅</td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Cloud Stage, Viewer</td>
<td>✅</td>
<td><span color="gray">N/A</span></td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Local Stage</td>
<td><span color="gray">N/A</span></td>
<td>✅</td>
<td>✅</td>
</tr>
</table>
<columns>
	<column>
		<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38b45184b5da803a8b2df8ec2798cc1e" alt="external_object_instance"/>
	</column>
	<column>
		<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38b45184b5da802eb2bdd0d400471adf" alt="external_object_instance"/>
	</column>
</columns>
<columns>
	<column>
		**EN**
		- When a user starts Record, the message log is recorded until the user presses Stop.
		- When a user Stops, the recorded message log is saved as a csv file.
			- Saved columns: Time, Message, Value, Pie, Source
		- For CoC (browser environment), the csv file is saved to the browser's default download location.
		- For the Desktop app, a Save dialog is shown and the user can choose where to save.
		- Pressing the Load button lets a user load a csv file obtained via recording.
			- **Play**: in this case the logs in the csv are shown and messages are sent one by one.
				- During Play, the Source column in Backstage and Console is not shown.
				- During Play, the sent message is highlighted in a selected state.
				- Repeat and Playback speed can be set.
			- Pause: pauses playback without resetting the Play state. Resuming Play starts from where it stopped.
			- Stop: resets the Play state and stops playback. Resuming Play starts from the beginning.
	</column>
	<column>
		**KO**
		- Record 시작할 경우 Stop을 누를 때까지 메시지 로그가 기록된다.
		- Stop할 경우 기록된 메시지 로그가 csv 파일로 저장된다.
			- 저장되는 column: Time, Message, Value, Pie, Source
		- CoC (브라우저 환경)의 경우 csv 파일이 브라우저의 default download 위치에 저장된다.
		- Desktop app의 경우 Save dialog가 노출되고 유저가 저장할 위치를 지정할 수 있다.
		- Load 버튼을 누를 경우 recording을 통해 받은 csv 파일을 로드할 수 있다.
			- **Play**: 이 경우 csv에 포함된 로그가 노출되고, 메시지를 하나씩 발송한다.
				- Play 중에는 Backstage 및 Console의 Source column이 표시되지 않는다.
				- Play 중에는 발신한 메시지가 selected 상태로 하이라이트된다.
				- Repeat, Playback speed를 설정할 수 있다.
			- Pause: Play 상태를 초기화하지 않고 재생을 멈춘다. 다시 Play할 경우 중단했던 지점에서 시작한다.
			- Stop: Play 상태를 초기화하고 재생을 멈춘다. 다시 Play할 경우 처음부터 시작한다.
	</column>
</columns>
#### Backstage
<table header-row="true" header-column="true">
<colgroup>
<col width="159.25">
<col width="147.25">
<col width="151.25">
<col width="166.25">
</colgroup>
<tr>
<td>**Availability matrix**</td>
<td>Connect on Cloud</td>
<td>Desktop (SSO)</td>
<td>Desktop (License)</td>
</tr>
<tr>
<td>Cloud Stage, Editor</td>
<td>Pie only</td>
<td>✅</td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Cloud Stage, Viewer</td>
<td>Pie only</td>
<td><span color="gray">N/A</span></td>
<td><span color="gray">N/A</span></td>
</tr>
<tr>
<td>Local Stage</td>
<td><span color="gray">N/A</span></td>
<td>✅</td>
<td>✅</td>
</tr>
</table>
<callout color="red_bg">
	#### Scoped out for this phase
	- Designs of nodes
	- Show contained messages within each node
	- Click the handle to add filters
	- Pie nodes
</callout>
<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38b45184b5da800faeabe1bba02a327f" alt="external_object_instance"/>
<columns>
	<column>
		**EN**
		- Pies and plugins connected to the Stage are represented as nodes.
			- **For plugins, as many nodes are shown as there are desktop apps that have the Stage open. (each plugin connected to each desktop app is a separate node)**
		- Messages contained in Pies and plugins are shown as badges.
		- When a message is triggered, the badge and node are highlighted.
		- Clicking a Handle shows the contained messages as a list, and a message selected here is applied as a filter in the Console. <mention-page url="https://app.notion.com/p/38b45184b5da809fb3e0d1687eb4a1e6">Filter</mention-page> 
	</column>
	<column>
		**KO**
		- Stage에 연결된 Pie 및 플러그인이 노드로 표현된다.
			- **플러그인의 경우 해당 Stage를 열고 있는 desktop app의 수만큼 노출된다. (각 desktop app에 연결된 플러그인이 각각 개별 노드)**
		- Pie 및 플러그인에 포함된 메시지가 badge로 노출된다.
		- 메시지가 trigger될 경우 badge 및 노드가 highlight된다.
		- Handle을 클릭할 경우 포함된 메시지가 리스트로 노출되며, 여기서 선택한 메시지는 Console에서 filter로 적용된다. <mention-page url="https://app.notion.com/p/38b45184b5da809fb3e0d1687eb4a1e6">Filter</mention-page> 
	</column>
</columns>
<columns>
	<column>
		<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38b45184b5da80058c11c4c48c7de1fa" alt="external_object_instance"/>
	</column>
	<column>
		<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38b45184b5da801683b5f9f523a24ef1" alt="external_object_instance"/>
	</column>
</columns>
**Connect node**
<columns>
	<column>
		**EN**
		- For a Local Stage, it shows the IP address set in the app.
		- For a Cloud Stage, it shows “Connect Cloud”.
	</column>
	<column>
		**KO**
		- Local Stage의 경우 앱에서 설정한 IP 주소를 노출한다.
		- Cloud Stage의 경우 “Connect Cloud” 노출한다.
	</column>
</columns>
**Plugin node**
<unknown url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38b45184b5da808f8a6cd23a5f1a557d" alt="external_object_instance"/>
<columns>
	<column>
		**EN**
		**API**
		- Input: Message from Pie in API Settings, a single value
		- Output: Message to Pie in API Settings, a single value
		**Arduino**
		- Input, Output: only the node is shown, without messages
		- Messages are not shown; no Handle click action
		**Gamepad, G29**
		- The node shows only the Gamepad/G29 name from the <mention-page url="https://app.notion.com/p/38b45184b5da80288b43d835a04d8883">Gamepad and G29 message map</mention-page> 
		- The menu shown when pressing the Handle displays “\[Connect message\] (\[Gamepad/G29 name\])”
		**Custom plugin**
		- Only messages configured in the Plugin are shown
		**blokdots, IFTTT **$`^\mathtt{scopeout}`$
		- blokdots has only Output; IFTTT has only Input
		- Messages are not shown; no Handle click action
	</column>
	<column>
		**KO**
		**API**
		- Input: API Settings의 Message from Pie, 단일 값
		- Output: API Settings의 Message to Pie, 단일 값
		**Arduino**
		- Input, Output: 메시지 없이 노드만 노출
		- 메시지는 노출하지 않음, Handle 클릭 액션 없음
		**Gamepad, G29**
		- Node에서는 <mention-page url="https://app.notion.com/p/38b45184b5da80288b43d835a04d8883">Gamepad and G29 message map</mention-page> 의 Gamepad/G29 name만 노출
		- Handle 누를 경우 노출되는 메뉴에서는 “\[Connect message\] (\[Gamepad/G29 name\])”으로 노출
		**Custom plugin**
		- Plugin에서 configure된 메시지에 한해 노출
		**blokdots, IFTTT **$`^\mathtt{scopeout}`$
		- blokdots은 Output만, IFTTT는 Input만 가짐
		- 메시지는 노출하지 않음, Handle 클릭 액션 없음
	</column>
</columns>
<empty-block/>
---
# Misc
## 1. Feature suggestions
- <mention-page url="https://app.notion.com/p/37c45184b5da80cb81a5f8b5df4c271e"/> 
- <mention-page url="https://app.notion.com/p/38a45184b5da80d49263dac78b1cc1de"/> 
## 2. Related docs
- <mention-page url="https://app.notion.com/p/38045184b5da808ca22bc615b6fbd239"/> 
- <mention-page url="https://app.notion.com/p/37d45184b5da80b080d7c00eab9053b5"/> 
## 3. FAQ
<synced_block_reference url="https://app.notion.com/p/36c45184b5da80788b6ce0e2ee7aedfe#38b45184b5da80689b58e17b2e375183">
	## Product Overview {color="gray_bg"}
	**How is this different from the Connect I've been using?**
	The original Connect was built around one machine on a local network. It worked well for individual use, but scaling it across a team was always a stretch. Connect on Cloud moves that experience to the web so your whole team can work from the same Stage regardless of where they are. Sharing with stakeholders is just a link. Your setup lives in the cloud, so it doesn't disappear when someone switches laptops or leaves the team.
	---
	**What problem does Connect on Cloud actually solve?**
	If you've tried scaling Connect across a larger team, you've probably hit the wall. Everyone needs to be on the same network, configurations are tied to specific machines, and bringing someone new up to speed takes more effort than it should. Connect on Cloud removes those constraints so teams can connect, prototype, and validate with real devices together, remotely, without the workarounds.
	---
	**Can I still use Connect the way I do today?**
	Yes. Local Stage works exactly like the Connect you're used to, same local network setup, nothing changes. If you're in a fully offline or air-gapped environment, the Embedded license has you covered too.
	---
	**What's the difference between a Cloud Stage and a Local Stage?**
	Cloud Stage runs in the cloud. It's accessible from anywhere, tied to a Team space, and shareable via link, which makes it great for remote collaboration and stakeholder reviews. Hardware connects through Desktop. Local Stage is your existing Connect experience: local network, direct hardware support, Unity layer, and full offline capability. Both are available within the same app so you can use whichever fits the workflow.
	---
	**What can I expect from the Closed Beta?**
	You'll get access to the core Cloud Stage experience: creating Stages, inviting teammates, sharing with external reviewers via link, and using Console.
	## Access & Roles {color="gray_bg"}
	**Who can use it?**
	Anyone with Editor access in a Team space can use Connect on Cloud. External reviewers or stakeholders don't need an account. They can join as Viewers through a shared link.
	---
	**Do I need an account?**
	Only if you're editing or running a Stage. Viewers can join without signing up. Just click the link and you're in.
	---
	**Can someone access it without an account?**
	Yes. Viewers don't need to install anything or sign in. Just open the shared link in a browser.<br>How access works depends on how the link was shared. When an Editor copies a share link, it includes an access token that lets Viewers join immediately without entering a PIN. The token doesn't expire, so previously copied links continue to work. After joining through the token link, the Viewer stays authenticated for up to 6 hours without needing to re-enter anything. If the link doesn't include a token, Viewers will be asked to enter a PIN instead. The PIN changes every five minutes, so expired PINs can no longer be used.
	---
	**What can a Viewer do?**
	By default, Viewers are in watch mode. They can flip on Interaction mode themselves to run Pies and send messages directly. Editing the Stage or generating share links is Editor-only.
	---
	**Can I preview what Viewers see from my Editor account?**
	No. Editors and Viewers use the same shared link, but an Editor can't switch into the Viewer experience. If you want to see exactly what a Viewer sees, open the link from a separate Viewer account.
	---
	**How does the permission model work?**
	There are two roles: Editor and Viewer. Editors get full access to build, configure, and share. One thing to keep in mind during the Closed Beta is that Editors can archive a Stage, but they can't permanently delete it. Once a Stage is archived, nobody can access it, including Editors, until it's restored.
	---
	**Can I share a single Pie instead of the whole Stage?**
	Yes. You can copy a preview link for any individual Pie directly from the Stage. Anyone who opens that link sees only the selected Pie, without the rest of the Stage or its controls. The experience is the same for everyone, regardless of whether they're an Editor or Viewer.
	---
	**Why can some people access the Stage without entering a passcode?**
	When an Editor copies a share link, it includes an access token. Anyone opening that link can join without entering a passcode. The token embedded in the URL doesn't expire automatically, so previously copied links can continue to work. After joining through a token link, the viewer stays authenticated for up to 6 hours without needing to enter a passcode again.
	## Collaboration & Sharing {color="gray_bg"}
	**Does it support multiplayer?**
	Yes. Multiple users on different networks can be in the same Cloud Stage at the same time, Editors and Viewers included.
	---
	**What about co-editing?**
	Simultaneous co-editing isn't available in this release.
	---
	**How do multiple people use it at the same time?**
	An Editor sets up the Stage and shares a link. Viewers join and can watch live or interact directly. Each person runs their own instance, and Editors can reset everyone's instances at once with a single Run action.
	---
	**Why don't Undo and Redo work?**
	Undo and Redo aren't available in the Closed Beta yet. They're planned for a future update.
	---
	**Why are layers moving on their own?**
	If someone else is active in the same Stage, you'll see their actions appear in real time. That includes Editors making changes and Viewers interacting with the Stage when Interaction mode is enabled. The current Beta doesn't yet provide collaborator awareness features such as live editing indicators, but those are on our radar for a future update.
	---
	**Viewers lost access to the Stage. What happened?**
	A Cloud Stage stays active as long as at least one Editor is connected. After the last Editor leaves, the session remains available for one more minute before it expires. Once the session ends, Viewers can no longer access the Stage until an Editor opens it again. The original share link still works, so Viewers can rejoin as soon as the Stage is active again.
	---
	**What happens when a Stage is archived?**
	Archiving a Stage makes it unavailable to everyone. Editors can't open or edit it, and Viewers can't access it either. The Stage isn't deleted though. Its contents are preserved and can be restored at any time by an Editor. Once restored, it reappears in the Stage list and works as before.
	---
	**Can I use Pies from another Team space in a Cloud Stage?**
	No. Every Cloud Stage belongs to a single Team space, and it can only use Pies from that same Team. Even if you have access to other Team spaces or your Personal Space, those Pies won't be available in the Stage. This restriction only applies to Cloud Stages. Local Stages continue to work the way they always have.
	---
	**Can I use a Pie that's saved locally on my computer in a Cloud Stage?**
	No. Cloud Stages can only use Pies that have been uploaded to the same Team space. Pies stored only on your local machine aren't available in Cloud Stages. To use one, simply upload it to your Team space first.
	## Hardware & Connectivity {color="gray_bg"}
	**What connection types are supported?**
	USB HID, Serial, MIDI, and other physical devices are all supported through the Desktop app, along with Bridge App, Built-in Plugins, and Custom Plugins. For Cloud Stages, Cloud Relay pulls together hardware from different PCs into one shared environment.
	---
	**Can hardware connect through the web?**
	Not directly. Hardware connections require the Desktop app. That said, Cloud Relay lets you bring hardware from different machines into a single Cloud Stage, so distributed hardware setups work even across locations.
	---
	**Where does Unity run?**
	Unity Layer is Desktop-only and works with Local Stages only. It's not available in the web app or Cloud Stages.
	---
	**Does Connect on Cloud support the Unity plugin?**
	No. Unity plugin support is not available in the Closed Beta.
	---
	**Will my existing custom plugins work in Connect on Cloud?**
	Probably, but not always. Most legacy custom plugins work without changes, but some may need to be updated due to differences in implementation, dependencies, or the runtime environment. The most common issue is Node.js compatibility, since Connect on Cloud runs plugins within a supported Node.js version range.
	There's no automatic migration tool. If a plugin doesn't work, it needs to be updated by the plugin author. The easiest way to check compatibility is to run the plugin in Connect desktop. If it fails, copy the error message from the terminal. That usually provides the quickest path to identifying what needs to be changed.
	## Security & Infrastructure {color="gray_bg"}
	**Do you support SSO?**
	Yes. It's a browser-based auth flow that redirects back into the app. Works for both general Cloud and Enterprise environments.
	---
	**What about security?**
	For detailed security documentation, reach out to your account team. We're happy to walk through specifics based on your requirements.
	---
	**Where is data stored?**
	Self-Serve runs on shared AWS ECS infrastructure. Enterprise customers get a dedicated EKS and PostgreSQL environment that's fully isolated. Anything you add to a Stage is preserved in the cloud as a Stage resource, even if the original file gets deleted.
	---
	**Does it meet Enterprise security requirements?**
	Enterprise customers get dedicated, isolated infrastructure. For compliance specifics or security reviews, get in touch with our sales team and we'll work through it with you.
	---
	**Which browsers are supported?**
	Connect on Cloud works in Chrome, Edge, Firefox, and other Chromium based browsers. Safari isn't fully supported during the Closed Beta. If you use Safari, Pie previews open in a new browser tab instead of a Picture in Picture window. For the best experience, we recommend using Chrome or Edge.
	---
	**Is on-premises supported?**
	Not yet. It's on the roadmap and we'll share more once timing is confirmed.
	---
	**How do I start using Cloud Stages if I'm already using Connect?**
	No migration is required. Simply sign in to the Desktop app as you normally would and your existing Local Stages will continue working as before. When you're ready to use Cloud Stages, create or join a Team space with the appropriate permissions.
	---
	**I'm using a License key without a Cloud login. What can't I do?**
	Without signing in to a Cloud account, Cloud features aren't available. You won't be able to view or duplicate Cloud Stages, or add Cloud Pies to a Local Stage. Everything that works locally, including creating and running Local Stages, connecting hardware, and using plugins, continues to work as usual. If you decide to use Cloud features later, you can sign in with your Cloud account at any time without affecting your existing local setup.
	---
	**What happened to 0.0.0.0 (All Networks)?**
	The 0.0.0.0 (All Networks) option has been removed. Allowing connections from any network introduces unnecessary security risks, so Connect on Cloud now requires a more explicit network configuration. You can choose which port Connect uses under Settings \> Network.
</synced_block_reference>
<empty-block/>
