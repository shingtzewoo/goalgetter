from flask import Flask, render_template

# blueprints
from goalgetter.blueprints.page import page
from goalgetter.blueprints.user import user
from goalgetter.blueprints.goals import goals

# extensions
from goalgetter.extensions import db
from goalgetter.extensions import login_manager

# model
from goalgetter.blueprints.user.models import User

def create_app():

    # creates flask instance that loads configuation files relative to the instance folder
    app = Flask(__name__, instance_relative_config=True)

    # loads in settings file from config folder
    app.config.from_object('config.settings')
    # loading settings.py file from an instance folder, silent = True tells Flask not to crash if file does not exist
    app.config.from_pyfile('settings.py', silent=True)
    
    # register blue prints here
    app.register_blueprint(page)
    app.register_blueprint(user)
    app.register_blueprint(goals)

    # register extensions
    extensions(app)

    # authenticate the user
    authentication(app, User)

    return app

def extensions(app):
    
    # registering extensions, taken from the extensions.py file

    login_manager.init_app(app)
    db.init_app(app)

    return None

def authentication(app, user_model):

    # user will be redirected via the user login route if they are not logged in and they try to access 
    # a route that requires a user to be logged in
    login_manager.login_view = 'user.login'

    # Flask-Login 
    # You will need to provide a user_loader callback. 
    # This callback is used to reload the user object from the user ID stored in the session. 
    # It should take the unicode ID of a user, and return the corresponding user object.
    @login_manager.user_loader
    def load_user(user_id):
        return user_model.query.get(user_id)   
    
