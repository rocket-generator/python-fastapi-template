import pytest
from pathlib import Path


@pytest.fixture(scope='module', autouse=True)
def scope_module():
    print("    setup before module")
    yield
    print("    teardown after module")

