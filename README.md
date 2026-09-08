# Dollars Archive · KR Localization Archive

한국어 패치 제작 과정에서 얻은 **범용 기술 노트, 실패/해결 기록, 자동화·검증 노하우, GPT/GitHub 운용 팁**을 모아두는 공개 아카이브입니다.

특정 게임의 원본 데이터나 개인정보를 보관하는 저장소가 아닙니다.

> [!IMPORTANT]
> 공개 문서에는 게임 본편, NSP/XCI/NCA, 원본 RomFS, 키 파일, 원작 이미지·영상·음성·전체 스크립트, 개인 경로, 토큰·비밀번호 등 민감하거나 저작권 문제가 될 수 있는 자료를 포함하지 않습니다.

## 문서 목록

### GPT / GitHub 운용

- [GPT → GitHub 작업 가이드](GPT-GITHUB-OPERATIONS.md)
  - GPT가 가능 여부를 추측하지 않고 실제 GitHub 도구를 호출하도록 지시하는 방법
  - README·파일 수정 검증
  - 직접 Release 수정 액션이 없을 때 GitHub Actions + REST API를 사용하는 일회용 우회 방식

### Nintendo Switch 한국어 패치

- [Nintendo Switch 게임 한국어 패치 제작 워크플로](switch/SWITCH-KOREAN-LOCALIZATION-GUIDE.md)
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
