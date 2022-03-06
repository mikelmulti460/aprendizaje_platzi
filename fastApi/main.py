#Python
from lib2to3.pgen2.token import OP
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastApi
from fastapi import FastAPI, Body, Query

app = FastAPI()

#Models

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


@app.get('/')
def home():
    return {"Hello": "World"}

# Request and response Body

@app.post('/person/new')
def create_person(person: Person = Body(...)):
    ''' This function create new person in API data '''
    return person

#validations: Query Parameters
@app.get("/person/detail")
def show_person(
        name:Optional[str] = Query(None, min_length=1, max_length=60),
        age: int = Query(..., ge=0, le=120)
    ):
    return {name: age}