from flask import redirect, render_template, url_for, flash, request
from shop import db, app
from .models import Brand, Category


@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if request.method == 'POST':
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'the brand {getbrand} added ','success')
        db.session.commit()
        return redirect(url_for('addbrand'))

    return render_template('products/addbrand.html', brands='brands')



@app.route('/addcategory', methods=['GET', 'POST'])
def addcat():
    if request.method == 'POST':
        getcategory = request.form.get('category')
        category = Category(name=getcategory)
        db.session.add(category)
        flash(f'the brand {getcategory} added ','success')
        db.session.commit()
        return redirect(url_for('addcat'))

    return render_template('products/addbrand.html', categories='categories ')
