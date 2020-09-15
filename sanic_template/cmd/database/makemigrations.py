import click


@click.command(help="Auto generate migrations")
@click.argument('message')
def makemigrations(message):
    import os
    from sanic_template.conf import settings
    from alembic.config import Config
    from alembic.command import revision

    alembic_cfg = Config(settings.ALEMBIC_CONFIG_PATH)
    path, dirs, files = next(os.walk(os.path.join(settings.ALEMBIC_MIGRATIONS_PATH, 'versions')))

    revision(alembic_cfg, message=message, autogenerate=True, rev_id="{:04}".format(len(files) + 1))
