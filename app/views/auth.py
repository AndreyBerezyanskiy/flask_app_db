from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app import db

from app.models import User
from app.forms import LoginForm

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(
            User.username == form.user_id.data.lower(),
            User.password == form.password.data,
        ).first()

        if user:
            login_user(user)
            flash("Login Successful")
            return redirect(url_for("todo.index"))

    return render_template("login.html", form=form)


@auth_blueprint.route("/logout")
@login_required
def logout():
    logout_user(current_user)

    return redirect(url_for("home.index"))
