
class Task:
    def __init__(self, email):
        self.email = email
        self.task_description = self.create_task()

    def create_task(self):
        return f"Task: Follow up with {self.email.from_address} regarding {self.email.subject}"
    