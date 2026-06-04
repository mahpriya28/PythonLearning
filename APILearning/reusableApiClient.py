import requests

class GithubClient:
    BASE_URL = "https://api.github.com"
    def get_user(self, username):
        url = f"{self.BASE_URL}/users/{username}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    
client = GithubClient()
user_data = client.get_user("octocat")
print(user_data)