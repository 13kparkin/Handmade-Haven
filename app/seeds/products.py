from app.models import db, Product, environment, SCHEMA, User
from sqlalchemy.sql import text
from datetime import datetime
from random import randint



# Adds a demo products
def seed_products():
    users = User.query.all()
    product = Product(
        name="Samsung Galaxy S23 Ultra",
        description="The upcoming flagship smartphone from Samsung which is awesome, rumored to feature a 6.8 inch AMOLED display, Exynos 2200 chipset, and 5G connectivity.",
        price=1199.99,
        quantity=50,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        seller_id=3
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
