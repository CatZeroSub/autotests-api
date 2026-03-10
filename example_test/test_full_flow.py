import httpx
import pytest



def creation_user():
    response = httpx.post('http://localhost:8000/api/v1/users', json={
  "email": "user@example.com",
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
})

    json_data = response.json()
    return json_data


def get_token():
    response = httpx.post('http://localhost:8000/api/v1/authentication/login', json={"email": "user@example.com", "password": "string"})

    access_token = response.json()['token']['accessToken']
    return access_token


def get_id():
    token = get_token()
    response = httpx.get('http://localhost:8000/api/v1/users/me', headers={'Authorization': 'Bearer ' + token})

    user_id = response.json()['user']['id']
    return user_id


def test_delete_user():
    user_id = get_id()
    access_token = get_token()
    response = httpx.delete(f'http://localhost:8000/api/v1/users/{user_id}', headers={'Authorization': 'Bearer ' + access_token})
    assert response.status_code == 200





    # 1. Создаьть user ручка / create

    # 2. авторизация и получение токена ручка /login

    # 3. запрашиваем user_id ручка /me

    # 4. обновим user (нужен ID и json{
    #   "email": "user@example.com",
    #   "lastName": "string",
    #   "firstName": "string",
    #   "middleName": "string"
    # })

    # 4. удалить user (нужен только ID)