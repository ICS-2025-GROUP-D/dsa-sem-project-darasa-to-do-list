class TaskTags:
    def __init__(self):
        self.tags = {}  # task_id -> list of tags

    def add_tag(self, task_id, tag):
        if task_id not in self.tags:
            self.tags[task_id] = []
        if tag not in self.tags[task_id]:
            self.tags[task_id].append(tag)

    def get_tags(self, task_id):
        return self.tags.get(task_id, [])

    def get_all(self):
        return self.tags