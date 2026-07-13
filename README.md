
ОПИСАНИЕ ЗАПУСКА ПРОЕКТА

Предварительные требования: 
Python 3.8 или выше
PostgreSQL
Установленный git

Шаг 1. Клонирование репозитория
git clone <https://github.com/FedorKK667/python_oktagon>
cd <python_oktagon>

Шаг 2. Создание виртуального окружения и установка зависимостей (macos)
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Шаг 3. Настройка переменных окружения
Создайте файл .env в корне проекта и добавьте туда параметры подключения к БД:
DATABASE_URL=postgresql://username:password@host:port/dbname

Шаг 4. Инициализация базы данных
python init_db.py

Шаг 5. Запуск сервера
uvicorn main:app --reload --host 127.0.0.1 --port 8000

