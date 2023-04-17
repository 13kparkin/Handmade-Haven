from app.models import db, Product, environment, SCHEMA, User
from sqlalchemy.sql import text
from datetime import datetime
from random import randint
from faker import Faker


# Adds a demo products
def seed_products():
    faker_instance = faker.Faker()
    users = User.query.all()
    for i in range(20):
        product = Product(
            name=faker_instance.word() + " " + faker_instance.word(),
            description=faker_instance.paragraph(),
            price=round(random.uniform(5, 500), 2),
            quantity=random.randint(10, 1000),
            created_at=faker_instance.date_time_this_year(),
            updated_at=faker_instance.date_time_between_dates(
                datetime_start=faker_instance.date_time_this_year(),
                datetime_end=datetime.utcnow()
            ),
            seller_id=random.choice(users).id
        )
        db.session.add(product)

    db.session.commit()


def undo_products():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.products RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM products"))
        
    db.session.commit()