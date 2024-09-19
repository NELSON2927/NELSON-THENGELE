class TaskManager:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Reads tasks from the file."""
        try:
            with open(self.filename, 'r') as file:
                tasks = file.readlines()
               
                return [task.strip() for task in tasks]
        except FileNotFoundError:
            print(f"{self.filename} not found. Starting with an empty task list.")
            return []

    def add_task(self, task):
        """Adds a new task to the list."""
        self.tasks.append(task)
        print(f"Task '{task}' added successfully!")

    def save_tasks(self):
        """Writes the updated task list to the file, appending new tasks."""
        with open(self.filename, 'a') as file:
            file.write('\n'.join(self.tasks[-(len(self.tasks) - len(self.load_tasks())):]) + '\n')

    def display_tasks(self):
        """Displays all current tasks."""
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nCurrent Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def run(self):
        """Runs the main loop of the task manager program."""
        while True:
            self.display_tasks()
            new_task = input("\nEnter a new task (or type 'exit' to quit): ")
            if new_task.lower() == 'exit':
                self.save_tasks()
                print("Exiting the program. All changes saved.")
                break
            elif new_task:
                self.add_task(new_task)

if __name__ == "__main__":
    task_manager = TaskManager('tasks.txt')
    task_manager.run()