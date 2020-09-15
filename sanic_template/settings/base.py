import os
import logging.config

DEBUG = True
DB_ECHO = True

# BASE
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ALEMBIC
ALEMBIC_CONFIG_PATH = os.getenv('ALEMBIC_CONFIG_PATH', os.path.join(os.path.dirname(BASE_DIR), 'alembic.ini'))
ALEMBIC_MIGRATIONS_PATH = os.getenv('ALEMBIC_MIGRATIONS_PATH', os.path.join(os.path.dirname(BASE_DIR), 'migrations'))

# LOGGING
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console_formatter': {
            'format': '[%(asctime)s]:[%(process)d] | [%(levelname)s] | %(name)-15s - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console_formatter'
        }
    }
}
LOGGING_LEVEL = logging.DEBUG
