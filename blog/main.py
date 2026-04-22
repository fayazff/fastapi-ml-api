from fastapi import FastAPI,Depends,status,Response,HTTPException
from . import schemas,models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session 
from .ml_model import model, scaler, columns
print("model imported")
print(type(model))
from .schemas import PredictionInput
import pandas as pd


app = FastAPI()



models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/blog")
def create(request:schemas.Blog,db: Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.put('/bog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog,db: Session = Depends(get_db)):
    blog =db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Blog with id {id} not found")
    blog.update(request.dict())
    db.commit()
    return 'updated'

@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

@app.get('/blog',response_model=list[schemas.ShowBlog])
def all(db: Session =Depends(get_db)):
    blog = db.query(models.Blog).all()
    return blog

@app.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog)
def all(id,response: Response,db: Session =Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'detail': f"Blog with the id {id} is not available"}
    return blog

@app.post('/user')
def create(request:schemas.User,db: Session = Depends(get_db)):
    new_user = models.User(name = request.name, email = request.email, password = request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



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
       
        return {"error": str(e)}
@app.get("/")
def home():
    return {"message": "ML Prediction API is running"}