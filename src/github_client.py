import requests

class GitHubClient:
    BASE_URL = "https://api.github.com"

    def __init__(self, token):
        self.headers = {"Authorization": f"token {token}"}

    def get_repository_updates(self, repo_name, since):
        url = f"{self.BASE_URL}/repos/{repo_name}/commits"
        params = {"since": since}
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
