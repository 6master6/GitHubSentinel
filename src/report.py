class ReportGenerator:
    def __init__(self, config):
        self.template = config.get("report_template", "default")

    def generate_report(self, updates):
        report = f"GitHub Repository Updates:\n\n"
        for repo, commits in updates.items():
            report += f"Repository: {repo}\n"
            for commit in commits:
                report += f"- {commit['commit']['message']} (by {commit['commit']['author']['name']})\n"
            report += "\n"
        return report
