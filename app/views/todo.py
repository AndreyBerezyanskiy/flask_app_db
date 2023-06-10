from typing import List
from app.models import Todo
from app.forms import AddTodoForm
from app.models import User
from app import db
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user

todo_blueprint = Blueprint("todo", __name__, url_prefix="/todo")


@todo_blueprint.route("/", methods=["GET", "POST"])
def index():
    form = AddTodoForm()
    user: User = current_user

    if current_user.is_authenticated:
        todos = Todo.query.order_by(Todo.id)
        todos: List[Todo] = todos.filter_by(user_id=current_user.id).all()

        if form.validate_on_submit():
            todo = Todo(title=form.title.data, user_id=user.id)

            db.session.add(todo)
            db.session.commit()
            flash("success")
            return redirect(url_for("todo.index"))

        return render_template("todo-list.html", todos=todos, form=form)

    return render_template("todo-list.html", todos=[], form=form)


# @todo_blueprint.route("/add", methods=["GET", "POST"])
# def add_todo():
#     form = AddTodoForm()
#     user: User = current_user

#     if form.validate_on_submit():
#         todo = Todo(title=form.title.data, user_id=user.id)

#         db.session.add(todo)
#         db.session.commit()
#         flash("success")
#         return redirect(url_for("todo.index"))

#     return render_template("todo-list.html", form=form)


@todo_blueprint.route("/<int:todo_id>/delete")
def delete_todo(todo_id: int):
    # user: User = current_user
    todo: Todo = Todo.query.filter(Todo.id == todo_id).first()
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for("todo.index"))
