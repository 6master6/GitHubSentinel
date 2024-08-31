import datetime

def current_timestamp():
    return datetime.datetime.now().isoformat()

def format_commit_message(commit):
    return f"{commit['commit']['message']} by {commit['commit']['author']['name']}"
