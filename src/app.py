from flask import Flask, request, render_template, redirect, url_for
from database import Database

app = Flask(__name__)

@app.route('/')
def index():
    todos = Database.get_todos()
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form['task']
    Database.add_todo(task)
    return redirect(url_for('index'))


@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    Database.delete_todo(todo_id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')