from flask_login import current_user
from flask import redirect, flash, url_for
from flask_login import current_user

def questionnaire_reroute(stage):

    '''
    Reroutes users based on their completion stage in the questionnaire
    '''

    messages = {
        1: "Please complete your goals",
        2: "Please complete your milestones",
        3: "Please complete your tasks",
        4: "You've completed the questionnaire already"
    }

    corrected_routes = {
        1: "goals.goal",
        2: "goals.milestones",
        3: "goals.tasks",
        4: "page.home"
    }

    if current_user.is_complete() == stage:
        flash(messages.get(stage), "danger")
        return redirect(url_for(corrected_routes.get(stage)))