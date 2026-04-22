import pickle

with open("blog/model.pkl", "rb") as f:
    model, scaler, columns = pickle.load(f)

print(type(model))