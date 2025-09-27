# Final-Project
FINAL PROJECT (Sherdos)

1. Установить зависимости:

    ```
    pip install fastapi uvicorn sqlalchemy pydantic python-jose~
    ```
    или
    ```
    requirements.txt
    ```
    
3. Запустить сервер:

    ```
    uvicorn app.main:app --reload
    ```
    
5. Авторизация для админа:
    
    - Логин: `admin`
    - Пароль: `admin123`
      
## Эндпоинты
- `/students` — CRUD студентов, поиск, список c курсами/оценками
- `/courses` — CRUD курсов
- `/enrollments` — Запись на курс, выставление оценки
- `/admin/login` — JWT-авторизация
