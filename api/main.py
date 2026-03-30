from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def home():
    return {"message": "NRL Prediction API is live"}

@app.get("/predict")
def predict():
    return {
        "match": "Knights vs Raiders",
        "home_win_probability": round(random.uniform(0.5, 0.7), 2),
        "tip": "Knights"
    }
