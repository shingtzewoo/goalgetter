import click
from goalgetter.app import create_app
from goalgetter.blueprints.user.models import User
from goalgetter.extensions import db

# Create an app context for the database connection
app = create_app()
app.app_context().push()

@click.group()
def cli():
    '''
    Allows commands below to be grouped together.
    '''
    pass

@click.command()
def seed():
    '''
    Seed the database with the initial user
    '''
    if User.identification(app.config['SEED_ADMIN_EMAIL']) is None:
        params = {
            'email': app.config['SEED_ADMIN_EMAIL'],
            'password': app.config['SEED_ADMIN_PASSWORD']
        }
        return User(**params).save()
    else:
        return None

@click.command()
def create():
    '''
    Create database models
    '''
    with app.app_context():
        db.create_all()

@click.command()
def reset():
    '''
    Drop database models
    '''
    with app.app_context():
        db.drop_all()

cli.add_command(seed)
cli.add_command(create)
cli.add_command(reset)