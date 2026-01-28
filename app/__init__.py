import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import render_template

load_dotenv()

db = SQLAlchemy()

login_manager = LoginManager()

def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'login'

    with app.app_context():
        from app.models import Admin, Order, Product
        db.create_all()

    # Роуты
    from app.routes.about import init_about
    from app.routes.api_hash import init_api_hash
    from app.routes.index import init_index
    from app.routes.register import init_register
    from app.routes.login import init_login
    from app.routes.product import init_product
    from app.routes.order import init_order
    from app.routes.max_revenue_query import init_max_revenue_query
    from app.routes.avg_revenue_query import init_avg_revenue_query
    from app.routes.totat_revenue_query import init_total_revenue_query
    from app.routes.top_products_query import init_top_products_query
    from app.routes.categories_query import init_categories_query
    from app.routes.stocks_query import init_stocks_query

    init_index(app)
    init_register(app)
    init_login(app)
    init_about(app)
    init_api_hash(app)
    init_product(app)
    init_order(app)
    init_max_revenue_query(app)
    init_avg_revenue_query(app)
    init_total_revenue_query(app)
    init_top_products_query(app)
    init_categories_query(app)
    init_stocks_query(app)

    # Обработчики ошибок
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('500.html'), 500

    return app