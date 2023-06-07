import pytest
from flask import Flask
from flask.testing import FlaskClient

from app import create_app
from app import db
from app.models import User


@pytest.fixture()
def app():
    app = create_app("testing")
    app.config["TESTING"] = True

    yield app


@pytest.fixture()
def client(app: Flask):
    # app = create_app("testing")
    # app.config["TESTING"] = True

    with app.test_client() as client:
        app_ctx = app.app_context()
        app_ctx.push()

        db.drop_all()
        db.create_all()

        user = User(username="test", password="test")
        db.session.add(user)
        db.session.commit()

        yield client
        db.session.remove()
        db.drop_all()
        app_ctx.pop()
