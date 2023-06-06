from app import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    first_name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    password = db.Column(db.String(64))
    is_active = db.Column(db.Boolean, default=False)
    todo = db.relationship("Todo")

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"
