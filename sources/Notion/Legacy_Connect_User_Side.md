# 📃 Legacy Connect (User Side)

> Notion 최종본 아카이브 · 원본: https://app.notion.com/p/36845184b5da8039a1d0fff338b723a5
> Notion view 시점: 2026-05-27T08:51:33.764Z
> CoC 스쿼드 종료(2026-06-30) 인수인계용. 원본 마크다운(표 포함) 그대로 보존.

---

작성일 : 2026.5.22

# 🔌 ProtoPie Connect 기능 목록
유저 관점에서 정리한 ProtoPie Connect의 전체 기능 리스트. 공식 문서([protopie.io/learn/docs/ko/connect](http://protopie.io/learn/docs/ko/connect)) 기준으로 작성.

> 💡 ProtoPie Connect는 **로컬 통신 서버** 역할을 하며 여러 기기, 디스플레이, 하드웨어, API, 플러그인, 브릿지앱을 하나로 연결하는 확장 앱. **Connect Free**(기본 제공), **Connect Core**(Basic/Pro 플랜 애드온), **Connect Enterprise**(Enterprise 기본 포함) 3가지 등급으로 제공.

---

## 📋 프로토타입 관리
- **프로토타입 추가 / 제거 / 교체**
  - New 버튼 클릭 또는 드래그&드롭으로 Pie 파일 추가.
  - 교체 시 동일 pieId 유지 → 메시지 연결 보존 (Replace > Cloud Pie, Local Pie)
- **Pie 그룹 구성**
  - 프로토타입을 그룹으로 묶어 관리.
  - Stage View 링크 복사, reload, delete, Stage View open
  - 드래그&드롭으로 그룹 간 이동, 그룹명 더블클릭으로 이름 변경
- **Studio 변경사항 자동 동기화 (로컬 저장 Pie파일)**
  - Connect에 로드된 프로토타입이 Studio에서 수정되면 변경사항이 자동 반영됨
- **Cloud Pie 사용**
  - ProtoPie Cloud에 업로드된 프로토타입을 Connect에서 바로 불러와 실행
  - Pie파일 편집 후 수동 리로드 필요
- **Local Pie 사용**
  - 로컬 디스크의 .pie 파일을 직접 불러와 실행.

---

## 📱 다기기 테스트
- **ProtoPie Player 연결 — QR 코드**
  - Connect에서 QR 코드를 띄우고 Player 앱으로 스캔하면 즉시 프로토타입 실행. iOS·Android·iPadOS 지원
- **ProtoPie Player 연결 — IP 주소 입력**
  - 동일 WiFi 네트워크에서 Connect에 표시된 IP(포트 9981)를 Player에 직접 입력해 연결
- **ProtoPie Player 연결 — USB 케이블**
  - WiFi 없이도 USB 케이블로 기기를 직접 연결해 프로토타입 테스트 가능
- **ProtoPie Player for Wear OS** (애플 워치 지원안함)
  - 스마트워치 프로토타입 테스트. Connect와 Wear OS 앱이 자동으로 페어링.
  - Wear OS 화면 두 번 탭으로 재시작/종료

---

## 🌐 웹 브라우저 플레이어
- **MultiView — 단일 탭에서 다중 프로토타입 동시 실행**
  - 여러 프로토타입이 포함된 그룹의 우측에 위치한 "View"(MultiView) 아이콘 클릭
  - 단일 브라우저 탭에서 멀티스크린 구현.
  - 배경색, 크기, 레이아웃 커스터마이징 가능
- **URL 파라미터로 뷰 옵션 제어**
  - `fullscreen`, `bg`, `hotspotHints`, `cursorHide`, `scaleToFit` 등 URL 파라미터로 세밀하게 표시 방식 제어 가능
- **웹 브라우저에서 음성 프로토타이핑**
  - Voice Command Trigger, Speak Response, Listen Response를 Web Player에서도 사용 가능. Chrome·Edge(Chromium) 최적화
  - 192.x.x.x 의 IP 구성시 일회성 브라우저 설정 필요
    - 구성의 IP는 Secure Context 정책상 마이크&카메라 사용시 일회용 허가만 하는걸로 알고 있습니다.
      - `https://192.168.x.x` ✅ 가능 (권한 요청 후)
      - `http://192.168.x.x` ❌ 불가 (비보안 컨텍스트) → 레거시 커넥트는 이거 사용중이라.
      - `http://localhost` ✅ 가능 (예외 허용)
      - `http://127.0.0.1` ✅ 가능 (예외 허용)
- **다른 기기 브라우저에서 원격 실행**
  - 동일 LAN 내 다른 기기의 브라우저에서 Connect IP 주소로 접속해 프로토타입 실행 (`http://[IP]:9981`)
  - PIN code 입력 필요

---

## 🖥️ Stage View — 커스텀 레이어 통합
- **Web Embed 레이어** `Free: 1개` / `Core+: 무제한`
  - URL 또는 iframe 코드로 외부 웹 콘텐츠 삽입.
  - Maps, Spline, Rive, Bezi 등 다양한 포맷 지원.
  - Stage에서 자유롭게 배치·크기 조정
- **Live Camera 레이어** `Free: 1개` / `Core+: 무제한`
  - USB 웹캠, 노트북 카메라, HLS 라이브 스트리밍 URL을 Stage에 레이어로 삽입.
  - 카메라 속성 패널에서 설정
- **Unity 레이어** `Core: 1개` / `Enterprise: 무제한`
  - Unity WebGL 빌드를 Stage에 레이어로 삽입.
  - Unity Plugin 설치 시 키보드 입력 충돌 해결 및 양방향 메시지 통신 가능

---

## 🔌 내장 플러그인
코드 없이 설정만으로 하드웨어, 서비스 연결 가능. Core 플랜은 동시 실행 3개 / Free는 1개 제한 (실행 시간 각각 무제한 / 3분).
- **API 플러그인**: REST API와 프로토타입 연동
- **IFTTT 플러그인**: IFTTT Webhook으로 외부 서비스 연결
- **Logitech G29 플러그인**: 레이싱 스티어링 휠 입력 연동
- **Arduino 플러그인**: Arduino 하드웨어 시그널 연동
- **Gamepad 플러그인**: 게임패드 컨트롤러 입력 연동
- **blokdots 플러그인**: blokdots 하드웨어 프로토타이핑 툴 연동
- **Unity 플러그인** (Stage view): Unity 씬과 양방향 메시지 통신

---

## 🧩 커스텀 플러그인 & Bridge App `Enterprise`
- **커스텀 플러그인 업로드**
  - Socket.IO를 지원하는 모든 하드웨어, API, 앱과 연결 가능.
  - .zip으로 패키징 후 Connect에서 바로 실행.
- **Bridge App 연동**
  - Node.js 기반 Bridge App으로 하드웨어 신호 ↔ Socket.IO 메시지 변환.
  - 하드웨어 입력을 ProtoPie가 이해하는 메시지로 중계.
  - API JSON 응답도 메시지로 변환 가능

---

## 🐛 디버깅 & 메시지 모니터링
- **실시간 메시지 대시보드**
  - Connect 인터페이스 우측에서 연결된 모든 프로토타입·플러그인·하드웨어와 주고받는 메시지를 실시간으로 확인
- **테스트 메시지 직접 전송**
  - 대시보드에서 직접 메시지를 보내 프로토타입이 올바르게 수신하는지 검증. 하드웨어 없이 메시지 연동 테스트 가능
- 주고 받은 메세지 레코딩 기능 `Enterprise`
  - CSV파일로 저장 가능
- CSV파일 임포트 기능 `Enterprise`
  - 임포트된 메세지로 Stage View 가동 실행 가능 (메세지가 없는 인터렉션은 대응 하지 않음)
  - 세팅에서 반복재생 설정 가능 / 재생 속도 설정 가능

---

## 🖥️ Connect Embedded `Enterprise`
- **임베디드 시스템 실행**
  - Raspberry Pi 등 임베디드 시스템에서 Connect를 터미널 기반 독립 서버로 실행.
  - 상설 설치형 데모 환경 구축에 활용

---

## ✨ Enterprise 전용 추가 기능
- **메시지 Recording & Playback** `Enterprise`: 실행 중 메시지 기록·재생. 시나리오 반복 재현·데모 자동화.
- **커스텀 폰트 지원** `Enterprise`: 프로토타입에 커스텀 폰트 적용. 브랜드 폰트 기업 데모.
- **ProtoPie Plugin for Unity** `Enterprise`: Unity ↔ ProtoPie 양방향 통신. WebGL 키보드 입력 충돌 방지. Automotive HMI + 3D 데모.
- **스마트워치 프로토타이핑** `Enterprise`: Player for Wear OS 페어링, 실기기 인터랙션 테스트. Smartwatch Solution 패키지 포함.

---

## 📊 플랜별 주요 기능 비교

| 기능 | Free | Core | Enterprise |
|---|---|---|---|
| 동시 실행 프로토타입 | 2개 | 무제한 | 무제한 |
| 동시 Player 연결 | 2개 | 무제한 | 무제한 |
| 로컬 Pie 사용 | ✗ | ✓ | ✓ |
| 워터마크 | 있음 | 없음 | 없음 |
| API 플러그인 설정 수 | 1개 | 3개 | 무제한 |
| 플러그인 동시 실행 | 1개 | 3개 | 무제한 |
| 플러그인 실행 시간 | 3분 | 무제한 | 무제한 |
| Stage Views 수 | 1개 | 무제한 | 무제한 |
| Web Embed / Camera 레이어 | 각 1개 | 무제한 | 무제한 |
| Unity 레이어 | ✗ | 1개 | 무제한 |
| 커스텀 플러그인 & Bridge App | ✗ | ✗ | ✓ |
| Unity Plugin (양방향 통신) | ✗ | ✗ | ✓ |
| 스마트워치 프로토타이핑 | ✗ | ✗ | ✓ |
| 커스텀 폰트 지원 | ✗ | ✗ | ✓ |
| 메시지 Recording & Playback | ✗ | ✗ | ✓ |
| Connect Embedded | ✗ | ✗ | 별도 문의 |
