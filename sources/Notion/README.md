# Notion 최종본 아카이브

CoC 스쿼드 종료(2026-06-30) 시점의 Notion 페이지 최종본을 마크다운으로 아카이브. 원본 표·구조 그대로 보존. 각 파일 상단에 원본 URL과 Notion view 시점 기재.

> 왜 md인가: md라야 검색·diff·텍스트 파싱이 됨. (구버전 PDF 4개는 정리 시 삭제 — git 이력에서 복원 가능.)

| 파일 | 원본 페이지 | view 시점 | 비고 |
|---|---|---|---|
| [Design_Brief.md](Design_Brief.md) | Connect on Cloud (Design Brief) | 2026-07-03 | spec rev12/15/16 핵심 근거. 용어(Stage/Instance)·Capability matrix·권한·Home/Stage 디자인 스펙. 이미지는 Notion 원본 참조 |
| [SSOT.md](SSOT.md) | SSOT | 2026-07-02 | 최신 확정본. 아키텍처·데이터모델·네트워크 |
| [ACL.md](ACL.md) | ACL | 2026-06-10 | 2-Role(Editor/Viewer), Platform 제약, §6 미결 5건 |
| [PRD_Draft.md](PRD_Draft.md) | PRD - Draft | 2026-07-02 | 제품 요구사항 |
| [Legacy_Connect.md](Legacy_Connect.md) | Legacy Connect | 2026-07-02 | 레거시 Connect 스펙 |
| [Legacy_Connect_User_Side.md](Legacy_Connect_User_Side.md) | Legacy Connect (User Side) | 2026-05-27 | 유저 관점 기능 목록, 플랜별 비교표 |
| [GLOSSARY.md](GLOSSARY.md) | GLOSSARY - WIP | 2026-05-09 | ⚠️ WIP·stale. Tenant/Room 모델은 CoC 확정(Room→Stage 통일)과 다름 — 용어 참고용 |

갱신 방법: 각 페이지를 Notion MCP(`notion-fetch`)로 다시 받아 같은 포맷으로 덮어쓰기.
