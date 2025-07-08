# === array_utils.py (Jakes) ===
def sort_tasks(task_list):
    return sorted(task_list, key=lambda x: x['description'])

def count_status(task_list, status):
    return len([t for t in task_list if t['status'] == status])

#Added function to search for tasks on GUI and webpage
def search_tasks(tasks,keyword):
     keyword = keyword.lower()
     return [task for task in tasks if keyword in task['description'].lower()]