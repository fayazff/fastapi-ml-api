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
    age:int = Field(gt=0, lt=120)
    cholesterol:float = Field(gt=0, lt=600)
    restingBP:float = Field(gt=0, lt=300)

