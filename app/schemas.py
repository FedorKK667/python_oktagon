from pydantic import BaseModel, ConfigDict
from typing import Optional, List

# --- СХЕМЫ ДЛЯ КНИГ ---
class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    url: Optional[str] = ""
    category_id: int

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int
    
    # Настройка для работы с моделями SQLAlchemy (вместо orm_mode)
    model_config = ConfigDict(from_attributes=True)

# --- СХЕМЫ ДЛЯ КАТЕГОРИЙ ---
class CategoryBase(BaseModel):
    title: str

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int
    books: List[BookResponse] = []

    model_config = ConfigDict(from_attributes=True)