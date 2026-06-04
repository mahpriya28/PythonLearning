import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
# print(response.json())

payload = {
    "name": "PriyaM",
    "email": "abc@gmail.com"
}
response = requests.post("https://jsonplaceholder.typicode.com/users", json=payload)
# print(response.json())

payload = {
    "name": "Priya Maheshwary"
}
response = requests.put("https://jsonplaceholder.typicode.com/users/1", json=payload)
# print(response.json())

payload = {
    "name": "John Doe"
}

response = requests.patch("https://jsonplaceholder.typicode.com/users/1", json=payload)
# print(response.json())

response = requests.delete("https://jsonplaceholder.typicode.com/users/1")
print("Status Code:", response.status_code)
