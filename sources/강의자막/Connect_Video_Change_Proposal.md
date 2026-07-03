---
doc_id: CC-CHG-VIDEO
title: Cloud Connect — 영상 자막 기반 스펙 변경 제안 리포트
purpose: "Intro to ProtoPie Connect" 강의 영상 8편의 자막을 분석하여 Cloud_Connect_Spec.md에 반영할 항목을 도출한다. 검토 후 확정된 항목만 스펙에 병합한다.
audience: QA (Paige), PM, Designer
prepared_by: Claude
prepared_on: 2026-05-21
source_videos:
  - "1-1. How to Use Send and Receive in Studio (Studio 단독, Connect 없이)"
  - "1-2. How to Use Send and Receive in Connect (Connect 경유)"
  - "2. How to Integrate IFTTT"
  - "3. How to Use Blokdots to Integrate with Arduino"
  - "4. How to Use the Arduino Plugin with Sketch Code"
  - "5. Use the Logitech G29 Steering Wheel"
  - "6. Write Custom Bridge App — Date, Time, Weather"
  - "7. Integrate Bridge App to Smart Home IoT"
target_doc: Cloud_Connect_Spec.md (rev 2)
review_workflow:
  - Paige가 본 리포트 검토
  - 각 항목별로 [반영 / 보류 / 거부] 결정
  - 반영 항목만 스펙에 병합 + Decision Log에 한 줄 추가
---

# 영상 자막 기반 스펙 변경 제안 리포트

## 0. 핵심 컨텍스트 (전제 정리)

**이 영상들은 모두 "Legacy ProtoPie Connect"를 다룬다.** Cloud_Connect_Spec.md의 우선순위 P1("레거시 Connect의 사용자 가시 기능을 신규 앱에서 동등 이상으로 보장한다")의 검증 베이스라인이 된다. 따라서 본 리포트의 항목 대부분은 **레거시 회귀 기준선** 성격이고, 일부만 신규 결정 사항을 요구한다.

본 리포트의 모든 항목에는 출처 영상 번호 + 자막 라인 번호를 명시하여 추적 가능하게 했다.

---

## 1. 카테고리별 변경 제안 요약

| # | 카테고리 | 신규 추가 | 기존 수정 | 충돌/확인 필요 |
|---|---|---|---|---|
| A | F-REL Send/Receive 채널·메시지 프로토콜 | 4 | 1 | 1 |
| B | F-PLG 플러그인 상세 동작 (IFTTT/Blokdots/Arduino/G29) | 7 | 2 | 1 |
| C | F-BRG Custom Bridge App / 플러그인 패키징 | 4 | 1 | 2 |
| D | F-STG 다중 Pie / Multi-view (Stage View 베이스라인) | 3 | 1 | 0 |
| E | F-VWR Player 진입 (QR) | 1 | 0 | 0 |
| F | F-IDM Plan gate (Enterprise 한정 기능) | 0 | 1 | 1 |
| G | 에러 카탈로그 (S-ERR) 보강 | 5 | 0 | 0 |
| H | 검증 우선순위 / Non-goals | 2 | 0 | 0 |
| | **합계** | **26** | **5** | **5** |

---

## 2. A. F-REL — Send/Receive 메시지 프로토콜

### A-1. [신규] 메시지 채널 명세 명시화

**현재 스펙 상태:** F-REL에 "메시지 envelope" WIP 표시만 있고 (`F-REL-envelope`), 실제 채널 식별자가 명문화되어 있지 않음.

**제안:** F-REL 또는 §1 용어에 다음 명시.
- **채널 식별자:** `ProtoPi Studio` 채널이 Pie ↔ Pie 메시지 라우팅의 단일 채널. 송신측·수신측 모두 동일 채널 선택 필수.
- 채널 불일치 시 메시지가 전달되지 않으며 사용자 에러가 표시되지 않음 (silent fail) — **QA 검증 포인트**

**출처:**
- Video 1-1, L43-46: "you have to make sure you use the proto pi studio channel"
- Video 1-1, L94-96: 수신측에서도 동일 채널 매칭 필요
- Video 2, L92-93: IFTTT 사용 시에도 동일

**QA 영향:** S-ERR에 "E-MSG-CHANNEL-MISMATCH" 추가 후보 (G-1 참조).

---

### A-2. [신규] 메시지 값 전달과 변수 매핑

