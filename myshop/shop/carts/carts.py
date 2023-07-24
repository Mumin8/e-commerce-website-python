from flask import redirect, render_template, url_for, flash
from flask import request, session, current_app
from shop import db, app
from shop.products.models import Addproduct
from shop.products.routes import brands, categories


def MergerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False


# the endpoint to the AddCart function
@app.route('/addcart', methods=['POST'])
def AddCart():
    '''
    AddCart:
            the function to add cart data
    '''
    try:
        product_id = request.form.get('product_id')
        quantity = request.form.get('quantity')
        colors = request.form.get('colors')
        product = Addproduct.query.filter_by(id=product_id).first()
        if request.method == 'POST':
            DictItems = {
                        product_id: {
                                'name': product.name, 'price': product.price,
                                 'discount': product.discount, 'color': colors,
                                'quantity': quantity, 'image': product.image_1,
                                'colors': product.color
                                    }
                        }
            if 'Shoppingcart' in session:
                # print(session['Shoppingcart'])
                if product_id in session['Shoppingcart']:
                    for key, item in session['Shoppingcart'].items():
                        if int(key) == int(product_id):
                            session.modified = True
                            item['quantity'] += 1
                    print(f'{product.name} already in shopping cart ')
                else:
                    session['Shoppingcart'] = MergerDicts(
                                                session['Shoppingcart'],
                                                DictItems
                                                )
                    return redirect(request.referrer)
            else:
                session['Shoppingcart'] = DictItems
                return redirect(request.referrer)
    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)


# the endpoint to the getCart function
@app.route('/carts')
def getCart():
    '''
    getCart:
            the function to get the cart data
    '''

    if 'Shoppingcart' not in session or len(session['Shoppingcart']) <= 0:
        return redirect(url_for('home'))
    subtotal = 0
    grandtotal = 0
    for key, product in session['Shoppingcart'].items():
        discount = int(product['quantity']) * (product['discount']/100) * float(product['price'])
        subtotal += float(product['price']) * int(product['quantity'])
        subtotal -= discount
        tax = ("%.2f" % (.06 * float(subtotal)))
        grandtotal = float("%0.2f" % (subtotal))-eval(tax)
    return render_template(
                            'products/carts.html',
                            tax=tax, grandtotal=grandtotal,
                            brands=brands(), categories=categories()
                            )


@app.route('/Updatecart/<int:code>', methods=["POST"])
def Updatecart(code):
    if 'Shoppingcart' not in session or len(session['Shoppingcart']) <= 0:
        return redirect(url_for('home'))
    if request.method == "POST":
        quantity =request.form.get('quantity')
        color = request.form.get('color')
        try:
            session.modified = True
            for key, item in session['Shoppingcart'].items():
                if int(key) == code:
                    item['quantity'] = quantity
                    item['color'] = color
                    flash(f'item is updated')
                    return redirect(url_for('getCart'))

        except Exception as e:
            print(e)
            return redirect(url_for('getCart'))

@app.route('/deleteitem/<int:id>')
def deleteitem(id):
    if 'Shoppingcart' not in session or len(session['Shoppingcart']) <= 0:
        return redirect(url_for('home'))
    try:
        session.modified = True
        for key, item in session['Shoppingcart'].items():
            if int(key) == id:
                session['Shoppingcart'].pop(key, None)
                return redirect(url_for('getCart'))
    except Exception as e:
        print(e)
        return redirect(url_for('getCart'))


@app.route('/clearcart')
def clearcart():
    try:
        # session.clear() this will remove everything and log you out
        session.pop('Shoppingcart', None)
        return redirect(url_for('home'))
    except Exception as e:
        print(e)
