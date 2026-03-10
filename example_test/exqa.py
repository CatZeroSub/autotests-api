import httpx
import faker
from faker import Faker



fake = Faker()


response = httpx.post("http://localhost:8000/api/v1/authentication/login", json={'email': 'user@example.com', 'password': 'string'})
json_data = response.json()
access_token = json_data['token']['accessToken']

login = httpx.get('http://localhost:8000/api/v1/users/me', headers={'Authorization': 'Bearer ' + access_token})


json_data = login.json()

user_id = json_data['user']['id']

update = httpx.patch(f'http://localhost:8000/api/v1/users/{user_id}', json={"email": fake.email(),   #andersonmitchell@example.net
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"}, headers={'Authorization': 'Bearer ' + access_token})

print(update.json())


