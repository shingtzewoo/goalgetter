from flask import Blueprint, render_template, url_for, flash, current_app, request, redirect
from werkzeug.security import generate_password_hash
from flask_login import login_required, login_user, current_user, logout_user
from goalgetter.blueprints.user.decorators import anonymous_required
from goalgetter.blueprints.user.forms import LoginForm, SignupForm
from goalgetter.blueprints.goals.models.goals import Goal
from goalgetter.blueprints.goals.models.milestones import Milestone
from goalgetter.extensions import db

goals = Blueprint('goals', __name__, template_folder='templates')


@goals.route('/questions/values', methods=['GET', 'POST'])
@login_required
def values():
    if request.method == "POST":
        return None
    return render_template('values.html')