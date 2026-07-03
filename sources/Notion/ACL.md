# ACL

> Notion 최종본 아카이브 · 원본: https://app.notion.com/p/36c45184b5da803bb98cd2f62f9f595d
> Notion view 시점: 2026-06-10T05:15:09.574Z
> CoC 스쿼드 종료(2026-06-30) 인수인계용. 원본 마크다운(표 포함) 그대로 보존.

---

<details>
<summary>기존 Connect Spec (접힘)</summary>

## 1. 권한 모델 구조
기존 Connect 권한 모델은 크게 두 축으로 구성된다.
- **Role**
  - 팀 운영 및 관리 권한 정의
  - 멤버 관리, 설정 변경, 결제/소유권 관리 등의 책임 범위 결정
- **Seat**
  - 제품 기능 접근 범위 정의
  - Design, UT, Dev 등 실제 사용 가능한 기능 범위 결정

### 핵심 원칙
- Role과 Seat는 독립적으로 동작
- "Full"은 권한(Role)이 아니라 상업적 번들(commercial bundle) 개념으로 정의
- 실제 권한은: Team Role → Seat → Resource-level access 순서로 판정됨

---

## 2. Team Role 정의
### Owner
팀당 1명만 존재 가능.
**권한 범위**: Admin 권한 전체 포함 / 결제 및 구독 관리 / 팀 삭제 / Owner 승계 / 전체 데이터 Export/Delete / 최종 소유 권한 보유
**제약 조건**: 마지막 Owner는 승계 없이 제거/탈퇴 불가

### Admin
팀 운영 담당 역할.
**권한 범위**: 멤버 초대/제거 / Seat 할당 / 워크스페이스 설정 변경 / 운영 관리 기능 수행
**제약 조건**: 최소 1명의 Admin 또는 Owner 유지 필요 / 마지막 관리자 제거 시 시스템 차단

### User
일반 멤버 역할. 실제 기능 접근 범위는 Seat에 의해 결정됨.

### Org Owner
Organization 레벨 역할. Team Role을 대체하지 않음 / 명시적 권한 부여 없이는 팀 콘텐츠 접근 불가.

---

## 3. Seat 정의
- **View**: 콘텐츠 열람 / 코멘트 가능
- **Design**: 프로토타입 생성 및 편집 / 라이브러리 사용 / 공유 설정 관리
- **UT**: UT 세션 생성 및 관리 / 결과 접근
- **Dev**: View 권한 포함 / 코드 스니펫 접근 / Connect 기능 접근 / API 접근
- **Full**: 모든 Seat 포함 / 상업적 번들 개념

### Seat 동작 규칙
- **복수 Seat 허용**: 하나의 멤버는 여러 Seat 동시 보유 가능
- **권한 계산 방식**: Seat 권한은 합집합(union) 기준 적용, 상하위 상속 구조 없음
  - 예: Design + Dev → 두 권한 모두 활성화. View는 자동 상속 개념이 아니라 개별 포함 기준

---

## 4. 권한 가드레일
- **Owner 연속성**: 팀에는 항상 1명의 Owner 필요 / 마지막 Owner 제거·탈퇴 불가 / Owner 승계 후에만 제거 가능
- **관리자 연속성**: 최소 1명의 Admin 또는 Owner 유지 필요 / 마지막 관리자 제거 시 시스템 차단
- **Billing 권한**: Owner 전용, 위임 불가 정책
- **충돌 시 판정 우선순위**: 1) Team Role → 2) Seat → 3) Resource-level access. 제한적인 정책이 우선 적용됨.

---

## 5. Legacy 권한 → 신규 모델 매핑

| Legacy Role | 신규 모델 |
|---|---|
| Team Owner | Owner |
| Team Admin | Admin |
| Editor | User + Design |
| Viewer | User + View |
| Moderator | User + UT |

### Audit 정책
변경 이력 기록 대상: Role 변경 / Seat 변경. 모든 변경 이력은 Audit 가능해야 함.

---

## 6. 콘텐츠(Pie) 단위 권한 모델
- **isVisible**: 콘텐츠 노출 여부 정의. 판정 예시 — 개인 Pie 여부 / 팀 멤버 여부 / 프로젝트 멤버 여부
- **isAvailable**: 실제 사용 가능 여부 정의. 판정 예시 — 구독/플랜 상태 / Editor 여부 / 기능 접근 권한. isVisible이 true인 상태를 전제로 추가 판정.
- **기능별 예외 처리**: 구독 만료 시 Download 제한 / 공유 설정 강제 변경 / Version History 제한 / Move/Copy 제한 / Record 제한
- **Connect Cloud 적용 시사점**: Visibility vs Availability 분리 / 기능별 예외 정책 구조 / 프로젝트·파이·UT 결과 단위 세분화 접근 제어 재사용 가능

