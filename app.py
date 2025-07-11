from flask import Flask,render_template, request, redirect
from data_structures import task_db, arrays_util
from data_structures.queue_tasks import TaskQueue

app = Flask(__name__)
task_queue = TaskQueue()

@app.route('/')
def index():
    tasks = task_db.get_tasks()
    return render_template('index.html', tasks=tasks)

@app.route("/search")
def search():
    query = request.args.get("q", "").strip()
    if query:
        results = arrays_util.search_tasks(task_db.get_tasks(), query)
    else:
        results= task_db.get_tasks()
    return render_template("index.html", tasks=results)


@app.route('/add', methods=['POST'])
def add():
    desc = request.form.get('description')
    if desc:
        task_db.add_task(desc)
        task_queue.enqueue(desc)
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete(task_id):
    task_db.delete_task(task_id)
    return redirect('/')

@app.route('/edit/<int:task_id>', methods=['POST'])
def edit(task_id):
    new_desc = request.form.get('new_desc')
    if new_desc:
        task_db.update_task(task_id,new_desc)
    return redirect('/')

@app.route('/toggle/<int:task_id>')
def toggle(task_id):
    task_db.toggle_status(task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)