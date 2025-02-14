import sqlite3

def task_b5(query: str):
    conn = sqlite3.connect("data/ticket-sales.db")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result