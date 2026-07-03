# 📝 Legacy Connect

> Notion 최종본 아카이브 · 원본: https://app.notion.com/p/35745184b5da8008aed7debf75da454a
> Notion view 시점: 2026-05-05T08:56:01.692Z
> CoC 스쿼드 종료(2026-06-30) 인수인계용. 원본 마크다운(표 포함) 그대로 보존.

---

# 레거시 ProtoPie Connect 사용자 가시 기능 인벤토리
> 상태: 분석 완료<br>범위: `protopie-connect/` 레거시 사용자 가시 기능 47개<br>분석 방법: `protopie-connect/` 폴더 직접 코드 탐색 (server/ + desktop/)
---
## 1. 목적·범위·분석 방법
### 1-1. 본 문서의 목적
레거시 ProtoPie Connect의 사용자 가시 기능을 코드 분석으로 인벤토리화·문서화한다. 각 기능마다 동작 흐름·입출력 명세·상태·에러·코드 위치를 한 문서에 정리한다. 추측 없이 실제 파일을 읽어 확인된 사실만 담는다.
### 1-2. 범위
- **포함**: 사용자가 직접 보거나 사용하는 기능 (UI 화면·메뉴·CLI 명령·외부 API·하드웨어 통합)
- **제외**: 순수 내부 아키텍처·헬퍼·미들웨어. 빌드·CI·테스트 인프라
### 1-3. 분석 방법
`protopie-connect/` (server/ + desktop/)를 직접 탐색하여 사용자 가시 기능을 12 카테고리로 분류했다. 각 기능마다:
- **사용자가 어떻게 접근하는가** (UI route, HTTP API, Socket event, CLI flag/env)
- **어떤 동작이 일어나는가** (step-by-step flow)
- **무엇이 들어오고 나가는가** (입출력 schema)
- **어떤 상태가 저장되는가** (메모리·SQLite·파일·키체인 + TTL·동시성)
- **어떤 에러가 발생하는가** (timeout·retry·lockout·edge case)
- **어디에 코드가 있는가** (file\:line\:function)
- **알려진 quirk** (비명백한 동작·하드코드 값·의도 불명확)
일부 기능은 동작 요약·코드 위치 수준에서만 정리되어 있다 (추가 분석 여지 있음).
---
## 2. 카테고리별 인벤토리
### 2-1. 인증·접근 제어 (4개)
### AUTH-1. PIN 기반 원격 접근 인증
**한줄 요약**: 데스크톱 모드에서 원격 클라이언트가 PIN 인증을 통해 접근. 6자리 영숫자 PIN(예: ABC123)을 5분 내에 검증 → 64자 hex 토큰 발급.
**진입점**:<br>- UI route: `/auth-required` (Next.js 페이지)<br>- HTTP API: `POST /api/request-new-pin` (PIN 생성), `POST /api/validate-pin` (PIN 검증)<br>- Socket event: `socket.emit(SClientToClientEvent.PinDisplay, pinData)`, `socket.emit(SClientToClientEvent.PinAuthenticationSuccess)`
**모드**: desktop 전용
**동작 흐름**:<br>1. 원격 클라이언트가 `/api/request-new-pin` POST<br>2. `pinController.requestNewPin()` → `NetworkUtils.isLocalRequest()` 체크 (로컬이면 거부)<br>3. `PinManager.generatePin()` → 6자리 PIN (대문자 3자 + 숫자 3자 형식)<br>4. PIN 메모리 저장, `EVENT_PIN_GENERATED` 발행<br>5. PIN이 디스플레이에 30초 표시 (자동 숨김)<br>6. 클라이언트가 PIN 입력 후 `/api/validate-pin` POST<br>7. `PinManager.validatePin()` → 유효성 검사 (만료·일회용·rate limit)<br>8. 유효하면 `AuthTokenManager.generateToken()` (64자 hex 토큰)<br>9. 응답: 쿠키(`auth-token`) + JSON body에 토큰
**입력 명세**:<br>- HTTP POST `/api/request-new-pin`: 본문 없음 (클라이언트 IP는 헤더에서 추출)<br>- HTTP POST `/api/validate-pin`: `{ pin: "ABC123" }`
**출력 명세**:<br>- `/request-new-pin` 성공 (200): `{ success: true, message: "New PIN generated and sent to server display" }`<br>- `/request-new-pin` 로컬 실패 (400): `{ success: false, error: "PIN not required for local access" }`<br>- `/validate-pin` 성공 (200): `{ success: true, token: "64charHex", tokenInfo: { issuedAt, clientIp } }`<br>- `/validate-pin` 실패 (401): `{ success: false, error: "Invalid or expired PIN" }`<br>- Socket: `PinDisplay` 이벤트로 클라이언트에 PIN 전송
**상태·저장**:<br>- 메모리: `PinManager.currentPin` (string), `PinManager.pinGeneratedAt` (timestamp), `AuthTokenManager.tokens` (Map\<token, AuthToken\>)<br>- PIN TTL: 5분 (`PIN_EXPIRATION_TIME = 5 * 60 * 1000`)<br>- PIN 디스플레이 TTL: 30초 (자동 숨김)<br>- 토큰 TTL: 코드에 명시 안 됨, 쿠키 `maxAge: 365 * 24 * 60 * 60 * 1000` (365일)<br>- 토큰 제한: IP당 최대 5개 (초과 시 가장 오래된 토큰 자동 삭제)<br>- Rate limit: IP당 1분에 최대 5회 검증 시도
**에러·엣지**:<br>- Timeout: PIN 5분 만료 시 자동으로 `clearPin()` → 상태 초기화<br>- Retry: rate limit 시 1분 대기 후 재시도 가능<br>- Lockout: IP당 1분에 5회 초과 시 “Rate limit exceeded”<br>- 네트워크 단절: 토큰은 메모리 저장이므로 서버 재시작 시 모두 무효<br>- 일회용: PIN은 검증 후 `pinValidated = true` 플래그로 재사용 방지<br>- 로컬 우회: `NetworkUtils.isLocalRequest()` 검사로 로컬(127.0.0.1, 192.168.x.x) 요청은 PIN 불필요
**코드 위치**:<br>- `server/src/server/manager/PinManager.ts:10-442` — `PinManager` 클래스<br>- `server/src/server/manager/AuthTokenManager.ts:25-193` — `AuthTokenManager`<br>- `server/src/server/controllers/pin.controller.ts:7-234`<br>- `server/src/server/utils/NetworkUtils.ts:8-245` — `isLocalRequest()`, `getClientIP()`<br>- `server/src/pages/auth-required.tsx:1-127` — 인증 UI
**알려진 quirk**:<br>- PIN 형식 약함: 첫 3자는 항상 대문자, 뒤 3자는 항상 숫자 → 26³ × 10³ = \~176M 조합만<br>- AuthTokenManager의 IP 검증 느슨함 (line 76-82): IP 불일치 경고만, 실제는 `allow` (주석 “Could be stricter here”)<br>- 쿠키 `httpOnly: false` → 클라이언트 JS가 토큰 접근 가능 (XSS 위험)<br>- PIN 검증과 Cloud 세션은 별개 (PIN은 로컬 인증, Cloud 로그인은 SessionManager)
---
### AUTH-2. 인증 토큰 관리
**한줄 요약**: PIN 검증 후 발급한 토큰의 생명 주기 관리. 생성·검증·폐기·통계 조회를 HTTP API로 제공.
**진입점**:<br>- HTTP API: `GET /api/tokens` (활성 토큰 조회), `DELETE /api/tokens/:token` (특정 토큰 폐기), `DELETE /api/tokens/ip/:ip` (IP별 토큰 폐기), `DELETE /api/tokens` (전체 폐기) — 모두 로컬 접근만 (`requireLocalAccess`)<br>- Socket event: `EVENT_TOKEN_GENERATED`, `EVENT_TOKEN_REVOKED`
**모드**: desktop 전용
**동작 흐름**:<br>1. PIN 검증 성공 후 `AuthTokenManager.generateToken(clientIp, userAgent)`<br>2. `crypto.randomBytes(32).toString('hex')` → 64자 토큰<br>3. 토큰 객체: `{ token, clientIp, userAgent, issuedAt, lastAccessedAt, isActive }`<br>4. Map 저장: `this.tokens.set(token, authToken)`<br>5. 토큰 사용 시 `validateToken(token, clientIp)` → 활성 확인 + `lastAccessedAt` 업데이트<br>6. 폐기 시 `revokeToken(token)` 또는 `revokeTokensForIp(clientIp)` → Map에서 삭제
**입력 명세**:<br>- HTTP GET `/api/tokens`: 쿼리 없음<br>- HTTP DELETE `/api/tokens/:token`: URL path에 토큰<br>- HTTP DELETE `/api/tokens/ip/:ip`: URL path에 IP<br>- HTTP DELETE `/api/tokens`: 본문 없음
**출력 명세**:<br>- GET 성공: `{ success: true, tokens: [...], stats: { totalTokens, uniqueIps, expiredTokens } }`<br>- DELETE/:token 성공: `{ success: true, message: "Token revoked successfully" }`<br>- DELETE/:token 실패 (404): `{ success: false, message: "Token not found" }`<br>- DELETE/ip/:ip 성공: `{ success: true, message: "...", revokedCount: N }`
**상태·저장**:<br>- 메모리: `AuthTokenManager.tokens` (Map\<string, AuthToken\>)<br>- TTL: 명시적 만료 없음 (서버 재시작 시 소실)<br>- 동시성: 단일 Process Node.js이므로 문제 없음
**에러·엣지**:<br>- 존재하지 않는 토큰: 검증 실패<br>- IP 불일치: 경고만 로그 (보안 느슨)<br>- 토큰 제한: IP당 5개 초과 시 가장 오래된 토큰 삭제
**코드 위치**:<br>- `server/src/server/manager/AuthTokenManager.ts:25-193`<br>- `server/src/server/routes/token.routes.ts:1-91`
**알려진 quirk**:<br>- `expiredTokens` 필드는 항상 0 (TTL 메커니즘 없음)<br>- IP 검증 선택적 (주석 참고)
---
### AUTH-3. ProtoPie Cloud 세션 인증
**한줄 요약**: 사용자가 ProtoPie Cloud 계정으로 로그인 → Cloud 서버에서 사용자·플랜 정보 조회 → 로컬 DB(Sequelize) 세션 저장 (1주 유효).
**진입점**:<br>- HTTP API: `POST /api/login` (로그인), `GET /api/session` (세션 확인)<br>- Socket event: `SessionManager.EVENT_CONNECT_LOGIN`, `EVENT_CONNECT_LOGOUT`
**모드**: desktop / server
**동작 흐름**:<br>1. 클라이언트가 로그인 UI에서 email/password 또는 token 입력<br>2. `POST /api/login`: `{ email, password, token, host, hostPlan }`<br>3. `loginController.login()`:<br>- 기존 세션 있으면 `clearSession()`<br>- `CloudServerRequester` 인스턴스화 (host)<br>- Token 없으면 email/password로 `/auth` 호출하여 token 획득<br>- Token으로 Cloud `/me` 호출, 사용자 정보 획득<br>- `checkUserPlan()` (deleted/deactivated/expiresAt 체크)<br>4. `sessionManager.createSession()`:<br>- 세션 객체: `{ host, token, featureType, expiresAt, fullName, email, ... }`<br>- `SSessionController.create()` → DB INSERT<br>- `loginTime` = now, `logoutTime` = now + 1주<br>5. 응답: 세션 + `featureLimits` (Free/Pro/Enterprise)
**입력 명세**:<br>- HTTP POST `/api/login`:<br>`json   { "email": "user@example.com", "password": "pass", "token": "optional_token",     "host": "https://cloud.protopie.io", "hostPlan": "team-cloud" | "enterprise-cloud" }`
**출력 명세**:<br>- 200: `{ session: { id, email, fullName, featureType, expiresAt, ... }, featureLimits: {...} }`<br>- 400/401/500: `{ message: "error details" }`
**상태·저장**:<br>- 메모리: `SessionManager.session` (SessionAttribute 객체)<br>- DB: `SSession` 테이블 (Sequelize ORM)<br>- TTL: 1주 (`EXPIRATION_TERM = 7 * 24 * 60 * 60 * 1000`)<br>- 만료 체크: 초기화 시 `checkSessionExpiration()` → 만료 시 자동 `clearSession()`
**에러·엣지**:<br>- Cloud 서버 연결 실패: `CloudRequestError` (proxy 설정 고려)<br>- Token 만료: Cloud에서 401 → 로그인 실패<br>- 플랜 검증 실패: Free 플랜으로 강등, 기능 제한 적용<br>- 네트워크 단절: `ProxyManager.getProxyUrl()`로 우회 시도
**코드 위치**:<br>- `server/src/server/manager/SessionManager/SessionManager.ts:41-266`<br>- `server/src/server/controllers/login.controller.ts:19-166`<br>- `server/src/server/controllers/controllerUtils/login.controller.utils.ts` (플랜 검증)
**알려진 quirk**:<br>- 라이선스 vs 세션: 서버 모드에서는 Cloud 세션 대신 로컬 라이선스 (`LicenseManager`)<br>- ProPlan 라이트: `hostPlan.includes('team-cloud')` 체크로 “ConnectLite” 판별 (line 33-39)<br>- 세션 만료 후: 만료된 세션은 체크만, 실제 로그아웃은 사용자 요청 시<br>- 기존 세션 자동 삭제: 로그인 시 이전 세션 무조건 덮어씀
---
### AUTH-4. 라이선스 검증
**한줄 요약**: 서버 모드(embedded) 전용. 라이선스 파일(.lic) 읽기 → AES 복호화 → device ID·만료일 검증 → 유효 라이선스 없으면 10분 후 서버 종료.
**진입점**:<br>- CLI/Env: 시작 시 `LicenseManager.init()` + `loadLicense(licenseFileDir)`<br>- 환경변수: `LICENSE_KEY`, `DEVICE_ID`, `RUNMODE=server`
**모드**: server (embedded 라이선스 모드 전용)
**동작 흐름**:<br>1. 서버 시작 시 `SessionManager.init({ runMode: 'server', licenseFileDir, version })`<br>2. `LicenseManager.init()`:<br>- `node-machine-id` → 머신 ID<br>- SHA256 해시 첫 10자 대문자 → device ID (`ABCD123456`)<br>- `process.env.DEVICE_ID`에 저장<br>3. `loadLicense(licenseFileDir)`:<br>- 디렉토리에서 “license” 포함 파일 찾기<br>- `PieExtractor.decryptString()` AES 복호화<br>- JSON 파싱: `{ deviceId, userName, expireDate }`<br>- Device ID 일치 + 미만료 검증<br>- 가장 만료일이 늦은 것 선택<br>4. 유효 라이선스 없으면: 상태 = ‘Trial’ → 10분 타이머 → `process.exit(0)`<br>5. 유효 라이선스 있으면: 상태 = ‘Valid’, 로그 `Licensed to [userName] until [expireDate]`
**입력 명세**:<br>- 라이선스 파일 (암호화 JSON): `{ deviceId, userName, expireDate }`<br>- 환경변수: `LICENSE_KEY=<encrypted_string>`
**출력 명세**:<br>- 유효: `{ state: 'Valid', deviceId, userName, expireDate }`<br>- 무효: `{ state: 'Trial', deviceId: null, expireDate: null }`
**상태·저장**:<br>- 메모리: `LicenseManager._state`, `_deviceId`, `_expireDate`<br>- TTL: 라이선스 만료일까지<br>- Trial 타이머: 10분 → `setTimeout(() => process.exit(0), 10 * 60 * 1000)`
**에러·엣지**:<br>- Device ID 불일치: 라이선스 무효<br>- 라이선스 만료: 무효 (Trial 모드, 10분 후 종료)<br>- 복호화 실패: 해당 파일 스킵<br>- 파일 없음: 경고 로그 후 Trial
**코드 위치**:<br>- `server/src/server/manager/LicenseManager.ts:11-218`<br>- `server/src/server/manager/SessionManager/SessionManager.ts:56-106` (init 로직)
**알려진 quirk**:<br>- Device ID 해싱 SHA256 첫 10자만 → 완전 unique 아님<br>- stderr 억제 코드 (코드 smell)<br>- 파일명 검색은 “license” 문자열 포함 여부만 (확장자 무관)<br>- 암호화 키 하드코딩 (코드 확인 필요)
---
### 2-2. 플러그인 시스템 (4개)
### PLG-1. IFTTT 플러그인
**한줄 요약**: IFTTT 웹훅 통합. webhook key + 트리거 이벤트 이름 + JSON payload 저장 → ProtoPie 메시지 이벤트 시 IFTTT 웹훅 POST.
**진입점**:<br>- HTTP API: `GET /api/builtin-plugins/ifttt`, `PUT /api/builtin-plugins/ifttt`<br>- Socket event: 설정 변경 시 `EVENT_IFTTT_CHANGED` 발행
**모드**: desktop / server (plan 기반 활성화)
**동작 흐름**:<br>1. 클라이언트가 IFTTT 설정 UI에서 webhook key 입력<br>2. `PUT /api/builtin-plugins/ifttt`: `{ webhookKey, eventNameForTest, jsonPayloadForTest, iftttEvents: [...] }`<br>3. `IftttPluginManager.setIftttPluginSetting()`:<br>- 기존 설정 있으면 `update()`, 없으면 `create()`<br>- 기존 이벤트 삭제 후 새 이벤트 INSERT<br>4. 런타임에 ProtoPie 메시지 이벤트 발생:<br>- 설정된 `eventNameForTest`와 메시지 ID 매칭<br>- IFTTT 웹훅: `POST https://maker.ifttt.com/trigger/{eventName}/with/key/{webhookKey}` + JSON payload
**입력 명세**:<br>- HTTP PUT body:<br>`json   { "webhookKey": "abc123def456",     "eventNameForTest": "test_event",     "jsonPayloadForTest": "{\"value1\": \"test\"}",     "isUsingArbitraryJsonForTest": false,     "iftttEvents": [       { "name": "button_press", "message": "button_click", "isUsingArbitraryJson": false }     ] }`
**출력 명세**:<br>- GET 성공: 전체 IFTTT 설정 객체<br>- PUT 성공: `{ result: 'ok' }`
**상태·저장**:<br>- DB: `SIftttPluginSetting` + `SIftttPluginEvent` (Sequelize)<br>- TTL: 없음
**에러·엣지**:<br>- 웹훅 실패: 코드에서 직접 처리 없음 (런타임 구현 필요)<br>- Webhook key 누락: 저장되나 전송 불가<br>- JSON 파싱 실패: 코드에서 직접 처리 없음
**코드 위치**:<br>- `server/src/server/manager/BuiltInPluginManager.ts:11-36` (IftttPluginManager)<br>- `server/src/server/model/DataModel/SIftttPlugin.ts:15-208`
**알려진 quirk**:<br>- 테스트 전송: UI에 “Test Event” 있지만 실제 트리거 로직은 별도 (런타임)<br>- `isUsingArbitraryJsonForTest` 사용 방식 불명확
---
### PLG-2. API 플러그인
**한줄 요약**: 사용자 정의 HTTP 엔드포인트로 ProtoPie 이벤트 → 임의 API 호출. JSON 파일 기반 설정 저장.
**진입점**:<br>- HTTP API: `GET /api/builtin-plugins/api`, `PUT /api/builtin-plugins/api`
**모드**: desktop / server
**동작 흐름**:<br>1. 클라이언트가 API 플러그인 UI에서 설정 추가:<br>- 이름, GET/POST 메서드, URL, headers, body<br>- 메시지 매칭: `messageFromPie` (수신), `messageToPie` (전송)<br>- 옵션: 메시지 값으로 URL/headers/body 오버라이딩<br>2. `PUT /api/builtin-plugins/api` 호출<br>3. `ApiPluginManager.setApiPluginSetting()` → JSON 파일 저장<br>4. 런타임에 메시지 이벤트:<br>- 설정된 `messageFromPie`와 매칭<br>- URL·headers·body에 메시지 값 대입 (옵션)<br>- HTTP 요청 전송<br>- 응답 받으면 `messageToPie` 메시지 발행
**입력 명세**:<br>- HTTP PUT body:<br>`json   { "modelVersion": 1,     "settings": [{       "id": "uuid", "isFolded": false, "name": "My API",       "method": "post", "url": "https://api.example.com/webhook",       "header": "Content-Type: application/json",       "body": "{\"event\": \"test\"}",       "messageFromPie": "send_event", "messageToPie": "api_response",       "overrideWithMsgValue": true, "overridingProp": "body"     }] }`
**출력 명세**:<br>- GET 성공: 전체 API 설정 객체<br>- PUT 성공: 저장 확인
**상태·저장**:<br>- 파일 저장: JSON 파일 (위치 코드 확인 필요)<br>- Zod 스키마 검증: `settingItemSchema` (lines 6-22)<br>- TTL: 없음<br>- 기본값: 새 설정 생성 시 기본 템플릿 (lines 37-54)
**에러·엣지**:<br>- JSON 파일 손상: 파싱 실패 시 기본값 초기화<br>- HTTP 요청 실패: 코드 추론 필요
**코드 위치**:<br>- `server/src/server/manager/BuiltInPluginManager.ts:38-61` (ApiPluginManager)<br>- `server/src/server/model/JsonModel/SApiPlugin.ts:1-59`
**알려진 quirk**:<br>- 메시지 라우팅 별도 구현 (모델은 메타정보만)<br>- JSON 파일 기반 → 동시 편집 문제 가능
---
### PLG-3. 커스텀 플러그인 (.zip)
**한줄 요약**: 사용자 .zip 패키지(바이너리 + metadata.json) 업로드 → 별도 프로세스 실행 → 표준입출력으로 통신. 세션당 실행 수 제한 (Free 1, Pro 3, Enterprise 무제한).
**진입점**:<br>- HTTP API: `POST /api/plugin/upload` (multipart/form-data)<br>- Socket event: 플러그인 stdout → `socket.emit(...)`<br>- 페이지: `/plugin/[pluginId]/terminal.tsx` (터미널/로그)
**모드**: desktop / server (plan 기반)
**동작 흐름**:<br>1. `.zip` 파일 업로드 (multipart)<br>2. `uploadCustomPlugin()`:<br>- Multer 파일 수신<br>- ZIP 검증<br>- Replace 모드 여부 (pluginId 쿼리 있으면 교체)<br>3. `CustomPluginManager.addCustomPlugin(userId, buffer)`:<br>- 새 plugin ID 생성<br>- `CustomPluginFileUtil.unzipAll()`: ZIP 압축 해제<br>- `plugin` (바이너리), `metadata.json` 검증<br>- 리눅스/맥: chmod 755 실행 권한<br>- `metadata.json` 읽기: `{ name: "Plugin Name" }`<br>- `SCustomPluginController.create()` → DB 저장<br>- `SCustomPluginProcess` 인스턴스 생성<br>4. 메시지 이벤트 시 `runCustomPlugin(id)`:<br>- 플러그인 바이너리 실행 (`child_process`)<br>- 표준입출력으로 메시지 송수신<br>5. 삭제: `deleteCustomPlugin(id)` → 프로세스 종료 + 파일 삭제 + DB DELETE
**입력 명세**:<br>- HTTP POST `/api/plugin/upload` (multipart/form-data):<br>- `file=<.zip>`, `pluginId=<optional_id>` (교체 모드)<br>- ZIP 구조: `plugin.exe (or plugin)` + `metadata.json` (`{ "name": "My Plugin" }`)
**출력 명세**:<br>- 성공: `{ result: 'ok' }`<br>- 실패 (400): 파일 오류·구조 오류
**상태·저장**:<br>- 파일: `{pluginDir}/{pluginId}/`<br>- DB: `SCustomPlugin` (id, name, dirPath, filePaths, UserId, orderInUser)<br>- 프로세스 메모리: `CustomPluginManager._customPluginProcesses` (Map)<br>- TTL: 없음 (명시 삭제까지)<br>- 제한: Plan별 동시 실행 수 (Free 1, Pro 3, Enterprise 무제한)
**에러·엣지**:<br>- ZIP 손상: `CustomPluginError` (ExtractError)<br>- 파일 누락: NoNecessaryFileError<br>- chmod 실패: ChmodError<br>- 디렉토리 생성 실패: MakePluginDirectoryError<br>- 프로세스 실행 실패: RunPluginError<br>- Orphan 정리: 시작 시 DB에는 없지만 파일 시스템에 남은 플러그인 자동 삭제
**코드 위치**:<br>- `server/src/server/manager/CustomPluginManager.ts:50-650`<br>- `server/src/server/controllers/plugin.controller.ts:12-91`<br>- `server/src/pages/plugin/[pluginId]/terminal.tsx`
**알려진 quirk**:<br>- 임시 디렉토리: 교체 시 기존을 `temp{id}`로 이름 변경 후 새 업로드 실패 시 복구<br>- Orphan 정리는 시작 시에만 (런타임 감지 없음)<br>- 통신은 표준입출력만 (IPC 없음)
---
### PLG-4. 외부 Bridge App 연동 (Blokdots 등)
**한줄 요약**: Socket.IO로 Blokdots 같은 외부 앱이 연결 → Bridge App 목록 관리 → 메시지 라우팅.
**진입점**:<br>- Socket.IO 자동 감지 (클라이언트의 `connect` 이벤트)<br>- 메시지: `socket.on(ClientToSocketConnectionEvent.PPBridgeApp, ...)`
**모드**: desktop / server
**동작 흐름**:<br>1. 외부 Bridge App이 Socket.IO 연결<br>2. `SocketManager.authenticateMultiViewSocket(socket)` (인증 체크)<br>3. `SBridgeApp` 인스턴스: `new SBridgeApp(socket, name)`<br>4. `BridgeAppManager.addBridgeApp(app)` → 내부 배열 추가, `EVENT_CHANGED` 발행<br>5. `SClient.notifyBridgeApps()` → 클라이언트에 `SClientToClientEvent.BridgeApps` emit<br>6. 메시지 라우팅: ProtoPie ↔︎ Bridge App 양방향
**입력 명세**:<br>- Socket.IO 연결: 일반 Socket.IO 클라이언트<br>- 메시지: `{ messageId: "...", value: "..." }`
**출력 명세**:<br>- Bridge App 목록: `{ name: "blokdots", ... }`<br>- 메시지 라우팅: `socket.emit(..., message)`
**상태·저장**:<br>- 메모리: `BridgeAppManager._bridgeApps` (배열)<br>- TTL: 없음 (연결 유지)
**에러·엣지**:<br>- 인증 실패: 연결 거부<br>- 연결 해제: 자동 `removeBridgeApp()` (코드 추론)
**코드 위치**:<br>- `server/src/server/manager/BridgeAppManager.ts:6-52`<br>- `server/src/server/model/SBridgeApp.ts:1-41`<br>- `server/src/server/model/SClient.ts` (notifyBridgeApps)
**알려진 quirk**:<br>- 기본 이름 `'unnamed-bridge-app'`<br>- `BridgeAppManager.getBlokdots()` 메서드로 Blokdots 필터링
---
### 2-3. 클라우드·네트워크 (4개)
### CLD-1. ProtoPie Cloud .pie 다운로드
**한줄 요약**: Cloud에서 .pie 파일 다운로드 (진행률 추적 + 재시도). Socket과 HTTP 이중 통신.
**진입점**:<br>- UI: `CloudFinder.tsx` — Cloud 프로토타입 선택 후 “열기”<br>- HTTP API: `GET /api/pies/addCloud?pieId=&cloudPieId=`<br>- Socket event: `downloadCloudPie(cloudPies: CloudFinderPie[])` (desktop → server)
**모드**: server / desktop
**동작 흐름**:<br>1. CloudFinder에서 Cloud 프로토타입 선택<br>2. Desktop이 SocketIO `downloadCloudPie` 이벤트 발송<br>3. Server `addCloudPieFile()`: DB에 임시 .pie 추가 (`isTemp=true`)<br>4. `CloudPieDownloadManager.downloadCloudPie()`:<br>- URL: `{cloudHost}/api/v3/pies/{pieId}/revisions/{lastRevisionNo}/studio.pie`<br>- Bearer 토큰, Proxy 적용<br>5. 바이너리 다운로드 중 `Content-Length` 기반 진행률 → `onProgress` 콜백<br>6. 완료 시 임시 디렉토리에 `.pie` 저장<br>7. 동시에 썸네일 다운로드 (HTTP GET, 파일 스트림)<br>8. DB의 `isTemp` 플래그를 false로 변경<br>9. 실패 시 `NoContentRetryDownload` 자동 재시도 (1회)
**입력 명세**:<br>- HTTP `GET /api/pies/addCloud?pieId=123&cloudPieId=456`<br>- Headers: `Authorization: Bearer {token}` (SessionManager)<br>- Socket: `event: 'downloadCloudPie'`, `payload: { cloudPies: CloudFinderPie[] }` (id, name, thumbnailUrl, lastRevisionNo)
**출력 명세**:<br>- HTTP: 200 `{ result: "ok" }` 또는 4xx/5xx<br>- Socket emit: `pieDownloadProgress { pieId, percent, loaded, total }`, `pieDownloadComplete { pieId, success }`<br>- Side effect: SQLite SPie INSERT/UPDATE, 파일 `{tempCloudPiesDir}/{pieId}.pie`, 썸네일 `{piesDir}/{pieId}/thumbnail/*.png`
**상태·저장**:<br>- 메모리: `_progresses` (Map), `_downloaders` (진행 중 객체)<br>- SQLite: SPie, SCloudPieInfo<br>- 파일: 로컬 .pie (임시 → 최종)<br>- TTL: 임시 → 최종 즉시 이동, 만료 없음<br>- 동시성: 다운로드별 독립 객체, 멀티플 동시 가능
**에러·엣지**:<br>- Timeout: 60초 (proxy-agent 기본)<br>- Retry: Content-Length 0일 경우만 1회 자동<br>- 네트워크 단절: HTTP 에러 → Socket 이벤트로 클라이언트에 전파, UI 취소 가능<br>- 잘못된 입력: Cloud API에서 pieId 없으면 CloudRequestError (“Incorrect CloudPie ID or No access permission”)
**코드 위치**:<br>- `server/src/server/manager/PieManager/CloudPieDownloadManager.ts:297-363` — `downloadCloudPie()` 매니저<br>- `server/src/server/manager/PieManager/CloudPieDownloadManager.ts:155-256` — 다운로드 로직<br>- `server/src/server/controllers/pies.controller.ts:190+` — `addCloudPieFile()` 컨트롤러<br>- `server/src/server/routes/api.ts:92-98` — 라우트
**알려진 quirk**:<br>- 썸네일 URL 하드코드 패턴<br>- 썸네일 다운로드 실패해도 전체 다운로드 진행 (에러 무시)<br>- `preventCancel()` 메서드 (의도 불명확)<br>- 진행률 콜백은 다운로드 중만, 썸네일 진행률 미전송
---
### CLD-2. Cloud 팀·프로젝트 관리
**한줄 요약**: Cloud API를 프록시하여 팀/프로젝트 계층 조회 + 신규 프로젝트 생성.
**진입점**:<br>- HTTP API:<br>- `GET /api/cloud/me/teams` — 사용자 팀 목록<br>- `GET /api/cloud/me/projects` — 사용자 프로젝트<br>- `GET /api/cloud/teams/{teamId}/projects` — 팀 내 프로젝트<br>- `POST /api/cloud/teams/{teamId}/projects` — 신규 프로젝트<br>- `GET /api/cloud/pies/{pieId}/revisions` — 파이 리비전
**모드**: server
**동작 흐름**:<br>1. 클라이언트가 `/api/cloud/me/teams` GET<br>2. `cloud.controller.ts:getMyTeams()` 진입<br>3. `createTaskForRequestToCloud<CloudTeamsResponse>()`:<br>- SessionManager에서 host, token<br>- UserManager에서 userId (로그인 확인)<br>- ProxyManager에서 proxy URL<br>4. `CloudServerRequester` 생성, Cloud API GET:<br>- URL: `{cloudHost}/api/v2/me/teams{?size,offset}`<br>- Headers: `Authorization: Bearer {token}`<br>- Proxy: proxy-agent<br>5. Cloud API 응답을 그대로 클라이언트에 (200 JSON)<br>6. 프로젝트 생성 시 POST body를 Cloud로 전달
**입력 명세**:<br>- `GET /api/cloud/me/teams?size=20&offset=0`<br>- `POST /api/cloud/teams/123/projects` + body `{ name, description }`
**출력 명세**:<br>- 200: `{ teams: [...] }` 또는 `{ projects: [...] }` (Cloud API 구조)<br>- 401: `{ code: 'NOT_LOGIN' | 'INVALID_AUTH_TOKEN', message }`<br>- 500: Cloud API 또는 네트워크 오류
**상태·저장**:<br>- SessionManager 세션 유지 (token, host)<br>- ProxyManager 사용자별 proxy 설정<br>- DB 영향 없음 (Cloud가 진실)
**에러·엣지**:<br>- 로그인 미필: `NotFoundSessionError` → 401<br>- 세션 만료: Cloud 401 반환 → 클라이언트가 재로그인 처리<br>- Proxy 오류: 재시도 로직 없음, 오류 전파<br>- 네트워크: 타임아웃·DNS 오류 → CloudRequestError
**코드 위치**:<br>- `server/src/server/controllers/cloud.controller.ts:117-381` — 컨트롤러 팩토리<br>- `server/src/server/routes/cloud.ts:11-54` — 라우트<br>- `server/src/server/controllers/controllerUtils/CloudServerRequester.ts` — HTTP 클라이언트
**알려진 quirk**:<br>- `createTaskForRequestToCloud<T>()` generic 함수, `req.method`로 GET/POST 자동 감지<br>- API 버전: v2 (기본), v3 (hashify에만)<br>- `createQueryString()` 헬퍼로 쿼리 구성 (중복 방지)<br>- 에러 응답 시 `from: req.baseUrl + req.path` (디버깅용)
---
### CLD-3. Proxy 설정·테스트
**한줄 요약**: 사용자 프록시 설정(없음/시스템/수동)을 DB에 저장 + 테스트 요청으로 검증.
**진입점**:<br>- HTTP API: `POST /api/proxy-test`
**모드**: server
**동작 흐름**:<br>1. 클라이언트가 proxy 폼 제출 (type, protocol, host, port, username, password)<br>2. `proxy-test.controller.ts:getProxyTestResult()`<br>3. UserManager에서 userId<br>4. ProxyType 변환:<br>- 0 NoProxy → DB null<br>- 1 SystemProxy → 시스템 명령 (scutil on macOS, PowerShell on Windows)<br>- 2 ManualProxy → 사용자 입력<br>5. ManualProxy:<br>- PAC: `pac+{url}`<br>- HTTP/HTTPS: `{protocol}://{user:pass@}host:port`<br>- 포트 검증 (0-65535)<br>6. 테스트: `HTTPClient.get('https://www.protopie.io/', { proxy, timeout: 60s })`<br>7. 성공 시 DB 저장: `{ result: true, proxy: proxyUrl }`<br>8. 실패: `{ result: false, proxy: null }`
**입력 명세**:<br>- `POST /api/proxy-test` body:<br>`typescript   { type: 0|1|2, protocol?, host?, port?, username?, password? }`
**출력 명세**:<br>- 200: `{ result: boolean, proxy: string | null }`<br>- Side effect: SUser.proxy 컬럼 업데이트
**상태·저장**:<br>- SQLite: SUser.proxy (String, nullable) — `http://user:pass@proxy.com:8080`<br>- 메모리: ProxyManager._proxyUrl 캐시
**에러·엣지**:<br>- SystemProxy 조회 실패: Unix 명령 오류 → resolve(null) 기본값<br>- 포트 범위 오류: return null, DB 미저장<br>- 인증 정보 누락: `isAuth && username.length > 0 && password.length > 0` 체크<br>- 테스트 URL 고정 (`https://www.protopie.io/`)<br>- 연결 타임아웃: 60초
**코드 위치**:<br>- `server/src/server/controllers/proxy-test.controller.ts:15-90`<br>- `server/src/server/manager/ProxyManager.ts:46-138` — proxy URL 생성<br>- `server/src/server/manager/ProxyManager.ts:140-204` — 시스템 proxy 조회
**알려진 quirk**:<br>- SystemProxy 로직 macOS/Windows만 (Linux 없음)<br>- PAC 프로토콜 (`pac+` 접두사) proxy-agent 지원 여부 확인 필요<br>- 테스트 실패해도 DB 이전 값 유지 (롤백 없음)<br>- 에러 로깅만, 사용자 피드백 없음 (try-catch 흡수)
---
### CLD-4. 네트워크 정보·접근 제어
**한줄 요약**: 클라이언트 로컬/원격 접근 여부 판단 + 네트워크 정보(IP, 접근 유형) 반환.
**진입점**:<br>- HTTP API: `GET /api/network/access-info`, `GET /api/network/health`
**모드**: server
**동작 흐름**:<br>1. 클라이언트 `/api/network/access-info` GET<br>2. `NetworkController.getAccessInfo()` 진입<br>3. `NetworkUtils.getNetworkInfo(req)`:<br>- 클라이언트 IP: req.ip 또는 X-Forwarded-For<br>- 로컬 IP 판단: `isLocalIP(clientIP)` (127.x, ::1, 192.168.x, 10.x, 172.16-31.x)<br>- Proxy 헤더 감지: X-Forwarded-For, X-Real-IP<br>4. 서버 IP: req.socket.localAddress<br>5. 응답:<br>`typescript    { isLocalAccess, clientIp, serverIp, accessType: 'local'|'remote',      networkInfo: { isPrivate, isLoopback, proxyHeaders, rawIP },      timestamp }`
**입력 명세**:<br>- `GET /api/network/access-info`<br>- Headers: 자동 (Express req)
**출력 명세**:<br>- 200: `{ isLocalAccess, clientIp, serverIp, accessType, networkInfo, timestamp }`<br>- 500: `{ error, isLocalAccess: false, clientIp: 'unknown', ... }`
**상태·저장**:<br>- 메모리 없음 (stateless)
**에러·엣지**:<br>- req.socket/req.connection 없음: serverIp = ‘0.0.0.0’ 폴백<br>- IP 파싱 실패: 500, isLocalAccess=false (보안 기본값)<br>- Proxy 뒤: X-Forwarded-For 첫 IP 사용
**코드 위치**:<br>- `server/src/server/controller/network.controller.ts:13-47`<br>- `server/src/server/utils/NetworkUtils.ts` — IP 판단 로직
**알려진 quirk**:<br>- 서버 IP 추출 “best effort” (복잡 네트워크에서 부정확)<br>- 로컬 판단이 ClientIP 기반만 (DNS rebind 방어 없음)<br>- 기본값 false (거부 안전)
---
### 2-4. 미러링·Stageview (5개)
### MIR-1. Web Player (브라우저 미러링)
**한줄 요약**: Express API로 현재 연결된 Web Player 목록 + hotspot hints 토글 제공.
**진입점**:<br>- HTTP API: `GET /webplayer`<br>- UI route: 브라우저 기반 Web Player
**모드**: server / desktop / cloud 전부
**동작 흐름**:<br>1. `GET /webplayer`<br>2. `WebplayerController` SessionManager에서 현재 세션<br>3. `WebPlayerManager.option(hotspotHints)` 상태 반환<br>4. Voice config 병합 → `HttpWebPlayerResponse` 응답<br>5. Web Player 클라이언트가 response로 초기 상태 설정
**입력 명세**:<br>- `GET /webplayer` (Headers: standard Express, Body: 없음)
**출력 명세**:<br>- 200: `{ email, username, hotspotHints, voiceLanguage, voiceEnabled }`
**상태·저장**:<br>- 메모리: `WebPlayerManager.option` (hotspotHints boolean)<br>- TTL: 없음 (세션 지속)<br>- 동시성: EventEmitter `EVENT_CHANGED`
**에러·엣지**:<br>- 세션 없음: `email: ''`, `username: ''`<br>- Voice config 파일 부재: 기본값<br>- 에러: 500
**코드 위치**:<br>- `server/src/server/manager/WebPlayerManager.ts:58-62` — `updateHotspotHints()`<br>- `server/src/server/routes/webplayer.ts:17`<br>- `server/src/server/controllers/webplayer.controller.ts:13-32`
**알려진 quirk**:<br>- hotspotHints는 global state (모든 Web Player 공유)<br>- Voice config 별도 유틸 함수
---
### MIR-2. USB Android 미러링
**한줄 요약**: adbkit으로 ADB over USB Android 감지 + PpRpc 프로토콜 통신, 포트 포워딩(19981+)으로 TCP 터널링.
**진입점**:<br>- System: ADB daemon (`adb` 또는 `adb.exe`)<br>- USB: Android 기기 USB 연결<br>- Protocol: PpRpc (custom binary)
**모드**: desktop / server (USB 하드웨어 접근 필요)
**동작 흐름**:<br>1. `AdbPlayerChannelManager.start()`: adbkit client (localhost:5037)<br>2. Installed ADB 실패 시 번들 바이너리 (`BIN_PATH/adb` or `BIN_PATH/adb.exe`)<br>3. `adbClient.trackDevices()` → add/remove 이벤트<br>4. Device add: `_getAvailableLocalPort()` → 19981부터 순차 (최대 100번)<br>5. `adbClient.forward(deviceId, 'tcp:LOCAL_PORT', 'tcp:9981')` (포트 포워딩)<br>6. `net.connect()` localhost:LOCAL_PORT (1초 재시도, RECONNECT_INTERVAL=1000)<br>7. 연결 성공 → PpRpc 인스턴스<br>8. CONNECTION_REQUEST 수신 → `isApproved()`<br>9. 승인 시 CONNECTION_ACCEPTED 송신, AdbPlayerChannel 생성 + delegate 등록<br>10. 이후 MESSAGE, COMMAND 처리
**입력 명세**:<br>- USB: Android 기기 (vendor/product ID 자동 감지)<br>- ADB 프로토콜: 표준<br>- PpRpc: 바이너리 frame (version, type, tag, length + payload)
**출력 명세**:<br>- Device 감지 → USBPlayerManager 등록<br>- PpRpc notify: CONNECTION_ACCEPTED, COMMAND, MESSAGE<br>- DB: `SPlayerConnectionRecord` (playerId, pieId, playerType=‘UsbPlayer’)
**상태·저장**:<br>- 메모리: `_devicePortMap: { [deviceId]: localPort }`, `_adbClient`, `_adbTracker`<br>- DB: `SPlayerConnectionRecord`<br>- TTL: 없음 (연결 해제 시 정리)<br>- 동시성: RepeatingDeviceAttachCounter (과도한 로그 방지)
**에러·엣지**:<br>- 포트포워딩 재시도: `PORT_FORWARD_RETRY_COUNT=6`, `INTERVAL=500ms`<br>- 연결 재시도: RECONNECT_INTERVAL=1000ms (indefinite)<br>- ADB 시작 실패: `_isReady=false`, tracker error 시 10초 간격 RETRY_COUNT=10<br>- Device 재부착 빠른 반복: 10초 window에 5회 초과 시 로그 억제<br>- 포트포워딩 제거 불가: adbkit 미지원 → 재시작 시 포트 재사용
**코드 위치**:<br>- `server/src/server/player/AdbPlayerChannelManager.ts:26-136` — `start()`<br>- `server/src/server/player/AdbPlayerChannelManager.ts:169-186` — `_onDeviceAdd()`<br>- `server/src/server/player/AdbPlayerChannelManager.ts:188-204` — `_addPortForwarding()`<br>- `server/src/server/player/AdbPlayerChannelManager.ts:222-241` — `_connect()`<br>- `server/src/server/player/AdbPlayerChannelManager.ts:262-294` — `_handleNotificationBeforeConnect()`<br>- `server/src/server/USBServer.ts:142-154`<br>- `server/src/server/manager/USBPlayerManager.ts`
**알려진 quirk**:<br>- LOCAL_PORT_START=19981, ANDROID_PORT=9981 하드코드<br>- adbkit `forward()` 제거 불가 (API 미지원)<br>- Device attach 직후 포트포워딩 실패 가능 (OS 차이)
---
### MIR-3. iOS 미러링
**한줄 요약**: usbmux로 iOS USB 감지 + PeerTalk frame 바이너리 프로토콜 (port 9982).
**진입점**:<br>- System: usbmux daemon (macOS: usbmuxd)<br>- USB: iOS 기기 USB<br>- Protocol: PeerTalk frame (32-bit header × 4: version, type, tag, length)
**모드**: desktop / server (주로 macOS)
**동작 흐름**:<br>1. `PeerTalkClient.start(9982)`: `usbmux.createListener()`<br>2. ‘attached’ 이벤트 → udid 배열 추가<br>3. `_connect(port, udid)`: `usbmux.getTunnel(9982, { udid })`<br>4. 연결 성공: tunnel 객체 저장, ‘data’ 리스너 등록<br>5. Binary 데이터 수신 → `readFrame()` 파싱:<br>- version (int32BE, offset 0)<br>- type (int32BE, offset 4) — 201 COMMAND, 202 GET, 203 DEVICE_INFO, 205 MESSAGE<br>- tag (int32BE, offset 8)<br>- payloadSize (int32BE, offset 12)<br>- payload (UTF8, offset 16+)<br>6. Frame callback: `_eventCallbacks['frame'](udid, type, tag, payload)`<br>7. `UsbmuxChannelManager._handlePeerTalkFrame()`:<br>- 203 (DEVICE_INFO): `_handleConnectionRequestFrame()` → CONNECTION_REQUEST<br>- 202 (GET): `_handleGetRequestFrame()` → 응답 type 202<br>- 205 (MESSAGE): `_handleMessageFrame()` → message emit<br>8. ‘close’ 이벤트 → `_connect()` 재시도 (attached 상태 확인)
**입력 명세**:<br>- USB: iOS (udid 자동 감지)<br>- PeerTalk frame: header 16 bytes + payload<br>- Frame types: 201 COMMAND, 202 GET, 203 DEVICE_INFO, 204 DENY, 205 MESSAGE, 206 STUDIO_INFO
**출력 명세**:<br>- Device → UsbmuxPlayerChannel + delegate<br>- Frame 송신: `sendFrame(udid, type, tag, payload)`<br>- DB: `SPlayerConnectionRecord` (playerId=udid)<br>- TYPE_STUDIO_INFO (206): protocol version ≥ 2일 때만
**상태·저장**:<br>- 메모리: `_tunnels: { [udid]: UsbMuxTunnel }`, `_attachedUdids: string[]`, `_playerInfoMap: { [udid]: PlayerInfo }`<br>- TTL: 없음 (연결 해제 시 정리)
**에러·엣지**:<br>- getTunnel() 실패: catch → 1초 재시도 (indefinite)<br>- Tunnel close: 즉시 재접속 (reconnectInterval=1000)<br>- attach 해제: tunnel 자동 destroy<br>- Protocol version: ≥ 2일 때만 STUDIO_INFO
**코드 위치**:<br>- `server/src/server/player/PeerTalkClient.ts:28-48` — `start()`<br>- `server/src/server/player/PeerTalkClient.ts:53-68` — `stop()`<br>- `server/src/server/player/PeerTalkClient.ts:77-99` — `sendFrame()`<br>- `server/src/server/player/PeerTalkClient.ts:108-146` — `_connect()`<br>- `server/src/server/player/PeerTalkClient.ts:149-169` — `readFrame()`<br>- `server/src/server/player/UsbmuxChannelManager.ts:88-103` — `_handlePeerTalkFrame()`<br>- `server/src/server/player/UsbmuxChannelManager.ts:105-120` — `_handleConnectionRequestFrame()`
**알려진 quirk**:<br>- USB_MUX_PORT=9982, reconnectInterval=1000 하드코드<br>- STUDIO_INFO_PROTOCOL_VERSION=2 (조건)<br>- udid를 playerInfo.id로 overwrite (line 112)<br>- 에러 응답 방식 미정의 (line 146 주석)
---
### MIR-4. Stage/Group 관리
**한줄 요약**: Pie를 Group(MultiView/Stage)으로 구성. 각 Group은 위치(index), 배경색, Unity 레이어 메타데이터.
**진입점**:<br>- HTTP API:<br>- `GET /groups/:multiViewId` — group 상세<br>- `GET /groups` — 모든 group<br>- `POST /groups` — group 추가<br>- `DELETE /groups/:multiViewId`<br>- `POST /groups/:multiViewId/background-color` — 배경색<br>- `POST /groups/:multiViewId/layers/unity/:layerId` — Unity 파일 업로드<br>- `GET /groups/:multiViewId/layers/unity/:layerId` — Unity 파일 다운로드
**모드**: desktop / server
**동작 흐름**:<br>1. `getGroups()`: `PieManager.getGroupsInfoForHttpApi(hostAddress)` → group 배열<br>2. `addGroup()`: `PieManager.addGroup()` → DB stage 추가<br>3. `removeGroups()`: `PieManager.deleteGroups([groupIds])` → DB DELETE<br>4. `movePieLayer()`: `PieManager.movePieLayer(fromGroupId, toGroupId, pieId, destIndex)` → 재배치<br>5. `updateBackgroundColor()`: `PieManager.updateGroupBackgroundColor(groupId, color, featureLimits)`<br>6. `addUnityFile()`: zip 업로드 → `UnityFileUtil.unzip` → `DATA_ROOT/data/groups/{groupId}/unity/{layerId}/`<br>7. `getUnityFile()`: 파일 시스템 resolve → sendFile()
**입력 명세**:<br>- `GET /groups/:multiViewId` (Params: groupId)<br>- `POST /groups/:multiViewId/background-color` body: `{ color: string }`<br>- `POST /groups/:multiViewId/layers/unity/:layerId` body: multipart file (zip)
**출력 명세**:<br>- 200: group metadata<br>- Side effect: DB (SGroup, SPieLayer, SUnityLayer), File `DATA_ROOT/data/groups/{groupId}/unity/{layerId}/*`
**상태·저장**:<br>- DB: SGroup, SPieLayer, SUnityLayer<br>- File: `DATA_ROOT/data/groups/{groupId}/unity/{layerId}/`
**에러·엣지**:<br>- groupId 없음: 400<br>- Group 미존재: 404<br>- non-zip: 400 + UnityErrorCode.UnityUnvalidZipError<br>- 필수 파일 부재: 400 + UnityErrorCode.UnityMissingFileError<br>- 기능 제한: featureLimits.groupCountLimit (Free=1)
**코드 위치**:<br>- `server/src/server/routes/groups.ts`<br>- `server/src/server/controllers/groups.controller.ts:46-75` — `getGroup()`<br>- `server/src/server/controllers/groups.controller.ts:107-128` — `addGroup()`<br>- `server/src/server/controllers/groups.controller.ts:130-178` — `removeGroups()`<br>- `server/src/server/controllers/groups.controller.ts:239-272` — `updateBackgroundColor()`<br>- `server/src/server/controllers/groups.controller.ts:301-396` — `addUnityFile()`
**알려진 quirk**:<br>- groupId param 명: multiViewId (legacy naming)<br>- featureLimits.groupCountLimit 강제 (free=1)<br>- Unity 저장 경로: `{DATA_ROOT}/data/groups/{groupId}/unity/{layerId}/`
---
### MIR-5. 핫스팟 힌트
**한줄 요약**: Web Player에서 hotspot 위치 표시 토글. `WebPlayerManager.updateHotspotHints()`로 모든 Web Player에 broadcast.
**진입점**:<br>- HTTP/Socket: hotspot 토글 (UI 통합, 명시 endpoint 미발견)
**모드**: server / desktop
**동작 흐름**:<br>1. UI에서 hotspot 토글 요청<br>2. `WebPlayerManager.updateHotspotHints(isHotspotHintsOn)`<br>3. `option.hotspotHints = isHotspotHintsOn`<br>4. 모든 Web Player에 `updateOption()` broadcast<br>5. Web Player가 option 받아 UI 렌더링 변경
**입력 명세**: Boolean toggle
**출력 명세**:<br>- 모든 Web Player의 hotspot 표시 상태 변경<br>- Event: `WebPlayerManager.EVENT_CHANGED` emit
**상태·저장**: 메모리 `WebPlayerManager.option.hotspotHints`
**에러·엣지**: Web Player 미연결 시 상태만 저장, 다음 연결 시 적용
**코드 위치**:<br>- `server/src/server/manager/WebPlayerManager.ts:58-62` — `updateHotspotHints()`
---
### 2-5. ProtoPie Studio 연동 (2개)
### STU-1. ProtoPie Studio 페어링
**한줄 요약**: Desktop과 Studio 간 SocketIO 연결 + 메시지 전파 중개.
**진입점**:<br>- Socket event:<br>- Client → Server: `connectToStudio(studioSessionInfo)`<br>- Server → Client: `pieListUpdated`, `newPieAdded` 등 (양방향)
**모드**: server, desktop
**동작 흐름**:<br>1. Desktop 시작 시 SocketIOClientManager 초기화<br>2. Desktop `socket.connect()` (자동 재연결 reconnectionDelay 500ms)<br>3. 연결 성공 → `connect` 이벤트 → Promise resolve<br>4. Server SocketManager가 새 SocketConnection<br>5. Desktop이 Studio 페어링 정보(IP, port, session token) 전송<br>6. Server가 Studio로 역방향 SocketIO 연결 시도<br>7. 메시지 라우팅 활성화:<br>- Desktop → Studio: 사용자 입력·이벤트<br>- Studio → Desktop: 렌더링 결과·피드백<br>8. 단절 시 자동 재연결 (3회 또는 설정값)
**입력 명세**:<br>- Socket: `event: 'connectToStudio'`, `payload: { studioIP, studioPort, sessionToken, deviceId? }`
**출력 명세**:<br>- Socket emit: `studioConnected { success, studioIP }`, `studioDisconnected { reason }`, message passthrough
**상태·저장**:<br>- 메모리: SocketConnection 객체 (양쪽 소켓 ref)
**에러·엣지**:<br>- 재연결 자동 (reconnectionDelay 500ms 고정 — exponential 없음)<br>- 강제 disconnect: `socket.emit('disconnect')` 시 재연결 안 함<br>- Timeout: Studio 연결 실패 시 에러 이벤트<br>- `logout` 이벤트: Electron session 클리어 (보안)
**코드 위치**:<br>- `desktop/src/managers/SocketIOClientManager.ts:13-55`<br>- `server/src/server/SocketManager.ts:59-116`<br>- `server/src/server/SocketConnection.ts`
**알려진 quirk**:<br>- reconnectionDelay 500ms 고정 (부하 증가 위험)<br>- `logout` 이벤트는 명시적 인증 요청<br>- disconnect 이유 필터링: `reason !== 'io client disconnect'` 시 자동 재연결
---
### STU-2. Studio에서 .pie 업로드
**한줄 요약**: Studio가 Server로 .pie 파일 multipart POST → 저장 → 즉시 실행 가능.
**진입점**:<br>- HTTP API: `POST /api/pies/add` (multipart/form-data)
**모드**: server (Studio는 HTTP 클라이언트)
**동작 흐름**:<br>1. Studio에서 .pie multipart POST<br>2. Express multer 파일 파싱<br>3. `pies.controller.ts:addPieFile()`<br>4. 파일 유효성:<br>- 확장자 `.pie` / `.PIE`<br>- 파일 존재·버퍼 검증<br>5. 파라미터 파싱:<br>- `pieId`: 교체 시 (선택)<br>- `groupId`: 스테이지/그룹 ID<br>- `filepath`: 클라이언트 파일 경로 (UI용)<br>- `extraInformation`: JSON 메타데이터<br>6. PieManager 추가: 신규 `addNewPieFile()` / 교체 `updatePieFile()`<br>7. 응답: `{ result: 'ok', pieId, ... }`
**입력 명세**:<br>- `POST /api/pies/add` (multipart/form-data):<br>`file: <binary .pie>   pieId: <number, optional>   stageId: <number>   filepath: <string, optional>   extraInformation: <JSON string, optional>`
**출력 명세**:<br>- 200: `{ result: 'ok', pieId, ... }`<br>- 400: `{ error: '... is not a pie file.' }`<br>- 413: `{ error: 'File too large' }`
**상태·저장**:<br>- SQLite: SPie, SPieExtraInformation<br>- 파일: `{piesDir}/{pieId}/pie.pie`
**에러·엣지**:<br>- 파일 크기: multer limit (default 코드 확인)<br>- extraInformation 파싱 실패: 400<br>- 동시 업로드 같은 pieId: race condition (현재 없음)<br>- 디스크 부족: 500
**코드 위치**:<br>- `server/src/server/controllers/pies.controller.ts:90-366` — `addPieFile()`<br>- `server/src/server/routes/api.ts:85-91`<br>- `server/src/server/manager/PieManager/PieManager.ts`
**알려진 quirk**:<br>- `isReplace = !!req.body.pieId`<br>- extraInformation 선택적 (파싱 실패해도 pie 저장)<br>- filepath UI 표시용
---
### 2-6. 프로토타입 관리 (6개)
### PIE-1. 로컬 .pie 파일 추가
**한줄 요약**: 사용자 파일 시스템에서 .pie 선택 → 로컬 라이브러리에 추가.
**진입점**:<br>- UI: `PieList/EmptyPieList/ImportButton.tsx` (또는 좌측 패널 “Add”)<br>- HTTP API: `POST /api/pies/add` (STU-2와 동일)
**모드**: desktop / server
**동작 흐름**:<br>1. UI에서 “Import Pie” 클릭<br>2. 파일 다이얼로그 (Electron 또는 HTML input)<br>3. 사용자가 로컬 .pie 선택<br>4. multipart POST로 Server 업로드 (STU-2와 동일)<br>5. Server 검증·저장<br>6. UI가 PieList에 표시
**입력/출력**: STU-2와 동일
**상태·저장**:<br>- SQLite: SPie 신규 행<br>- 파일: `{piesDir}/{pieId}/pie.pie`
**에러·엣지**:<br>- 파일 선택 취소: 다이얼로그만 종료<br>- 파일 이동/삭제: 부분적 업로드 후 오류<br>- 같은 이름 추가: 별도 pieId, 이름 deduplication
**코드 위치**:<br>- `server/src/components/CloudFinder/PieList/EmptyPieList/ImportButton.tsx`<br>- `server/src/server/controllers/pies.controller.ts:90-366`
**알려진 quirk**:<br>- ImportButton이 CloudFinder에 속함 (Cloud 다운로드와 로컬 추가 혼합)
---
### PIE-2. 프로토타입 목록 조회
**한줄 요약**: 사용자의 모든 .pie 메타데이터 + 실행 상태 목록.
**진입점**:<br>- HTTP API: `GET /api/pies` (로그인 필수)
**모드**: server
**동작 흐름**:<br>1. `/api/pies` GET<br>2. `pies.controller.ts:getPies()`<br>3. UserManager userId 조회 (로그인 확인)<br>4. `PieManager.getPiesInfoForHttpApi(userId, address)`<br>5. PieItemsManager DB 조회 (SPie, userId 필터)<br>6. WebPlayerManager·AppPlayerManager·USBPlayerManager에서 활성 플레이어 ID 수집<br>7. 응답: `[ { id, name, filePath, isTemp, ..., webPlayerIds, appPlayerIds, usbPlayerIds } ]`
**입력 명세**: `GET /api/pies` (자동 로그인 토큰)
**출력 명세**:<br>- 200: `[ { id, name, webPlayerIds, appPlayerIds, usbPlayerIds, ... } ]`<br>- 403: `{ error: 'userId is not defined' }`<br>- 500
**상태·저장**: PlayerManager 활성 연결 맵 (메모리)
**에러·엣지**:<br>- isTemp=true: 다운로드 중인 pie (filePath 없음)<br>- 파일 삭제됨: isValid=false 표시 (코드 확인 필요)<br>- 플레이어 할당 변경: 실시간 미반영 (클라이언트 폴링)
**코드 위치**:<br>- `server/src/server/controllers/pies.controller.ts:46-88` — `getPies()`<br>- `server/src/server/manager/PieManager/PieItemsManager.ts:129-131` — `getPiesInfoForApi()`<br>- `server/src/server/routes/api.ts:78-84`
**알려진 quirk**:<br>- address 파라미터 (로컬 서버 주소)는 pie URI 생성용<br>- 플레이어 정보는 항상 포함
---
### PIE-3. 프로토타입 삭제
**한줄 요약**: .pie 파일을 DB·파일시스템에서 제거.
**진입점**:<br>- HTTP API: `GET/POST /api/pies/remove` (쿼리 또는 바디)
**모드**: server
**동작 흐름**:<br>1. `/api/pies/remove?pieId=123` (또는 POST body)<br>2. `pies.controller.ts:removePies()`<br>3. pieId 추출 (string 또는 array)<br>4. 숫자 변환 검증<br>5. `PieManager.deletePies(pieIds[])`:<br>- PieItemsManager.deletePie() (DB DELETE)<br>- PieGroupManager.deletePieLayerByPieId() (스테이지 정리)<br>- PieFileWatcher 재초기화<br>- `EVENT_PIE_CHANGED`<br>6. 응답: `{ result: 'ok' }`
**입력 명세**:<br>- `GET /api/pies/remove?pieId=123` (단일)<br>- `GET /api/pies/remove?pieId=123&pieId=456` (배열)<br>- `POST /api/pies/remove` body: `{ pieId: 123 | [123, 456] }`
**출력 명세**:<br>- 200: `{ result: 'ok' }`<br>- 400: `{ error: '... is invalid' }`<br>- 500
**상태·저장**:<br>- SQLite: SPie 행 DELETE, SCloudPieInfo 정리<br>- 파일: `{piesDir}/{pieId}/` 디렉토리 삭제
**에러·엣지**:<br>- 동시 삭제: 같은 pieId 여러 요청 → 2번째 “pie not found”<br>- 파일 삭제 실패: DB 삭제되나 파일 남음 (orphan)<br>- 플레이어 실행 중: 삭제 후 플레이어 오류 가능
**코드 위치**:<br>- `server/src/server/controllers/pies.controller.ts:367-412` — `removePies()`<br>- `server/src/server/manager/PieManager/PieManager.ts:242-267` — `deletePies()`<br>- `server/src/server/routes/api.ts:99-112`
**알려진 quirk**:<br>- GET/POST 모두 지원 (legacy, REST 위반)<br>- 쿼리·바디 동시 지원: `hasQueryParam` 플래그로 우선순위 (쿼리 우선)
---
### PIE-4. 프로토타입 실행
**한줄 요약**: 특정 .pie를 모든 연결된 플레이어(웹·앱·USB)에서 동시 재생.
**진입점**:<br>- HTTP API: `GET/POST /api/pies/run`
**모드**: server
**동작 흐름**:<br>1. `/api/pies/run?pieId=123`<br>2. `players.controller.ts:runPlayersByPieId()`<br>3. pieId 추출 (string 또는 array)<br>4. 검증<br>5. 각 pie마다 플레이어 수집·재생:<br>- `AppPlayerManager.getAppPlayersByPieId(pieId)` → `.play()`<br>- `WebPlayerManager.getWebPlayersByPieId(pieId)` → `.play()`<br>- `USBPlayerManager.getUSBPlayersByPieId(pieId)` → `messageManager.emit('play-usb-player')`<br>6. 응답: `{ result: 'ok' }`
**입력 명세**:<br>- `GET /api/pies/run?pieId=123` (단일/배열)<br>- `POST /api/pies/run` body: `{ pieId: 123 | [123, 456] }`
**출력 명세**:<br>- 200: `{ result: 'ok' }` (플레이어 없어도 ok)<br>- 400: `{ error: '... is invalid' }`
**상태·저장**: 메모리 (플레이어 상태)
**에러·엣지**:<br>- 플레이어 없음: 에러 아님<br>- 배열: forEach 동시 실행 (async 아님)<br>- USB 플레이어: messageManager.emit() (fire-and-forget)
**코드 위치**:<br>- `server/src/server/controllers/players.controller.ts:151-209` — `runPlayersByPieId()`<br>- `server/src/server/manager/AppPlayerManager/AppPlayerManager.ts`<br>- `server/src/server/routes/api.ts:113-126`
**알려진 quirk**:<br>- GET/POST 모두 지원<br>- 배열 처리 forEach 내 async 미await<br>- USB는 fire-and-forget
---
### PIE-5. 프로토타입 파일 감시 (File Watcher)
**한줄 요약**: 로컬 폴더의 .pie 파일 변경 감지 → 자동 재로드 (개발 워크플로우).
**진입점**: 설정 폴더 구성 시 자동 활성화
**모드**: server (주로 개발)
**외부 의존**: `chokidar` npm 패키지
**코드 위치**: `server/src/server/manager/PieManager/PieFileWatcher.ts`
---
### PIE-6. Cloud 다운로드 진행률
**한줄 요약**: Cloud .pie 다운로드 중 % 및 바이트 진행 상황을 Socket으로 클라이언트에 전송.
**진입점**:<br>- Socket event: `pieDownloadProgress` (server → client)
**모드**: server, client (양방향)
**동작 흐름**:<br>1. CloudPieDownloadManager 다운로드 시작<br>2. `addProgress(pieId)` → `_progresses[pieId] = 0`<br>3. HTTP 스트림 수신:<br>- `res.on('data', chunk)` → downloaded += chunk.length<br>- onProgress 콜백:<br>`typescript      { direction: 'download', loaded, total?, percent? }`<br>4. `updateProgress(pieId, percent)` → `_progresses[pieId] = percent`<br>5. `_onProgressesChange()` → Socket emit<br>6. 완료/실패 → `removeProgress(pieId)` → 정리
**입력 명세**: 내부 `onProgress: (ProgressEvent) => void`
**출력 명세**:<br>- Socket: `event: 'pieDownloadProgress'`, `payload: { pieId, percent, loaded, total? }`
**상태·저장**: 메모리 (`_progresses` Map)
**에러·엣지**:<br>- Content-Length 없음: total/percent 미포함<br>- Content-Length 0: percent 오류 → 재시도 트리거<br>- 연결 단절: 진행률 중단, Socket error<br>- 배열 다운로드: 각 pie 독립 진행 (병렬)
**코드 위치**:<br>- `server/src/server/manager/PieManager/CloudPieDownloadManager.ts:214-226` — onProgress<br>- `server/src/server/manager/PieManager/CloudPieDownloadManager.ts:274-291` — progress 관리<br>- `server/src/server/manager/PieManager/PieItemsManager.ts` — Socket emit
**알려진 quirk**:<br>- percent 부동소수점 (정수 반올림 없음)<br>- 썸네일 다운로드 진행률 미추적
---
### 2-7. 하드웨어 통합 (4개)
### HW-1. USB 기기 감지·관리
**한줄 요약**: AdbPlayerChannelManager + UsbmuxChannelManager 통합. ADB(Android) + usbmux(iOS) 감지 + 생명주기 관리.
**진입점**: System events (ADB trackDevices, usbmux listener) + delegate `PlayerChannelManagerDelegate` (USBServer)
**모드**: desktop / server
**동작 흐름**:<br>1. `USBServer.start()` → `adbChannelManager.start()` + `usbmuxChannelManager.start()`<br>2. ADB device add/remove 감지 (포트포워딩·재접속)<br>3. iOS device attach/detach 감지 (tunnel 관리)<br>4. Connection request 수신 → `USBServer.isApproved()` 확인<br>5. 승인 → `handleNewConnection()` → `USBPlayerManager.addPlayer()`<br>6. 메시지 수신 → `handlePlayerMessage()` → MessageManager emit<br>7. 분리 → `handleDisconnect()` → `USBPlayerManager.removePlayer()`
**상태·저장**:<br>- 메모리: `_players: { [playerId]: PlayerInfo }`, `_playerChannels: { [playerId]: PlayerChannel }`<br>- DB: `SPlayerConnectionRecord`
**에러·엣지**:<br>- ADB 실패: tracker error 재시도<br>- iOS 실패: indefinite 재시도<br>- 강제 분리: channel close 감지, player 제거<br>- 포트 충돌: 19981부터 100 포트 탐색
**코드 위치**:<br>- `server/src/server/USBServer.ts:142-149` — `start()`<br>- `server/src/server/USBServer.ts:151-154` — `stop()`<br>- `server/src/server/USBServer.ts:212-225` — `handleNewConnection()`<br>- `server/src/server/USBServer.ts:227-238` — `handleDisconnect()`
---
### HW-2. Serial 포트 통신 (Arduino)
**한줄 요약**: serialport로 Arduino 등 시리얼 기기 감지·연결·메시지 송수신 (delimiter `\r\n`).
**진입점**:<br>- System: `SerialPort.list()` (macOS/Linux/Windows)<br>- Message events:<br>- `'open-serial-ports'` → `{ port, baudrate }`<br>- `'close-serial-ports'`<br>- `'request-serial-ports-state'`
**모드**: desktop / server (시리얼 포트 접근)
**동작 흐름**:<br>1. `SerialServer.start()` → `_updatePortList()` → `SerialPort.list()`<br>2. Arduino 모델 매칭 (ArduinoModels 배열, vendor/product ID)<br>3. `'open-serial-ports'` 수신 → `_open(portName, baudRate)`<br>4. SerialPort 인스턴스, 콜백 바인딩<br>5. `'open'` 이벤트 → ReadlineParser (delimiter `'\r\n'`)<br>6. `'data'` 이벤트 → `messageId||value` 파싱 (`||` separator)<br>7. emit `'pp-message-serial'` → messageManager<br>8. `'close'` / `'error'` → SerialPortEvent emit
**입력 명세**:<br>- 메시지: `{ port: string, baudrate: string }` (숫자 string)<br>- 직렬 데이터: `messageId||value\r\n` (delimited)
**출력 명세**:<br>- Event: `SerialPortEvent { state, serialPort: { portPath, baudRate } }`<br>- Message: `{ messageId, value }` via ‘pp-message-serial’
**상태·저장**:<br>- 메모리: `_serialport: SerialPort | null`, `_portPath`, `_baudRate`, `_isConnecting`, `_portList`
**에러·엣지**:<br>- 포트 열기 실패: error 콜백, state=Error<br>- 포트 이미 열림: `_closePort()` 먼저<br>- 데이터 파싱 실패: messageId만 전송, value=null<br>- 포트 목록 업데이트: 메시지 driven (`'update-serial-ports'`)
**코드 위치**:<br>- `server/src/server/SerialServer.ts:48-103` — `start()`<br>- `server/src/server/SerialServer.ts:105-127` — `_open()`<br>- `server/src/server/SerialServer.ts:192-224` — `_handlePortOpen()`<br>- `server/src/server/SerialServer.ts:268-287` — `_handleSerialMessage()`
**알려진 quirk**:<br>- ArduinoModels 배열 (17개) 하드코드<br>- delimiter `\r\n` 하드코드<br>- separator `||` 하드코드<br>- port.model 매칭 실패 시 빈 문자열
---
### HW-3. MQTT 메시지 브로커
**한줄 요약**: aedes (Node.js MQTT broker) localhost:1883 → pp-message-\*에서 받은 메시지를 MQTT topic으로 publish.
**진입점**:<br>- System: net.Server port 1883<br>- Message events: `'pp-message-socket'`, `'pp-message-usb'`, `'pp-message-serial'`, `'pp-message-http'`
**모드**: server / desktop
**동작 흐름**:<br>1. `MQTTServer.start(port)` → aedes.Server() + net.createServer()<br>2. `_bindCallbacks()` → ‘client’, ‘clientDisconnect’, ‘publish’ 리스너<br>3. Client 연결 → log<br>4. Client publish (topic: messageId, payload: value) → `_handleOnPublish()`<br>5. \$SYS 토픽 제외 → emit `'pp-message-mqtt'`<br>6. pp-message-\* 수신 → `_sendMessage()` → aedes.publish()
**입력 명세**:<br>- MQTT publish: `{ topic, payload }`<br>- Message: `{ messageId, value }`
**출력 명세**:<br>- MQTT publish: `{ topic: messageId, payload: value }`<br>- Event: `'pp-message-mqtt'`
**상태·저장**: 메모리 `_aedes`, `_server`, `_port`
**에러·엣지**:<br>- \$SYS 토픽 필터링<br>- publish error: log only, silent fail<br>- client 없음: tunnel queue 자동 (aedes)
**코드 위치**:<br>- `server/src/server/MQTTServer.ts:23-27` — `start()`<br>- `server/src/server/MQTTServer.ts:50-76` — `_handleOnPublish()`<br>- `server/src/server/MQTTServer.ts:78-87` — `_sendMessage()`
**알려진 quirk**:<br>- Port 1883 하드코드 (표준 MQTT)<br>- \$SYS 필터 (aedes 시스템 토픽)<br>- 에러 silent
---
### HW-4. Logitech G29 게임패드
**한줄 요약**: G29 휠·페달·시프터 입력을 ProtoPie 이벤트로 변환.
**진입점**: 게임패드 연결 → 자동 감지 → 버튼/조이스틱 입력
**모드**: desktop / server (웹 전용)
**외부 의존**: `logitech-g29` npm 패키지 \^1.3.0
**코드 위치**:<br>- `server/src/components/Providers/GamepadsProvider.tsx`<br>- `server/package.json: "logitech-g29": "^1.3.0"`
---
### 2-8. 폰트 관리 (3개)
### FNT-1. Cloud 폰트 다운로드·캐싱
**한줄 요약**: Cloud에서 커스텀 폰트 목록 조회 + 로컬 다운로드·캐시.
**진입점**:<br>- HTTP API: `GET /api/fonts/reload`
**모드**: server
**동작 흐름**:<br>1. Server 시작 또는 `/api/fonts/reload` 요청<br>2. `fonts.controller.ts:getFontFromCloud()`<br>3. SessionManager session·featureLimits 조회<br>4. `featureLimits.customFontsEnabled` 확인 (비활성 시 빈 배열)<br>5. ProxyManager proxy URL<br>6. `FontManager.loadFonts(session, proxy)`:<br>- `CustomFontLoader.update()`<br>- Cloud API: `GET /api/v3/fonts` (Bearer)<br>- 응답: `{ fonts: [{ id, name, version, thumbnailUrl, deleted, ... }] }`<br>7. 다운로드 대상 필터 (id, version 비교)<br>8. 각 폰트 다운로드 (HTTP GET 스트림) → `{fontsDir}/custom/{fontId}`<br>9. 메타 캐시: `{fontsDir}/customFonts.json`<br>10. 응답: `[ ClientFontDescriptor[] ]`
**입력 명세**: `GET /api/fonts/reload` (자동 토큰)
**출력 명세**:<br>- 200: `[ { id, name, version, isDownloadComplete, ... } ]`<br>- 403: `{ error: 'userId is not defined' }`<br>- 400: FontDownloadError<br>- 500
**상태·저장**:<br>- 파일: `{fontsDir}/custom/{fontId}` (실제 폰트), `{fontsDir}/customFonts.json` (메타)<br>- 메모리: `FontManager.customFonts` 배열
**에러·엣지**:<br>- 폰트 \< 100 바이트: 무효 → 삭제<br>- 파일/메타 불일치: init() 시 자동 정리 (`checkFontFilesAndFontInfo()`)<br>- Cloud API 오류: FontDownloadError<br>- 디스크 부족: 파일 쓰기 실패<br>- featureLimits 비활성: 빈 배열 (Cloud 요청 안 함)
**코드 위치**:<br>- `server/src/server/controllers/fonts.controller.ts:113-160` — `getFontFromCloud()`<br>- `server/src/server/manager/FontManager/FontManager.ts:29-88` — 로드·캐싱<br>- `server/src/server/manager/FontManager/CustomFontLoader.ts:40-127` — 검증·메타<br>- `server/src/server/routes/fonts.ts:27`
**알려진 quirk**:<br>- MIN_VALID_FONT_SIZE_BYTES = 100 하드코드<br>- isDownloadComplete: “파일 존재 여부” (이름 혼동)<br>- customFonts 메모리만 (매번 로드 필요)
---
### FNT-2. 폰트 목록 조회
**한줄 요약**: 로컬 캐시된 커스텀 폰트 목록 반환 (Cloud 미동기).
**진입점**: `GET /api/fonts/list`
**모드**: server
**동작 흐름**:<br>1. `/api/fonts/list` GET<br>2. `fonts.controller.ts:getFontsList()`<br>3. UserManager userId<br>4. `FontManager.getLocalCustomFonts()`:<br>- `CustomFontLoader.getLocalCustomFontList()`<br>- customFonts.json에서 메타 로드 (init() 후)<br>5. 응답: `[ ClientFontDescriptor[] ]`
**입력/출력 명세**:<br>- `GET /api/fonts/list`<br>- 200: `[ { id, name, version, isDownloadComplete, ... } ]`<br>- 403/500
**상태·저장**:<br>- 메모리: `FontManager.customFonts` (캐시)<br>- 파일: `{fontsDir}/customFonts.json` (읽기)
**에러·엣지**:<br>- customFonts.json 없음: 빈 배열<br>- JSON 파싱 실패: catch → 빈 배열 (오류 무시)<br>- 폰트 파일 삭제됨: isDownloadComplete=false
**코드 위치**:<br>- `server/src/server/controllers/fonts.controller.ts:30-67` — `getFontsList()`<br>- `server/src/server/manager/FontManager/FontManager.ts:69-72`
---
### FNT-3. 폰트 재로드
**한줄 요약**: FNT-1과 동일 (`GET /api/fonts/reload` 엔드포인트는 FNT-1과 완전히 같음).
**코드 위치**: `server/src/server/routes/fonts.ts:27` — `fontsController.getFontFromCloud`
---
### 2-9. 설정·관리 (6개)
### CFG-1. 세션 정보 (User Profile)
**한줄 요약**: `GET /session`로 현재 로그인 사용자 정보·권한 반환 (없으면 null).
**진입점**: `GET /session`
**모드**: server / desktop / cloud
**동작 흐름**:<br>1. `GET /session`<br>2. SessionManager `getSessionOrNull()`<br>3. 200: 세션 JSON 또는 null
**입력 명세**: `GET /session`
**출력 명세**:<br>- 200: `SSessionModel` JSON 또는 null<br>- Fields: email, username, token, host, expiresAt, highestPlan, featureType, cloudId, …
**상태·저장**: DB SSession, TTL expiresAt
**에러·엣지**: 만료 체크 (application logic), 없음 시 null (200)
**코드 위치**:<br>- `server/src/server/routes/session.ts`<br>- `server/src/server/controllers/session.controller.ts:9-20` — `getSession()`
---
### CFG-2. 로그인/로그아웃
**한줄 요약**: `POST /login` Cloud 인증 + 세션 + featureLimits. `POST /logout` 세션 제거.
**진입점**: `POST /login`, `POST /logout`
**모드**: server / desktop
**동작 흐름 - Login**:<br>1. `POST /login` `{ email, password, token?, host, hostPlan }`<br>2. SessionManager 기존 세션 있으면 `clearSession()`<br>3. CloudServerRequester:<br>- token 있으면 사용, 없으면 `/auth` POST → token<br>- `setToken()`, `setOption()` (proxy)<br>4. `GET /me` → CloudUser 정보<br>5. `checkUserPlan()`:<br>- isTeamCloudServer (`hostPlan.includes('team-cloud')`)? Pro/Enterprise<br>- user.deleted, deactivated 체크<br>- 승인·expiresAt 계산<br>6. SessionManager.createSession() → DB SSession<br>7. `getFeatureLimits()` → 계획 제한<br>8. 200: `{ session, featureLimits }`
**동작 흐름 - Logout**:<br>1. `POST /logout`<br>2. SessionManager.clearSession() → DB DELETE
**입력/출력 명세**:<br>- Login: body `{ email, password, token?, host, hostPlan }` → 200 `{ session, featureLimits }`<br>- Logout: empty body → 200 empty
**상태·저장**: DB SSession, TTL expiresAt (기본 +7일)
**에러·엣지**:<br>- 토큰 없음: createHttpError(500)<br>- Cloud 조회 실패: CloudRequestError → 400<br>- deactivated/deleted: 세션 생성하나 free plan 강등<br>- 프록시 실패: `proxyManager.getProxyUrl()`
**코드 위치**:<br>- `server/src/server/routes/login.ts`<br>- `server/src/server/routes/logout.ts`<br>- `server/src/server/controllers/login.controller.ts:24-147`<br>- `server/src/server/controllers/controllerUtils/login.controller.utils.ts` — `checkUserPlan()`
**알려진 quirk**:<br>- `PRO_PLAN_INDICATOR = 'team-cloud'` 하드코드<br>- expiresAt: 미승인만 override (승인된 경우 Cloud 응답값)<br>- featureType: 미승인 시 FeatureType.Free 강제
---
### CFG-3. 버전 확인·업데이트 알림
**한줄 요약**: 최신 버전 체크, 새 버전 출시 시 알림, 강제 업데이트 판단.
**진입점**: UI → “About” 또는 상단 알림 배너
**모드**: desktop / server
**외부 의존**: 버전 정보 서버
**코드 위치**: `server/src/server/manager/UpdateManager.ts`
---
### CFG-4. About / App Data
**한줄 요약**: `GET /about?host=` Cloud 앱 정보. `GET /about/appData` 로컬 APP_VERSION.
**진입점**: `GET /about?host=<cloudHost>`, `GET /about/appData`
**모드**: server / desktop / cloud
**동작 흐름 - About**:<br>1. `GET /about?host=<cloudServerUrl>`<br>2. AboutController.getAbout():<br>- UserManager userId (NotFoundUserError)<br>- ProxyManager proxy<br>- CloudServerRequester GET `about` (host param)<br>3. 200: CloudAbout JSON
**동작 흐름 - AppData**:<br>1. `GET /about/appData`<br>2. AboutController.getAppData():<br>- process.env.APP_VERSION (NotFoundEnvError)<br>3. 200: `{ appVersion }`
**입력/출력 명세**:<br>- About: query `host` (required) → 200 CloudAbout<br>- AppData: empty → 200 `{ appVersion: string }`
**상태·저장**: process.env.APP_VERSION (build time)
**에러·엣지**:<br>- host 없음: CloudServerRequester 실패 → 400<br>- userId 없음: 403<br>- APP_VERSION 없음: 500<br>- Cloud 실패: 400 + code
**코드 위치**:<br>- `server/src/server/routes/about.ts`<br>- `server/src/server/controllers/about.controller.ts:19-61` — `getAbout()`<br>- `server/src/server/controllers/about.controller.ts:62-82` — `getAppData()`
**알려진 quirk**: host는 query (body 아님), APP_VERSION은 build-time env
---
### CFG-5. 팝업 상태 저장 (What’s New)
**한줄 요약**: 사용자 팝업 표시 이력 저장, 재시작 후 비표시.
**진입점**: UI → “What’s New” 모달 → “Don’t show again”
**모드**: 전부
**코드 위치**: `server/src/server/manager/PreferenceManager/PreferenceManager.ts`
---
### CFG-6. 네트워크 주소 수동 재시작
**한줄 요약**: 데스크톱 메뉴에서 특정 네트워크 인터페이스로 서버 재시작.
**진입점**: 데스크톱 메뉴 → “Network” → “Restart Server” → IP 선택
**모드**: desktop only
**코드 위치**:<br>- `desktop/src/managers/MenuManager.ts`<br>- `desktop/src/managers/ServerProcessManager.ts`
---
### 2-10. Desktop 모드 특화 (2개)
### DSK-1. Electron 데스크톱 래퍼
**한줄 요약**: Node.js 서버 프로세스 관리, 웹 UI를 Electron 창에 표시, 시스템 메뉴.
**진입점**: ProtoPie Connect 애플리케이션 실행
**모드**: desktop only
**외부 의존**: Electron npm 패키지
**코드 위치**:<br>- `desktop/src/App.ts`<br>- `desktop/src/managers/MainWindowManager.ts`
---
### DSK-2. Deep Link (`protopie-connect://`)
**한줄 요약**: URL 스킴 처리 → Connect 서버 리다이렉트 → 외부 앱 통합.
**진입점**: `protopie-connect://` 또는 `protopie-connect+http://` URL 클릭
**모드**: desktop only
**코드 위치**:<br>- `desktop/src/managers/ProtocolClientManager.ts`<br>- `desktop/package.json: CFBundleURLSchemes`
---
### 2-11. 협업·세션 (1개)
### COL-1. Feature Limits (Plan별 제한)
**한줄 요약**: 세션 plan에 따라 feature limits 객체 반환 (free/pro/enterprise 3단계).
**진입점**: 코드 `SessionManager.getFeatureLimits()`. Login response에 `featureLimits` field 포함.
**모드**: server / desktop / cloud
**동작 흐름**:<br>1. `getFeatureLimits()` 호출<br>2. 현재 session.featureType 확인<br>3. FeatureType별 limits 반환:<br>- Free: freePlanFeature<br>- Pro: proPlanFeature<br>- ProPlus: proPlusFullFeature<br>- Enterprise: fullFeature
**출력 명세** — FeatureLimits:<br>- `piesLoadingCountLimit`: null or number<br>- `localPieLoadingEnabled` / `cloudPieLoadingEnabled`: bool<br>- `playerCountLimit` / `groupCountLimit`: null or number<br>- `builtinPluginsEnabled`: `{ apiPlugin, iftttPlugin, ... }`<br>- `builtinPluginParallelRunningCountLimit` / `builtinPluginTimeLimit`: null or number (ms)<br>- `customPluginEnabled`: bool<br>- `builtinViewEnabled`: `{ webView, cameraView, unityView }`<br>- `builtinViewParallelRunningCountLimit` / `unityViewParallelRunningCountLimit`: null or number<br>- `unityMessageBindingEnabled` / `wearOsEnabled` / `customFontsEnabled` / `messageReplayerEnabled`: bool
**상태·저장**: 코드 상수 (featureLimits.ts)
**제한 정책**:<br>- **Free**: 2 pies, 2 players, 1 group, 3 plugins parallel, 3분 plugin time, no custom plugins/unity/wearos/custom fonts<br>- **Pro**: unlimited pies/players/groups, 3 plugins, all builtin views, 1 unity, no custom plugins/wearos<br>- **ProPlus**: full feature (custom fonts only false)<br>- **Enterprise**: full feature
**코드 위치**:<br>- `server/src/server/manager/SessionManager/featureLimits.ts:3-36` — fullFeature<br>- `server/src/server/manager/SessionManager/featureLimits.ts:38-42` — proPlusFullFeature<br>- `server/src/server/manager/SessionManager/featureLimits.ts:44-77` — proPlanFeature<br>- `server/src/server/manager/SessionManager/featureLimits.ts:79-112` — freePlanFeature
**알려진 quirk**:<br>- 하드코드 상수<br>- builtinPluginTimeLimit 1000 \* 60 \* 3 = 180000ms = 3분 (Free only)<br>- unityViewParallelRunningCountLimit: free=0, pro=1, enterprise=null<br>- customFontsEnabled: proPlusFullFeature만 false
---
### 2-12. 기타 (6개)
### MSG-1. 메시지 라우팅 (PP Message)
**한줄 요약**: ProtoPie 메시지 이벤트를 HTTP/Socket로 수신 + broadcast/특정 클라이언트 라우팅. EventEmitter pub-sub.
**진입점**:<br>- HTTP API: `GET /api/pp-message` (쿼리), `POST /api/pp-message` (바디)<br>- Socket: `socket.on(ClientToSocketConnectionEvent.PPMessage, ...)`
**모드**: desktop / server
**동작 흐름**:<br>1. **HTTP** (`POST /api/pp-message`):<br>- 쿼리/바디에 `message`, `value`<br>- `ppMessageController.sendMessageFromHttp()`<br>- `MessageManager.emit('pp-message-http', { message, from })`<br>- `from: { getName, getType, getPieId }` 메타<br>2. **Socket**:<br>- 클라이언트 메시지 발송<br>- `SocketConnection.on(ClientToSocketConnectionEvent.PPMessage, ...)`<br>- 라우팅 (broadcast 또는 특정)
**입력 명세**:<br>- `GET /api/pp-message?message=click&value=button1`<br>- `POST /api/pp-message` body: `{ message: 123, value: "data" }` (number/string)
**출력 명세**:<br>- 200: `{ result: 'ok' }`<br>- 400: invalid message
**상태·저장**: 메모리 `_event` (EventEmitter)
**에러·엣지**: 파라미터 누락 400, 잘못된 타입 400
**코드 위치**:<br>- `server/src/server/manager/MessageManager.ts:4-14`<br>- `server/src/server/controllers/pp-message.controller.ts:1-56`<br>- `server/src/server/routes/pp-message.ts:1-15`
**알려진 quirk**:<br>- 라우팅 로직 없음 (EventEmitter만, 라우팅은 리스너가)<br>- message는 number/string 모두
---
### MSG-2. SSL 인증서 제공
**한줄 요약**: 자체 서명/CA 인증서, HTTPS 지원.
**진입점**: 브라우저 HTTPS 연결 시 자동
**모드**: 전부
**코드 위치**: `server/src/server/routes/certificate.ts`
---
### MSG-3. QR 코드 생성
**한줄 요약**: ProtoPie Player 원격 접근용 QR 생성. URL·포트·PIE ID 인코딩 → 이미지 데이터 URL.
**진입점**: UI Component `/components/ListView/ListViewPopups/QRCodeDialog/`. Library `qrcode-generator`.
**모드**: 전부
**동작 흐름**:<br>1. 사용자가 프로토타입 목록에서 “QR 코드”<br>2. `QRCodeDialog` 표시<br>3. `generateQRCode(address, pieId)`:<br>- `qrcodeGenerator(0, 'M')`<br>- 데이터: `protopie-studio:ADDR:{host};PORT:{port};TOKEN:{pieId};`<br>- `qr.make()`<br>- `qr.createDataURL(8, 0)` (셀 8px, 정정 0)<br>4. `<img src={dataURL}>`
**입력 명세**: `generateQRCode(address: "192.168.1.1:8080", pieId: "123")`
**출력 명세**: Data URL `data:image/png;base64,...`, 크기 180x180px (UI 고정)
**상태·저장**: 실시간 생성 (저장 없음)
**에러·엣지**: 잘못된 주소: 인코딩 실패 (에러 처리 없음)
**코드 위치**:<br>- `server/src/components/ListView/ListViewPopups/QRCodeDialog/index.tsx:1-93`<br>- `package.json: "qrcode-generator": "^1.4.3"`
**알려진 quirk**:<br>- 프로토콜 `protopie-studio:` 커스텀 URI 스킴<br>- 셀 크기 8px 고정
---
### MSG-4. HLS 스트리밍 (비디오)
**한줄 요약**: HLS 스트림(`.m3u8`) 재생 지원.
**진입점**: 프로토타입 내 비디오 플레이어 자동 사용
**모드**: 전부 (Web Player)
**외부 의존**: `hls.js` \^1.4.12
**코드 위치**: `package.json: "hls.js": "^1.4.12"`
---
### MSG-5. Unity 레이어 지원 (WebGL)
**한줄 요약**: Unity WebGL 빌드를 Stage 레이어로 삽입.
**진입점**: Stage → 레이어 추가 → Unity 타입 선택
**모드**: 전부 (Web Player)
**외부 의존**: `react-unity-webgl` \^9.5.0
**코드 위치**:<br>- `server/src/server/manager/UnityManager/UnityFileUtil.ts`<br>- `server/src/components/StageView/Stage.tsx`<br>- `package.json: "react-unity-webgl": "^9.5.0"`
---
### MSG-6. Swagger API 문서
**한줄 요약**: REST API 명세, 개발자 탐색·테스트.
**진입점**: `/swagger` 또는 `/swagger-ui`
**모드**: 전부 (개발/테스트)
**외부 의존**: `swagger-jsdoc`, `swagger-ui-express`
**코드 위치**: `server/src/server/routes/swagger.ts`
---
## 3. 외부 의존성 정리 (사용자 가시 기능 관련)
<table header-row="true">
<tr>
<td>의존성</td>
<td>용도</td>
<td>버전</td>
</tr>
<tr>
<td>`adbkit`</td>
<td>Android USB 연결</td>
<td>\^2.11.1</td>
</tr>
<tr>
<td>`usbmux`</td>
<td>iOS USB 연결</td>
<td>\^0.1.0</td>
</tr>
<tr>
<td>`serialport`</td>
<td>Serial 포트 통신</td>
<td>\^10.5.0</td>
</tr>
<tr>
<td>`aedes`</td>
<td>MQTT 브로커</td>
<td>\^0.42.4</td>
</tr>
<tr>
<td>`socket.io` / `socket.io-client`</td>
<td>실시간 통신</td>
<td>\^4.6.1</td>
</tr>
<tr>
<td>`next`</td>
<td>웹 프론트엔드</td>
<td>\^11</td>
</tr>
<tr>
<td>`protopie-webengine-dist`</td>
<td>ProtoPie 렌더링 엔진</td>
<td>v10.0.1</td>
</tr>
<tr>
<td>`codemirror`</td>
<td>커스텀 플러그인 콘솔</td>
<td>\^6.0.1</td>
</tr>
<tr>
<td>`lottie-web`</td>
<td>애니메이션</td>
<td>\^5.12.2</td>
</tr>
<tr>
<td>`hls.js`</td>
<td>HLS 스트리밍</td>
<td>\^1.4.12</td>
</tr>
<tr>
<td>`react-unity-webgl`</td>
<td>Unity WebGL</td>
<td>\^9.5.0</td>
</tr>
<tr>
<td>`qrcode-generator`</td>
<td>QR 코드</td>
<td>\^1.4.3</td>
</tr>
<tr>
<td>`d3`</td>
<td>데이터 시각화</td>
<td>\^7.8.5</td>
</tr>
<tr>
<td>`sqlite3`</td>
<td>로컬 DB</td>
<td>\^5.1.6</td>
</tr>
<tr>
<td>`sequelize`</td>
<td>ORM</td>
<td>\^6.29.3</td>
</tr>
<tr>
<td>`logitech-g29`</td>
<td>G29 게임패드</td>
<td>\^1.3.0</td>
</tr>
</table>
---
## 4. 숨겨진 기능 (UI 외 API/CLI/Socket으로만 접근)
<table header-row="true">
<tr>
<td>기능</td>
<td>진입점</td>
<td>비고</td>
</tr>
<tr>
<td>직접 .pie 업로드 (HTTP)</td>
<td>`POST /api/pies/add`</td>
<td>UI 없이 자동화 가능</td>
</tr>
<tr>
<td>커스텀 플러그인 업로드</td>
<td>`POST /api/plugins`</td>
<td>CLI·CI에서 사용</td>
</tr>
<tr>
<td>Cloud 프로젝트 생성</td>
<td>`POST /cloud/teams/:teamId/projects`</td>
<td>UI는 일부만 노출</td>
</tr>
<tr>
<td>토큰 관리 (로컬만)</td>
<td>`/api/tokens` (requireLocalAccess)</td>
<td>보안 — 로컬 호스트</td>
</tr>
<tr>
<td>Serial 포트 상태 요청</td>
<td>Socket.IO `request-serialports-state`</td>
<td>UI 미노출</td>
</tr>
<tr>
<td>MQTT 클라이언트 연결</td>
<td>MQTT broker port 1883</td>
<td>외부 IoT 직결</td>
</tr>
<tr>
<td>Hashify (보안 토큰)</td>
<td>`POST /cloud/hashify`</td>
<td>내부 보안</td>
</tr>
<tr>
<td>Proxy 테스트</td>
<td>`POST /api/proxy-test`</td>
<td>UI 설정 화면만</td>
</tr>
</table>
---
## 5. Deprecated / 실험적
<table header-row="true">
<tr>
<td>항목</td>
<td>상태</td>
<td>비고</td>
</tr>
<tr>
<td>Old Database Loader</td>
<td>deprecated</td>
<td>`OldVersionDatabaseLoader.ts` 존재하나 주석 처리</td>
</tr>
<tr>
<td>Cloud 이벤트 로깅</td>
<td>불완전</td>
<td>`cloud.ts` 안 `TODO EVENT LOGS` 주석</td>
</tr>
</table>
---
## 6. 변경 이력
[LEGACY_FEATURE_INVENTORY_CHANGELOG.md](./LEGACY_FEATURE_INVENTORY_CHANGELOG.md) 참고.
