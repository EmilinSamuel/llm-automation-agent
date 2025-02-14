import requests
import os

def task_a7():
    # Read email content
    with open("data/email.txt", "r") as file:
        email_content = file.read()
    
    # AI Proxy API call
    headers = {
        "Authorization": f"Bearer {os.environ['AIPROXY_TOKEN']}",  # Use AIPROXY_TOKEN
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o-mini",  # Use GPT-4o-Mini
        "messages": [
            {"role": "user", "content": f"Extract only the sender's email address from: {email_content}"}  # Concise prompt
        ],
        "max_tokens": 20  # Limit output length
    }
    
    # AI Proxy endpoint
    url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    
    # Timeout after 15 seconds to meet 20s total limit
    response = requests.post(
        url,
        headers=headers,
        json=data,
        timeout=15
    )
    
    # Handle errors
    if response.status_code != 200:
        raise Exception(f"AI Proxy error: {response.text}")
    
    # Log the response for debugging
    print("LLM Response:", response.json())
    
    # Extract email
    sender_email = response.json()["choices"][0]["message"]["content"].strip()
    
    # Log the extracted email for debugging
    print("Extracted Email:", sender_email)
    
    # Write result
    with open("data/email-sender.txt", "w") as file:
        file.write(sender_email)