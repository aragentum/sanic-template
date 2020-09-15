import click

from sanic_template.runner import run


@click.command(help="Run server in development mode")
def runserver():
    run()
