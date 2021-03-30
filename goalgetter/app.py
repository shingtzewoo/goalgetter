from flask import Flask, render_template

def create_app():

    # creates flask instance that loads configuation files relative to the instance folder
    app = Flask(__name__, instance_relative_config=True)

    # loads in settings file from config folder
    app.config.from_object('config.settings')
    # loading settings.py file from an instance folder, silent = True tells Flask not to crash if file does not exist
    app.config.from_pyfile('settings.py', silent=True)
    
    # register blue prints here

    @app.route('/')
    def index():
        """
        Render a Hello World response.

        :return: Flask response
        """
        return render_template('app.html')

    return app