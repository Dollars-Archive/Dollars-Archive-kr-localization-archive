# 웹 설치 가이드 공통 템플릿

GPT·Codex가 게임 저장소의 설치 페이지를 만들 때 복제하는 실제 파일입니다. 먼저 [운영 표준](../../workflow/GITHUB-PAGES-INSTALL-GUIDE-STANDARD.md)을 읽습니다.

## 적용

1. 대상 저장소의 기본 브랜치·Pages·기존 `docs/`를 확인합니다.
2. 이 폴더의 `docs/`를 설치 페이지 위치에 복제합니다. 기존 사이트는 필요한 파일만 병합합니다.
3. `docs/assets/config.js`에서 저장소, 브랜치, 게임명, 플랫폼, 문서 경로를 채웁니다.
4. `docs/index.html`의 제목·설명을 게임에 맞게 바꾸고 `style.css`의 포인트 색을 조정합니다.
5. 원본 `INSTALL.md`를 준비합니다. 기존 문서가 없을 때만 `INSTALL.template.md`를 참고합니다.
6. 해당 게시 방식으로 배포하고 실제 본문·이미지·Release 링크를 확인합니다.
7. 마지막으로 README·Release의 설치 안내를 확인된 Pages URL로 바꿉니다.

기본값은 GitHub 원본 읽기입니다. Pages의 사본을 읽는 기존 사이트에 적용하려면 `sourceMode: 'published'`로 바꾸고 사본 동기화·재배포 workflow도 확인합니다. 이 템플릿에는 그 workflow가 포함되어 있지 않습니다.

`releaseUrl`은 공개 Release가 있을 때만 설정합니다. 한 게임의 정식 배포는 `/releases/latest`, 독립 프로젝트가 여럿이면 명시적 배포 주소를 사용합니다.

## 포함 기능

목차, callout, 코드 복사, 상대 이미지·링크 보정, 모바일·다크모드, 읽기 실패 시 원본 링크를 제공합니다. Marked 18.0.14와 DOMPurify 3.4.16을 고정 CDN 주소로 불러옵니다. CDN 접속이 막혀도 오류 안내가 나오며, 게임 파일·인증·외부 API 키는 필요하지 않습니다.

CSS의 공통 레이아웃은 이 아카이브의 문서 뷰어와 같은 계열입니다. 버전 정보는 원문에 기록하며 고정 배지에 추측값을 넣지 않습니다.

`file://`로 HTML을 열지 말고 로컬 HTTP 서버 또는 Pages에서 확인하세요. 화면 검증과 배포 검증은 별도로 수행합니다.
