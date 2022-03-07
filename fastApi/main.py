#Python
from typing import Optional
from enum import Enum


#Pydantic
from pydantic import BaseModel
from pydantic import Field

#FastApi
from fastapi import FastAPI, Body, Path, Query

app = FastAPI()

#Models

class HairColor(Enum):
    """Heir colors"""
    white = 'white'
    brown = 'brown'
    black = 'black'
    blonde = 'blonde'
    red = 'red'

class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=60,
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=60,
        )
    age: int = Field(
        ...,
        gt=0,
        le=115,
    )
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)

class Location(BaseModel):
    city: str
    state: str
    country: str

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

#Validations: Request body

@app.put('/person/{person_id}')
def update_person(
    person_id: int = Path(
        ...,
        title='Person ID',
        description='This is the person ID',
        gt=0
    ),
    person: Person = Body(...),
    location: Location = Body(...),
):
    results = person.dict()
    results.update(location)
    return results