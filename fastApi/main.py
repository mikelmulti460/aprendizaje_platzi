#Python
from email import message
from typing import Optional
from enum import Enum


#Pydantic
from pydantic import BaseModel
from pydantic import Field, EmailStr

#FastApi
from fastapi import FastAPI
from fastapi import Body, Path, Query, Form, Header, Cookie, File , UploadFile
from fastapi import status

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
    password: str = Field(..., min_length=8)

    class Config:
        schema_extra = {
            "example": {
                "first_name" : "Mikel",
                "last_name" : "Aranda",
                "age": 21,
                "hair_color": "black",
                "is_maried": False,
                "password": "dadadada"
            }
        }

class Location(BaseModel):
    city: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    state: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    country: str = Field(
        ...,
        min_length=1,
        max_length=50
    )

class LoginOut(BaseModel):
    username: str = Field(..., max_length=20, example = "pandita451")
    password: str = Field(..., min_length=8, example = "dadadada")
    message: str = Field(default='Login Succesfully!')

@app.get(
    path='/',
    status_code=status.HTTP_200_OK
    )
def home():
    return {"Hello": "World"}

# Request and response Body

@app.post(
    path='/person/new', 
    response_model=Person, 
    response_model_exclude={'password'},
    status_code=status.HTTP_201_CREATED
    )
def create_person(person: Person = Body(...)):
    ''' This function create new person in API data '''
    return person

#validations: Query Parameters
@app.get(
    path="/person/detail",
    status_code=status.HTTP_200_OK
    )
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

@app.get(
    path='/person/detail/{person_id}',
    response_model=Person,
    response_model_exclude={'password'},
    status_code=status.HTTP_200_OK
    )
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
    )
):
    return {person_id: "It exist!"}

#Validations: Request body

@app.put(
    path='/person/{person_id}',
    response_model=Person,
    status_code=status.HTTP_200_OK
    )
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

@app.post(
    path='/login',
    response_model=LoginOut,
    response_model_exclude={'password'},
    status_code=status.HTTP_200_OK,
    )
def login(
    username: str = Form(...),
    password: str = Form(...)
    ):
    """Login function from frontend"""
    return LoginOut(username=username,password=password)

# Cookies and Headers Parameters
@app.post(
    path='/contact',
    status_code=status.HTTP_200_OK
)
def contact(
    fist_name : str = Form(
        ...,
        max_length=60,
        min_length=1
    ),
    last_name : str = Form(
        ...,
        max_length=60,
        min_length=1
    ),
    email : EmailStr = Form(...),
    message: str = Form(
        ...,
        min_length=20
    ),
    user_agent: Optional[str] = Header(default=None),
    ads: Optional[str] = Cookie(default=None)

):
    return user_agent

@app.post(
    path="/post-image",
)
def post_image(
    image: UploadFile = File(...,)
): 
    return {
        "Filename": image.filename,
        "Format": image.content_type,
        "Size(kb)": round(len(image.file.read())/1024, 2)
    }