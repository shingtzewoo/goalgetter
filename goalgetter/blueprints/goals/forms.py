from flask_wtf import FlaskForm

from wtforms.validators import DataRequired, Length
from wtforms.fields import PasswordField, StringField
from wtforms.fields.html5 import EmailField

class GoalsForm(FlaskForm):
    goal1 = StringField('Name', [DataRequired(), Length(3, 254)])
    goal2 = StringField('Name', [DataRequired(), Length(3, 254)])
    goal3 = StringField('Name', [DataRequired(), Length(3, 254)])