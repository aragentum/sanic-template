from sanic import Sanic
from sanic_openapi import swagger_blueprint


def setup(app: Sanic):
    if app.config.DEBUG:
        app.blueprint(swagger_blueprint)
