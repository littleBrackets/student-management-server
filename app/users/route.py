from fastapi import FastAPI, Depends, HTTPException, APIRouter, status
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from app.database import get_db_session
from app.config import TOKEN_SECRET_KEY, TOKEN_ALGORITHM, TOKEN_EXPIRE_MINUTES
from app.dependencies import get_current_user
from .curd import get_user_by_username, create_user
from .model import ReqUserLoginModel, ReqUserSignupModel, ResUserModel


app = FastAPI()
router = APIRouter()

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Token generation function
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, TOKEN_SECRET_KEY, algorithm=TOKEN_ALGORITHM)
    return encoded_jwt

# Password verification function
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# User authentication function
def authenticate_user(db, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user or not verify_password(password, user.password):
        return False
    return user


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def login_for_access_token(form_data: ReqUserSignupModel, db: Session = Depends(get_db_session)):
    hashed_password = pwd_context.hash(form_data.password)
    user = create_user(db, form_data.username, password=hashed_password)
    if not user:
        raise HTTPException(status_code=401, detail="Failed to create user")
    return


# Route for token generation
@router.post("/login", status_code=status.HTTP_200_OK)
async def login_for_access_token(form_data: ReqUserLoginModel, db: Session = Depends(get_db_session)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


# Example protected route
@router.get("/profile", response_model=ResUserModel, status_code=status.HTTP_200_OK)
async def protected_route(current_user: ResUserModel = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(status_code=401, detail="User not found")
    return current_user
