import os
from dotenv import load_dotenv
import psycopg2
from flask import render_template
from flask_login import login_required


def init_max_revenue_query(app):
    @app.route('/max_revenue_query')
    @login_required
    def max_revenue_query():
        load_dotenv()

        uri = os.environ.get('SQLALCHEMY_DATABASE_URI')
        uri_for_psycopg2 = uri.replace('+psycopg2', '')

        conn = psycopg2.connect(uri_for_psycopg2)

        cur = conn.cursor()

        cur.execute('''
        SELECT MAX(orders.amount * products.price)
        FROM orders
        INNER JOIN products 
        ON orders.product_id = products.id
        ;''')

        result = cur.fetchone()
        conn.commit()

        cur.close()
        conn.close()

        return render_template('query_result.html', result=result, name="Максимальная выручка")