import requests

headers = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json'
}

payload = {
    "id": 12,
    "title": "Ramya",
    "dueDate": "2024-11-01T17:35:18.207Z",
    "completed": True
}


response = requests.put(url="https://fakerestapi.azurewebsites.net/api/v1/Activities/15",
                        headers=headers,
                        json=payload)

print(response.status_code)

data = response.json()
print(data)