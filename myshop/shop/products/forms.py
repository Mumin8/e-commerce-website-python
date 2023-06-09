from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import IntegerField, StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class Addproducts(FlaskForm):
    """this is the class for the product model"""

    name = StringField('Name', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    color = TextAreaField('Color', validators=[DataRequired()])

    image_1 = FileField('Image_1', validators= [FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'], 'Images only')])
    image_2 = FileField('Image_2', validators= [FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image_3 = FileField('Image_3', validators= [FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
