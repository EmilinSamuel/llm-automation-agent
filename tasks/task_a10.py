import sqlite3

def task_a10():
    conn = sqlite3.connect("data/ticket-sales.db")
    cursor = conn.cursor()
    
    # Calculate total sales for "Gold" tickets
    cursor.execute("SELECT SUM(units * price) FROM tickets WHERE type = 'Gold'")
    total_sales = cursor.fetchone()[0]
    
    # Write the total sales to a new file
    with open("data/ticket-sales-gold.txt", "w") as file:
        file.write(str(total_sales))
    
    conn.close()