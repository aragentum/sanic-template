from .base import *

DEBUG = True
DB_ECHO = False

# DATABASE
PG_HOST = os.getenv('PG_HOST', 'st-db')
PG_PORT = os.getenv('PG_PORT', '5432')
PG_USER = os.getenv('PG_USER', 'st')
PG_PASSWORD = os.getenv('PG_PASSWORD', 'st123')
PG_DB = os.getenv('PG_DB', 'st')
PG_SSL_MODE = "disable"

PG_URL = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}?sslmode={PG_SSL_MODE}"

# LOGGING
LOGGING_LEVEL = logging.DEBUG
