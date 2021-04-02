from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from goalgetter.extensions import db

class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, index=True, nullable=False,
                      server_default='')
    password = db.Column(db.String(128), nullable=False, server_default='')

    def __init__(self):
        super(User, self).__init__(**kwargs)
        self.password = generate_password_hash('password')