from flask import render_template
from app.models import Product

def init_product(app):
    @app.route("/product", methods=["GET", "POST"])
    def product():
        products = Product.query.order_by(Product.created_at.desc()).all()
        return render_template(template_name_or_list="product.html", products=products)
