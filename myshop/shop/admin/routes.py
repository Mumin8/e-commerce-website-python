from flask import render_template, session, request, redirect, url_for, flash
from shop import app, db, bcrypt
from .forms import RegistrationForm
from .models import User
import os

@app.route("/")
def home():
    '''the admin page'''
    return render_template('admin/index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    '''the Registration page
       method:
                the POST method will be used here
    '''
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        with app.app_context():
            hash_password = bcrypt.generate_password_hash(form.password.data)
            user = User(name=form.name.data, username=form.username.data, email=form.email.data, password=hash_password)
            db.session.add(user)
            db.session.commit()
        flash(f'Welcome {form.name.data} Thanks for registering', 'success')
        return redirect(url_for('home'))
    return render_template('admin/register.html', form=form, title="Registration page")
