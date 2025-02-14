import subprocess

def task_a2():
    # Format the file using Prettier
    subprocess.run(["npx", "prettier@3.4.2", "--write", "data/format.md"])