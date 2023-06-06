from flask import Blueprint, render_template, flash, redirect, url_for

from app.models import User
from app.forms import AddUserForm
from app import db


user_blueprint = Blueprint("user", __name__, url_prefix="/user")


@user_blueprint.route("/create", methods=["GET", "POST"])
def create():
    form = AddUserForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)

        db.session.add(user)
        db.session.commit()
        # user: User = db.query.filter_by(username=form.username.data)
        # user.is_active = True
        # db.session.commit()
        flash("User was added")
        return redirect(url_for("home.index"))

    return render_template("create-user.html", form=form)


@user_blueprint.route("/delete/<int:user_id>")
def delete_user(user_id):
    user = User.query.get_or_404(user_id, description=None)

    db.session.delete(user)
    db.session.commit()

    return "<p>user was deleted</p>"
