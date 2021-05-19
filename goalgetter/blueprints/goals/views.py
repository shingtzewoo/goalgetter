from flask import Blueprint, render_template, url_for, flash, current_app, request, redirect
from werkzeug.security import generate_password_hash
from flask_login import login_required, login_user, current_user, logout_user
from goalgetter.blueprints.user.decorators import anonymous_required
from goalgetter.blueprints.goals.models.values import Value
from goalgetter.blueprints.goals.models.goals import Goal
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

            # updating user's completion stage to 1 for the questionnaire, there are 3 stages in total
            current_user.questionnaire+=1
            current_user.save()
        
        return redirect(url_for("goals.goal"))
    
    if current_user.is_complete() == 1:
        flash("You've already chosen your values, please complete your goals", "danger")
        return redirect(url_for("goals.goal"))
    else:
        return render_template("values.html")

    """elif current_user.is_complete() == 2:
            flash("You've already chosen your values and goals, please complete your milestones and tasks", "danger")
        # need to add more validation for other completion stages"""

@goals.route('/questions/goals', methods=['GET','POST'])
@login_required
def goal():
    if current_user.is_complete() == 1:
        if request.method == "POST":
            goal1, goal2, goal3 = Goal(name=request.form.get(current_user.values[0].value)), Goal(name=request.form.get(current_user.values[1].value)), Goal(name=request.form.get(current_user.values[2].value))

            # connecting the goals to the correct values
            connected1, connected2, connected3 = goal1.connect(current_user.values[0].id) , goal2.connect(current_user.values[1].id), goal3.connect(current_user.values[2].id)
            
            if connected1 and connected2 and connected3:
                # updating user's completion stage to 2 for the questionnaire, there are 3 stages in total
                current_user.questionnaire+=1
                current_user.save()

            return redirect(url_for("goals.milestones"))

        return render_template("develop_goals.html", value1=current_user.values[0].value, value2=current_user.values[1].value, value3=current_user.values[2].value)
    else:
        flash("You've already completed your goals.", "danger")
        return redirect(url_for("page.home"))

@goals.route('/questions/milestones', methods=['GET','POST'])
@login_required
def milestones():
    if current_user.is_complete() == 2:
        return render_template("milestones.html", goal1=Goal.query_goal(current_user.values[0].id), goal2=Goal.query_goal(current_user.values[1].id), goal3=Goal.query_goal(current_user.values[2].id))