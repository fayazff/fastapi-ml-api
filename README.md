# Heart Disease Prediction API

This is a machine learning backend project built using FastAPI and Scikit-learn.

The main idea of this project is to predict whether a person is likely to have heart disease based on medical attributes such as age, cholesterol, blood pressure, heart rate, chest pain type, etc.

I built this project to understand:
- how machine learning models are trained
- how trained models are saved using pickle
- how ML models can be integrated with backend APIs
- how real-time predictions work using FastAPI

---

## Technologies Used

- Python
- FastAPI
- Scikit-learn
- Pandas
- NumPy
- Uvicorn

---

## Machine Learning Part

For this project, I used the Heart Disease dataset in CSV format.

Steps followed:
- loaded dataset using pandas
- separated features and target column
- applied one-hot encoding for categorical columns
- scaled numerical values using StandardScaler
- trained Logistic Regression model
- saved model, scaler, and feature columns using pickle

Model accuracy was around 85%.

---

## FastAPI Integration

The trained model is connected with FastAPI to provide real-time predictions through REST API endpoints.

The API:
- accepts JSON input
- preprocesses incoming data
- applies scaling and column alignment
- predicts result using trained model
- returns prediction with confidence score

---

## API Endpoint

### POST /predict

Sample input:

```json
{
  "Age": 63,
  "Sex": "M",
  "ChestPainType": "ASY",
  "RestingBP": 160,
  "Cholesterol": 310,
  "FastingBS": 1,
  "RestingECG": "ST",
  "MaxHR": 110,
  "ExerciseAngina": "Y",
  "Oldpeak": 3.5,
  "ST_Slope": "Down"
}

Sample output:

{
  "prediction": 1,
  "confidence": 0.95
}

## Project Structure

```bash
heart-disease-prediction-api/

│
├── app/
│   ├── data/
│   │   └── heart.csv
│   │
│   ├── __init__.py
│   ├── main.py
│   ├── ml_model.py
│   ├── schemas.py
│   ├── model.pkl
│   ├── scaler.pkl
│   └── columns.pkl
│
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## To Run the Project

1. Clone the repository

```
git clone <your-github-link>
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Start FastAPI server

```
uvicorn app.main:app --reload
```

4. Open Swagger UI in browser

```
http://127.0.0.1:8000/docs
```

This project helped me understand how machine learning models can be integrated into backend APIs for real-time predictions.
