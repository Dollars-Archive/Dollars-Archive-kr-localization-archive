# Dollars Archive · KR Localization Archive

한국어 패치 제작 과정에서 얻은 **범용 기술 노트, 실패/해결 기록, 자동화·검증 노하우, GPT/GitHub 운용 팁**을 모아두는 공개 아카이브입니다.

특정 게임의 원본 데이터나 개인정보를 보관하는 저장소가 아닙니다.

> [!TIP]
> 읽기 좋은 웹 버전은 **[Dollars Archive 문서 아카이브](https://dollars-archive.github.io/Dollars-Archive-kr-localization-archive/)**에서 볼 수 있습니다.
>
> 앞으로 공개용 기술 `.md` 문서는 Markdown을 단일 원본으로 유지하고, 기본 사용자 링크는 GitHub Pages 문서 뷰어를 사용합니다.

> [!IMPORTANT]
> 공개 문서에는 게임 본편, NSP/XCI/NCA, 원본 RomFS, 키 파일, 원작 이미지·영상·음성·전체 스크립트, 개인 경로, 토큰·비밀번호 등 민감하거나 저작권 문제가 될 수 있는 자료를 포함하지 않습니다.

## 문서 목록

### GPT / GitHub 운용

- [GPT → GitHub 작업 가이드](https://dollars-archive.github.io/Dollars-Archive-kr-localization-archive/doc.html?file=GPT-GITHUB-OPERATIONS.md)
  - GPT가 가능 여부를 추측하지 않고 실제 GitHub 도구를 호출하도록 지시하는 방법
  - README·파일 수정 검증
  - 직접 Release 수정 액션이 없을 때 GitHub Actions + REST API를 사용하는 일회용 우회 방식

### Codex 한글화 프로젝트 운영

- [Codex 한글화 프로젝트 부트스트랩](https://dollars-archive.github.io/Dollars-Archive-kr-localization-archive/doc.html?file=CODEX-LOCALIZATION-BOOTSTRAP.md)
  - 게임별 프로젝트·검수 프로그램 분리
  - GPT-5.6 Sol / Luna 역할 분담
  - Google Drive 기반 1차·2차·3차 검수 구조
  - 용어집·캐릭터·관계도·말투 기준 자료 운영
  - 최종 CSV 반영과 실제 플레이 피드백 우선순위

### 공개 작업일지

- [공개 작업일지 운영 표준](https://dollars-archive.github.io/Dollars-Archive-kr-localization-archive/doc.html?file=workflow%2FPUBLIC-WORKLOG-STANDARD.md)
  - 게임별 `WORKLOG.md` 단일 파일 운영
  - README의 `🚧 한국어화 작업 진행 중` 선언과 작업일지 링크
  - 사용자에게는 성과와 진행 상황을 공개하고 제작 노하우는 비공개로 유지

### 설치 가이드 / GitHub Pages

- [GitHub Pages 설치 가이드 표준](https://dollars-archive.github.io/Dollars-Archive-kr-localization-archive/doc.html?file=workflow%2FGITHUB-PAGES-INSTALL-GUIDE-STANDARD.md)
  - `INSTALL.md`를 단일 원본으로 유지하고 GitHub Pages에서 자동 렌더링
  - README와 최신 Release의 설치 링크를 Pages로 연결
  - 공통 레이아웃 + 게임별 포인트 컬러 테마
  - 목차·경고 박스·코드 복사·모바일·다크모드 공통 기능
  - `main /docs` 배포와 Pages build 검증
  - 새 게임 저장소에 재사용하는 기본 체크리스트

### Nintendo Switch 한국어 패치

- [Nintendo Switch 게임 한국어 패치 제작 워크플로](https://dollars-archive.github.io/Dollars-Archive-kr-localization-archive/doc.html?file=switch%2FSWITCH-KOREAN-LOCALIZATION-GUIDE.md)
  - clean merged RomFS 기준 잡기
  - 텍스트·제어 코드·폰트·UI 이미지·영상 작업 흐름
  - xdelta/VCDIFF 차이 패치 배포 구조
  - Atmosphere LayeredFS용 폴더 구조
  - 원본/결과 해시 검증과 패처 설계
  - 실기·Windows·Android 검수
  - 공개 저장소에 올리면 안 되는 자료 체크리스트

## 기본 원칙

```text
조사 → 단일 샘플 → 실기 검증 → 전체 적용 → 자동 검증 → 변경분만 배포
```

그리고 모든 기술 노트는 가능한 한 **다른 게임에도 재사용할 수 있는 형태**로 정리합니다.
