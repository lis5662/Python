import requests

url = "https://icanhazdadjoke.com/search"


response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": "cat", "limit": 1}
)

# print(type(response.text))
data = response.json()


print(data['results'])
# print(data['joke'])
# print(f"status: {data['status']}")

