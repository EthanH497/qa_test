from fastapi import APIRouter
from .services import (
    find_all_users,
    insert_one_user,
    update_one_user,
    delete_one_user
)
from fastapi.testclient import TestClient

# User router
user_router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


# Get all users
@user_router.get("/")
async def get_all_users():
    return find_all_users()


# Create new user with client_code and organization in url params
@user_router.post("/")
async def post_user(client_code: str, organization: str):
    return insert_one_user(client_code, organization)


# Update user's client_code
@user_router.put("/")
async def put_user(client_code: str, new_client_code: str):
    return update_one_user(client_code, new_client_code)


# Delete user by client_code and organization
@user_router.delete("/")
async def delete_user(client_code: str, organization: str):
    return delete_one_user(client_code, organization)


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
