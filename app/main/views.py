from . import main
from flask import render_template


@main.route('/')
@main.route('/index')
def index():
    title = 'Home'
    return render_template('index.html', title=title)

@main.route('/timer')
def timer():
    '''
    Function to display timer
    '''
    title = 'Timer'
    return render_template('timer.html', title=title)