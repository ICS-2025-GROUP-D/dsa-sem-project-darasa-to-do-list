from flask import Flask,render_template, request, redirect
from data_structures import task_db

app = Flask(__name__)

@app.route('/')
def index():
    tasks = task_db.get_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    desc = request.form.get('description')
    if desc:
        task_db.add_task(desc)
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