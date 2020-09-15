import click


@click.command(help="List changeset scripts in chronological order")
def history():
    from sanic_template.conf import settings
    from alembic.config import Config
    from alembic.command import history

    alembic_cfg = Config(settings.ALEMBIC_CONFIG_PATH)
    history(alembic_cfg)
