# Sanic Template
This is simple template project on Sanic + Gino + Alembic.

## Run
```
python -m sanic_template
```

## Migrations
In this project used database migration tool Alembic. This tool only works in sync mode, it required sync PostgreSQL driver - psycopg2.
By default for Alembic database url `postgresql://...` means `postgresql+psycopg2://...` and for Gino by default it means `postgresql+asyncpg://`, for this reason, the same database url will be works for both Gino and Alembic. 

Some useful commands:
```
# display the current revision for a database
alembic current
```

```
# apply all migrations
alembic upgrade head
```

```
# generate new migration
alembic revision --autogenerate --rev-id "0001" -m "Create users table"
```
