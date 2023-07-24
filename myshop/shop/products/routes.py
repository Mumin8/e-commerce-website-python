from flask import redirect, render_template, url_for, flash
from flask import request, session, current_app
from shop import db, app, photos, search
from .models import Brand, Category, Addproduct
from .forms import Addproducts
import secrets
import os
import time


def brands():
    brands = Brand.query.join(
                            Addproduct, (Brand.id == Addproduct.brand_id)
                              ).all()
    return brands

def categories():
    categories = Category.query.join(
                            Addproduct, (Category.id == Addproduct.category_id)
                                    ).all()
    return categories

# the endpoint to home function
@app.route('/')
def home():
    '''
    home:
            the function to Home
    '''
    page = request.args.get('page', 1, type=int)
    products = Addproduct.query.filter(
                                        Addproduct.stock > 0
                                        ).order_by(
                                        Addproduct.id.desc()
                                        ).paginate(page=page, per_page=3)


    # brands = Brand.query.all()
    return render_template(
                        'products/index.html', products=products,
                        brands=brands(), categories=categories()
                        )


@app.route('/result')
def result():
    searchword = request.args.get('q')
    products = Addproduct.query.msearch(searchword, fields=['name', 'desc'], limit=3)
    return render_template('products/result.html', products=products,
    brands=brands(), categories=categories())

@app.route('/product/<int:id>')
def single_page(id):
    product = Addproduct.query.get_or_404(id)
    return render_template('products/single_page.html', product=product, brands=brands(), categories=categories())


# the endpoint to the get_brand function
@app.route('/brand/<int:id>')
def get_brand(id):
    '''
    get_brand:
                the function to get all brands
    args:
        id:
             the id of the brand required
    '''
    page = request.args.get('page', 1, type=int)
    get_b = Brand.query.filter_by(id=id).first_or_404()
    brand = Addproduct.query.filter_by(brand=get_b).paginate(
                                        page=page, per_page=2
                                        )
    return render_template(
                        'products/index.html', brand=brand,
                    brands=brands(), categories=categories(), get_b=get_b
                        )


@app.route('/categories/<int:id>')
def get_category(id):
    page = request.args.get('page', 1, type=int)
    get_cat = Category.query.filter_by(id=id).first_or_404()
    get_cat_prod = Addproduct.query.filter_by(category=get_cat).paginate(
                                                        page=page, per_page=2
                                                        )

    categories = Category.query.join(
                        Addproduct, (Category.id == Addproduct.category_id)
                                    ).all()
    return render_template(
                        'products/index.html', get_cat_prod=get_cat_prod,
                        categories=categories(), brands=brands(), get_cat=get_cat
                        )


# the endpoint to the addbrand function
@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand() -> 'login or addbrand or render_template':
    '''
    addbrand:
                this function adds a brand to the database
    '''
    if 'email' not in session:
        flash(f'please login first', 'danger')
        return redirect(url_for('login'))
    if request.method == 'POST':
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'the brand {getbrand} added ', 'success')
        db.session.commit()
        return redirect(url_for('addbrand'))

    return render_template('products/addbrand.html', brands='brands')


# the endpoint to the updatebrand function
@app.route('/updatebrand/<int:id>', methods=['GET', 'POST'])
def updatebrand(id):
    '''
    updatebrand:
                this function updates a brands
    args:
            id: the id of the brand to be updateproduct
    '''
    if 'email' not in session:
        flash(f'please login first', 'danger')
    updatebrand = Brand.query.get_or_404(id)
    brand = request.form.get('brand')
    if request.method == 'POST':
        updatebrand.name = brand
        flash(f'Your brand has been updated successfull', 'success')
        db.session.commit()
        return redirect(url_for('brands'))
    return render_template(
                            'products/updatebrand.html',
                            title='update brand page', updatebrand=updatebrand
                            )


# the endpoint to the deletebrand function
@app.route('/deletebrand/<int:id>', methods=['POST'])
def deletebrand(id):
    '''
    deletebrand:
                the function to deletebrand
    args:
        id: the id of the brand to be delete
    '''
    brand = Brand.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(brand)
        db.session.commit()
        flash(f'the brand {brand.name} was has been deleted', 'success')
        return redirect(url_for('admin'))
    flash(f'The brand {brand.name} cant be deleted', 'warning')
    return redirect(url_for('admin'))


# the endpoint to the addcat function
@app.route('/addcategory', methods=['GET', 'POST'])
def addcat():
    '''
    addcat:
            this function adds a new category to the database
    '''
    if 'email' not in session:
        flash(f'please login first', 'danger')
        return redirect(url_for('login'))
    if request.method == 'POST':
        getcategory = request.form.get('category')
        category = Category(name=getcategory)
        db.session.add(category)
        flash(f'the brand {getcategory} added ', 'success')
        db.session.commit()
        return redirect(url_for('addcat'))
    return render_template('products/addbrand.html')


# the endpoint to the updatecategory function
@app.route('/updatecat/<int:id>', methods=['GET', 'POST'])
def updatecat(id):
    '''
    updatecat:
                the function to update the category of the products
    args:
            id: the id of the product to update
    '''
    if 'email' not in session:
        flash(f'please login first', 'danger')
    updatecat = Category.query.get_or_404(id)
    category = request.form.get('category')
    if request.method == 'POST':
        updatecat.name = category
        flash(f'Your category has been updated successfull', 'success')
        db.session.commit()
        return redirect(url_for('categories'))
    return render_template(
                        'products/updatebrand.html',
                        title='update category page', updatecat=updatecat
                        )


