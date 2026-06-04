import requests

page = 1
while True:
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url, params = { "page": page })
    data = response.json()
    if not data:
        break
    print(data)
    page+=1

