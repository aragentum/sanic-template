# Sanic Template
This is simple template project on Sanic + Gino + Alembic.

## Run
To run in dev mode:
```
python manage.py runserver
```

To run in prod mode:
```
sanic sanic_template.runner.app --port 8000 --host 0.0.0.0 --workers 4
```
or
```
uvicorn sanic_template.runner:app ...
```
or
```
gunicorn sanic_template.runner:app --bind 0.0.0.0:8000 --worker-class sanic.worker.GunicornWorker
```

## Migrations
In this project used database migration tool Alembic (https://alembic.sqlalchemy.org/en/latest/tutorial.html). This tool only works in sync mode, it required sync PostgreSQL driver - psycopg2.
By default, for Alembic database url `postgresql://...` means `postgresql+psycopg2://...` and for Gino by default it means `postgresql+asyncpg://`, for this reason, the same database url will be works for both Gino and Alembic. 
This project has some custom commands which simplifies the process interaction with database. 

To apply migrations:
```
python manage.py migrate
```

To generate new migration:
```
python manage.py makemigrations <migration message>
```

To display the current revision for a database:
```
python manage.py current
```

To display history of migration:
```
python manage.py history
```

## Documentation
This project has Swagger UI by next url `host:port/swagger/` and OpenAPI 2.0 spec at `host:port/swagger/swagger.json`.
OpenAPI urls is only available if your configuration has `DEBUG=True`.
