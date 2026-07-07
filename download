"""
Text-to-SQL 모델 호출 인터페이스.

모델 방식(LLM API 호출 vs 파인튜닝 모델 서빙)이 아직 정해지지 않았으므로,
공통 인터페이스(TextToSQLModel)만 정의해두고, 방식이 정해지면 그에 맞는
구현체(예: AnthropicTextToSQL, ServingEndpointTextToSQL)를 추가하면 됩니다.
"""

from abc import ABC, abstractmethod


class TextToSQLModel(ABC):
    """모든 Text-to-SQL 모델 구현체가 따라야 하는 공통 인터페이스."""

    @abstractmethod
    def generate_sql(self, question: str, schema_context: str) -> str:
        """자연어 질문과 스키마 컨텍스트를 받아 SQL 문자열을 반환."""
        raise NotImplementedError


class DummyTextToSQLModel(TextToSQLModel):
    """구현체가 없는 상태에서도 파이프라인 흐름을 테스트할 수 있는 더미 모델."""

    def generate_sql(self, question: str, schema_context: str) -> str:
        return "-- TODO: 실제 모델 구현 연결 필요\nSELECT 1;"


# 모델 방식이 정해지면 아래와 같은 형태로 구현체를 추가합니다.
#
# class AnthropicTextToSQL(TextToSQLModel):
#     def __init__(self, model_name: str = "claude-sonnet-4-6"):
#         ...
#     def generate_sql(self, question, schema_context):
#         ...
#
# class ServingEndpointTextToSQL(TextToSQLModel):
#     """Databricks Model Serving 엔드포인트로 배포된 파인튜닝 모델 호출."""
#     def __init__(self, endpoint_name: str):
#         ...
#     def generate_sql(self, question, schema_context):
#         ...