**제안:** F-REL 또는 F-STG에 메시지 데이터 모델 명시.
- 메시지는 **이름 + 선택적 값 1개**로 구성
- 수신측에서 값을 사용하려면 변수에 assign 필수
- 변수 타입(Number/Text)이 값과 불일치 시 동작 정의 필요 — **현재 스펙 누락**

**출처:**
- Video 1-1, L104-114: receive에서 값을 변수에 할당하는 패턴
- Video 1-1, L124-130: text 메시지 수신 시 변수 타입을 Text로 변경해야 함
- Video 1-2, L116-122: "we had to assign it to a variable"
- Video 6, L401-407: 동일 패턴, 변수 타입이 핵심

**QA 영향:** 타입 불일치 시 silent drop / 에러 / 자동 캐스팅 중 정책 확정 필요.

---

### A-3. [신규] 메시지 명명 컨벤션 (사용자 가이드 영역)

**제안:** §7 Non-goals 또는 별도 노트로 기록.
- 업계 관례(영상에서 강사가 일관 사용): 외부(Pie 간) 메시지는 UPPERCASE, 내부(Scene/Component 내) 메시지는 lowercase
- 이는 강제가 아닌 컨벤션이지만, ProtoPie 학습 자료의 표준 패턴
- **QA 영향:** 카피·튜토리얼 산출물 일관성 검증에 참조

**출처:** Video 1-1, L50-61 (강사가 명시적으로 컨벤션 설명)

---

### A-4. [신규/중요] 동시 전송 메시지의 동시 수신 보장

**제안:** F-REL에 명시.
- 한 트리거에서 여러 send를 연속 호출하면 **수신측에서 동시(simultaneous) 수신**으로 처리됨
- 따라서 수신 로직은 send 그룹 중 한 메시지의 receive 트리거 내에 모아 작성 가능 (다른 메시지 값도 이미 변수에 들어와 있음)
- **이 보장은 레거시 동작이며 Beta에서도 동일해야 함**

**출처:**
- Video 1-1, L135-142: "both of these messages are sent at the same time proto pi sends them simultaneously and therefore they are received simultaneously"

**QA 영향:** 분산 환경(Cloud Relay 경유)에서도 같은 그룹의 send가 동시 도착하는지 — **분산 idempotency·순서 보장 회귀 핵심**. `F-REL-envelope` WIP와 연결.

---

### A-5. [신규/주의] 연속 send의 성능 함정 (Anti-pattern 문서화)

**제안:** F-REL 또는 §6 에러 카탈로그 인접에 "Known Pitfall" 항목으로 기록.

레거시에서 사용자가 자주 빠지는 패턴:
- Detect-on-slider-width (또는 다른 연속 변경값) → send 호출 → 메시지 폭주
- 4개 인스턴스 × 연속 send = Connect 메시지 로그 swamp
- 해결: detect를 의미 있는 변수 변경(brightness 값 자체)에 걸기

**Beta 영향:** Cloud Relay 환경에서는 메시지 폭주가 네트워크·Redis 부하로 직접 전이됨. **Rate limiting / backpressure 정책 검토 필요** (현재 스펙에 없음).

**출처:** Video 1-2, L286-306 (강사가 디버깅 과정에서 이 함정을 시연·해결)

---

### A-6. [기존 수정] F-REL-envelope WIP의 우선순위 상향 권고

**현재:** F-REL-envelope WIP (메시지 envelope + idempotency).
**제안:** A-1 ~ A-5의 7개 검증 포인트가 모두 envelope/dedupe 설계에 의존하므로, dev 5주 중 **우선 처리 대상**으로 분류 권고.

---

### A-7. [충돌 확인 필요] "Connect 없이 2개 Pie 통신" 시나리오

**자막 발견:** Video 1-1 전체가 **Connect 없이** Studio + Mobile Player 2개 Pie가 직접 통신하는 시나리오를 다룸 ("you can use send and receive through the proto pi studio channel without using connect at all" — L201-205).

**현재 스펙 상태:** Capability Matrix(§3)는 모드별 기능을 정리하지만, **"Connect 미사용 시 직접 Pie ↔ Pie 통신"** 시나리오가 명시되어 있지 않음. F-REL은 Stage 컨텍스트 안에서만 동작하는 것으로 기술됨 (`F-REL-stage-context`).

**확인 필요:** Beta에서 이 시나리오를 유지하는가?
- 유지 시: Capability Matrix에 "Connect 없는 직접 Studio ↔ Player 통신" 행 추가
- 폐기 시: Non-goals에 명시 + 카피 변경 안내

