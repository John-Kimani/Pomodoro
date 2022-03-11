from app.auth import auth
from flask import render_template, flash, redirect, url_for
# from app import db
from app.auth.forms import LoginForm, SignupForm
from flask_login import current_user, login_user,logout_user
from app.models import User


@auth.route('/login', methods=['GET','POST'])
def login():
    
    if current_user.is_authenticated:
        
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        flash('You are logged in succesfully')
        return redirect(url_for('main.index'))
    title = "LogIn"
    return render_template('auth/login.html', title=title, form=form )

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    
    if current_user.is_authenticated:
        
        return redirect(url_for('main.index'))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password_hash=form.password.data)
        
        user.set_password(form.password.data) #handles password hashing
        db.session.add(user)
        db.session.commit()
        flash('Congratulatons you are now a registered user')
        return redirect('login')
    return render_template('auth/signup.html', title="Register", form=form)


# @bp.route('/logout')
# def logout():
    
#     logout_user()
#     return redirect(url_for('main.index'))
