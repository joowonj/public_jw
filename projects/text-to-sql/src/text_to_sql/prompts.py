"""
Text-to-SQL 프롬프트 템플릿 관리.

모델(LLM API vs 파인튜닝)에 따라 프롬프트 형식이 달라질 수 있으므로,
템플릿을 이 모듈에 모아두고 inference.py에서 조합해서 사용합니다.
"""

from typing import List
from .schema_loader import TableInfo

SYSTEM_PROMPT = """당신은 자연어 질문을 SQL 쿼리로 변환하는 어시스턴트입니다.
주어진 테이블 스키마만 사용해서 정확한 SQL을 작성하세요.
설명 없이 SQL 쿼리만 반환하세요.
"""


def build_schema_context(tables: List[TableInfo], max_tables: int = 20) -> str:
    """테이블 정보 리스트를 프롬프트에 넣을 스키마 컨텍스트 문자열로 변환."""
    selected = tables[:max_tables]
    return "\n\n".join(t.to_ddl() for t in selected)


def build_user_prompt(question: str, schema_context: str) -> str:
    return f"""다음은 사용 가능한 테이블 스키마입니다:

{schema_context}

질문: {question}

위 스키마만 사용해서 SQL 쿼리를 작성하세요.
"""