# the endpoint to the deletecategory function
@app.route('/deletecategory/<int:id>', methods=['POST'])
def deletecategory(id):
    '''
    deletecategory:
                the function that deletes a category
    args:
        id:
            the id of the category to be deleted
    '''
    category = Category.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(category)
        db.session.commit()
        flash(f'the category {category.name} was has been deleted', 'success')
        return redirect(url_for('admin'))
    flash(f'The category {category.name} cant be deleted', 'warning')
    return redirect(url_for('admin'))


# The end point to addproduct function
@app.route('/addproduct', methods=['GET', 'POST'])
def addproduct():
    '''
    addproduct:
                this function adds a product to the database
    '''

    if 'email' not in session:
        flash(f'please login first', 'danger')
        return redirect(url_for('login'))
    brands = Brand().query.all()
    categories = Category.query.all()
    form = Addproducts(request.form)

    # Get the required data from the front end
    if request.method == 'POST':
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        desc = form.description.data
        color = form.color.data
        brand = request.form.get('brand')
        category = request.form.get('category')

        # upload the required images from your system
        image_1 = photos.save(
                            request.files.get('image_1'),
                            name=secrets.token_hex(10)+'.'
                            )
        image_2 = photos.save(
                            request.files.get('image_2'),
                            name=secrets.token_hex(10)+'.'
                            )
        image_3 = photos.save(
                                request.files.get('image_3'),
                                name=secrets.token_hex(10)+'.'
                                )

        # Add the data to the models
        addprod = Addproduct(
                name=name, price=price, discount=discount, stock=stock,
                desc=desc, color=color, brand_id=brand, category_id=category,
                image_1=image_1, image_2=image_2, image_3=image_3
                )

        # add the data to session
        db.session.add(addprod)

        # message to the admin
        flash(
            " {} has been added to the database".format(name),
            'success'
            )

        # commit the data to the database
        db.session.commit()
        return redirect(url_for('admin'))

    return render_template(
            'products/addproduct.html', title='Add PRODUCT page',
            form=form, brands=brands, categories=categories
            )


# the endpoint for the updateproduct function
@app.route('/updateproduct/<int:id>', methods=['GET', 'POST'])
def updateproduct(id):
    '''
    updateproduct:
                    this function updates a products

    args:
        id:
            the id of the product to be updated
    '''
    # query the database for all brands and categories
    brands = Brand.query.all()
    categories = Category.query.all()
    # query database for a product by an id
    product = Addproduct.query.get_or_404(id)
    brand = request.form.get('brand')
    category = request.form.get('category')
    form = Addproducts(request.form)

    # checks for and updates a request for update with new data
    if request.method == 'POST':
        product.name = form.name.data
        product.price = form.price.data
        product.discount = form.discount.data
        product.stock = form.stock.data
        product.brand_id = brand
        product.category_id = category
        product.color = form.color.data
        product.desc = form.description.data
        if request.files.get('image_1'):
            try:
                os.unlink(
                            os.path.join(
                                    current_app.root_path,
                                    'static/images/' + product.image_1
                                    )
                        )
                product.image_1 = photos.save(
                                request.files.get('image_1'),
                                name=secrets.token_hex(10)+'.'
                                )
            except Exception:
                product.image_1 = photos.save(
                                request.files.get('image_1'),
                                name=secrets.token_hex(10)+'.'
                                )
        if request.files.get('image_2'):
            try:
                os.unlink(
                            os.path.join(
                                        current_app.root_path,
                                        'static/images/' + product.image_2
                                        )
                        )
                product.image_2 = photos.save(
                                request.files.get('image_2'),
                                name=secrets.token_hex(10)+'.'
                                )
            except Exception:
                product.image_2 = photos.save(
                                request.files.get('image_2'),
                                name=secrets.token_hex(10)+'.'
                                )
        if request.files.get('image_3'):
            try:
                os.unlink(
                            os.path.join(
                                        current_app.root_path,
                                        'static/images/' + product.image_3
                                        )
                        )
                product.image_3 = photos.save(
                                request.files.get('image_3'),
                                name=secrets.token_hex(10)+'.'
                                )
            except Exception:
                product.image_3 = photos.save(
                                request.files.get('image_3'),
                                name=secrets.token_hex(10)+'.'
                                )
        db.session.commit()
        flash(f'Your product was updated successfully', 'success')
        return redirect(url_for('admin'))

    form.name.data = product.name
    form.price.data = product.price
    form.discount.data = product.discount
    form.stock.data = product.stock
    form.color.data = product.color
    form.description.data = product.desc
    return render_template(
                        'products/updateproduct.html', form=form,
                        brands=brands, categories=categories, product=product
                         )


# the endpoint to the deleteproduct function
@app.route('/deleteproduct/<int:id>', methods=['POST'])
def deleteproduct(id) -> 'admin':
    '''
    deleteproduct:
                    the function that deletes a product from database
    args:
            id:
                the id of the product to be deleteproduct
    '''
    # get the product by its id
    product = Addproduct.query.get_or_404(id)
    if request.method == "POST":
        # if request.files.get('image_1'):
        try:
            os.unlink(
                        os.path.join(
                                current_app.root_path,
                                'static/images/' + product.image_1
                                )
                    )

            os.unlink(
                        os.path.join(
                                    current_app.root_path,
                                    'static/images/' + product.image_2
                                    )
                    )

            os.unlink(
                        os.path.join(
                                    current_app.root_path,
                                    'static/images/' + product.image_3
                                    )
                    )
            time.sleep(1)
        except Exception as e:
            print(f'{e}')

        db.session.delete(product)
        db.session.commit()
        flash(f'The product {product.name} has been deleted', 'success')
        return redirect(url_for('admin'))
    flash(f'Could not delete product', 'danger')
    return redirect(url_for('admin'))
