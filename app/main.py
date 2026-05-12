from fastapi import FastAPI, HTTPException
from .ml_model import model, scaler, columns
from .schemas import PredictionInput
import pandas as pd

app = FastAPI()


@app.post("/predict")
def predict(data: PredictionInput):

    try:
        input_dict = data.dict()

        df = pd.DataFrame([input_dict])

        df = pd.get_dummies(df)

        for col in columns:
            if col not in df:
                df[col] = 0

        df = df[columns]

        df = scaler.transform(df)

        result = model.predict(df)

        proba = model.predict_proba(df)

        return {
            "prediction": int(result[0]),
            "confidence": float(max(proba[0]))
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )


@app.get("/")
def home():
    return {
        "project": "Heart Disease Prediction API",
        "status": "running"
    }