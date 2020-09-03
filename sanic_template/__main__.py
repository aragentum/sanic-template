import logging

from sanic import Sanic
from sanic.response import json

from sanic_template import database
from sanic_template.conf import settings
from sanic_template.database.model.user import User

app = Sanic("sanic_app", log_config=settings.LOGGING_CONFIG)
app.config.from_object(settings)

logger = logging.getLogger(__name__)


@app.route("/")
async def test(request):
    user_data = []
    for user in await User.query.gino.all():
        user_data.append({"first_name": user.first_name,
                          "last_name": user.last_name,
                          "username": user.username})
    return json(user_data)


@app.listener("after_server_start")
async def create_initial_data(app, loop):
    await User.create(first_name="Roman",
                      last_name="Averchenkov",
                      username="aragentum")


if __name__ == "__main__":
    database.setup(app)
    app.run(host="127.0.0.1", port=8000, workers=1,
            debug=app.config.DEBUG, auto_reload=app.config.DEBUG)
