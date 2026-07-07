# Databricks notebook source
# MAGIC %md
# MAGIC # 01. Schema Exploration
# MAGIC Text-to-SQL 대상이 될 카탈로그/스키마의 테이블 구조를 탐색합니다.

# COMMAND ----------

import sys, os
sys.path.append(os.path.abspath("../src"))

from text_to_sql import schema_loader

# COMMAND ----------

# MAGIC %md
# MAGIC ## 대상 카탈로그/스키마 지정
# MAGIC configs/config.yaml 에 값이 채워지면 아래를 그 값으로 대체하세요.

# COMMAND ----------

CATALOG = "main"     # TODO: 실제 카탈로그로 교체
SCHEMA = "default"   # TODO: 실제 스키마로 교체

# tables = schema_loader.list_tables(CATALOG, SCHEMA)
# tables

# COMMAND ----------

# MAGIC %md
# MAGIC ## information_schema 직접 조회 (참고용)

# COMMAND ----------

# display(
#     spark.sql(f"""
#         SELECT table_name, column_name, data_type, comment
#         FROM {CATALOG}.information_schema.columns
#         WHERE table_schema = '{SCHEMA}'
#         ORDER BY table_name, ordinal_position
#     """)
# )
