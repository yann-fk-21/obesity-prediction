from fastapi import FastAPI

import numpy as np
from app.models.models import Person
from src.models.save import load_model

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "redirect to ..."}


@app.post("/api/v1/predictions")
async def get_predictions(person: Person):
    model = load_model("./models/obesity_pred_model_4.pkl")
    features = np.array([person.age, person.height, person.weight, person.family_history])
    features = features.reshape(1, -1)

    pred = model.predict(features)
    final_pred = ""

    if pred[0] == 0:
        final_pred = "Insufficient_Weight"
    if pred[0] == 1 :
        final_pred = "Normal Weight"
    if pred[0] == 2:
        final_pred = "Obesity Type I"
    if pred[0] == 3:
        final_pred = "Obesity Type II"
    if pred[0] == 4:
        final_pred = "Obesity Type III"
    if pred[0] == 5:
        final_pred = "Overweight Level I"
    if pred[0] == 6:
        final_pred = "Overweight Level II"
    return {"prediction": final_pred}
