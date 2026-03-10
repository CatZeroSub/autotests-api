import httpx
import pytest




def login_payload():
    response = httpx.post("http://localhost:8000/docs#/authentication/login_view_api_v1_authentication_login_post", json={"email": "user@example.com", "password": "string"})
    json_data = response.json()
    print(json_data.status_code)
    access_token = json_data["token"]['accessToken']

    return access_token

def get_tokin():
    token = login_payload()
    response = httpx.get("http://localhost:8000/docs#/users/get_user_me_view_api_v1_users_me_get", header={'Authorization': 'Bearer ' + token})
    json_data = response.json()
    return json_data.status_code

print(get_tokin)

