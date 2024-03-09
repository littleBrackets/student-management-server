from fastapi import APIRouter, Depends, HTTPException, status
from datetime import timedelta
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Annotated
from typing import List

from app.dependencies import authenticate_user, create_access_token, get_current_user, get_password_hash
from app.config import Config
from app.database import get_db_session

from .curd import get_users, create_user

router = APIRouter()

class Token(BaseModel):
    access_token: str
    token_type: str

class AuthModel(BaseModel):
    email: str
    password: str

class User(BaseModel):
    id: int
    email: str
    status: str


@router.post("/login")
def read_users(form_data: AuthModel, db: Session = Depends(get_db_session)):
    user = authenticate_user(db, form_data.email, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.post("/signup")
def read_users(form_data: AuthModel, db: Session = Depends(get_db_session)):
    hashed_password = get_password_hash(form_data.password)
    user = create_user(db, form_data.email, hashed_password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")



@router.get("/profile", response_model=User)
async def read_users(current_user = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorised access",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return current_user


@router.get("/", response_model=List[User])
def read_users(current_user = Depends(get_current_user), skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorised access",
            headers={"WWW-Authenticate": "Bearer"},
        )
    users = get_users(db, skip=skip, limit=limit)
    return users