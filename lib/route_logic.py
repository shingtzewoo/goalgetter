from flask_login import current_user
from flask import redirect, flash, url_for
from flask_login import current_user
from functools import wraps
from flask import request

def questionnaire_reroute(f):

    '''
    Wrapper function for routes that redirects the user back to the questionnaire 
    '''
    
    @wraps(f)
    def decorated_function(*args, **kwargs):
        messages = {
            0: "Please complete your values",
            1: "Please complete your goals",
            2: "Please complete your milestones",
            3: "Please complete your tasks",
        }
        corrected_routes = {
            0: "goals.values",
            1: "goals.goal",
            2: "goals.milestones",
            3: "goals.tasks",
        }
        if current_user.is_complete() < 4:
            if url_for(corrected_routes.get(current_user.is_complete())) != request.path:
                flash(messages.get(current_user.is_complete()), "danger")
                return redirect(url_for(corrected_routes.get(current_user.is_complete())))
        else:
            if url_for(corrected_routes.get(current_user.is_complete())) == request.path:
                flash("You have already completed the questionnaire", "danger")
                return redirect(url_for("page.home"))
        return f(*args, **kwargs)
    return decorated_function