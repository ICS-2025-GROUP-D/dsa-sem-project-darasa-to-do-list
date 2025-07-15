import logging, hashlib
from flask import Flask,render_template, request, redirect
from data_structures import task_db, arrays_util
from data_structures.queue_tasks import TaskQueue
from data_structures.stack_undo import UndoStack
from data_structures.dictionary_tags import TaskTags

#Update for different tag colors from Jolene's code (AMANI)
TAG_COLORS = [
    "#2dd4bf", "#f472b6", "#60a5fa", "#facc15", "#f87171", "#a78bfa", "#34d399", "#fb923c"
]

def get_color_for_tag(tag):
    hash_object = hashlib.md5(tag.encode())
    hash_int = int(hash_object.hexdigest(), 16)
    return TAG_COLORS[hash_int % len(TAG_COLORS)]

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
task_queue = TaskQueue()
undo_stack = UndoStack()
task_tags = TaskTags()

@app.route('/')
def index():
    tasks = task_db.get_tasks()
    for task in tasks:
        task['tags'] = task['tags'].split(',') if task['tags'] else []
        task['tag_colors'] = {tag: get_color_for_tag(tag) for tag in task['tags']}
    logging.info(f"Fetched {len(tasks)} tasks.")
    return render_template('index.html', tasks=tasks)
    

@app.route("/search")
def search():
    query = request.args.get("q", "").strip()
    if query:
        results = arrays_util.search_tasks(task_db.get_tasks(), query)
    else:
        results= task_db.get_tasks()
    logging.info(f"Searched for '{query}', found {len(results)} tasks.")
    return render_template("index.html", tasks=results)

@app.route('/tag/<int:task_id>', methods=['POST'])
def tag(task_id):
    tag= request.form.get('tag')
    if tag:
        tags= task_db.get_tags(task_id)
        if tag not in tags:
            tags.append(tag)
            task_db.update_tags(task_id, ','.join(tags))
            logging.info(f"Added tag '{tag}' to task {task_id}")
    return redirect('/')

@app.route('/add', methods=['POST'])
def add():
    desc = request.form.get('description')
    if desc:
        task_db.add_task(desc)
        task_queue.enqueue(desc)
        undo_stack.push({"action":"add","desc": desc})
        logging.info(f"Added new task: {desc}")
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete(task_id):
    try:
        tasks = task_db.get_tasks()
        task= next((t for t in task_db.get_tasks() if t['id']== task_id), None)
        if task:
            undo_stack.push({
                "action": "delete",
                "id": task_id,
                "desc": task['description'],
                "status": task['status']
            })
            task_db.delete_task(task_id)
            logging.info(f"Deleted task with ID: {task_id}")
        else:
            logging.warning(f"Task{task_id} not found for deletion.")
    except Exception as e:
        logging.error(f"Error deleting task {task_id}: {e}")
    return redirect('/')

@app.route('/edit/<int:task_id>', methods=['POST'])
def edit(task_id):
    new_desc = request.form.get('new_desc')
    if new_desc:
        task_db.update_task(task_id,new_desc)
        logging.info(f"Updated task {task_id} to: {new_desc}")
    return redirect('/')

@app.route('/toggle/<int:task_id>')
def toggle(task_id):
    task_db.toggle_status(task_id)
    logging.info(f"Toggled status for task {task_id}")
    return redirect('/')

@app.route('/undo')
def undo():
    action = undo_stack.pop()
    if not action:
        return redirect('/')
    if action["action"] == "add":
        tasks = task_db.get_tasks()
        for t in tasks:
            if t['description']== action ["desc"]:
                task_db.delete_task(t['id'])
                break

    elif action["action"] == "delete":
        # Restore the deleted task with its original description
        task_db.add_task(action["desc"])
        # If the original status was 'done', toggle status after adding
        if action.get("status") == "done":
            tasks = task_db.get_tasks()
            for t in tasks:
                if t['description'] == action["desc"]:
                    task_db.toggle_status(t['id'])
                    break
    logging.info(f"Undo performed: {action}")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)