from random import random

import pandas as pd

def save_data_csv(data: pd.DataFrame, filename: str):
    data.to_csv(f"../../data/processed/{filename}.csv", index=False)

def save_data_excel(data: pd.DataFrame, filename: str):
    data.to_excel(f"../../data/processed/{filename}.xlsx", index=False)