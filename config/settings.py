DEBUG = True

SERVER_NAME = 'localhost:8000'

# SQLAlchemy.
db_uri = 'postgresql://goalgetter:devpassword@postgres:5432/goalgetter'
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

# User.
SEED_ADMIN_EMAIL = 'dev@local.host'
SEED_ADMIN_PASSWORD = 'devpassword'
REMEMBER_COOKIE_DURATION = timedelta(days=90)