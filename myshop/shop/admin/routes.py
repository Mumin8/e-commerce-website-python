from flask import render_template, session, request, redirect, url_for, flash
from shop import app, db, bcrypt
from .forms import RegistrationForm, LoginForm
from .models import User
import os


@app.route("/admin")
def admin():
    '''the admin page'''
    if 'email' not in session:
        flash(f'please login first', 'danger')
        return redirect(url_for('login'))
    return render_template('admin/index.html', title='Admin page')

@app.route('/register', methods=['GET', 'POST'])
def register():
    '''the Registration route
       method:
              register: this implement the Registration of the page
    '''
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome {form.name.data} Thanks for registering', 'success')
        return redirect(url_for('login'))
    return render_template('admin/register.html', form=form, title="Registration page")


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''the LoginForm
        method:
                login: this implement the login of the page

     '''
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        #user = db.one_or_404(db.select(User).filter_by(email=form.email.data))
        user = User.query.filter_by(email=form.email.data).one_or_404()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f' logged', 'success')
            return redirect(request.args.get('next'))
        else:
            flash(f'wrong email and  password combination', 'danger')
    return render_template('admin/login.html', form=form, title='Login page')
