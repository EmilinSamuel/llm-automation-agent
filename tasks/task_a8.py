import requests
import os

def task_a8():
    # Use AI Proxy to extract the credit card number
    headers = {
        "Authorization": f"Bearer {os.environ['AIPROXY_TOKEN']}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": "Extract the credit card number from this image: data/credit-card.png"}
        ],
        "max_tokens": 20
    }
    
    response = requests.post(
        "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
        headers=headers,
        json=data,
        timeout=15
    )
    
    if response.status_code != 200:
        raise Exception(f"AI Proxy error: {response.text}")
    
    card_number = response.json()["choices"][0]["message"]["content"].strip()
    
    # Write the card number to a new file
    with open("data/credit-card.txt", "w") as file:
        file.write(card_number)