from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": {'name':'jhon'}}

@app.get('/about')
def about():
    return {'data':'about check'}