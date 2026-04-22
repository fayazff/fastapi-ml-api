import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import pickle

#dataset 
df = pd.read_csv("blog/data/heart.csv")

#clean column names
df.columns = df.columns.str.strip()

#select features
X = df.drop(columns=['HeartDisease'])
y = df['HeartDisease']

#convert categorical variables to numeric

X = pd.get_dummies(X, drop_first=True)

#split dataset(80% train,20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# scale 
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#model train
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

#evaluate model
pred = model.predict(X_test)
accuracy = accuracy_score(y_test,pred)

print("Model Accuracy:", accuracy)

#save model
with open("blog/model.pkl", "wb") as f:
    pickle.dump((model, scaler, X.columns), f)



print("model trained and saved successfully")