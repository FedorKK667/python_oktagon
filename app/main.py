from fastapi import FastAPI
from app.api import categories, books
from app.db.db import engine, Base

# Автоматически создаем таблицы при запуске сервера, если их нет
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Octagon Book Store API",
    description="Интеграционный модуль работы с книгами и категориями",
    version="1.0.0"
)

# Подключаем созданные роутеры
app.include_router(categories.router)
app.include_router(books.router)

# Простой эндпоинт для проверки работоспособности сервиса
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "alive", "database": "connected"}