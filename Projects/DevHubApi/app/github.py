import requests
from requests.utils import str

GET /github/{username}

def getGithubUser(username: str):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    data = response.json()
    return {
        "username": data["login"],
        "name": data["name"],
        "public_repos": data["public_repos"],
        "followers": data["followers"],
        "following": data["following"]
    }