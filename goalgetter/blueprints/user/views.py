from flask import Blueprint, render_template, url_for, flash
from goalgetter.blueprints.user.decorators import anonymous_required
from goalgetter.blueprints.user.forms import LoginForm, NameForm
from goalgetter.blueprints.user.models import User

user = Blueprint('user', __name__, template_folder='templates')

@user.route('/login', methods=['GET', 'POST'])
@anonymous_required
def login():
    form = LoginForm()
    user2 = User.identification('dev@local.host')

    if form.validate_on_submit():

        # if the form is valid upon submission, we take the the emailfield information submitted via the login form
        # and use that information to supply to our identification method which queries the users table for that email
        user = User.identification(request.form.get('email'))
        password = request.form.get('password')
        
        if user and user.passwordcheck(password):
            return redirect(url_for('user/signup'))
    else:
        flash("Email or passwod is incorrect.", "error")
    
    return render_template('login.html', form=form, user2=user2)

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