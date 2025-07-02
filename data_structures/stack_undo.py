class UndoStack:
    def __init__(self):
        self.stack = []

    def push(self, action):
        self.stack.append(action)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def view(self):
        return list(reversed(self.stack))