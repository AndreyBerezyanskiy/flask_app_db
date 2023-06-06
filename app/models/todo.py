from app import db
from sqlalchemy import ForeignKey


class Todo(db.Model):
    __tablename__ = "todo"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    is_done = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, ForeignKey("user.id"))