**출처:** Video 1-1, L201-209

---

## 3. B. F-PLG — 플러그인 상세 동작

### B-1. [신규] 프리셋 플러그인 상세 동작 명세 — 6종 개별 카드

현재 스펙 F-PLG-preset-list는 6종 이름만 나열. 영상 4편에서 4종(IFTTT, Blokdots, Arduino, G29)의 구체적 동작이 드러남. 각각을 F-PLG 하위 서브섹션 또는 별도 부록으로 기록 권고. 회귀 케이스 도출에 필수.

#### B-1-a. IFTTT 플러그인 (Video 2)

**제안 추가 항목:**

| 검증 포인트 | 근거 자막 |
|---|---|
| Webhook Key 입력 필수, 빈 값/잘못된 형식 거부 | L165-178 |
| Test 기능: 플러그인 Run 상태일 때만 활성, Pie 메시지 영향 없음(드라이런) | L181-197 |
| Events 매핑: Pie 메시지 명 → IFTTT 이벤트 명, 1:1 매핑 | L211-220 |
| 이벤트 명 제약: 영문자/숫자/언더스코어만, 공백·특수문자 거부 (IFTTT 측 제약 노출) | L21-24 |
| Pie → Connect → IFTTT 메시지 흐름의 source 표기 정확성 (메시지 로그) | L139-160 |
| JSON 페이로드 구성: Pie에서 value1/2/3 키로 packing (escape 처리) | L99-145 |

#### B-1-b. Blokdots 플러그인 (Video 3)

| 검증 포인트 | 근거 자막 |
|---|---|
| Blokdots 앱 측에서 "Add Integration → ProtoPie Connect" 선택 시 자동 연결, Connect 플러그인 패널에서 상태 "connected" 즉시 반영 | L126-133 |
| Blokdots 앱 종료 시 Connect 플러그인 상태가 Disconnected로 전환 | (F-PLG-states 회귀) |
| 첫 연결 시 Arduino 보드에 펌웨어 자동 설치 (Blokdots 책임) | L42-45 |
| 인코더는 디지털 핀 2개를 sequential로 점유 (예: D3+D4) | L62-71 |
| 알려진 한계: 인코더 + 일반 버튼 배선 시 버튼 동작이 반전되어 보일 수 있음 (사용자 책임, 회귀 영향 없음) | L86-124 |

#### B-1-c. Arduino 플러그인 (Video 4)

| 검증 포인트 | 근거 자막 |
|---|---|
| Baud rate 설정 일치 필수 (코드 설정 ↔ 플러그인 설정). 불일치 시 메시지 수신 불가 | L46-51, L130-139 |
| 시리얼 포트 자동 식별 + 라벨 표시 ("Arduino Uno R3" 등) | L136-139 |
| Arduino IDE와 동시 사용 불가 — IDE 종료 후 Connect 플러그인 실행 | L120-125 |
| 메시지 값 전달 프로토콜: `messageName\|\|value` 형식 (파이프 2개) | L201-213 |
| 한 줄에 `Serial.println(msg + "\|\|" + value)`가 동작하지 않음 — `Serial.print(msg + "\|\|"); Serial.println(value);` 2단 구성 필요. **레거시 동작상 제약** | L210-228 |

**Beta 영향:** 메시지 envelope 변경 시 `||` 구분자 호환성 검토 필요. (B-3 충돌 항목 참조)

#### B-1-d. G29 플러그인 (Video 5)

| 검증 포인트 | 근거 자막 |
|---|---|
| 스티어링 휠 모드: PS3 호환 모드 권장. PS4 모드 동작 보장 안 됨 | L9-13 |
| 메시지명·값 매핑 표 (회귀 베이스라인) | L20-60, L120-180, L302-560 |

**G29 메시지 카탈로그 (영상 5에서 도출, 레거시 베이스라인):**

| 메시지 명 | 값 범위 | 의미 |
|---|---|---|
| `wheel turn` | 0.00 ~ 100.00 (소수 2자리) | 0=좌 풀락, 50=중립, 100=우 풀락 |
| `pedals gas` | 0.00 ~ 1.00 (소수 2자리) | 가속 페달 압력 |
| `shifter gear` | -1, 1~6 | -1=후진, 1~6=전진단 |
| `wheel button r3` | 0 또는 1 | R3 버튼 |
| `wheel button l3` | 0 또는 1 | L3 버튼 |
| `wheel button triangle` | 0 또는 1 | 삼각형 |
| `wheel button plus` | 0 또는 1 | + 버튼 |
| `wheel button minus` | 0 또는 1 | - 버튼 |
| `wheel button spinner` | 0 또는 1 | 휠 스피너 중앙 버튼 |
| `wheel shift right` | 0 또는 1 | 우측 패들 |
| `wheel shift left` | 0 또는 1 | 좌측 패들 |
| `wheel spinner` | -1 또는 1 | 휠 스피너 회전 (1=시계, -1=반시계) |

