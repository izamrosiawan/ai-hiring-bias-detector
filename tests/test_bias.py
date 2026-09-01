import os
import pytest
import pandas as pd
from src.bias_engine import HiringBiasEngine

def test_hiring_bias_engine():
    engine = HiringBiasEngine()
    df = engine.load_and_clean_data("data/hiring_bias_dataset.csv")
    assert not df.empty
    assert 'disparate_impact_ratio' in df.columns
    summary = engine.calculate_fairness_summary(df)
    assert 'disparate_impact_ratio' in summary.columns
