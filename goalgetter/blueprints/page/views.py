from flask import Blueprint, render_template

page = Blueprint('page', __name__, template_folder='templates')

@page.route('/')
def home():
    return render_template('home.html')

@page.route('/values')
def values():
    return render_template('values.html')

@page.route('/goals')
def goals():
    return render_template('goals.html')

@page.route('/journal')
def journal():
    return render_template('journal.html')