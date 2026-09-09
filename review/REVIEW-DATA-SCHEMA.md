# 웹 GPT 검수 데이터 스키마

이 문서는 1차·2차·3차 검수에서 공통으로 참조하는 게임별 기준 자료와 최종 CSV의 최소 규칙을 정의합니다.

## 1. 공통 기준 파일

### `glossary.csv`

고정 용어를 관리합니다.

권장 항목:

```csv
source_term,approved_ko,category,notes,status
```

### `characters.csv`

캐릭터의 안정적인 성격·특징을 관리합니다.

권장 항목:

```csv
character_id,name,aliases,personality,traits,base_speech_style,verbal_habits,notes
```

### `relationships.csv`

화자 → 청자 방향 관계를 관리합니다.

A → B와 B → A는 서로 다른 행으로 관리할 수 있어야 합니다.

권장 항목:

```csv
speaker_id,listener_id,relationship,speech_level,address_rule,effective_from,effective_to,exceptions,notes
```

### `speech_style.csv`

캐릭터가 누구와 대화하는지와 별개로, 그 캐릭터 자체의 화법을 관리합니다.

권장 항목:

```csv
character_id,base_style,sentence_length,vocabulary_tendency,emotional_expression,avoid,approved_examples,notes
```

## 2. 관계도와 말투를 분리하는 이유

다음 둘은 다른 정보입니다.

- 누구에게 존댓말/반말을 하는가
- 어떤 어휘와 리듬으로 말하는가

따라서 관계도와 캐릭터 말투를 하나의 값으로 합치지 않습니다.

## 3. 단계별 CSV 기본 규칙

게임마다 실제 컬럼은 달라질 수 있지만 다음 개념은 유지합니다.

- 변하지 않는 안정적인 행 ID
- 원문 필드
- 현재 한국어 번역 필드
- 필요한 경우 화자/청자 ID
- 보호해야 하는 제어 코드/태그/구조 필드
- 검수 상태
- 비고/근거
- 스키마 버전 또는 데이터 버전이 필요한 프로젝트에서는 명시적 버전 값

## 4. 보호 필드

번역 검수에서 다음 값은 임의로 재생성하거나 삭제하지 않습니다.

- 행 ID
- 제어 코드
- 태그
- 플레이스홀더
- 분기/이벤트 식별자
- 음성/캐릭터/장면 참조 ID
- 빌더가 요구하는 구조 필드

게임별 추가 보호 필드는 해당 프로젝트 규칙을 따릅니다.

## 5. 최종 CSV 요구사항

3차 검수 결과 CSV는 게임별 검수 프로그램으로 결정론적으로 반입할 수 있어야 합니다.

반입 시 최소 확인:

1. 예상 스키마인가
2. 필수 컬럼이 존재하는가
3. 행 ID가 중복되지 않는가
4. 알려지지 않은 ID가 있는가
5. 보호 필드가 손상되지 않았는가
6. 제어 코드/태그가 보존되었는가
7. 인코딩과 개행이 지원 형식인가

검수 프로그램은 이상한 행을 추측해서 고치기보다 **거부 또는 격리**하고 사용자가 확인할 수 있게 합니다.

## 6. 단계 간 데이터 전달

권장 흐름:

```text
원장/현재 번역
→ 1차 결과
→ 2차 결과
→ 3차 최종 결과
→ 게임별 검수 프로그램
```

각 단계는 이전 단계의 결과를 입력으로 받을 수 있지만, 다른 단계의 지시문까지 함께 가져오지는 않습니다.
