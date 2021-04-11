from flask import Blueprint, render_template, url_for, flash, current_app, request, redirect
from werkzeug.security import generate_password_hash
from flask_login import login_required, login_user, current_user, logout_user
from goalgetter.blueprints.user.decorators import anonymous_required
from goalgetter.blueprints.user.forms import LoginForm, SignupForm
from goalgetter.blueprints.user.models import User
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

            # https://flask-login.readthedocs.io/en/latest/#flask_login.login_user
            # if user is logged in successfully, they will be redirected to the home page via page's home route
            login_user(user)
            return redirect(url_for("page.home"))
        else:
            flash("Email or password is incorrect.", "danger")
    
    return render_template('login.html', form=form)

@user.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("page.landing"))

@user.route('/signup', methods=['GET', 'POST'])
@anonymous_required
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        new_user = User()
        
        # check if the user's email already exists in the database, if it doesn't, then we proceed forward with signing the user up
        if not User.identification(request.form.get('email')):
            
            # https://wtforms.readthedocs.io/en/2.3.x/forms/
            # Populates the attributes of the passed obj with data from the form’s fields.
            form.populate_obj(new_user)

            new_user.password = generate_password_hash(request.form.get('password'))
            new_user.save()

            if login_user(new_user):
                flash('Welcome to Goalgetter, thank you for signing up!', 'success')
                return redirect(url_for('page.home'))
        else:
            flash('This email already exists.', 'danger')

    return render_template('signup.html', form=form)

@user.route('/account')
@login_required
def account():
    return render_template('signup.html')