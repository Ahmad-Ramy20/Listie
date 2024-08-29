from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

class Task:
    def __init__(self, id, status='uncompleted'):
        self.id = id
        self.status = status

    def __str__(self):
        status_marker = '[x]' if self.status == 'completed' else ''
        return f'{status_marker} {self.id}'

    @staticmethod
    def from_string(task_str):
        status = 'completed' if '[x]' in task_str else 'uncompleted'
        task_id = task_str.replace('[x] ', '').strip()
        return Task(task_id, status)

class TaskManager:
    def __init__(self, file_name='tasks.txt'):
        self.file_name = file_name
        
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as file:
                pass

    def read_tasks(self):
        try:
            with open(self.file_name, 'r') as file:
                tasks = [Task.from_string(line.strip()) for line in file.readlines()]
            print(tasks)
        except FileNotFoundError:
            tasks = []
        return tasks

    def write_tasks(self, tasks):
        with open(self.file_name, 'w') as file:
            for task in tasks:
                file.write(str(task) + '\n')

    def set_file(self, file_name):
        self.file_name = file_name

    def create_file(self, file_name):
        if not os.path.exists(file_name):
            with open(file_name, 'w') as file:
                pass
            
            self.set_file(file_name)

           
            tasks = self.read_tasks()
            if tasks:
                self.write_tasks(tasks)

    def add_task(self, task_text):
        tasks = self.read_tasks()
        if task_text:
            bullet_task = f'• {task_text}'
            if bullet_task not in [t.id for t in tasks]:
                tasks.append(Task(bullet_task))
                self.write_tasks(tasks)
                return None
            else:
                return f"Task '{task_text}' already exists."

    def remove_task(self, task_id):
        tasks = self.read_tasks()
        self.write_tasks([t for t in tasks if t.id != task_id])

    def complete_task(self, task_text):
        tasks = self.read_tasks()
        for task in tasks:
            if task.id == task_text:
                task.status = 'completed'
        self.write_tasks(tasks)

    def clear_tasks(self):
        self.write_tasks([])

task_manager = TaskManager()

@app.route('/')
def index():
    tasks = task_manager.read_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_text = request.form.get('task')
    message = task_manager.add_task(task_text)
    task_list = task_manager.read_tasks()
    return render_template('index.html', tasks=task_list, message=message)

@app.route('/complete/<task>')
def complete_task(task):
    task_manager.complete_task(task)
    return redirect('/')

@app.route('/remove/<task>')
def remove_task(task):
    task_manager.remove_task(task)
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear_tasks():
    task_manager.clear_tasks()
    return redirect('/')

@app.route('/set_file', methods=['POST'])
def set_file():
    file_name = request.form.get('file_name')
    task_manager.set_file(file_name)
    return redirect('/')

@app.route('/create_file', methods=['POST'])
def create_file():
    file_name = request.form.get('new_file_name')
    task_manager.create_file(file_name)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)