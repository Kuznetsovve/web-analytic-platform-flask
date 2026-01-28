import os
from dotenv import load_dotenv
import psycopg2
from flask import render_template
from flask_login import login_required


def init_top_products_query(app):
    @app.route('/top_products_query')
    @login_required
    def top_products_query():
        load_dotenv()

        uri = os.environ.get('SQLALCHEMY_DATABASE_URI')
        uri_for_psycopg2 = uri.replace('+psycopg2', '')

        conn = psycopg2.connect(uri_for_psycopg2)

        cur = conn.cursor()

        cur.execute('''
        SELECT products.id, SUM(orders.amount)
        FROM orders
        INNER JOIN products
        ON orders.product_id = products.id
        GROUP BY products.id
        ORDER BY SUM(orders.amount) DESC
        LIMIT 1
        ;''')
        result = cur.fetchone()
        result = [f'ID: {result[0]}, Количество заказов: {result[1]}']
        conn.commit()

        cur.close()
        conn.close()
        return render_template('query_result.html', result=result, name="Самый продаваемый товар")