from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField
from wtforms.validators import DataRequired

class OrderForm(FlaskForm):
    product_id = IntegerField('Product ID', validators=[DataRequired()], render_kw={'readonly': True})
    quantity = IntegerField('Количество', validators=[DataRequired()])
    address = StringField('Адрес доставки', validators=[DataRequired()])
    submit = SubmitField('Заказать')