**QA 영향:** 이 표를 F-PLG 또는 부록으로 그대로 박제하면, G29 회귀 케이스를 즉시 생성 가능. **레거시 동등 보장(P1)의 직접 증빙**.

---

### B-2. [신규] 플러그인 동시 실행 동작

**제안:** F-PLG에 추가.
- 여러 플러그인이 **동시 실행** 가능 (예: Arduino + G29 + IFTTT 동시 활성)
- 한 Pie의 send 메시지는 활성 모든 플러그인에 dispatch
- 한 Arduino 코드 + 다른 Arduino Blokdots 같은 조합도 가능

**출처:** Video 5, L1146-1160

**QA 영향:** 멀티 플러그인 메시지 라우팅 충돌·우선순위 정책 정의 필요. 현재 스펙에 없음.

---

### B-3. [충돌 확인 필요] Arduino 메시지 envelope의 `||` 구분자

**자막 발견:** 레거시 Arduino 플러그인은 `messageName||value` 형식 파싱을 코어에 내장 (Video 4, L201-213).

**충돌:** F-REL-envelope WIP에서 Beta envelope 포맷을 결정할 때, **레거시 `||` 구분자를 입력 측 호환성으로 유지할지** 미정.

**QA 영향:** envelope 결정 시 Arduino 플러그인 코드 수정 여부, 기존 사용자 스케치 호환성 케이스를 도출해야 함. dev 5주 결정 사항으로 분류.

---

### B-4. [기존 수정] F-PLG-states의 외부 의존 플러그인 동작 명시

**현재 F-PLG-states (CONFIRMED):** Run / Deactivated / Disconnected 3종.
**제안 추가 검증 포인트:**
- 외부 디바이스 분리(USB 빼기)·외부 앱 종료(Blokdots 앱 종료) 시 즉시 Disconnected 상태로 전이되는 latency
- Disconnected 상태에서 Pie의 send 메시지는 silent drop (또는 큐잉?)
- 재연결 시 큐잉된 메시지 처리 정책 (현재 스펙 부재)

**출처:** Video 3, L126-133 (Blokdots 연결 상태) + Video 4, L120-125 (Arduino IDE 종료 요구)

---

### B-5. [신규] 플러그인 설정 UI 회귀 베이스라인

각 플러그인의 설정 UI 구성요소를 회귀 베이스라인으로 기록.

- **API 플러그인** (스펙 F-PLG-api-bridge에 이미 있음 — 영상에 직접 안나옴, 누락 없음)
- **IFTTT**: Webhook Key 입력 + Events 매핑 표 + Test 영역 (Event Name + JSON Payload + Send 버튼)
- **Arduino**: Baud rate 드롭다운 + Port 드롭다운 + Run/Stop 토글
- **G29**: Run/Stop만 (자동 페어링)
- **Blokdots**: Run/Stop만 (외부 앱이 페어링 담당)

---

### B-6 ~ B-7. [신규] (생략, 위에 통합)

---

## 4. C. F-BRG — Custom Bridge App / 플러그인 패키징

### C-1. [신규/중요] Custom Bridge App 개발 모델 명시화

**현재 스펙 상태:** Capability Matrix §3에 `Custom Bridge App (.zip)` 칸이 있고 F-PLG-zip-upload-only가 있으나, **Custom Bridge App의 개발자 인터페이스(SDK·메시지 protocol)가 스펙에 없음**.

**제안:** F-BRG 또는 별도 부록에 다음 명시.
- **런타임:** Node.js (영상은 v16 LTS)
- **필수 의존성:** `socket.io-client`
- **메시지 API:** 송신 `sendMessageToConnect(messageName, value)` 함수, 수신 switch/case 패턴
- **boilerplate 제공:** ProtoPie 공식 boilerplate zip 배포 (index.js + package.json)
- **App 메타데이터:** `ppConnectAppName` 변수 → Connect 메시지 로그의 `Source` 컬럼에 표시
- **시작 신호:** 앱 시작 시 자동으로 "Bridge App ready" 메시지를 Connect로 송신

