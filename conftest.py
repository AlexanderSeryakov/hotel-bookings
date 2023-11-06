from typing import Generator

import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture(scope="session")
def test_client() -> Generator:
    with TestClient(app) as cl:
        yield cl
