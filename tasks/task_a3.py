from datetime import datetime

def task_a3():
    with open("data/dates.txt", "r") as file:
        dates = file.readlines()
    
    # Count Wednesdays
    wednesdays = [date.strip() for date in dates if datetime.strptime(date.strip(), "%Y-%m-%d").weekday() == 2]
    
    # Write the count to a new file
    with open("data/dates-wednesdays.txt", "w") as file:
        file.write(str(len(wednesdays)))