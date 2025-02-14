import csv
import json

def task_b10(csv_path: str, filter_key: str, filter_value: str):
    with open(csv_path, "r") as file:
        reader = csv.DictReader(file)
        filtered_data = [row for row in reader if row[filter_key] == filter_value]
    return json.dumps(filtered_data)