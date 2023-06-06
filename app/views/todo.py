from app.models import Todo
from app.forms import AddTodoForm
from app.models import User
from app import db
from flask import Blueprint, render_template, flash
from flask_login import current_user

todo_blueprint = Blueprint("todo", __name__, url_prefix="/todo")


@todo_blueprint.route("/")
def index():
    form = AddTodoForm()
    if current_user.is_authenticated:
        todos: Todo = Todo.query.order_by(Todo.id)
        todos = todos.filter_by(user_id=current_user.id)
        return render_template("todo-list.html", todos=todos)

    return render_template("todo-list.html", todos=[], form=form)


@todo_blueprint.route("/add", methods=["GET", "POST"])
def add_todo():
    form = AddTodoForm()
    # user: User = current_user

    if form.validate_on_submit():
        todo = Todo(title=form.title.data)

        db.session.add(todo)
        db.session.commit()
        flash("success")
    return render_template("todo-list.html", form=form)
