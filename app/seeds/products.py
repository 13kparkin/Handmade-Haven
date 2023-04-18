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
    product = Product(
        name="Sony PlayStation 6",
        description="The latest gaming console from Sony which is to cool, featuring a powerful AMD Zen 2 processor, 4K gaming capabilities, and support for the latest games.",
        price=499.99,
        quantity=200,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        seller_id=2
    )
    db.session.add(product)

    product = Product(
        name="Apple MacBook Pro M2",
        description="The latest laptop from Apple, featuring the M1 chip for fast performance and long battery life, a Retina display, and macOS Monterey.",
        price=1499.00,
        quantity=50,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        seller_id=3
    )
    db.session.add(product)

    product = Product(
        name="Amazon Echo (5th Gen)",
        description="The latest smart speaker from Amazon who knows all, featuring improved sound quality, Alexa voice assistant, and smart home integration.",
        price=99.99,
        quantity=150,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        seller_id=2
    )
    db.session.add(product)

    product = Product(
        name="DJI Mavic 5 Pro",
        description="The latest drone from DJI which got all things on camera, featuring a Hasselblad camera, 4K video recording, and obstacle avoidance.",
        price=1999.00,
        quantity=20,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        seller_id=3
    )
    db.session.add(product)

    product = Product(
        name="Bose QuietComfort 46",
        description="The latest noise-cancelling headphones from Bose which do infact cancel noise, featuring improved noise cancellation, voice assistant support, and long battery life.",
        price=329.99,
        quantity=100,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        seller_id=2
    )
    db.session.add(product)
    product = Product(
        name="Samsung Galaxy S28 Ultra",
        description="The upcoming flagship smartphone from Samsung which is awesome and cool, rumored to feature a 6.8 inch AMOLED display, Exynos 2200 chipset, and 5G connectivity.",
        price=1199.99,
        quantity=50,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        seller_id=3
    )


    db.session.add(product)

    product = Product(
        name="Sony PlayStation 5",
        description="The latest gaming console from Sony which is the ps45, featuring a powerful AMD Zen 2 processor, 4K gaming capabilities, and support for the latest games.",
        price=499.99,
        quantity=200,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        seller_id=2
    )
    db.session.add(product)

    product = Product(
        name="Apple MacBook Pro M10",
        description="The latest laptop from Apple the macbook 10, featuring the M1 chip for fast performance and long battery life, a Retina display, and macOS Monterey.",
        price=1499.00,
        quantity=50,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        seller_id=3
    )
    db.session.add(product)

    product = Product(
        name="Amazon Echo (22th Gen)",
        description="The latest smart speaker from Amazon, tim cook, featuring improved sound quality, Alexa voice assistant, and smart home integration.",
        price=99.99,
        quantity=150,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        seller_id=2
    )
    db.session.add(product)

    product = Product(
        name="Samsung Galaxy S22 Ultra",
        description="The upcoming flagship smartphone from Samsung the cool phone to rule them all, rumored to feature a 6.8 inch AMOLED display, Exynos 2200 chipset, and 5G connectivity.",
        price=1199.99,
        quantity=50,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        seller_id=3
    )


    db.session.add(product)

    product = Product(
        name="Sony PlayStation 55",
        description="The latest gaming console from Sony the ps345, featuring a powerful AMD Zen 2 processor, 4K gaming capabilities, and support for the latest games.",
        price=499.99,
        quantity=200,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        seller_id=2
    )
    db.session.add(product)

    product = Product(
        name="Apple MacBook Pro M1",
        description="The latest laptop from Apple, featuring the M1 chip for fast performance and long battery life, a Retina display, and macOS Monterey.",
        price=1499.00,
        quantity=50,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        seller_id=3
    )
    db.session.add(product)

    product = Product(
        name="Amazon Echo (4th Gen)",
        description="The latest smart speaker from Amazon, featuring improved sound quality, Alexa voice assistant, and smart home integration.",
        price=99.99,
        quantity=150,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        seller_id=2
    )
    db.session.add(product)

    product = Product(
        name="DJI Mavic 3 Pro",
        description="The latest drone from DJI, featuring a Hasselblad camera, 4K video recording, and obstacle avoidance.",
        price=1999.00,
        quantity=20,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        seller_id=3
    )
    db.session.add(product)

    product = Product(
        name="Bose QuietComfort 45",
        description="The latest noise-cancelling headphones from Bose, featuring improved noise cancellation, voice assistant support, and long battery life.",
        price=329.99,
        quantity=100,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        seller_id=2
    )
    db.session.add(product)
    product = Product(
        name="Samsung Galaxy S228 Ultra",
        description="The upcoming flagship smartphone from Samsung, rumored to feature a 6.8 inch AMOLED display, Exynos 2200 chipset, and 5G connectivity.",
        price=1199.99,
        quantity=50,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        seller_id=3
    )


    db.session.add(product)

    product = Product(
        name="Sony PlayStation 50",
        description="The latest gaming console from Sony, featuring a powerful AMD Zen 2 processor, 4K gaming capabilities, and support for the latest games.",
        price=499.99,
        quantity=200,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        seller_id=2
    )
    db.session.add(product)

    product = Product(
        name="Apple MacBook Pro M1",
        description="The latest laptop from Apple, featuring the M1 chip for fast performance and long battery life, a Retina display, and macOS Monterey.",
        price=1499.00,
        quantity=50,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        seller_id=3
    )
    db.session.add(product)

    product = Product(
        name="Amazon Echo (4th Gen)",
        description="The latest smart speaker from Amazon, featuring improved sound quality, Alexa voice assistant, and smart home integration.",
        price=99.99,
        quantity=150,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        seller_id=2
    )
    db.session.add(product)


    db.session.add(product)

    db.session.commit()


def undo_products():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.products RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM products"))

    db.session.commit()
