from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

from app.database import get_db_session
from app.dependencies import get_current_user
from .model import ReqTestModel, ResTestModel
from .curd import get_test_list, get_test_by_id, create_test, update_test, delete_test

app = FastAPI()
router = APIRouter()


@router.get("/", response_model=List[ResTestModel], status_code=status.HTTP_200_OK)
def read_items(current_user = Depends(get_current_user), items = Depends(get_test_list)):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorised access",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return items



@router.get("/details", response_model=ResTestModel, status_code=status.HTTP_200_OK)
def read_item(id: int, current_user = Depends(get_current_user), db: Session = Depends(get_db_session)):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorised access",
            headers={"WWW-Authenticate": "Bearer"},
        )    
    item = get_test_by_id(db, id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return item



@router.post("/create", response_model=ResTestModel, status_code=status.HTTP_201_CREATED)
def create_item(form_data: ReqTestModel, db: Session = Depends(get_db_session), current_user = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorised access",
            headers={"WWW-Authenticate": "Bearer"},
        )
    item = create_test(db, form_data)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Faild to create item",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return item



@router.put("/update",  status_code=status.HTTP_200_OK)
def update_item(form_data: ResTestModel, db: Session = Depends(get_db_session), current_user = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorised access",
            headers={"WWW-Authenticate": "Bearer"},
        )
    updatedItem = update_test(db, form_data)
    if not updatedItem:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return updatedItem



@router.delete("/delete",  status_code=status.HTTP_204_NO_CONTENT)
def delete_item(id: int, db: Session = Depends(get_db_session), current_user = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorised access",
            headers={"WWW-Authenticate": "Bearer"},
        )
    isDeleted = delete_test(db, id=id)
    if not isDeleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return

