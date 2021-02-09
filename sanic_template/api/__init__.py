from sanic import Blueprint, Sanic

from .swagger import setup as swagger_setup
from .view.v1.sample_view import sample_bp
from .view.v1.user_view import user_bp


def setup(app: Sanic):
    api_v1 = Blueprint.group(user_bp, sample_bp, url_prefix='/api/v1')
    app.blueprint(api_v1)

    # init swagger blueprint
    swagger_setup(app)
