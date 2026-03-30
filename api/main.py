from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def home():
    return {"message": "NRL Prediction API is live"}

@app.get("/predict")
def predict(home_team: str, away_team: str):
    return {
        "match": f"{home_team} vs {away_team}",
        "home_win_probability": round(random.uniform(0.5, 0.7), 2),
        "tip": home_team
    }
