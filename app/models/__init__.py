from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import func


class Admin(db.Model, UserMixin):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime, server_default=func.now())

    orders = db.relationship('Order', back_populates='admin')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_admin(admin_id):
    return Admin.query.get(int(admin_id))


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    amount = db.Column(db.Integer, nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('admins.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    address = db.Column(db.String(255), nullable=False)

    admin = db.relationship('Admin', back_populates='orders')
    product = db.relationship('Product', back_populates='orders')


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    amount = db.Column(db.Integer)
    price = db.Column(db.Integer)

    orders = db.relationship('Order', back_populates='product')