import pytest
from alembic import command
from alembic.config import Config

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
