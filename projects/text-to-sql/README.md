# Text-to-SQL 개발 프로젝트

자연어 질의를 SQL로 변환하는 모델/파이프라인을 개발하기 위한 작업 공간입니다.
Databricks 노트북 환경을 기준으로 구성되어 있으며, 모델/방식(LLM API, 파인튜닝 등)은
아직 미확정 상태로 두고 이후 자유롭게 교체할 수 있도록 구조를 잡았습니다.

## 폴더 구조

```
text-to-sql/
├── notebooks/          # Databricks 노트북 (탐색, 실험, 평가 등 실행 흐름)
│   ├── 00_setup.py
│   ├── 01_schema_exploration.py
│   ├── 02_prompt_experiments.py
│   └── 03_evaluation.py
├── src/text_to_sql/    # 재사용 가능한 파이썬 모듈 (노트북에서 import)
│   ├── schema_loader.py    # 테이블/스키마 메타데이터 로딩
│   ├── prompts.py          # 프롬프트 템플릿 관리
│   ├── inference.py        # 모델 호출 인터페이스 (LLM API / 파인튜닝 모델 공용)
│   └── evaluation.py       # 생성된 SQL 평가 로직
├── configs/
│   └── config.yaml     # 카탈로그/스키마, 모델 설정 등
├── tests/               # 단위 테스트
└── data/                # 로컬 샘플 데이터 (실제 데이터는 커밋 금지, .gitignore 처리)
```

## 사용 방식 (Databricks Repos 연동)

1. Databricks 워크스페이스에서 이 GitHub 레포를 Repos로 연결
2. `notebooks/` 하위 노트북을 Databricks에서 직접 열어 실행
3. `src/text_to_sql/` 모듈은 노트북 상단에서 아래처럼 import
   ```python
   import sys
   sys.path.append("../src")
   from text_to_sql import schema_loader, prompts, inference, evaluation
   ```

## 다음에 정할 것들 (TODO)

- [ ] 모델/방식 확정 (LLM API vs 오픈소스 파인튜닝)
- [ ] 대상 카탈로그/스키마 목록 정리 → `configs/config.yaml`에 반영
- [ ] 평가 데이터셋(자연어-SQL 쌍) 확보 방법 결정
- [ ] 평가 지표 정의 (Exact Match, Execution Accuracy 등)
