from app.models import db, Product, environment, SCHEMA, User
from sqlalchemy.sql import text
from datetime import datetime
from random import randint

from datetime import datetime, timedelta
import random

PRODUCT_NAMES = ['Apple Watch', 'MacBook Air', 'Kindle Paperwhite', 'Nintendo Switch', 'Fitbit Charge',
                 'Bose QuietComfort', 'Canon EOS', 'Dyson V11', 'Samsung Galaxy S21', 'Sony WH-1000XM4',
                 'iRobot Roomba', 'Weber Spirit', 'Google Nest', 'Microsoft Surface Pro', 'Keurig K-Mini',
                 'Anker PowerCore', 'Oculus Quest 2', 'KitchenAid Stand Mixer', 'Garmin Forerunner', 'Roku Streaming Stick']

PRODUCT_DESCRIPTIONS = ['The ultimate companion for your active lifestyle.', 'The perfect balance of power and portability.',
                        'Escape into your next great read with the Kindle Paperwhite.', 'Take your gaming anywhere with the Nintendo Switch.',
                        'Track your fitness and health with the Fitbit Charge.', 'Experience world-class noise cancellation with Bose.',
                        'Capture stunning photos and videos with the Canon EOS.', 'Clean your home with ease with the Dyson V11.',
                        'Experience the power of the Samsung Galaxy S21.', 'Immerse yourself in your music with Sony WH-1000XM4.',
                        'Clean your floors without lifting a finger with the iRobot Roomba.', 'Grill like a pro with the Weber Spirit.',
                        'Make your home smarter with Google Nest.', 'Unleash your creativity with the Microsoft Surface Pro.',
                        'Brew your perfect cup of coffee with the Keurig K-Mini.', 'Stay powered up on the go with Anker PowerCore.',
                        'Step into a virtual world with the Oculus Quest 2.', 'Mix like a pro with the KitchenAid Stand Mixer.',
                        'Train like a pro with the Garmin Forerunner.', 'Stream your favorite content with the Roku Streaming Stick.']

PRODUCT_PRICES = [199.99, 999.99, 129.99, 299.99, 129.99, 329.99, 799.99, 599.99, 1199.99, 349.99,
                  499.99, 399.99, 99.99, 1099.99, 69.99, 39.99, 299.99, 399.99, 199.99, 49.99]

PRODUCT_QUANTITIES = [10, 25, 50, 75, 100, 150, 200]




# Adds a demo products
def seed_products():
    users = User.query.all()
    for i in range(20):
        product = Product(
            name=random.choice(PRODUCT_NAMES),
            description=random.choice(PRODUCT_DESCRIPTIONS),
            price=random.choice(PRODUCT_PRICES),
            quantity=random.choice(PRODUCT_QUANTITIES),
            created_at=datetime.now() - timedelta(days=random.randint(1, 365)),
            updated_at=created_at + timedelta(days=random.randint(1, 30)),
            seller_id=random.randint(2, 3)
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
