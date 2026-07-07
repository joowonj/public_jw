# public_jw

Databricks 환경에서의 개발 프로젝트 및 학습 자료 저장소입니다.

## 📁 구조

```
public_jw/
├── projects/
│   ├── text-to-sql/           # Text to SQL 모델 개발
│   │   ├── notebooks/         # 실험 및 탐색 노트북
│   │   ├── src/text_to_sql/   # 핵심 모듈 (inference, prompts, evaluation 등)
│   │   ├── configs/           # 설정 파일
│   │   ├── tests/             # 테스트 코드
│   │   └── data/              # 샘플 데이터
│   └── databricks-education/  # Databricks 공식 교육 자료
└── README.md
```

## 🚀 Projects

### Text to SQL (`projects/text-to-sql/`)
자연어 질문을 SQL 쿼리로 변환하는 모델 개발 공간.
- LLM 기반 프롬프트 엔지니어링
- 스키마 탐색 및 컨텍스트 주입
- 평가 파이프라인

### Databricks Education (`projects/databricks-education/`)
Databricks 공식 교육 교재 및 실습 자료.
