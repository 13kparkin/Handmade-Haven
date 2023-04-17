from app.models import db, Product, environment, SCHEMA, User
from sqlalchemy.sql import text
from datetime import datetime
from random import randint
from faker import Faker

fake = Faker()


# Adds a demo products
def seed_products():
    faker_instance = faker.Faker()
    users = User.query.all()
    for i in range(20):
        product = Product(
            name=fake.word(),
            description=fake.sentence(),
            price=round(fake.pyfloat(left_digits=2,
                        right_digits=2, positive=True), 2),
            quantity=fake.random_int(min=1, max=100),
            created_at=fake.date_time_between(
                start_date='-1y', end_date='now'),
            updated_at=fake.date_time_between(
                start_date='-1y', end_date='now'),
            seller_id=users[randint(1, len(users)-1)].id
        )

        db.session.add(product)

    db.session.commit()


def undo_products():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.products RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM products"))

    db.session.commit()