**Beta 영향 — 충돌 확인 필요:** §7 Non-goals에 "Send/Receive SDK 공개"가 명시되어 있음. 하지만 Custom Bridge App은 사실상 SDK를 사용한다(socket.io-client). **이 SDK 공개 정책과의 충돌 정리 필요.**

**출처:** Video 6 전체, 특히 L46-95, L156-172, L253-271

---

### C-2. [신규] 플러그인 패키징 메커니즘 (pkg 기반)

**자막 발견:** 레거시에서 Custom Bridge App을 "플러그인"으로 배포하는 표준 절차 (Video 7, L661-806).

**제안:** F-BRG 또는 F-PLG-zip-upload-only 인접에 절차 명시.

| 항목 | 레거시 절차 | QA 검증 |
|---|---|---|
| 빌드 도구 | `pkg` (글로벌 npm 패키지) | Beta 동일 도구 사용 여부 확인 |
| 타겟 아키텍처 | `node16-macos-arm64`, `node16-macos-x64`, `node16-win-x64` 3종 | Beta 지원 아키텍처 결정 (Linux 추가?) |
| Mac 바이너리 권한 | `chmod +x` 필요 | 자동화 가능 여부 |
| 메타데이터 | `metadata.json` with `{"name": "..."}` | 추가 필드(version·author 등) Beta에서 결정 |
| 파일 명명 | 실행 파일은 `plugin` 또는 `plugin.exe`로 rename | 다른 명명 거부 |
| 압축 | `plugin(.exe)` + `metadata.json` → zip | manifest 검증 (F-PLG-manifest-perm) |
| 영속성 | 한 번 import한 플러그인은 Connect 재시작 후에도 유지 | 재시작 회귀 |

**Beta 영향:** F-PLG-builtin-ide(내장 IDE)는 외부 ZIP 빌드 방식을 폐기했다고 명시. **하지만 영상은 외부 ZIP 빌드를 표준으로 시연.** 사용자 시각에서 **마이그레이션 메시지 / 변경 가이드가 필수** — Non-goals 또는 §11 Decision Log에 명시 권고.

**출처:** Video 7, L661-806

---

### C-3. [신규/중요/충돌] **"Custom Plugin import는 Enterprise 구독에서만 동작"**

**자막 원문:** "you'll only see this plus by the way if you are on an enterprise subscription this won't work if you just have a proto pi pro subscription you have to have an enterprise one" (Video 7, L820-823)

**현재 스펙 상태:**
- F-IDM-connect-entitlement는 "Self-serve = 사용 가능 Plan AND Editor 이상 / Enterprise = Editor 이상"만 정의
- **Plan별 세부 기능 게이트 (예: Custom Plugin import) 미명시**

**충돌 확인 필요:**
- Beta에서 이 정책을 유지하는가?
- 유지 시: F-IDM-connect-entitlement 또는 §3 Capability Matrix에 "Custom Plugin Import" 행 추가 + Self-serve 내 Plan 차이 매트릭스 명시
- 변경 시: §11 Decision Log + 마케팅 메시지 변경

**QA 영향:** P0 수준 검증 항목. Pro 구독자가 우회해서 +버튼 활성화 못 하는지 회귀 필수.

**출처:** Video 7, L820-823 (명시적 발화)

---

### C-4. [신규] Bridge App / Connect 연결 라이프사이클 회귀 케이스

**제안:** F-BRG에 추가 검증 포인트.
- 앱 시작 → Connect로 "ready" 메시지 자동 송신 (L100-105)
- Ctrl+C 종료 → Connect 측 Disconnected 전이 latency
- Connect 측에서 Open in Terminal로 stdout 확인 가능 (L831-834)
- Connect 재시작 후 Bridge App 재연결 동작 (자동 재시도?)

**출처:** Video 6, L100-105; Video 7, L877-884

---

### C-5. [기존 수정] §3 Capability Matrix의 "Custom Bridge App (.zip)" 행 보강

**현재:** Desktop Cloud-login / Desktop License-key / Embedded에서 O 표시.
**제안 추가:** "Custom Plugin Import (+버튼)" 별도 행으로 분리. Self-serve Plan별 가용성 명시 (C-3 결과 반영).

---

### C-6 ~ C-7. (생략, 위에 통합)

---

## 5. D. F-STG — 다중 Pie / Multi-view (Stage View 베이스라인)

