import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

uri = os.environ.get('SQLALCHEMY_DATABASE_URI')
uri_for_psycopg2 = uri.replace('+psycopg2', '')

conn = psycopg2.connect(uri_for_psycopg2)

cur = conn.cursor()

try:
    cur.execute('''
    
    UPDATE products 
    SET amount = amount + 100
    
    ;''')

    conn.commit()
    print("1")

except psycopg2.Error as e:

    print(f"Ошибка: {e}")

finally:

    cur.close()
    conn.close()

