#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastApi
from fastapi import FastAPI, Body, Path, Query

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
    name:Optional[str] = Query(
        None,
        min_length=1,
        max_length=60,
        title="Person Name",
        description="This is the person name. It's between 1 and 50 characters",
        ),
    age: int = Query(
        ...,
        gt=0,
        le=120
        )
):
    return {name: age}

#Validations: Path Parameters

@app.get('/person/detail/{person_id}')
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
    )
):
    return {person_id: "It exist!"}