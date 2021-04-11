from flask_wtf import FlaskForm

from wtforms.validators import DataRequired, Length
from wtforms.fields import PasswordField, StringField
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
    email = EmailField('Email Address', [DataRequired(), Length(3, 254)])
    password = PasswordField('Password', [DataRequired(), Length(3, 254)])

class SignupForm(FlaskForm):
    name = StringField('Name', [DataRequired(), Length(3, 254)])
    email = EmailField('Email Address', [DataRequired(), Length(3, 254)])
    password = PasswordField('Password', [DataRequired(), Length(3, 254)])