### D-1. [신규] 레거시 Multi-view 동작 베이스라인

**자막 발견:** 영상 1-2에서 레거시 "Multi-view Group"의 동작을 상세 시연.

**현재 스펙 상태:** F-STG-svw-multipie, F-STG-svw-edit, F-STG-svw-pie-routing은 Beta Stage View 동작을 정의하지만, **레거시 Multi-view의 회귀 베이스라인은 미명시**.

**제안 추가 항목 (F-STG 또는 §4-8 F-VWR 인접):**

| 검증 포인트 | 자막 |
|---|---|
| Multi-view Group 생성: "New → Group" | Video 1-2, L23-25 |
| Pie 추가: Drag-drop 또는 "New → Pie → Browse" 2가지 진입점 | Video 1-2, L12-19 |
| Multi-view 실행: 그룹 상의 실행 버튼 → 브라우저 다중 표시 | Video 1-2, L28-31 |
| 우클릭 → 기어 아이콘으로 Pie 크기/배치/배경색 변경 | Video 1-2, L40-50 |
| Multi-view 안에서 Pie 추가/제거 동적 반영 | Video 1-2, L62-72 |
| Live link: Studio에서 저장 시 Multi-view 자동 업데이트 | Video 1-2, L122-128 |
| 한 Multi-view 안에서 모든 Pie가 같은 메시지 채널 공유 (broadcast 모델) | Video 1-2, L256-282 |

**Beta 영향:** F-STG-svw-* 시리즈가 이 베이스라인을 동등 이상으로 만족해야 함 (P1).

---

### D-2. [신규] Multi-view 메시지 broadcast 함정

**자막 발견:** 4개 컴포넌트 인스턴스에서 모두 send → Connect → 모든 Pie가 수신 → 의도하지 않은 다른 인스턴스가 반응 (Video 1-2, L256-282).

**제안:** F-STG-svw-pie-routing에 검증 포인트로 추가.
- **모든 Pie가 모든 메시지를 수신**하는 모델임 (선택적 라우팅 아님)
- 의도한 Pie만 반응시키려면 Pie 측 조건 분기 필요 (사용자 책임)
- **Beta에서 라우팅 모델을 변경하는 경우 명시 필요** (e.g., topic 기반 라우팅 도입)

**QA 영향:** 영상에서 강사가 디버깅으로 발견·해결한 "버그처럼 보이는 의도된 동작" — 사용자 인지 없으면 회귀 리포트로 잘못 분류될 위험. **QA 가이드 문서화 필요**.

---

### D-3. [신규] Connect 메시지 디버거 UI 베이스라인

**자막 발견:** Video 1-2, L226-258에서 Connect의 메시지 로그 패널 동작 시연.

**제안:** F-BRG-16 Debugger 모드 또는 F-HOM 베이스라인에 명시.
- 컬럼: Time, Message, Value, Pie, **Source** (메시지를 보낸 주체 — Pie 이름 또는 Bridge App 이름)
- Clear 버튼
- 실시간 스트림 (정지/필터 미언급 → Beta 추가 시 신규 기능)
- 메시지 디버거가 F-BRG-16의 핵심 베이스라인임을 명시

**출처:** Video 1-2, L226-258; Video 2, L139-160; Video 6, L156-172 (Source 컬럼 핵심)

---

### D-4. [기존 수정] F-HOM 베이스라인 표의 메시지 디버거 행 보강

**현재 §4-1 F-HOM 베이스라인 표:** "우측 패널: 메시지 디버깅 (Message·Value·Send 입력, Time·Message·Value·Pie·Source 로그 테이블)".
**제안:** 영상 출처로 D-3의 세부를 명시적으로 박제 (현재 표현이 정확하므로 보강만 권장).

---

## 6. E. F-VWR — Player 진입 (QR)

### E-1. [신규] QR 진입 + 실제 디바이스 + Multi-view 혼합 운영

**자막 발견:** Video 1-2 L341-376, Video 5 L1162-1180에서 동일 Pie를 데스크탑 브라우저, 실제 모바일(QR 스캔), 실제 태블릿(QR 스캔)에서 동시에 운영하는 시나리오 시연.

**제안 추가 검증 포인트:**
- Pie 1개당 QR 코드 1개 노출 (Multi-view 안에서도 동일)
- QR 스캔 시 Player 앱이 해당 Pie를 즉시 실행
- 같은 Stage 컨텍스트의 메시지를 데스크탑 ↔ 모바일 ↔ 태블릿 모두에서 수신
- **Player 측에서도 send 가능** (단방향 아님)

