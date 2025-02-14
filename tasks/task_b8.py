import requests
import os

def task_b8(audio_path: str):
    headers = {
        "Authorization": f"Bearer {os.environ['AIPROXY_TOKEN']}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": f"Transcribe the audio from this file: {audio_path}"}
        ],
        "max_tokens": 100
    }
    
    response = requests.post(
        "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
        headers=headers,
        json=data,
        timeout=15
    )
    
    if response.status_code != 200:
        raise Exception(f"AI Proxy error: {response.text}")
    
    transcription = response.json()["choices"][0]["message"]["content"].strip()
    
    # Write the transcription to a new file
    with open("data/transcription.txt", "w") as file:
        file.write(transcription)