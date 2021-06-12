from flask import Blueprint, render_template
from goalgetter.blueprints.user.decorators import anonymous_required
from flask_login import login_required, current_user

page = Blueprint('page', __name__, template_folder='templates')

@page.route('/home')
@login_required
def home():
    return render_template('home.html', value1=current_user.values[0].value, value2=current_user.values[1].value, value3=current_user.values[2].value)

@page.route('/goals')
@login_required
def goals():
    return render_template('goals.html')

@page.route('/journal')
@login_required
def journal():
    return render_template('journal.html')

@page.route('/')
def landing():
    return render_template('landingpage.html')
