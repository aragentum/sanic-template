import click


@click.command(help="Apply migrations")
def migrate():
    from sanic_template.conf import settings
    from alembic.config import Config
    from alembic.command import upgrade

    alembic_cfg = Config(settings.ALEMBIC_CONFIG_PATH)
    upgrade(alembic_cfg, "head")
