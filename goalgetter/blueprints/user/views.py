from flask import Blueprint, render_template
from goalgetter.blueprints.user.decorators import anonymous_required

user = Blueprint('user', __name__, template_folder='templates')

@user.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@user.route('/logout')
def logout():
    return None

@user.route('/signup', methods=['GET', 'POST'])
@anonymous_required
def signup():
    return render_template('signup.html')

@user.route('/account')
def account():
    return None