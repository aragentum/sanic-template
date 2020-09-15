import click


@click.command(help="Show current revision")
def current():
    from sanic_template.conf import settings
    from alembic.config import Config
    from alembic.command import current

    alembic_cfg = Config(settings.ALEMBIC_CONFIG_PATH)
    current(alembic_cfg)
