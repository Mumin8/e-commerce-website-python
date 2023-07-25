from wtforms import Form,SubmitField, TextAreaField, BooleanField, StringField, PasswordField, validators
from flask_wtf.file import FileRequired, FileAllowed, FileField
from wtforms.validators import DataRequired

class  CustomerRegistrationForm(Form):
    """docstring for  CustomerRegistrationForm."""
    name = StringField('Name: ')
    username = StringField('Username: ', [validators.DataRequired()])
    email = StringField('Email: ', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password: ', [validators.DataRequired(), validators.EqualTo('confirm',
    message='Both password must match!')])
    confirm = PasswordField('Repeat Password: ', [validators.DataRequired()])

    country = StringField('Country: ', [validators.DataRequired()])
    contact = StringField('Contact: ', [validators.DataRequired()])
    state = StringField('State: ', [validators.DataRequired()])
    city = StringField('City: ', [validators.DataRequired()])
    address = StringField('Address: ', [validators.DataRequired()])
    zipcode = StringField('Zipcode: ', [validators.DataRequired()])

    profile = FileField('Profile ', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'],
    "Image only please")])

    submit = SubmitField('Register')
