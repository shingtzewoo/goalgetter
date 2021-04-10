from flask import Blueprint, render_template, url_for, flash, current_app, request, redirect
from flask_login import login_required, login_user, current_user, logout_user
from goalgetter.blueprints.user.decorators import anonymous_required
from goalgetter.blueprints.user.forms import LoginForm, NameForm
from goalgetter.blueprints.user.models import User
from goalgetter.blueprints.page.views import page
from goalgetter.extensions import db

user = Blueprint('user', __name__, template_folder='templates')

@user.route('/login', methods=['GET', 'POST'])
@anonymous_required
def login():
    form = LoginForm()

    if form.validate_on_submit():

        # if the form is valid upon submission, we take the the emailfield information submitted via the login form
        # and use that information to supply to our identification method which queries the users table for that email
        user = User.identification(request.form.get('email'))
        password = request.form.get('password')
        
        if user and user.passwordcheck(password):

            # flask login function 
            login_user(user)
            return redirect(url_for("page.home"))
        else:
            flash("Email or passwod is incorrect.", "error")
    
    return render_template('login.html', form=form)

@user.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

@user.route('/signup', methods=['GET', 'POST'])
@anonymous_required
def signup():
    # redirect to landing page
    # have to work on landing page
    return render_template('signup.html')

@user.route('/account')
@login_required
def account():
    return render_template('signup.html')