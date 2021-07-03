from flask import Blueprint, render_template, url_for, flash, request, redirect, jsonify, make_response
from flask_login import login_required, current_user
from datetime import *
from dateutil.relativedelta import *
from goalgetter.blueprints.goals.models.milestones import Milestone

page = Blueprint('page', __name__, template_folder='templates')

@page.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == "POST":
        req = request.get_json()
        res = make_response(jsonify(req), 200)
        return res

    return render_template('home.html', 
                            value1=current_user.values[0], value2=current_user.values[1], value3=current_user.values[2], 
                            current_milestones=Milestone.query_by_date(date.today()), day=date.today().weekday())

@page.route('/goals')
@login_required
def goals():
    return render_template('goals.html', value1=current_user.values[0], value2=current_user.values[1], value3=current_user.values[2], 
                            current_milestones=Milestone.query_by_date(date.today()), day=date.today().weekday())

@page.route('/journal')
@login_required
def journal():
    return render_template('journal.html')

@page.route('/')
def landing():
    return render_template('landingpage.html')
