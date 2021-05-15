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
        
        if len(values) > 3 or len(values) < 0:
            flash("Number of values chosen have to be 3", "danger")
        
        value1, value2, value3 = Value(value=values[0]), Value(value=values[1]), Value(value=values[2])
        connected1, connected2, connected3 = value1.connect(current_user), value2.connect(current_user), value3.connect(current_user)
        # if connected1 and connected2 and connected3:
        #    flash("Thanks for joining, here are your values " + str(value1) + " " + str(value2) + " " + str(value3))
        
        return str("Thanks for joining, here are your values " + str(current_user.values[0].value))

    return render_template('values.html')
