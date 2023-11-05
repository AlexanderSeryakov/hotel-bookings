from fastapi.testclient import TestClient


def test_health_check(test_client: TestClient):
    response = test_client.get("/")

    assert response.status_code == 200
    assert response.json() == {"ok": True}
