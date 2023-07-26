from shop import db, app, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def user_loader(user_id):
    return Register.query.get(user_id)


class Register(db.Model,  UserMixin):
    """docstring for Register."""
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(60), unique= False)
    username = db.Column(db.String(80), unique= True)
    email = db.Column(db.String(80), unique= True)
    password = db.Column(db.String(180), unique= False)
    country = db.Column(db.String(60), unique= False)
    # state = db.Column(db.String(60), unique= False)
    city = db.Column(db.String(60), unique= False)
    contact = db.Column(db.String(60), unique= False)
    address = db.Column(db.String(60), unique= False)
    zipcode = db.Column(db.String(60), unique= False)
    profile = db.Column(db.String(200), unique= False, default='profile.jpg')
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repre__(self):
        return '<Register %r> % self.name'
with app.app_context():
    db.create_all()
