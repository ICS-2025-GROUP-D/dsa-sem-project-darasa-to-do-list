# === array_utils.py (Jakes) ===
def sort_tasks(task_list):
    return sorted(task_list, key=lambda x: x['description'])

def count_status(task_list, status):
    return len([t for t in task_list if t['status'] == status])