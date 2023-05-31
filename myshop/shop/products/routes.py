from flask import redirect, render_template, url_for, flash, request, session
from shop import db, app, photos
from .models import Brand, Category, Addproduct
from .forms import Addproducts
import secrets


@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if 'email' not in session:
        flash(f'please login first', 'danger')
        return redirect(url_for('login'))
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
    if 'email' not in session:
        flash(f'please login first', 'danger')
        return redirect(url_for('login'))
    if request.method == 'POST':
        getcategory = request.form.get('category')
        category = Category(name=getcategory)
        db.session.add(category)
        flash(f'the brand {getcategory} added ','success')
        db.session.commit()
        return redirect(url_for('addcat'))

    return render_template('products/addbrand.html')


@app.route('/addproduct', methods=['GET','POST'])
def addproduct():
    if 'email' not in session:
        flash(f'please login first', 'danger')
        return redirect(url_for('login'))
    brands = Brand().query.all()
    categories = Category.query.all()
    form = Addproducts(request.form)
    if request.method == 'POST':
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        desc = form.description.data
        color = form.color.data
        brand = request.form.get('brand')
        category = request.form.get('category')
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10)+'.')
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10)+'.')
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10)+'.')

        addprod = Addproduct(name=name, price=price, discount=discount, stock=stock, desc=desc,
        color=color, brand_id=brand, category_id=category,image_1=image_1, image_2 = image_2,
                             image_3=image_3 )
        db.session .add(addprod)
        flash("the product {} has been added to the database".format(name), 'success')
        db.session.commit()
        return redirect(url_for('admin'))

    return render_template('products/addproduct.html', title='Add PRODUCT page', form=form,
    brands= brands, categories=categories)
