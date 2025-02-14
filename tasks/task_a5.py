import os

def task_a5():
    log_files = sorted(
        [f for f in os.listdir("data/logs") if f.endswith(".log")],
        key=lambda x: os.path.getmtime(os.path.join("data/logs", x)),
        reverse=True
    )[:10]  # Get the 10 most recent files
    
    first_lines = []
    for log_file in log_files:
        with open(os.path.join("data/logs", log_file), "r") as file:
            first_lines.append(file.readline().strip())
    
    # Write the first lines to a new file
    with open("data/logs-recent.txt", "w") as file:
        file.write("\n".join(first_lines))