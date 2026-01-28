import os
from dotenv import load_dotenv
import psycopg2
from flask import render_template
from flask_login import login_required


def init_avg_revenue_query(app):
    @app.route('/avg_revenue_query')
    @login_required
    def avg_revenue_query():
        load_dotenv()

        uri = os.environ.get('SQLALCHEMY_DATABASE_URI')
        uri_for_psycopg2 = uri.replace('+psycopg2', '')

        conn = psycopg2.connect(uri_for_psycopg2)

        cur = conn.cursor()

        try:
            cur.execute('''
            SELECT AVG(orders.amount * products.price)
            FROM orders
            INNER JOIN products
            ON orders.product_id = products.id
            ;''')
            result = cur.fetchone()
            conn.commit()
            print("1")
        except psycopg2.Error as e:
            print(f"Ошибка: {e}")
        finally:
            cur.close()
            conn.close()
        return render_template('query_result.html', result=result, name="Средняя выручка")