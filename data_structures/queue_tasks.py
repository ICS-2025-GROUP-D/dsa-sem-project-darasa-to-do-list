# === Queue_tasks.py (DAVIS)===
from collections import deque

class TaskQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, task):
        self.queue.append(task)

    def dequeue(self):
        return self.queue.popleft() if self.queue else None

    def view(self):
        return list(self.queue)