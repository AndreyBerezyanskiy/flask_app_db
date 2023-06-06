from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddTodoForm(FlaskForm):
    title = StringField("Title", [DataRequired()])
    submit = SubmitField("Add_todo")