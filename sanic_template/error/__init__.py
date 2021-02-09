import logging

from sanic import Sanic
from sanic.exceptions import NotFound, InvalidUsage, Unauthorized, Forbidden
from sanic.response import json
from schematics.exceptions import BaseError

logger = logging.getLogger(__name__)


def schematics_handler(app: Sanic, status: int):

    async def custom_handler(request, exception: BaseError):
        logger.debug(exception.to_primitive())
        # logger.exception(exception)
        return json({
            "error": "Validation error",
            "detail": exception.to_primitive()
        },
            status=status)

    return custom_handler


def common_handler(app: Sanic, status: int):

    async def custom_handler(request, exception):
        # logger.exception(exception)
        return json({"error": str(exception)}, status=status)

    return custom_handler


def setup(app: Sanic):
    app.error_handler.add(BaseError, schematics_handler(app, 400))
    app.error_handler.add(NotFound, common_handler(app, 404))
    app.error_handler.add(InvalidUsage, common_handler(app, 400))
    app.error_handler.add(Unauthorized, common_handler(app, 401))
    app.error_handler.add(Forbidden, common_handler(app, 403))
    app.error_handler.add(Exception, common_handler(app, 500))
