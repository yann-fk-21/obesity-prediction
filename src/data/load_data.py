import pandas as pd

def load_data_csv(path: str):
    return pd.read_csv(path)

def load_data_excel(path: str):
    return pd.read_excel(path)