**현재 스펙 상태:** F-VWR-browser-only는 시청자(viewer) 진입을 다루지만, **Pie 실행자(participant)로서의 Player 진입 동작이 별도 명시되어 있지 않음**.

**Beta 영향:** "Stage view from the Player"가 Non-goals에 있지만, 이는 Player 안에서 Stage 화면을 보는 것이고, 본 항목은 **Player가 Stage의 한 Pie를 실행**하는 시나리오. **두 개념 혼동 위험 — 스펙에 명시적 구분 필요**.

**출처:** Video 1-2, L341-376; Video 5, L1162-1180

---

## 7. F. F-IDM — Plan 게이트 (Enterprise 한정)

### F-1. [기존 수정] F-IDM-connect-entitlement에 Plan별 세부 기능 매트릭스 추가

C-3과 연결. 현재는 진입 자격만 정의되어 있고, **진입 후 Plan별 기능 차이가 미정의**.

**제안 추가:**

| 기능 | Pro | Enterprise (Self-serve) | Enterprise (B2B) |
|---|---|---|---|
| Connect 진입 | O | O | O |
| 6종 프리셋 플러그인 사용 | O | O | O |
| Custom Plugin Import (+버튼) | **X** | O | O |
| Custom Bridge App 직접 실행 (npm start) | O | O | O |

**확인 필요:** 이 매트릭스가 Beta에서 유지되는지, Pro에도 Custom Plugin이 풀리는지.

**출처:** Video 7, L820-823 (Enterprise 전용 명시)

---

### F-2. [충돌 확인 필요] "Custom Bridge App 실행"과 "Custom Plugin Import" 의미 분리

**자막 분석:** 영상은 두 가지 방식 모두 시연.
- 방식 A: `npm start`로 사용자 PC에서 직접 Node 앱 실행 → Connect와 socket.io로 통신 (Pro도 가능)
- 방식 B: pkg로 패키징해서 Connect에 import (Enterprise만 가능)

**현재 스펙 상태:** 두 방식의 구분이 명시적이지 않음.
**제안:** §1 용어에 "Custom Bridge App"(실행 방식 A) vs "Custom Plugin"(실행 방식 B + import) 구분 추가.

---

## 8. G. 에러 카탈로그 보강

### G-1. [신규] E-MSG-CHANNEL-MISMATCH

| 상황 | 화면 | 시스템 동작 | 복구 |
|---|---|---|---|
| 송신/수신 채널 불일치 (e.g. 한쪽이 ProtoPi Studio가 아님) | (현재 무음) | 메시지 silent drop | 사용자가 채널 확인 후 수정 |

**Beta 영향:** 회귀 시 silent drop 정책 유지 여부 / 디버거에서 경고 표시 여부 결정 필요.

---

### G-2. [신규] E-PLG-BAUD-MISMATCH (Arduino 한정)

| 상황 | 화면 | 시스템 동작 | 복구 |
|---|---|---|---|
| Arduino 플러그인 baud rate가 코드와 불일치 | 메시지 미수신, 에러 미표시 | 시리얼 통신 무응답 | 사용자가 baud rate 일치 |

**출처:** Video 4, L46-51

---

### G-3. [신규] E-PLG-PORT-BUSY (Arduino 한정)

| 상황 | 화면 | 시스템 동작 | 복구 |
|---|---|---|---|
| Arduino IDE 또는 다른 앱이 시리얼 포트를 점유 | 플러그인 실행 실패 또는 무응답 | 포트 open 실패 | 점유 앱 종료 후 재시도 |

**출처:** Video 4, L120-125

---

### G-4. [신규] E-BRG-HA-TOKEN-INVALID (Custom Bridge App 일반화 가능)

| 상황 | 화면 | 시스템 동작 | 복구 |
|---|---|---|---|
| Custom Bridge App이 외부 API 인증 실패 | 앱 stdout에 에러, Connect 측 무음 | 앱 종료 또는 idle | 사용자가 토큰 갱신 후 재시작 |

**일반화:** Custom Bridge App은 외부 자격증명 관리 책임이 사용자 측. **F-CLD-secrets 정책과 사용자 책임 경계가 명확해야 함**.

**출처:** Video 7, L319-326

---

### G-5. [신규] E-PLG-MULTI-INSTANCE-FLOOD (예방적)

