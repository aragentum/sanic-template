from sanic import Sanic

from sanic_template import database, api, error
from sanic_template.conf import settings

from sanic_template.other import logging

app = Sanic("sanic_app", log_config=settings.LOGGING_CONFIG)
app.config.from_object(settings)

# init
logging.setup()
database.setup(app)
api.setup(app)
error.setup(app)


@app.listener("after_server_start")
async def create_initial_data(app, loop):
    from sanic_template.database.repo.user_repo import user_repo
    await user_repo.create_or_update("aragentum", "Roman", "Averchenkov")


def run():
    app.run(host="0.0.0.0", port=8000, workers=1,
            debug=app.config.DEBUG, auto_reload=app.config.DEBUG)


if __name__ == '__main__':
    run()
