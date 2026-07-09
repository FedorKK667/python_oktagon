from app.db.db import SessionLocal
from app.db import crud

def main():
    print("--- ЗАПРОС ДАННЫХ ИЗ ПОДКЛЮЧЕННОЙ ПОСТГРЕС БАЗЫ ---\n")
    
    db = SessionLocal()
    try:
        categories = crud.get_categories(db)
        
        if not categories:
            print("В базе данных пока нет категорий. Сначала запустите app/init_db.py")
            return
            
        for cat in categories:
            print(f"Категория: {cat.title} (ID: {cat.id})")
            print("-" * 40)
            
            if not cat.books:
                print("  В этой категории пока нет книг.")
            else:
                for book in cat.books:
                    print(f"  • Книга: {book.title}")
                    print(f"    Цена: {book.price} руб.")
                    print(f"    Описание: {book.description}")
                    print()
            print("=" * 40)
            
    except Exception as e:
        print(f"Ошибка при чтении данных: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()