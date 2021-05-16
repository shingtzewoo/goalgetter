from flask import Blueprint, render_template, url_for, flash, current_app, request, redirect
from werkzeug.security import generate_password_hash
from flask_login import login_required, login_user, current_user, logout_user
from goalgetter.blueprints.user.decorators import anonymous_required
from goalgetter.blueprints.user.forms import LoginForm, SignupForm
from goalgetter.blueprints.goals.models.values import Value
from goalgetter.blueprints.goals.models.milestones import Milestone

goals = Blueprint('goals', __name__, template_folder='templates')


@goals.route('/questions/values', methods=['GET', 'POST'])
@login_required
def values():
    if request.method == "POST":
        # https://stackoverflow.com/questions/59656684/how-do-i-store-multiple-checkbox-data-in-a-list-of-array
        values = request.form.getlist('value')
    
        if len(values) > 3 or len(values) < 0 or (len(values) < 3 and len(values) >= 0):
            flash("Number of values chosen have to be 3", "danger")
            return redirect(url_for("goals.values"))
        
        value1, value2, value3 = Value(value=values[0]), Value(value=values[1]), Value(value=values[2])
        connected1, connected2, connected3 = value1.connect(current_user), value2.connect(current_user), value3.connect(current_user)
        if connected1 and connected2 and connected3:
            current_user.questionnaire+=1
            current_user.save()
        
        return redirect(url_for("goals.goal"))
    
    if current_user.is_complete() == 1:
        flash("You've already chosen your values, please complete your goals", "danger")
        return redirect(url_for("goals.goal"))
    '''elif current_user.is_complete() == 2:
            flash("You've already chosen your values and goals, please complete your milestones and tasks", "danger")
        # need to add more validation for other completion stages
    ''' 
    else:
        return render_template('values.html')

@goals.route('/questions/goals', methods=['GET','POST'])
@login_required
def goal():

    # fix this validation check
    if current_user.is_complete() <= 1:
        return str(current_user.is_complete())
    else:
        flash("You've already completed your goals.", "danger")
        return redirect(url_for("page.home"))
