import os
from dotenv import load_dotenv
import psycopg2
from flask import render_template
from flask_login import login_required


def init_stocks_query(app):
    @app.route('/stocks_query')
    @login_required
    def stocks_query():
        load_dotenv()

        uri = os.environ.get('SQLALCHEMY_DATABASE_URI')
        uri_for_psycopg2 = uri.replace('+psycopg2', '')

        conn = psycopg2.connect(uri_for_psycopg2)

        cur = conn.cursor()

        cur.execute('''
        SELECT id, amount, price 
        FROM products
        ORDER BY id
        ;''')
        result_pack = cur.fetchall()
        result = []
        for row in result_pack:
            result += [f'{row[0]},    {row[1]} шт.,   {row[2]} руб.']
        conn.commit()

        cur.close()
        conn.close()
        return render_template('query_result.html', result=result, name="Складские запасы")