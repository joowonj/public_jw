"""
Unity Catalog / 스키마 메타데이터를 불러와 Text-to-SQL 프롬프트에 사용할
테이블/컬럼 정보를 정리하는 모듈.

Databricks 노트북에서는 보통 spark.catalog 또는 information_schema를 통해
메타데이터를 조회합니다. 아래는 뼈대만 잡아둔 상태이며, 실제 카탈로그/스키마가
정해지면 구현을 채워 넣으면 됩니다.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class ColumnInfo:
    name: str
    data_type: str
    comment: str = ""


@dataclass
class TableInfo:
    catalog: str
    schema: str
    table: str
    columns: List[ColumnInfo] = field(default_factory=list)

    @property
    def full_name(self) -> str:
        return f"{self.catalog}.{self.schema}.{self.table}"

    def to_ddl(self) -> str:
        """프롬프트에 넣기 좋은 형태의 간단한 DDL 문자열 생성."""
        cols = ",\n  ".join(f"{c.name} {c.data_type}" for c in self.columns)
        return f"CREATE TABLE {self.full_name} (\n  {cols}\n);"


def list_tables(catalog: str, schema: str) -> List[TableInfo]:
    """
    지정한 catalog.schema 하위 테이블 목록과 컬럼 정보를 조회합니다.

    Databricks 노트북 환경에서는 아래처럼 구현 가능:

        rows = spark.sql(f'''
            SELECT table_name, column_name, data_type, comment
            FROM {catalog}.information_schema.columns
            WHERE table_schema = '{schema}'
        ''').collect()

    지금은 구조만 잡아둔 상태이며, 실제 구현은 TODO 입니다.
    """
    raise NotImplementedError("TODO: information_schema 조회 로직 구현")
