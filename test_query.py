import requests

response = requests.post(
    "http://127.0.0.1:8000/v1/queries",
    json={"query": "cats riding bikes"}
)

print(response.json())
