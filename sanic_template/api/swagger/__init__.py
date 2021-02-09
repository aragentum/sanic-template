from sanic import Sanic
from sanic_openapi import swagger_blueprint


def setup(app: Sanic):
    app.blueprint(swagger_blueprint)
