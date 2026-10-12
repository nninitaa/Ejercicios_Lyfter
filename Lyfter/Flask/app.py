from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/tasks', methods=['GET', 'POST'])
def handle_tasks():
    with open('tasks.json', 'r') as f:
        tasks = json.load(f)

    if request.method == 'POST':
        new_task = request.get_json()

        if not new_task or not new_task.get('title') or not new_task.get('description') or not new_task.get('id'):
            return {'error': 'Missing required fields'}, 400

        valid_statuses = ['To Do', 'In Progress', 'Completed']
        if new_task.get('status') not in valid_statuses:
            return {'error': 'Invalid status'}, 400

        for task in tasks:
            if task['id'] == new_task['id']:
                return {'error': 'Duplicate task ID'}, 400

        tasks.append(new_task)
        with open('tasks.json', 'w') as f:
            json.dump(tasks, f, indent=4)

        return {'message': 'Task created successfully', 'task': new_task}, 201

    status = request.args.get('status')
    if status is not None:
        filtered_tasks = [task for task in tasks if task.get('status') == status]
        return filtered_tasks

    return tasks

if __name__ == '__main__':
    app.run(debug=True)