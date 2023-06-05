import os
from dotenv import load_dotenv

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required

load_dotenv()

LOCAL_DB_PORT = os.environ.get("LOCAL_DB_PORT", 5432)

app = Flask(__name__)

app.config["WTF_CSRF_ENABLED"] = False
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://postgres:postgres@127.0.0.1:{LOCAL_DB_PORT}/postgres"
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# --------------FORM CLASS------------------


class LoginForm(FlaskForm):
    user_id = StringField("Username", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    submit = SubmitField("Login")


class AddUserForm(FlaskForm):
    username = StringField("Username", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    submit = SubmitField("Add_user")


# ------------DB MODEL --------------------


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    password = db.Column(db.String(64))
    is_active = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"


class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    body = db.Column(db.String(500))
    user_id = db.Column(db.Integer, ForeignKey("user.id"))

    def __repr__(self):
        return f"User('{self.title}')"


#  --------------ROUTES---------------


@app.route("/")
def home_page():
    return render_template("home-page.html")


@app.route("/handle-create")
def handle_create_user():
    user = User(name="Andrii Berezianskii")

    post = Post(title="first post", body="content some text")

    db.session.add(user, post)
    db.session.commit()

    return "<p>user was created</p>"


@app.route("/delete/<int:user_id>")
def delete_user(user_id):
    user = User.query.get_or_404(user_id, description=None)

    db.session.delete(user)
    db.session.commit()

    return "<p>user was deleted</p>"


@app.route("/create", methods=["GET", "POST"])
def create():
    form = AddUserForm()
    if form.validate_on_submit():
        user = User(
            name=form.username.data,
            password=form.password.data,
            email=form.email.data
        )

        db.session.add(user)
        db.session.commit()
        flash("User was added")
        return redirect(url_for("home_page"))

    return render_template("create-user.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(
            User.name == form.user_id.data.lower(),
            User.password == form.password.data
        ).first()

        if user:
            login_user(user)
            flash("Login Successful")
            return redirect(url_for("home_page"))

    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user(current_user)

    return redirect(url_for("home-page"))
