import sqlite3

class Database:
    def __init__(self):
        conct = sqlite3.connect("todo.db")
        cur = conct.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title text, description text, time text, status BOOLEAN DEFAULT FALSE)")
        conct.commit()
        conct.close()

    def load_tasks(self):
        conct = sqlite3.connect("todo.db")
        cur = conct.cursor()
        cur.execute("SELECT * FROM tasks ORDER BY status")
        rows = cur.fetchall()
        conct.close()
        return rows

    def insert_task(self, title, description, time):
        conct = sqlite3.connect("todo.db")
        cur = conct.cursor()
        cur.execute("INSERT INTO tasks (title, description, time) VALUES (?, ?, ?)", (title, description, time))
        conct.commit()
        conct.close()

    def edit_task_done(self, id):
        conct = sqlite3.connect("todo.db")
        cur = conct.cursor()
        cur.execute("UPDATE tasks SET status = NOT status WHERE id=?", (id,))
        conct.commit()
        conct.close()

    def delete_task(self, id):
        conct = sqlite3.connect("todo.db")
        cur = conct.cursor()
        cur.execute("DELETE FROM tasks WHERE id=?", (id,))
        conct.commit()
        conct.close()

    def show_description(self, id):
        conct = sqlite3.connect("todo.db")
        cur = conct.cursor()
        cur.execute("SELECT * FROM tasks WHERE id=?", (id,))
        rows = cur.fetchall()
        conct.close()
        return rows