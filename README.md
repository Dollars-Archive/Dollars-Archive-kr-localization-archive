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

웹 대문은 **한글화 프로젝트**(GPT 선임·Claude 선임), **프로젝트 운영**(공개 작업일지·Codex ↔ Claude 연결), **GitHub 운영**(GitHub 작업·Pages 설치 가이드), **기종별 기술 문서**(Nintendo Switch) 순서로 표시합니다. **문서 카드는 PC에서 항상 2열, 모바일에서 1열**로 구성하며 3열 배치는 사용하지 않습니다. 문서를 추가할 때도 이 배치 규칙을 유지합니다.

대문 스크립트·스타일을 수정할 때는 `docs/index.html`과 `docs/doc.html`의 자산 URL에 붙인 `v=` 값을 함께 갱신합니다. 이전 스크립트 캐시가 새 HTML에 적용되어 카드 구성이 섞이는 것을 방지합니다.

### GPT / GitHub 운용

- [GPT → GitHub 작업 가이드](https://dollars-archive.github.io/Dollars-Archive-kr-localization-archive/doc.html?file=GPT-GITHUB-OPERATIONS.md)
  - GPT가 가능 여부를 추측하지 않고 실제 GitHub 도구를 호출하도록 지시하는 방법
  - README·파일 수정 검증
  - 직접 Release 수정 액션이 없을 때 GitHub Actions + REST API를 사용하는 일회용 우회 방식

### Codex 한글화 프로젝트 운영

- [Codex 한글화 프로젝트 부트스트랩](https://dollars-archive.github.io/Dollars-Archive-kr-localization-archive/doc.html?file=CODEX-LOCALIZATION-BOOTSTRAP.md)
  - Codex·GPT 공통 16단계, 진행상태 기록과 사용자 실기 확인
  - 모든 차수 500행: 1차 번역 → 2차 화자·관계·용어 → 3차 출력 규격·말투 반영
  - [Google Drive 공통 양식](templates/drive-review/README.md): 전체 지시문과 빈 CSV
  - [프로젝트 공통 지시문](templates/PROJECT-INSTRUCTIONS.md) / [진행상태 양식](templates/진행상태.template.md)

### Claude 담당자 방식의 한글화 프로젝트

- [Claude 한글화 프로젝트 부트스트랩](https://dollars-archive.github.io/Dollars-Archive-kr-localization-archive/doc.html?file=CLAUDE-LOCALIZATION-BOOTSTRAP.md)
  - Claude가 진행 관리·실제 구현을 맡고 Codex에 테스트 ROM·패처 제작을 의뢰
  - Google Drive 웹 GPT의 대사 1·2·3차 검수와 기존 실기 확인 순서 유지
  - 선택한 프로젝트에서만 적용, 기존 Codex 운영 방식과 자동 전환 없음

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
  - 기존 게시 설정 보존, 실제 Pages 배포 확인 후 공개 링크 전환
  - [복제할 설치 페이지 템플릿](templates/pages-install-guide/README.md)
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

### Codex ↔ Claude 연결·프로젝트 팀 복구

- [Codex ↔ Claude 연결·프로젝트 팀 복구 가이드](https://dollars-archive.github.io/Dollars-Archive-kr-localization-archive/doc.html?file=workflow%2FCODEX-CLAUDE-TEAM-RECOVERY.md)
  - 검증된 브리지 소스·정션 수정본·해시를 보관한 복구 자료
  - 초기화 후 재설치·재연결·최소화 왕복 확인
  - 독립 담당자 1명과 주 워커·이미지·동영상 실무자 3명 지정
  - Claude 분석·검토와 실무자 배차·회수 프롬프트

## 기본 원칙

```text
조사 → 단일 샘플 → 실기 검증 → 전체 적용 → 자동 검증 → 변경분만 배포
```

그리고 모든 기술 노트는 가능한 한 **다른 게임에도 재사용할 수 있는 형태**로 정리합니다.
