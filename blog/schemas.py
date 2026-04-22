from pydantic import BaseModel,Field

class Blog(BaseModel):
    title:str
    body:str

class ShowBlog(BaseModel):
    title:str
    body:str
    class config():
        orm_mode = True

class User(BaseModel):
    name:str
    email:str
    password:str

class PredictionInput(BaseModel):
    Age: int
    Sex: str
    ChestPainType: str
    RestingBP: int
    Cholesterol: int
    FastingBS: int
    RestingECG: str
    MaxHR: int
    ExerciseAngina: str
    Oldpeak: float
    ST_Slope: str
