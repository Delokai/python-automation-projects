import os

class Task:
    def __init__(self, description, done=False):
        self.description = description
        self.done = done

    def mark_done(self):
        self.done = True

    def __str__(self):
        status = "✔️ Done" if self.done else "⬜ Not done"
        return f"{self.description} — {status}"


class ToDoList:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, description):
        new_task = Task(description)
        self.tasks.append(new_task)
        print(f"Added: {description}")
        self.save_tasks()

    def list_tasks(self):
        if not self.tasks:
            return "No tasks yet."
        return "\n".join(f"{i+1}. {task}" for i, task in enumerate(self.tasks))

    def complete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_done()
            print("Task completed!")
            self.save_tasks()
        else:
            print("Invalid task number.")

    def save_tasks(self):
        with open(self.filename, "w") as f:
            for task in self.tasks:
                f.write(f"{task.description}|{task.done}\n")

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, "r") as f:
            for line in f:
                description, done = line.strip().split("|")
                self.tasks.append(Task(description, done == "True"))


# ------- TEST SYSTEM -------
todo = ToDoList()

todo.add_task("Finish Day 17 project")
todo.add_task("Study OOP basics again")
todo.add_task("Read chapter from CS textbook")

print("\nYour Tasks:")
print(todo.list_tasks())

todo.complete_task(1)

print("\nUpdated Tasks:")
print(todo.list_tasks())
