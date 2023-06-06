from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    is_active = db.Column(db.Boolean, default=False)

    todos = db.relationship("Todo", backref='user')

    def __repr__(self):
        return f"User('{self.username}', '{self.password}')"
