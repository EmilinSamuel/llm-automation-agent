import subprocess

def task_b4(repo_url: str, commit_message: str):
    subprocess.run(["git", "clone", repo_url])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", commit_message])