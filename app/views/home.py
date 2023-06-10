# from app.models import User
from flask import Blueprint, render_template

# from flask_login import login_required, current_user

home_blueprint = Blueprint("home", __name__)


@home_blueprint.route("/")
# @login_required
def index():
    # user: User = current_user
    return render_template("index.html")
