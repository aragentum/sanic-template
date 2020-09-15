from sanic import Sanic

from sanic_template.view.sample_view import sample_bp
from sanic_template.view.user_view import user_bp


def setup(app: Sanic):
    app.blueprint(user_bp)
    app.blueprint(sample_bp)
