from flask import Blueprint, render_template

todo_blueprint = Blueprint("todo", __name__, url_prefix="/todo")


@todo_blueprint.route("/")
def index():
    return render_template("todo-list.html")