from src.github_client import GitHubClient

class SubscriptionManager:
    def __init__(self, config):
        self.client = GitHubClient(config.get("github_token"))
        self.subscriptions = config.get("subscriptions", [])

    def fetch_updates(self):
        updates = {}
        for repo in self.subscriptions:
            updates[repo] = self.client.get_repository_updates(repo, self.get_last_checked(repo))
        return updates

    def get_last_checked(self, repo_name):
        return "2023-01-01T00:00:00Z"
