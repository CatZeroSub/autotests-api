import httpx
import requests
import pytest


@pytest.fixture
def login_post():
    response = httpx.post("http://localhost:8000/api/v1/authentication/login", json={'email': 'artem1996@example.com', 'password': 'artem1996'})
    access_token = response.json()['token']['accessToken']
    return access_token

#print(login_post())

def test_authorization(login_post):
    response = httpx.get("http://localhost:8000/api/v1/users/me", headers={'Authorization': 'Bearer ' + login_post})
    assert response.status_code == 200