## 7. Connect 권한 정보의 아키텍처 반영
Connect V2 아키텍처 기준: 인증/세션(JWT)에 권한 정보 포함 — tenantId, role, kind 등이 토큰 claim으로 stamp됨. 핵심 권한 판정 키: Tenant(Workspace/Team) / Role / Session 기반 Claim.

## 8. 추가 참고 사항
Permission 릴리즈 히스토리(Pie Owner 제거, Role/Permission 구조 변경 등) 추적 가능. 참고: Jira / Confluence / QA Release 문서.

</details>

## 1. 권한 모델

| 구분 | 내용 |
|---|---|
| 모델 | 2-Role (Editor / Viewer) |
| 변경 범위 | 최소 변경 — 기존 Connect 구조 유지 |
| 진입 경로 | Role을 결정하는 유일한 기준은 Team Space 소속 여부 + Connect 접근 권한 |
| 편집 권한 | Stage 편집 = Editor 전용, Viewer에게 부여 불가 |
| Interaction | Viewer는 기본 View-only, 개인 토글로 Interaction mode 전환 가능 |

**진입 경로 요약**: Team Space 멤버 + Connect 접근 권한 → [EDITOR] → 공유 링크 / QR 생성 → [VIEWER] (계정 없이 접근 가능) → 기본: View-only → 토글 → Interaction mode

## 2. Role 정의

### Editor
- **대상:** Connect를 구매한 Team + 동일 Team Space에서 Stage에 접근한 모든 팀원
- **진입 경로:** Team Space 로그인 상태에서 Stage 접근 시 자동 부여

| 카테고리 | 기능 | 가능 여부 | 비고 |
|---|---|---|---|
| **Stage 편집** | Pie 추가 / 삭제 / 교체 / 재로드 | ✅ | |
| | Embed layer 추가 / 설정 / 삭제 | ✅ | |
| | Canvas 크기 조정 / 이동 | ✅ | |
| | Plugin 연결 (Built-in) | ✅ | |
| **하드웨어** | Bridge App 추가 | ✅ App 전용 | Cloud Web 불가 |
| | Hardware 연결 (USB HID, Serial 등) | ✅ App 전용 | Cloud Web 불가 |
| **Preview** | Pie preview (웹 브라우저) | ✅ | |
| | Stage instance 확인 | ✅ | |
| | Stage View (전체 레이아웃) | ✅ | |
| **Player** | QR / USB 연결 | ✅ | |
| | Player source 교체 | ✅ | |
| **Log / Debug** | Console 로그 확인 / 기록 | ✅ | |
| | Node View 확인 | ✅ | |
| | Node View 편집 | ✅ | |
| | Recording / Playback | ✅ | |
| **공유** | Viewer 초대 링크 / QR 생성 | ✅ | |

### Viewer
- **대상:** Connect 접근 권한 없는 외부 사용자. URL / QR Code로 Stage에 접근
- **진입 경로:** Editor가 생성한 공유 링크 또는 QR Code 통해 접근 (계정 불필요)
- **기본 상태: View-only mode**

| 카테고리 | 기능 | 가능 여부 | 비고 |
|---|---|---|---|
| **Stage 편집** | 모든 편집 기능 | ❌ | 토글해도 불가 |
| **Preview** | Stage instance 확인 (보기) | ✅ | |
| | Pie 실행 / 인터랙션 | ❌ | 토글 전 기본값 |
| | 메시지 전송 | ❌ | 토글 전 기본값 |
| **Log / Debug** | Node View 확인 | ✅ | URL로만 공유 가능 |
| | Node View 편집 | ❌ | |
| | Console 로그 | ❌ | |
| **Player** | QR / USB 연결 | ❌ | Player 내 접근 불가. Editor만 Player를 연결할 수 있으며, Guest/Viewer는 브라우저 Preview에서만 Pie를 조작할 수 있다. |
| **하드웨어** | 모든 하드웨어 기능 | ❌ | |

**Interaction Mode 전환 (토글)**: Viewer 화면 내 토글로 개인이 직접 전환. 권한 관리 없음, 개인 설정.
⚠️ Stage 편집은 Interaction mode에서도 불가. 토글은 실행 권한만 부여, 구조 변경 불가.

| 전환 후 추가 가능 기능 | 내용 |
|---|---|
| Pie 실행 | Stage 위의 Pie에 실제 인터랙션 가능 |
| 메시지 전송 | 인터랙션에 따른 메시지 발생 / 전송 가능 |
| 여러 명 동시 가능 | 동일 Pie에서 다수 Viewer가 동시 Interaction mode 가능 |

