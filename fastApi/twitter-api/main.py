# Python
from datetime import date, datetime
from typing import Optional, List
from uuid import UUID

# Pydantic
from pydantic import BaseModel, Field
from pydantic import EmailStr

# FastAPI
from fastapi import FastAPI
from fastapi import status

app = FastAPI()

# Models
class User(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(
        ...,
        min_length=8
    )
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=60
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=60
    )
    birth_date: Optional[date] = Field(default=None)

class Tweet(BaseModel):
    tweet_id : UUID = Field(
        ...,
    )
    content: str = Field(
        ...,
        min_length=1, 
        max_length=256
    )
    created_at : datetime = Field(default=datetime.now())
    updated_at : Optional[datetime] = Field(default=None)
    by : User = Field(...)

# Home


# Users
@app.get(
    path='/users',
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary='Get all users',
    tags=['Users']
    )
def user():
    pass
    

@app.post(
    path='/users',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary='Create a new user',
    tags=['Users']
)
def create_user(user: User):
    return user

@app.get(
    path='/users/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Get a user',
    tags=['Users']
)
def get_user(user_id: UUID):
    return {'user_id': user_id}

# Tweets
@app.get(
    path='/',
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary='Show all tweets',
    tags=['Tweets']
    )
def home():
    return {"Twitter API":"Working!"}

### Show a tweet
@app.get(
    path='/tweets/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Show a tweet',
    tags=['Tweets']
    )
def show_tweet(tweet_id: UUID):
    return {"tweet_id": tweet_id}

### Post a tweet
@app.post(
    path='/',
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary='Post a new tweet',
    tags=['Tweets']
)
def post_tweet(tweet: Tweet):
    return tweet

### Update a tweet
@app.put(
    path='/tweets/{tweet_id}/update',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Update a tweet',
    tags=['Tweets']
)
def update_tweet(tweet_id: UUID, tweet: Tweet):
    return tweet