from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

from app.database import get_db_session
from app.dependencies import get_current_user
from app.items.model import ResItemModel, ReqItemModel
from app.items.curd import get_items, get_item_by_id, create_item, update_item, delete_item

app = FastAPI()
router = APIRouter()


@router.get("/", response_model=List[ResItemModel], status_code=status.HTTP_200_OK)
def read_users(current_user = Depends(get_current_user), items = Depends(get_items)):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorised access",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return items



@router.get("/details", response_model=ResItemModel, status_code=status.HTTP_200_OK)
def read_users(id: int, current_user = Depends(get_current_user), db: Session = Depends(get_db_session)):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorised access",
            headers={"WWW-Authenticate": "Bearer"},
        )    
    item = get_item_by_id(db, id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return item



@router.post("/create",  status_code=status.HTTP_201_CREATED)
def read_users(form_data: ReqItemModel, db: Session = Depends(get_db_session), current_user = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorised access",
            headers={"WWW-Authenticate": "Bearer"},
        )
    item = create_item(db, id=form_data.id, title=form_data.title, description=form_data.description)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Faild to create item",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return



@router.put("/update",  status_code=status.HTTP_200_OK)
def read_users(form_data: ReqItemModel, db: Session = Depends(get_db_session), current_user = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorised access",
            headers={"WWW-Authenticate": "Bearer"},
        )
    updatedItem = update_item(db, id=form_data.id, title=form_data.title, description=form_data.description)
    if not updatedItem:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return updatedItem



@router.delete("/delete",  status_code=status.HTTP_204_NO_CONTENT)
def read_users(id: int, db: Session = Depends(get_db_session), current_user = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorised access",
            headers={"WWW-Authenticate": "Bearer"},
        )
    isDeleted = delete_item(db, id=id)
    if not isDeleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return

