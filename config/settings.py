from datetime import timedelta
import os
import psycopg2

DEBUG = True

SERVER_NAME = 'gentle-bayou-82963.herokuapp.com'
SECRET_KEY = "b'}\x15\xfa:4A_\x85\x02\xcc\xbfN1\xf9\xe3/\xfd\xb25\xdeK\x97\x84\xc2'"

# SQLAlchemy.
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(db_uri, sslmode='require')
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

# User.
SEED_ADMIN_EMAIL = 'dev@local.host'
SEED_ADMIN_PASSWORD = 'devpassword'
REMEMBER_COOKIE_DURATION = timedelta(days=90)