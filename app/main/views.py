from . import main
from flask import render_template


@main.route('/')
@main.route('/index')
def index():
    title = 'Home'
    return render_template('index.html', title=title)