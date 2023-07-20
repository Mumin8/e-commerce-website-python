from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import IMAGES, UploadSet, configure_uploads
import os

# Get the base directory
basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()

# instance flask app
app = Flask(__name__)

# configure sqlite database
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///mydb.db'

# flask_uploads configuration
app.config['SECRET_KEY'] = os.urandom(24)
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

# initialize the database with flask app
db.init_app(app)

# instantiate Bcrypt with the flask app
bcrypt = Bcrypt(app)

# import from routes from the packages
from shop.admin import routes
from shop.products import routes
from shop.carts import carts
