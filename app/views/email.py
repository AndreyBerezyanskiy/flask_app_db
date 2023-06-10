import os
from app import mail

from flask import Blueprint, render_template, redirect, url_for
from flask_mail import Message

# MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
# MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

email_blueprint = Blueprint("email", __name__, url_prefix="/email")


@email_blueprint.route("/")
def send_email():
    msg = Message(
        "Hello",
        sender="no-replye@gmail.com",
        recipients=["andrey.berezyanskiy@gmail.com"],
    )
    # msg.body = "Hello Flask message sent from Flask-Mail"
    msg.html = render_template("email-layout.html")
    mail.send(msg)

    return render_template("email-layout.html", name="Andrii")
