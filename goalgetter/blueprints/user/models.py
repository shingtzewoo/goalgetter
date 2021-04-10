from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash 
from goalgetter.extensions import db

class User(UserMixin, db.Model):
    '''
    UserMixin parent class allows the User class to inherit is_active, get_id, is_authenticated, and is_anonymous https://flask-login.readthedocs.io/en/latest/
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, index=True, nullable=False, server_default='')
    password = db.Column(db.String, nullable=False, server_default='')
    name = db.Column(db.String(128))

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.password = generate_password_hash(kwargs.get('password', ''))
    
    @classmethod
    def identification(cls, identity):
        '''
        Searches the users table for a username that matches the one supplied using SQLAlchemy's query class
        '''
        return User.query.filter_by(email = identity).first()
    
    def save(self):
        '''
        Saves an instance of the user model
        '''
        db.session.add(self)
        db.session.commit()
        return self
    
    def delete(self):
        '''
        Deletes an instance of the user model
        '''
        db.session.delete(self)
        db.session.commit()
        return True

    def passwordcheck(self, password):
        '''
        Checks password hash against unhashed password to see if they match 
        '''
        return check_password_hash(self.password, password)