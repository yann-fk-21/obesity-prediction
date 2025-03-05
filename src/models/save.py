from datetime import datetime

import joblib

def save_model(model, model_name: str):
    joblib.dump(model, f"../../models/{model_name}_{datetime.now().day}.pkl")

def load_model(path: str):
    return joblib.load(path)