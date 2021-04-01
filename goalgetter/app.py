from flask import Flask, render_template

# blueprints
from goalgetter.blueprints.page import page
from goalgetter.blueprints.user import user

# extensions
from goalgetter.extensions import db
from goalgetter.extensions import login_manager

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
    extensions(app)

    return app

def extensions(app):
    
    # registering extensions, taken from the extensions.py file

    login_manager.init_app(app)
    db.init_app(app)

    return None