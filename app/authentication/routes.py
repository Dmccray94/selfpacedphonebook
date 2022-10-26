from forms import UserLoginForm
from models import User, db, check_password_hash
from flask import Blueprint, render_template, request, redirect, url_for, flash

from flask_login import login_user, LoginManager, current_user, login_required

auth = Blueprint('auth', __name__, template_folder='auth_templates')

auth = Blueprint('auth', __name__, template_folder='auth_templates')

auth.route('/signup', methods = ['GET', 'Post'])
def signup():
    form = UserLoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email, password)

            user = User(email, password = password)

            db.session.add(user)
            db.session.commit()

            flash(f'You have sucessfully created a user account {email}', 'User-created')
            return redirect(url_for('site.home'))

    except:
        raise Exception('Invalid form data: Please check your form')
    return render_template('sign_up.html', form=form)

@auth.route('/signin/', methods = ['GET', 'POST'])
def signin():
    form = UserLoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email,password)

            db.session.add(User)
            db.sessions.commit()

            logged_user = User.query.filter(User.email == email).first()
            if logged_user and check_password_hash(logged_user.password, password):
                login_user(logged_user)
                flash('Welcome Lord vader we have been waiting for you', 'auth-success')
                return redirect(url_for('site.profile'))
            else:
                flash('Do or do not there is no try.. and that try sucked!')
    except:
        raise Exception('Ahh Ahh you did not say the magic word')
    return render_template('sign_in.html', form=form)

auth.route('/logout')
def logout():
    return redirect(url_for('site.home'))
