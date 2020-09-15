import click

from sanic_template.cmd.database.current import current
from sanic_template.cmd.database.history import history
from sanic_template.cmd.database.makemigrations import makemigrations
from sanic_template.cmd.database.migrate import migrate
from sanic_template.cmd.server.runserver import runserver


@click.group()
def cli():
    pass


cli.add_command(runserver)
cli.add_command(current)
cli.add_command(migrate)
cli.add_command(history)
cli.add_command(makemigrations)
