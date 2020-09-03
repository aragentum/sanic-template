import os
import logging.config

# BASE
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['console']
        },
        'sanic': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False
        },
        'sanic_template': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
