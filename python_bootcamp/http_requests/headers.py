import requests

url = "https://icanhazdadjoke.com"


response = requests.get(url, headers={"Accept": "application/json"})

# print(type(response.text))
data = response.json()


print(type(data))
print(data['joke'])
print(f"status: {data['status']}")

