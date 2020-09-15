import pytest
import sqlalchemy
from sqlalchemy_utils import database_exists, drop_database, create_database

from sanic_template.conf import settings


def alembic_migrate():
    from alembic.config import Config
    from alembic import command

    command.upgrade(Config(settings.ALEMBIC_CONFIG_PATH), "head")


@pytest.fixture(scope="module")
def replace_pg_url():
    """Add to settings.PG_DB suffix '_test' and update settings.PG_URL."""
    if not settings.PG_DB.endswith("_test"):
        settings.PG_DB = settings.PG_DB + "_test"
    settings.PG_URL = (
        f"postgresql://{settings.PG_USER}:{settings.PG_PASSWORD}@"
        f"{settings.PG_HOST}:{settings.PG_PORT}/{settings.PG_DB}"
    )
    yield settings.PG_URL


@pytest.fixture(scope="module")
def sa_engine(replace_pg_url):
    """Create test db and apply migrations."""
    engine = sqlalchemy.create_engine(settings.PG_URL, echo=settings.PG_ECHO)
    if database_exists(engine.url):
        drop_database(engine.url)
    create_database(engine.url)
    alembic_migrate()
    yield engine
    drop_database(engine.url)
    engine.dispose()


@pytest.yield_fixture
def app(sa_engine):
    from sanic_template.runner import app
    yield app


@pytest.fixture
def test_client(loop, app, sanic_client):
    return loop.run_until_complete(sanic_client(app))
