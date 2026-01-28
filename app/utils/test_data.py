import random
from datetime import datetime, timedelta

from app import db, create_app
from app.models import Admin, Product, Order

def seed_products(n=12):
    products = []
    for i in range(1, n + 1):
        product = Product(amount=random.randint(0, 500),
            price=random.randint(100, 10000),
            created_at=datetime.utcnow() - timedelta(days=random.randint(0, 60)))
        products.append(product)
        db.session.add(product)
    db.session.commit()
    return products

def seed_orders(products, n=100):
    for _ in range(n):
        product = random.choice(products)
        quantity = random.randint(1, 5)

        order = Order(
            created_at=datetime.utcnow() - timedelta(days=random.randint(0, 30),
                                                     hours=random.randint(0, 23),
                                                     minutes=random.randint(0, 59)),
            amount=quantity,
            admin_id=1,
            product_id=product.id,
            address=random.choice([
                'Москва, Тверская ул., д. 1',
                'Санкт-Петербург, Невский пр., д. 25',
                'Казань, Кремлёвская ул., д. 5',
                'Екатеринбург, Ленина ул., д. 10',
                'Новосибирск, Красный пр., д. 15']))
        db.session.add(order)

    db.session.commit()

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        products = Product.query.all()
        if not products:
            products = seed_products(n=15)
        seed_orders(products, n=200)