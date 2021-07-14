from datetime import timedelta
DEBUG = True

SERVER_NAME = 'gentle-bayou-82963.herokuapp.com'
SECRET_KEY = "b'}\x15\xfa:4A_\x85\x02\xcc\xbfN1\xf9\xe3/\xfd\xb25\xdeK\x97\x84\xc2'"

# SQLAlchemy.
db_uri = 'postgresql://goalgetter:devpassword@postgres:5432/goalgetter'
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

# User.
SEED_ADMIN_EMAIL = 'dev@local.host'
SEED_ADMIN_PASSWORD = 'devpassword'
REMEMBER_COOKIE_DURATION = timedelta(days=90)