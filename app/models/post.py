from app import db
from sqlalchemy import ForeignKey


class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    body = db.Column(db.String(500))
    user_id = db.Column(db.Integer, ForeignKey("user.id"))

    def __repr__(self):
        return f"User('{self.title}')"
