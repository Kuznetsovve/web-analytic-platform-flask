from time import sleep
from datetime import datetime
from flask import render_template, redirect, flash, url_for
from app.models import Product, Order
from app.forms.order_form import OrderForm
from app import db

def init_order(app):
    @app.route('/order/<product_id>', methods=['GET', 'POST'])
    def order(product_id):
        product = Product.query.get_or_404(product_id)
        form = OrderForm(product_id=product_id)
        if form.validate_on_submit():
            flash('Заказ успешно оформлен!', 'success')
            amount = form.quantity.data
            if amount > product.amount:
                flash('На складе недостаточно товара', 'danger')
                return render_template('order.html', form=form, product=product)

            order = Order(
                product_id=product.id,
                amount=amount,
                address=form.address.data,
                admin_id=1,
                created_at=datetime.now()
            )
            product.amount -= amount
            db.session.add(order)
            db.session.commit()
            sleep(0.2)
            return redirect(url_for('index'))
        return render_template('order.html', form=form, product=product)