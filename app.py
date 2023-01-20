from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask("Hello World")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#defining class for db entry with unique id, title and boolean option if completed or not
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

@app.route('/')
def index():
    #show complete list of todos on index page
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template('base.html', todo_list=todo_list)

@app.route("/add", methods=["Post"])
def add():
    #add new task for Samurai
    title = request.form.get("title")
    new_todo = Todo(title="title", complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index")) #reload page / redirect

@app.route('/about')
def about():
    return 'About 7 Samurai ToDos'

if __name__ == "__main__":
    db.create_all()


    db.session.add(new_todo)
    db.session.commit()

    app.run(debug=True, port=5000)