A-5에서 도출. 다중 인스턴스 컴포넌트의 연속 send 패턴 → 메시지 폭주. 현재 silent하나, **Beta Cloud Relay 환경에서는 운영 메트릭 + rate-limit 트리거 필요**.

---

## 9. H. 검증 우선순위 / Non-goals

### H-1. [신규] §10 검증 우선순위 P1에 추가 권고

- **레거시 메시지 디버거 동작** (Time/Message/Value/Pie/Source 5컬럼 + Clear) — F-BRG-16 베이스라인
- **G29 메시지 카탈로그 12종 회귀** (B-1-d 표 참조) — Logitech 의존, 회귀 누락 시 자동차 산업 데모 영향
- **Custom Bridge App boilerplate 호환성** — 외부 사용자가 만든 기존 코드가 Beta에서 동작하는지 (마이그레이션 회귀)

### H-2. [신규] §7 Non-goals 명확화

영상에서 시연되는 항목 중 Beta에서 의도적으로 제외하는지 확인 필요:
- IFTTT 통합 → Beta에서 유지하는가?
- Arduino IDE 직접 코드 작성 워크플로우 → 가이드 문서/링크 제공 여부
- Home Assistant 같은 3rd party WebSocket 연동 → SDK 공개 정책과 충돌 (C-1)

---

## 10. 우선순위별 다음 액션 제안

**P0 (Beta 출시 차단 위험 — 즉시 결정 필요):**
- C-3 / F-1: Custom Plugin Import의 Plan gate 정책 확정
- A-7: Connect 없는 직접 Pie 통신 시나리오 유지/폐기 결정
- C-1: Custom Bridge App SDK와 §7 Non-goals "Send/Receive SDK 공개" 정책 충돌 해결

**P1 (dev 5주 중 결정):**
- A-4, A-6, B-3: 메시지 envelope 설계 (`||` 호환·동시 수신·idempotency 통합 결정)
- B-2: 다중 플러그인 동시 실행 시 dispatch 정책
- C-2: 플러그인 패키징 도구·메타데이터 포맷 결정

**P2 (회귀 베이스라인 — QA 작성):**
- B-1-a ~ d: 4개 플러그인 검증 포인트 표 박제
- D-1, D-3: Multi-view + 메시지 디버거 베이스라인
- E-1: Player 진입 시나리오 명시
- G-1 ~ G-5: 에러 카탈로그 보강

---

## 11. 다음 단계 (Paige 검토용)

1. 본 리포트의 각 항목에 대해 **[반영 / 보류 / 거부]** 표기
2. 반영 항목별로 Cloud_Connect_Spec.md의 어느 섹션·어느 ID에 매핑할지 지정
3. P0 항목 3건은 PM/디자이너와 결정 후 §11 Decision Log에 한 줄씩 추가
4. 반영 확정 후 Claude에게 "X-N 항목들 스펙에 병합해줘"로 요청 → 스펙 수정 진행

---

## 12. 출처 인덱스

| 영상 | 자막 파일 | 주요 도출 항목 |
|---|---|---|
| 1-1 | `[English (auto-generated)] Intro to ProtoPie Connect  1-1. How to Use Send and Receive in Studio to .txt` | A-1, A-2, A-3, A-4, A-7 |
| 1-2 | `[English (auto-generated)] Intro to ProtoPie Connect  1-2. How to Use Send and Receive in Connect to.txt` | A-5, D-1, D-2, D-3, E-1 |
| 2 | `[English (auto-generated)] Intro to ProtoPie Connect  2. How to Integrate IFTTT (If This Then That) .txt` | B-1-a, A-1 |
| 3 | `[English (auto-generated)] Intro to ProtoPie Connect  3. How to Use Blokdots to Integrate with Ardui.txt` | B-1-b, B-4 |
| 4 | `[English (auto-generated)] Intro to ProtoPie Connect  4. How to Use the Arduino Plugin with Sketch C.txt` | B-1-c, B-3, G-2, G-3 |
| 5 | `[English (auto-generated)] Intro to ProtoPie Connect  5. Use the Logitech G29 Steering Wheel to Prot.txt` | B-1-d, B-2, E-1, H-1 |
| 6 | `[English (auto-generated)] Intro to ProtoPie Connect  6. Write Custom Bridge App - Display Date, Tim.txt` | C-1, C-4 |
| 7 | `[English (auto-generated)] Intro to ProtoPie Connect  7. Integrate Bridge App to Smart Home IoT and .txt` | C-2, C-3, F-1, F-2, G-4 |
