from loguru import logger
from sanic import Sanic


async def on_startup(app, loop):
    from sanic_template.database.db import db
    from sanic_template.conf import settings

    logger.info("Setup gino connection")
    await db.set_bind(settings.PG_URL,
                      min_size=app.config.setdefault("DB_POOL_MIN_SIZE", 5),
                      max_size=app.config.setdefault("DB_POOL_MAX_SIZE", 10),
                      echo=app.config.setdefault("DB_ECHO", False),
                      loop=loop)


async def on_shutdown(app, loop):
    from sanic_template.database.db import db

    bind = db.pop_bind()
    if bind:
        logger.info("Close gino connection")
        await bind.close()


def setup(app: Sanic):
    app.register_listener(on_startup, "before_server_start")
    app.register_listener(on_shutdown, "after_server_stop")
