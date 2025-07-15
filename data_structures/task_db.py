# === task_db (RAY) ===
import sqlite3

conn = sqlite3.connect("darasa_todo.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        status TEXT DEFAULT 'pending',
        tags TEXT DEFAULT ''
    )
''')
conn.commit()

def add_task(description, tags= ''):
    cursor.execute("INSERT INTO tasks (description, tags) VALUES (?, ?)", (description,tags))
    conn.commit()

def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    return [{"id": row[0], "description": row[1], "status": row[2], "tags": row[3]} for row in cursor.fetchall()]

def update_task(task_id, new_desc):
    cursor.execute("UPDATE tasks SET description = ? WHERE id = ?", (new_desc, task_id))
    conn.commit()


#Updated tags function (AMANI)
def add_tag(task_id,tag):
    tag= tag.strip()
    if tag:
        tags= get_tags(task_id)
        if tag not in tags:
            tags.append(tag)
            update_tags(task_id, ','.join(tags))

def update_tags(task_id, tags):
    cursor.execute("UPDATE tasks SET tags = ? WHERE id = ?", (tags, task_id))
    conn.commit()

def get_tags(task_id):
    cursor.execute("SELECT tags FROM tasks WHERE id = ?", (task_id,))
    row= cursor.fetchone()
    return row[0].split(',') if row and row[0] else []



def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()

def toggle_status(task_id):
    cursor.execute("SELECT status FROM tasks WHERE id = ?", (task_id,))
    current = cursor.fetchone()
    if current:
        new_status = 'done' if current[0] == 'pending' else 'pending'
        cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id))
        conn.commit()
