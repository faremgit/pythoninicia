from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para almacenar las tareas
tasks = []

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if 'add_task' in request.form:
            task_content = request.form['content']
            tasks.append({"content": task_content, "id": len(tasks) + 1})  # Asignamos un ID a cada tarea
        elif 'modify_task' in request.form:
            task_id = int(request.form['task_id'])
            new_content = request.form['new_content']
            for task in tasks:
                if task['id'] == task_id:
                    task['content'] = new_content
                    break
        elif 'delete_task' in request.form:
            task_id = int(request.form['task_id'])
            tasks[:] = [task for task in tasks if task['id'] != task_id]

        return redirect(url_for('index'))

    return render_template('index.html', tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)