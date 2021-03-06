from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash 
from goalgetter.extensions import db
from goalgetter.blueprints.goals.models.values import Value
from lib.sql_alchemy import ResourceMixin
from datetime import *
from dateutil.relativedelta import *

class User(UserMixin, ResourceMixin, db.Model):
    '''
    UserMixin parent class allows the User class to inherit is_active, get_id, is_authenticated, and is_anonymous https://flask-login.readthedocs.io/en/latest/
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, index=True, nullable=False, server_default='')
    password = db.Column(db.String, nullable=False, server_default='')
    name = db.Column(db.String(128))
    questionnaire = db.Column('is_complete', db.Integer, nullable=False, server_default='0')

    # tracking the sign in date for the user
    current_sign_in = db.Column(db.DateTime, nullable=False, default=date.today())
    
    # 1:M relationship with the values table
    values = db.relationship(Value, uselist=True, backref='values', passive_deletes=True)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.password = generate_password_hash(kwargs.get('password', ''))
    
    @classmethod
    def identification(cls, identity):
        '''
        Searches the users table for a username that matches the one supplied using SQLAlchemy's query class
        '''
        return User.query.filter_by(email = identity).first()

    def passwordcheck(self, password):
        '''
        Checks password hash against unhashed password to see if they match 
        '''
        return check_password_hash(self.password, password)
    
    def is_complete(self):
        '''
        Return whether the user has completed the initial sign up questionnaire
        '''
        return self.questionnaire