## 3. Platform별 기능 제약
하드웨어 연결은 Desktop App 전용. Cloud Web에서는 Bridge App / Plugin 포함 모든 하드웨어 기능 비활성화.
Connect Cloud는 Team 바운더리를 넘는 리소스 접근을 허용하지 않음. 모든 Pie 조회, 선택 및 연결은 현재 선택된 Team 범위 내에서만 가능.

| 기능 | Cloud Web | Desktop App (로그인) | Desktop App (License key) |
|---|---|---|---|
| Cloud Stage 조회 | ✅ | ✅ | ❌ |
| Cloud Stage 생성 | ✅ | ✅ | ❌ |
| Local Stage 조회 | ❌ | ✅ | ✅ |
| Local Stage 생성 | ❌ | ✅ | ✅ |
| **하드웨어 연결** | **❌** | **✅** | **✅** |
| Bridge App | ❌ | ✅ | ✅ |
| Built-in Plugin | ❌ | ✅ | ✅ |
| Cloud Pie → Local Stage 추가 | ❌ | ✅ | ❌ |
| 원격 연결 (Cross-network) | ✅ | ❌ | ❌ |
| Local Pie Import | **❌** | ✅ | ✅ |

### 추가 설명
- **Team Scope**: Connect Cloud와 Connect Desktop 모두 Team 단위 접근 제어. 여러 Team 소속이라도 Pie 조회·사용 범위는 현재 선택된 Team으로 제한.
- **Pie Visibility**: 현재 선택된 Team에 속한 Pie만 조회·선택 가능. 조회 불가 — 다른 Team의 Pie(Editor/Viewer 권한 무관), Personal Space Pie. 요약: Team 간 Pie 공유·교차 참조 미지원.
- **Pie Layer Creation**: Pie Layer 추가 시에도 동일 ACL 적용. Cloud/Desktop 모두 현재 선택된 Team의 Pie만 선택 가능.
- **Resource Ownership**: Stage는 Team에 종속 / Pie는 Stage에 종속 → Stage에 연결된 Pie는 Team 범위 내에서 관리.
- **Imported Pie Persistence**: Pie가 Stage에 추가된 이후에는 Stage 리소스로 관리(Legacy Connect와 동일). 원본 Pie 삭제되어도 이미 연결된 Pie는 유지·정상 동작해야 함.

### 4. Node View 접근 규칙
Node View는 URL로만 Viewer에게 공유 가능. Stage Player 내부에서 Viewer가 직접 진입하는 경로 없음.
- (TBD) 플레이어 진입 경로에서는 노드 뷰로의 이동을 비활성화한다?? Editor는 Player 내 접근 가능? Viewer 공유 제약만? — Player 내 접근이 Editor에게도 차단되는지 확인 필요.

| Role | 접근 방법 | 확인 | 편집 | 비고 |
|---|---|---|---|---|
| Editor | Player / URL | ✅ | ✅ | 다만, 노드 뷰는 플레이어를 통해 접근할 수 없다 |
| Viewer | URL 직접 공유만 가능 | ✅ | ❌ | - |
| Viewer | Player / Stage 화면 내 | ❌ | ❌ | - |

### 5. 기존 개념과의 매핑 (이전 → 현재)

| 이전 개념 | 현재 | 비고 |
|---|---|---|
| Host | Editor | 동일 |
| Editor | Editor | 동일 |
| Participant (Guest) | Viewer + Interaction mode ON | 토글로 흡수 |
| Viewer | Viewer (기본 View-only) | 동일 |
| Guest ↔ Viewer 전환 | Viewer 내 토글로 처리 | Role 전환 아님, mode 전환 |
| Private Stage | **이번 스코프 제외** | 추후 고려 |

### 6. 미결 사항

| # | 질문 | 영향 범위 |
|---|---|---|
| 1 | Viewer가 Interaction mode ON 시 Editor에게 알림 필요한가? | UI, 실시간 상태 표시 |
| 2 | 동일 Pie에 다수 Viewer가 동시 인터랙션 시 충돌 처리 방식 | Engine, 인스턴스 설계 |
| 3 | Viewer용 공유 링크 만료 정책 (시간 제한, 무기한) | 보안, 운영 |
| 4 | Node View URL 공유 시 Viewer 인증 여부 (무인증 접근 허용할지) - PIN? | 보안 |
| 5 | Interaction mode 토글을 Editor가 비활성화할 수 있는가? (잠금 여부) | 권한 설계 |
