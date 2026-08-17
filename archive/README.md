# 아카이브

보관용. 참조하지 않는다.

| 파일 | 무엇 |
|---|---|
| `Cloud_Connect_Spec_rev16.md` | 분리 전 통합 스펙 문서 (150KB, 721줄, rev16 / 2026-06-12) |

## Cloud_Connect_Spec_rev16.md 를 왜 남겼나

2026-08-17에 이 문서를 두 개로 쪼갰다.

- **SSOT에 없는 스펙** → [`spec.md`](../spec.md)
- **테스트 기준** → [`qa-guide.md`](../qa-guide.md)

나머지(기능 동작 설명, 아키텍처, 용어 정의, Capability Matrix, Decision Log, 출처 목록, 갱신 절차)는
**SSOT가 이미 갖고 있어서 버렸다.** → https://ssot.protopie.works/ko/connect/

버린 내용을 확인해야 할 때만 이 파일을 연다. git 이력에도 남아 있다.

## 원본에 있던 것 → 어디로 갔나

| 원본 섹션 | 결과 |
|---|---|
| §0 한눈에 보기 | 버림 (SSOT `10-overview`, `40-product-overview`) |
| §1 용어 정의 | 버림. 단 **권한 3축 + View/Interaction Mode**는 `spec.md` §1로 |
| §2 아키텍처 | 버림 (SSOT `41-cloud`, `42-desktop`, `43-embedded`) |
| §3 Capability Matrix | 버림 (SSOT 각 문서의 플랫폼 표) |
| §3-2 플랜별 정량 한도 | 버림 (SSOT `30-bm-pricing`) |
| §4-1 F-HOM | 버림 (SSOT `45-workspace`) |
| §4-2 F-IDM | → `spec.md` §2 |
| §4-3 F-STG | 버림 (SSOT `44-core-features`) |
| §4-4 F-PLG | 버림 (SSOT `47-layers-plugins`) |
| §4-5 F-BRG | 버림 (SSOT `42-desktop`) |
| §4-6 F-CLD | 버림 (SSOT `41-cloud`) |
| §4-7 F-REL | 버림 (SSOT `44-core-features`) |
| §4-8 F-VWR | **권한·모드 부분만** → `spec.md` §3. 기능 동작은 버림 (SSOT `46-share`) |
| §4-9 F-AUD | 버림 (SSOT `48-console`). 단 Record/Import 미결 1건은 `spec.md` Q-11로 |
| §4-10 F-API | → `spec.md` §7 |
| §5 핵심 시나리오 | 버림 (SSOT Scenario) |
| §6 에러 카탈로그 | → `spec.md` §6 |
| §7 Non-goals | → `qa-guide.md` §3 |
| §8 정량 목표 (Beta) | 버림 — 임계값이 끝까지 안 채워졌고 베타 Go/No-Go용이라 만료 |
| §9 테스트 환경 | → `qa-guide.md` §1 |
| §9-2 회귀 시드 | → `qa-guide.md` §4 |
| §10 검증 우선순위 | → `qa-guide.md` §2. 미결 항목은 `spec.md` §4로 분리 |
| §11 Decision Log | 버림 (SSOT `changelog`가 코드 근거까지 포함해 관리) |
| §12 출처 | 버림 (`sources/README.md`가 같은 역할) |
| §13 Legacy ↔ CoC Delta | → `spec.md` §5 |
| §14 갱신 절차 | 버림 → `AGENTS.md`로 재작성 |
