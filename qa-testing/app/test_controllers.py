from fastapi.testclient import TestClient
from .controllers import user_router

client = TestClient(user_router)


def test_get_all_users():
    response = client.get("/users")
    assert response.status_code == 200, response.text


def test_post_user():
    user = {"client_code": "1234", "organization": "Test Organization"}
    response = client.post(f"/users/?client_code={user['client_code']}&organization={user['organization']}")
    assert response.status_code == 200, response.text


def test_put_user():
    user = {"client_code": "1234", "organization": "Test Organization"}
    new_code = "5678"
    response = client.put(f"/users/?client_code={user['client_code']}&new_client_code={new_code}")
    assert response.status_code == 200, response.text


def test_delete_user():
    user = {"client_code": "1234", "organization": "Test Organization"}
    response = client.delete(f"/users/?client_code={user['client_code']}&organization={user['organization']}")
    assert response.status_code == 200, response.text