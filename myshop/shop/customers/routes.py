from flask import redirect, render_template, url_for, flash
from flask import request, session, current_app
from shop import db, app, photos, search, bcrypt
from .forms import CustomerRegistrationForm
from .model import Register
import secrets
import os

@app.route('/customer/register', methods=['GET', 'POST'])
def customer_register():
    form = CustomerRegistrationForm(request.form)
    if request.method == 'POST':
        hash_password = bcrypt.generate_password_hash(form.password.data)
        register = Register(name=form.name.data, username=form.username.data, email=form.email.data,
                            password=form.password.data, country=form.country.data, state=form.state.data, city=form.city.data,
                            address=form.address.data, zipcode=form.zipcode.data)
        db.session.add(register)
        db.session.commit()
        flash(f'Welcome {form.name.data} Thank you for registering', 'success')
        return redirect(url_for('login'))
    return render_template('customer/register.html', form=form)
