from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from typing import List
from app.dependencies import get_current_user
from .curd import get_items
from .model import ResItems

app = FastAPI()
router = APIRouter()

@router.get("/", response_model=List[ResItems])
def read_users(current_user = Depends(get_current_user), items = Depends(get_items)):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorised access",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return items