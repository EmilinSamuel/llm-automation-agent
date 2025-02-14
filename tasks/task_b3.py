import requests

def task_b3(url: str, save_path: str):
    response = requests.get(url)
    with open(save_path, "w") as file:
        file.write(response.text)