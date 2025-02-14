import os
import json

def task_a6():
    index = {}
    for root, _, files in os.walk("data/docs"):
        for file in files:
            if file.endswith(".md"):
                with open(os.path.join(root, file), "r") as f:
                    for line in f:
                        if line.startswith("# "):
                            index[file] = line.strip("# ").strip()
                            break
    
    # Write the index to a JSON file
    with open("data/docs/index.json", "w") as file:
        json.dump(index, file, indent=4)