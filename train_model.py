import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Dummy dataset (simple for beginner)
data = {
    "Age": [25, 45, 50, 60, 30, 55, 40, 65],
    "Cholesterol": [180, 220, 240, 260, 200, 230, 210, 270],
    "RestingBP": [120, 140, 150, 160, 130, 145, 135, 170],
    "HeartDisease": [0, 1, 1, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[['Age', 'Cholesterol', 'RestingBP']]
y = df['HeartDisease']

model = LogisticRegression()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("model.pkl created successfully")