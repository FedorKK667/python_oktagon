from app.db.db import engine, Base, SessionLocal
from app.db import crud

def init_database():
    print("Создание таблиц в базе данных...")
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:
        existing_categories = crud.get_categories(db)
        if existing_categories:
            print("База данных уже содержит категории. Пропускаем заполнение.")
            return

        print("Заполнение базы данных тестовыми данными...")
        
        programming = crud.create_category(db, title="Программирование")
        fiction = crud.create_category(db, title="Художественная литература")
        
        crud.create_book(
            db, 
            title="Изучаем Python", 
            description="Легендарное руководство от Марка Лутца.", 
            price=2500.0, 
            category_id=programming.id
        )
        crud.create_book(
            db, 
            title="Чистый код", 
            description="Создание, анализ и рефакторинг кода от Роберта Мартина.", 
            price=1800.0, 
            category_id=programming.id
        )
    
        crud.create_book(
            db, 
            title="1984", 
            description="Роман-антиутопия Джорджа Оруэлла.", 
            price=600.0, 
            category_id=fiction.id
        )
        crud.create_book(
            db, 
            title="Мастер и Маргарита", 
            description="Шедевр Михаила Булгакова.", 
            price=750.0, 
            category_id=fiction.id
        )
        
        print("База данных успешно инициализирована и заполнена!")
        
    except Exception as e:
        print(f"Произошла ошибка при инициализации: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    init_database()