from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.db import get_db
from app.db import crud
from app import schemas

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/", response_model=List[schemas.CategoryResponse])
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)

@router.get("/{category_id}", response_model=schemas.CategoryResponse)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_category_by_id(db, category_id)
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@router.post("/", response_model=schemas.CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = crud.get_category_by_title(db, title=category.title)
    if db_category:
        raise HTTPException(status_code=400, detail="Category already exists")
    return crud.create_category(db, title=category.title)

@router.put("/{category_id}", response_model=schemas.CategoryResponse)
def update_category(category_id: int, category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = crud.update_category(db, category_id, title=category.title)
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    if not crud.delete_category(db, category_id):
        raise HTTPException(status_code=404, detail="Category not found")