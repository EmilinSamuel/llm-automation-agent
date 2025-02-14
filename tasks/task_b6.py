import requests
from bs4 import BeautifulSoup

def task_b6(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text()