# Databricks notebook source
# MAGIC %md
# MAGIC # 03. Evaluation
# MAGIC 생성된 SQL을 정답과 비교해 평가하는 노트북.
# MAGIC 평가 데이터셋(자연어-SQL 쌍)이 확보되면 이 노트북에서 배치로 돌립니다.

# COMMAND ----------

import sys, os
sys.path.append(os.path.abspath("../src"))

from text_to_sql import evaluation

# COMMAND ----------

# MAGIC %md
# MAGIC ## 샘플 평가 (더미 데이터)

# COMMAND ----------

predicted_sql = "SELECT 1"
gold_sql = "select   1"

print("Exact match:", evaluation.exact_match(predicted_sql, gold_sql))

# COMMAND ----------

# MAGIC %md
# MAGIC ## 평가 데이터셋 로드 (TODO)
# MAGIC - 자연어 질문 + 정답 SQL 쌍을 담은 파일/테이블 로드
# MAGIC - 각 건에 대해 모델 예측 → exact_match / execution_accuracy 계산 → 집계

