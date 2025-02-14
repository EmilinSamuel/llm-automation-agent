from fastapi import FastAPI, HTTPException
import os
import requests
from dotenv import load_dotenv

# Import task functions
from tasks.task_a1 import task_a1
from tasks.task_a2 import task_a2
from tasks.task_a3 import task_a3
from tasks.task_a4 import task_a4
from tasks.task_a5 import task_a5
from tasks.task_a6 import task_a6
from tasks.task_a7 import task_a7
from tasks.task_a8 import task_a8
from tasks.task_a9 import task_a9
from tasks.task_a10 import task_a10
from tasks.task_b1 import task_b1
from tasks.task_b2 import task_b2
from tasks.task_b3 import task_b3
from tasks.task_b4 import task_b4
from tasks.task_b5 import task_b5
from tasks.task_b6 import task_b6
from tasks.task_b7 import task_b7
from tasks.task_b8 import task_b8
from tasks.task_b9 import task_b9
from tasks.task_b10 import task_b10

load_dotenv()  # Load environment variables from .env

app = FastAPI()

@app.post("/run")
async def run(task: str):
    try:
        # Parse the task and execute steps
        result = execute_task(task)
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/read")
async def read(path: str):
    try:
        with open(path, "r") as file:
            content = file.read()
        return {"content": content}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

def execute_task(task: str):
    # Normalize task input
    task = task.lower()

    # Map tasks to their corresponding functions
    if "install uv" in task and "datagen.py" in task:
        email = task.split()[-1]  # Extract email from the task
        task_a1(email)
        return "Installed uv and ran datagen.py"
    elif "format" in task and "format.md" in task:
        task_a2()
        return "Formatted data/format.md with Prettier"
    elif "count the number of wednesdays" in task:
        task_a3()
        return "Counted Wednesdays and saved to data/dates-wednesdays.txt"
    elif "sort the contacts" in task:
        task_a4()
        return "Sorted contacts and saved to data/contacts-sorted.json"
    elif "write the first line of the 10 most recent .log files" in task:
        task_a5()
        return "Wrote the first line of the 10 most recent .log files to data/logs-recent.txt"
    elif "extract h1 headings" in task:
        task_a6()
        return "Extracted H1 headings and saved to data/docs/index.json"
    elif "extract the sender's email" in task:
        task_a7()
        return "Extracted sender's email and saved to data/email-sender.txt"
    elif "extract the credit card number" in task:
        task_a8()
        return "Extracted credit card number and saved to data/credit-card.txt"
    elif "find the most similar pair of comments" in task:
        task_a9()
        return "Found the most similar pair of comments and saved to data/comments-similar.txt"
    elif "calculate total sales for gold tickets" in task:
        task_a10()
        return "Calculated total sales for Gold tickets and saved to data/ticket-sales-gold.txt"
    elif "fetch data from an api" in task:
        url = task.split("from")[1].split("and")[0].strip()
        save_path = task.split("to")[1].strip()
        task_b3(url, save_path)
        return f"Fetched data from {url} and saved to {save_path}"
    elif "clone a git repo" in task:
        repo_url = task.split("clone")[1].split("and")[0].strip()
        commit_message = task.split("message")[1].strip().strip("'\"")
        task_b4(repo_url, commit_message)
        return f"Cloned {repo_url} and committed with message '{commit_message}'"
    elif "run a sql query" in task:
        query = task.split("query")[1].strip()
        result = task_b5(query)
        return f"Ran SQL query: {query}. Result: {result}"
    elif "scrape data from" in task:
        url = task.split("from")[1].strip()
        result = task_b6(url)
        return f"Scraped data from {url}. Result: {result}"
    elif "compress or resize an image" in task:
        image_path = task.split("resize")[1].split("to")[0].strip()
        size = tuple(map(int, task.split("to")[1].split("and")[0].strip().split("x")))
        output_path = task.split("save to")[1].strip()
        task_b7(image_path, output_path, size)
        return f"Resized {image_path} to {size} and saved to {output_path}"
    elif "transcribe audio from" in task:
        audio_path = task.split("from")[1].strip()
        task_b8(audio_path)
        return f"Transcribed audio from {audio_path} and saved to data/transcription.txt"
    elif "convert markdown to html" in task:
        markdown_path = task.split("convert")[1].split("to")[0].strip()
        html_path = task.split("save to")[1].strip()
        task_b9(markdown_path, html_path)
        return f"Converted {markdown_path} to HTML and saved to {html_path}"
    elif "filter a csv file" in task:
        csv_path = task.split("filter")[1].split("by")[0].strip()
        filter_key = task.split("column=")[1].split("and")[0].strip().strip("'\"")
        filter_value = task.split("value=")[1].strip().strip("'\"")
        result = task_b10(csv_path, filter_key, filter_value)
        return f"Filtered {csv_path} by {filter_key}={filter_value}. Result: {result}"
    else:
        raise ValueError("Task not recognized")