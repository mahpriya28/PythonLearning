import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response.status_code == 200:
    data = response.json()
    print(data)
    print(f"Title: {data['title']}")
else:
    print("Failed to retrieve data")

post_data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=post_data)
if response.status_code == 201:
    data = response.json() 
    print("Post created successfully:")
    print(data)
else: print("Failed to create post")