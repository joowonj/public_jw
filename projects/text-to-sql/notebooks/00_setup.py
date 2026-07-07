# Databricks notebook source
# MAGIC %md
# MAGIC # 00. Setup
# MAGIC 프로젝트 공통 설정 로드 및 환경 점검용 노트북.
# MAGIC Databricks Repos로 이 레포를 연결한 뒤 실행하세요.

# COMMAND ----------

import sys
import os

# src 모듈 import 경로 추가 (Repos 기준 상대 경로)
sys.path.append(os.path.abspath("../src"))

import yaml
from text_to_sql import schema_loader, prompts, inference, evaluation

# COMMAND ----------

# MAGIC %md
# MAGIC ## 설정 로드

# COMMAND ----------

with open("../configs/config.yaml") as f:
    config = yaml.safe_load(f)

config

# COMMAND ----------

# MAGIC %md
# MAGIC ## 환경 점검
# MAGIC - Unity Catalog 접근 가능 여부
# MAGIC - SQL Warehouse 연결 여부
# MAGIC 등을 여기서 확인 (구체 로직은 카탈로그/스키마 확정 후 추가)

