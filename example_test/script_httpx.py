import httpx
import pytest


base_url = 'http://localhost:8000'

def login_payload():
    response = httpx.post(base_url + "/api/v1/authentication/login",
                          json={"email": "user@example.com",
                                "password": "string"})


    print(f"Login status code: {response.status_code}")

    json_data = response.json()
    access_token = json_data["token"]['accessToken']

    return access_token


def get_token():
    token = login_payload()
    response = httpx.get(base_url + "/api/v1/users/me",
                         headers={'Authorization':
                                      'Bearer ' + token})

    print(f"User info status code: {response.status_code}")
    json_data = response.json()
    print("User data:", json_data)

    return response.status_code


print(get_token())

