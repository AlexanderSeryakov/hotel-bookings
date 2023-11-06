from fastapi.testclient import TestClient

hotels = {"Moscow": 5, "Mone": 5, "The World": 3}


def test_health_check(test_client: TestClient) -> None:
    response = test_client.get("/")

    assert response.status_code == 200
    assert response.json() == {"is_running": True}


def test_list_hotels(test_client: TestClient) -> None:
    response = test_client.get("/booking/hotels")

    assert response.status_code == 200
    assert response.json() == {"Moscow": 5, "Mone": 5, "The World": 3}


def test_add_hotel(test_client: TestClient) -> None:
    new_hotel = {"title": "test_hotel", "stars": 4}
    response = test_client.post("booking/hotels", json=new_hotel)

    assert response.status_code == 201
    res_json = response.json()
    assert new_hotel["title"] in res_json
    assert res_json[new_hotel["title"]] == res_json[new_hotel["title"]]
