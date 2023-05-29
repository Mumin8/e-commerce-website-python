from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///mydb.db'
app.config['SECRET_KEY'] = 'somegibrishword'

db.init_app(app)
bcrypt = Bcrypt(app)

from shop.admin import routes
from shop.products import routes
