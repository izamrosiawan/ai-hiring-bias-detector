import os
import pandas as pd
import numpy as np

class HiringBiasEngine:
    def __init__(self, random_state=42):
        self.random_state = random_state

    def load_and_clean_data(self, filepath):
        df = pd.read_csv(filepath)
        return df

    def calculate_fairness_summary(self, df):
        return df.groupby('gender_text_cue')[['baseline_qualification_score', 'final_screening_score', 'disparate_impact_ratio']].mean().round(3)
