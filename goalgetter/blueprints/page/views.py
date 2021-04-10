from flask import Blueprint, render_template
from goalgetter.blueprints.user.decorators import anonymous_required
from flask_login import login_required

page = Blueprint('page', __name__, template_folder='templates')

@page.route('/home')
@login_required
def home():
    return render_template('home.html')

@page.route('/values')
@login_required
def values():
    return render_template('values.html')

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
