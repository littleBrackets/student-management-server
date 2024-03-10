# from fastapi import APIRouter, Depends, HTTPException, status
# from datetime import timedelta
# from pydantic import BaseModel
# from typing import Annotated
# from typing import List

# from app.dependencies import authenticate_user, create_access_token, get_current_user, get_password_hash
# from app.config import Config
# from app.database import get_db_session

# from .curd import get_users, create_user

# router = APIRouter()

# class Token(BaseModel):
#     access_token: str
#     token_type: str

# class AuthModel(BaseModel):
#     email: str
#     password: str

# class User(BaseModel):
#     id: int
#     email: str
#     status: str


# @router.post("/login")
# def read_users(form_data: AuthModel, db: Session = Depends(get_db_session)):
#     user = authenticate_user(db, form_data.email, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.email}, expires_delta=access_token_expires
#     )
#     return Token(access_token=access_token, token_type="bearer")


# @router.post("/signup")
# def read_users(form_data: AuthModel, db: Session = Depends(get_db_session)):
#     hashed_password = get_password_hash(form_data.password)
#     user = create_user(db, form_data.email, hashed_password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.email}, expires_delta=access_token_expires
#     )
#     return Token(access_token=access_token, token_type="bearer")



# @router.get("/profile", response_model=User)
# async def read_users(current_user = Depends(get_current_user)):
#     print(current_user)
#     if not current_user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Unauthorised access",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     return current_user


# @router.get("/", response_model=List[User])
# def read_users(current_user = Depends(get_current_user), skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):
#     if not current_user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Unauthorised access",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     users = get_users(db, skip=skip, limit=limit)
#     return users


from fastapi import FastAPI, Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.database import get_db_session
from .curd import get_user_by_username, create_user_v2
from app.config import TOKEN_SECRET_KEY, TOKEN_ALGORITHM, TOKEN_EXPIRE_MINUTES

app = FastAPI()
router = APIRouter()

# Example user model
class User(BaseModel):
    username: str
    password: str

class UserSignup(BaseModel):
    username: str
    password: str
    fullname: str
    email: str

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme for token handling
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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

# Dependency to get current user based on the token
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db_session)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, TOKEN_SECRET_KEY, algorithms=[TOKEN_ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user_by_username(db, username)
    if user is None:
        raise credentials_exception
    return user

# Route for token generation
@router.post("/login")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db_session)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}



# Route for token generation
@router.post("/signup")
async def login_for_access_token(form_data: UserSignup, db: Session = Depends(get_db_session)):
    hashed_password = pwd_context.hash(form_data.password)
    user = create_user_v2(db, form_data.username, fullname=form_data.fullname, email=form_data.email, password=hashed_password)
    if not user:
        raise HTTPException(status_code=401, detail="Failed to create user")
    # access_token_expires = timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    # access_token = create_access_token(
    #     data={"sub": user.username}, expires_delta=access_token_expires
    # )
    return True



# Example protected route
@router.get("/protected")
async def protected_route(current_user: User = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(status_code=401, detail="User not found")
    return current_user
