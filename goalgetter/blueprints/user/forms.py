from flask_wtf import FlaskForm

from wtforms.validators import DataRequired, Length, Optional
from wtforms.fields import PasswordField, StringField
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
    email = EmailField('Email Address', [DataRequired(), Length(3, 254)])
    password = PasswordField('Password', [DataRequired(), Length(3, 254)])

class NameForm(FlaskForm):
    name = StringField('Name', [DataRequired(), Length(3, 254)])