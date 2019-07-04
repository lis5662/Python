import requests

# res = requests.get("https://news.ycombinator.com/")
# print(res.text)

url = "http://www.google.com"
response = requests.get(url)

print(f"you request to {url} came back w/ status code {response.status_code}")

print(response.text)