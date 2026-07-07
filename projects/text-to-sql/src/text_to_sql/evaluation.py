"""
생성된 SQL 평가 로직.

일반적인 Text-to-SQL 평가 지표:
- Exact Match: 정답 SQL과 문자열 정규화 후 완전 일치 여부
- Execution Accuracy: 실행 결과(row set)가 정답과 동일한지 여부
"""

from typing import Iterable


def normalize_sql(sql: str) -> str:
    """공백/대소문자 등을 정규화해서 단순 비교에 사용."""
    return " ".join(sql.strip().lower().split())


def exact_match(predicted_sql: str, gold_sql: str) -> bool:
    return normalize_sql(predicted_sql) == normalize_sql(gold_sql)


def execution_accuracy(predicted_rows: Iterable, gold_rows: Iterable) -> bool:
    """
    predicted_rows, gold_rows: 실제 쿼리를 실행(spark.sql(...).collect() 등)한
    결과를 넘겨받아 비교합니다. 순서에 의존하지 않도록 정렬 후 비교하는 것을 권장.

    TODO: 실제 실행 로직은 Databricks 환경에서 spark.sql()로 연결해서 채우기.
    """
    return sorted(map(tuple, predicted_rows)) == sorted(map(tuple, gold_rows))
