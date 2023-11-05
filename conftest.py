import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture(scope="session")
def test_client():
    with TestClient(app) as cl:
        print("Before testing")
        yield cl
        print("Next session started...")


