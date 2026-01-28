import os
from dotenv import load_dotenv
import psycopg2
from flask import render_template, url_for
from flask_login import login_required


def init_categories_query(app):
    @app.route('/categories_query')
    @login_required
    def categories_query():
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
        ;''')
        result_pack = cur.fetchall()
        conn.commit()
        result = []
        for res in result_pack:
            result.append(str(res[0])+'     '+str(res[1]))

        cur.close()
        conn.close()
        return render_template('query_result.html', result=result, name="ID Количество продаж")