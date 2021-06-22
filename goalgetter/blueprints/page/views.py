from flask import Blueprint, render_template
from flask_login import login_required, current_user
from datetime import *
from dateutil.relativedelta import *
from goalgetter.blueprints.goals.models.milestones import Milestone
from lib.route_logic import questionnaire_reroute

page = Blueprint('page', __name__, template_folder='templates')

@page.route('/home')
@questionnaire_reroute
@login_required
def home():
    return render_template('home.html', value1=current_user.values[0], value2=current_user.values[1], value3=current_user.values[2], current_milestones=Milestone.query_by_date(date.today()))

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
