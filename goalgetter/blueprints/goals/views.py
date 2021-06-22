from flask import Blueprint, render_template, url_for, flash, request, redirect
from flask_login import login_required, current_user
from goalgetter.blueprints.goals.models.values import Value
from goalgetter.blueprints.goals.models.goals import Goal
from goalgetter.blueprints.goals.models.milestones import Milestone
from goalgetter.blueprints.goals.models.tasks import Task
from datetime import *
from dateutil.relativedelta import *
from lib.route_logic import questionnaire_reroute

goals = Blueprint('goals', __name__, template_folder='templates')

@goals.route('/questions/values', methods=['GET', 'POST'])
@questionnaire_reroute
@login_required
def values():
    if request.method == "POST":
        # https://stackoverflow.com/questions/59656684/how-do-i-store-multiple-checkbox-data-in-a-list-of-array
        values = request.form.getlist('value')
    
        if len(values) > 3 or len(values) < 0 or (len(values) < 3 and len(values) >= 0):
            flash("Number of values chosen have to be 3", "danger")
            return redirect(url_for("goals.values"))
        
        value1, value2, value3 = Value(value=values[0]), Value(value=values[1]), Value(value=values[2])
        connected1, connected2, connected3 = value1.connect(current_user.id), value2.connect(current_user.id), value3.connect(current_user.id)

        if connected1 and connected2 and connected3:

            current_user.questionnaire+=1
            current_user.save()
        
        return redirect(url_for("goals.goal"))
    else:
        if current_user.is_complete() == 0:
            return render_template("values.html")

@goals.route('/questions/goals', methods=['GET','POST'])
@questionnaire_reroute
@login_required
def goal():
    if request.method == "POST":
        goal1, goal2, goal3 = Goal(name=request.form.get(current_user.values[0].value)), Goal(name=request.form.get(current_user.values[1].value)), Goal(name=request.form.get(current_user.values[2].value))
        # Connecting the goals to the correct values
        connected1, connected2, connected3 = goal1.connect(current_user.values[0].id) , goal2.connect(current_user.values[1].id), goal3.connect(current_user.values[2].id)
        
        if connected1 and connected2 and connected3:
            # Updating user's completion stage to 2 for the questionnaire, there are 3 stages in total
            current_user.questionnaire+=1
            current_user.save()

        return redirect(url_for("goals.milestones"))
    else:
        if current_user.is_complete() == 1:
            return render_template("develop_goals.html", value1=current_user.values[0].value, value2=current_user.values[1].value, value3=current_user.values[2].value)

@goals.route('/questions/milestones', methods=['GET','POST'])
@questionnaire_reroute
@login_required
def milestones():
    goal1, goal2, goal3 = Goal.query_by_foreignid(current_user.values[0].id).first(), Goal.query_by_foreignid(current_user.values[1].id).first(), Goal.query_by_foreignid(current_user.values[2].id).first()

    if request.method == "POST":
        
        goal1_milestones, goal2_milestones, goal3_milestones = request.form.getlist(str(goal1.id)), request.form.getlist(str(goal2.id)), request.form.getlist(str(goal3.id))
        # Connecting each milestone to a goal and setting the start and end date for each. Each goal has 3 milestones
        Milestone.info_setter(goal1_milestones, goal1)
        Milestone.info_setter(goal2_milestones, goal2)
        Milestone.info_setter(goal3_milestones, goal3)
        
        # Updating user's completion stage to 3 for the questionnaire, there are 3 stages in total
        current_user.questionnaire+=1
        current_user.save()
        return redirect(url_for("goals.tasks"))
    else:
        if current_user.is_complete() == 2:
            return render_template("milestones.html", goal1=goal1, goal2=goal2, goal3=goal3)

@goals.route('/questions/tasks', methods=['GET','POST'])
@questionnaire_reroute
@login_required
def tasks():
    
    value1, value2, value3 = current_user.values[0], current_user.values[1], current_user.values[2]
    if request.method == "POST":

        # Below we set the task for each milestone. A loop that cycles 3 times is used because each value has 3 milestones.
        for i in range(0, 3):
            task_info = request.form.getlist(str(value1.goal.milestone[i].id))
            Task.info_setter(value1.goal.milestone[i].id, task_info)
        
        for i in range(0, 3):
            task_info = request.form.getlist(str(value2.goal.milestone[i].id))
            Task.info_setter(value2.goal.milestone[i].id, task_info)
        
        for i in range(0, 3):
            task_info = request.form.getlist(str(value3.goal.milestone[i].id))
            Task.info_setter(value3.goal.milestone[i].id, task_info)
        
        # updating user's completion stage to 4 for the questionnaire, user is finished with questionnaire
        current_user.questionnaire+=1
        current_user.save()

        return redirect(url_for("page.home"))
    else:
        if current_user.is_complete() == 3:
            return render_template("tasks.html", value1=value1, value2=value2, value3=value3)