from sqlalchemy.orm import Session
from app.db import models

# ==================== CRUD ДЛЯ КАТЕГОРИЙ ====================

def create_category(db: Session, title: str):
    """Создать новую категорию"""
    db_category = models.Category(title=title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session):
    """Получить все категории"""
    return db.query(models.Category).all()

def get_category_by_title(db: Session, title: str):
    """Найти категорию по названию"""
    return db.query(models.Category).filter(models.Category.title == title).first()


# ==================== CRUD ДЛЯ КНИГ ====================

def create_book(db: Session, title: str, description: str, price: float, category_id: int, url: str = ""):
    """Создать новую книгу в привязке к категории"""
    db_book = models.Book(
        title=title,
        description=description,
        price=price,
        category_id=category_id,
        url=url
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session):
    """Получить все книги"""
    return db.query(models.Book).all()