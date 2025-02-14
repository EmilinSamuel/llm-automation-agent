import subprocess
import os

def task_a1(email: str):
    # Install uv if not already installed
    subprocess.run(["uv", "install", "requests"])
    
    # Run datagen.py with the email argument
    subprocess.run(["python", "datagen.py", email])