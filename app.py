from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask("Hello World")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# base app based on following blog post: https://www.python-engineer.com/posts/flask-todo-app/

# defining class for db entry with unique id, title and boolean option if completed or not
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
    category_id = db.Column(db.Integer)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


@app.route('/')
def index():
    # show complete list of todos on index page
    todo_list = Todo.query.all()
    category_list = Category.query.all()
    return render_template('base.html', todo_list=todo_list, category_list=category_list)


@app.route("/add", methods=["POST"])
def add():
    # add new task for Samurai
    title = request.form.get("title")
    category_id = request.form.get("category_id")
    new_todo = Todo(title=title, complete=False, category_id=category_id)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))  # reload page / redirect


@app.route("/update/<int:todo_id>")
def update(todo_id):
    # change status of Samurai task
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))  # reload page / redirect


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    # remove a task from the Samurais mind
    todo = Todo.query.filter_by(id=todo_id).first()  # find the proper todo id
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))  # reload page / redirect

# about page
@app.route('/about')
def about():
    return 'About 7 Samurai ToDos'


CATEGORIES = [
    'heavy',
    'difficult',
    'fast',
    'hidden',
    'agressive',
    'shy',
    'challenging'
]


def init_categories(db):
    if Category.query.count() != 0:
        return

    for categoryName in CATEGORIES:
        db.session.add(Category(name=categoryName))
        db.session.commit()


if __name__ == "__main__":
    db.create_all()
    init_categories(db)

    app.run(debug=True, port=5000)
