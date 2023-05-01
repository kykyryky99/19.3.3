import requests

base_url = 'https://petstore.swagger.io'
headers = {'Content-Type': 'application/json'}
create_data = {
    "name": "Cat_Yarik",
    "photoUrls": [
        "string"
    ],
    "status": "available"
}

resp = requests.post(base_url + '/v2/pet', headers=headers, json=create_data)
result_create = resp.json()
result_create_status_code = resp.status_code

print(result_create)
print(result_create_status_code)

pet_id = result_create['id']

resp = requests.get(base_url + f'/v2/pet/{pet_id}')

print(resp.status_code)
print(resp.json())

put_data = {
    "id": pet_id,
    "name": "Cat_Yarik",
    "photoUrls": [
        "string"
    ],
    "status": "sold"
}
resp = requests.put(base_url + '/v2/pet', headers=headers, json=put_data)

print(resp.status_code)
print(resp.json())

resp = requests.get(base_url + f'/v2/pet/{pet_id}')

print(resp.status_code)
print(resp.json())

resp = requests.delete(base_url + f'/v2/pet/{pet_id}', headers=headers)

print(resp.status_code)
print(resp.json())

resp = requests.get(base_url + f'/v2/pet/{pet_id}')

print(resp.status_code)
print(resp.json())
