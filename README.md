## Hotel booking API

---

### API for hotels online-booking

### Stack:

- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL

---

### Before starting the project, don`t forget to create a .env file 

> example .env file for local setup
```
POSTGRES_PASSWORD=postgres
POSTGRES_USER=postgres
POSTGRES_DB=postgres

DB_HOST=db
DB_PORT=5432
DB_USER=postgres
DB_PASS=postgres
DB_NAME=postgres
```

---

### Get started

1) Clone this repository:
    ```
    git clone https://github.com/AlexanderSeryakov/hotel-bookings.git
    ```
2) Move to root directory and paste command in terminal:
    ```
   make runsever
    ```
3) Connect to application and apply migrations:
   ```
   make conn-app
   ```
   > enter next command before application connected
   ```
   alembic upgrade head
   ```
4) Open swagger(open-api) for comfortable working:
    ```
   http://127.0.0.1:8000/docs/
   ```