import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("app/data/heart.csv")

# Features and target
X = df.drop("HeartDisease", axis=1)
y = df["HeartDisease"]

# One-hot encoding
X = pd.get_dummies(X)

# Save column names
columns = X.columns.tolist()

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

# Model
model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# Save model
with open("app/model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save scaler
with open("app/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

# Save columns
with open("app/columns.pkl", "wb") as f:
    pickle.dump(columns, f)

print("Model, scaler, and columns saved successfully.")