import asyncio

import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy.orm import scoped_session

from app.bootstrap.create_app import create_app
from database.seeds import seed as seeder


@pytest.fixture(scope='module', autouse=True)
def setup_database():
    # Migrate to the latest version
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")
    # Seed the database
    seeder()

    yield

    # Downgrade to the base version
    command.downgrade(alembic_cfg, "base")


@pytest.fixture(scope='module', autouse=True)
async def clean_event_loop():
    yield
    await asyncio.sleep(0)


@pytest.fixture(scope="function")
def app():

    app = create_app(environment="test")
    db = app.state.injector.get(scoped_session)

    yield app

    db.close()
