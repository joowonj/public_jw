import sys
import os

sys.path.append(os.path.abspath("../src"))

from text_to_sql import evaluation, inference


def test_exact_match_normalizes_whitespace_and_case():
    assert evaluation.exact_match("SELECT 1", "select   1")


def test_dummy_model_returns_string():
    model = inference.DummyTextToSQLModel()
    result = model.generate_sql("아무 질문", "-- schema")
    assert isinstance(result, str)
