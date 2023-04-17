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

created_at = datetime.now() - timedelta(days=random.randint(1, 365)),


# Adds a demo products
def seed_products():
    users = User.query.all()
    {
        "name": "Apple iPhone 13 Pro Max",
        "description": "The latest flagship smartphone from Apple, featuring a 6.7 inch Super Retina XDR display, A15 Bionic chip, and 5G connectivity.",
        "price": 1099.00,
        "quantity": 100,
        "created_at": datetime.now() - timedelta(days=30),
        "updated_at": datetime.now() - timedelta(days=5),
        "seller_id": 2
    },
    db.session.add(product)
    {
        "name": "Samsung Galaxy S22 Ultra",
        "description": "The upcoming flagship smartphone from Samsung, rumored to feature a 6.8 inch AMOLED display, Exynos 2200 chipset, and 5G connectivity.",
        "price": 1199.99,
        "quantity": 50,
        "created_at": datetime.now() - timedelta(days=60),
        "updated_at": datetime.now() - timedelta(days=20),
        "seller_id": 3
    },
    db.session.add(product)
    {
        "name": "Sony PlayStation 5",
        "description": "The latest gaming console from Sony, featuring a powerful AMD Zen 2 processor, 4K gaming capabilities, and support for the latest games.",
        "price": 499.99,
        "quantity": 200,
        "created_at": datetime.now() - timedelta(days=90),
        "updated_at": datetime.now() - timedelta(days=10),
        "seller_id": 2
    },
    db.session.add(product)
    {
        "name": "Apple MacBook Pro M1",
        "description": "The latest laptop from Apple, featuring the M1 chip for fast performance and long battery life, a Retina display, and macOS Monterey.",
        "price": 1499.00,
        "quantity": 50,
        "created_at": datetime.now() - timedelta(days=120),
        "updated_at": datetime.now() - timedelta(days=15),
        "seller_id": 3
    },
    db.session.add(product)
    {
        "name": "Amazon Echo (4th Gen)",
        "description": "The latest smart speaker from Amazon, featuring improved sound quality, Alexa voice assistant, and smart home integration.",
        "price": 99.99,
        "quantity": 150,
        "created_at": datetime.now() - timedelta(days=150),
        "updated_at": datetime.now() - timedelta(days=25),
        "seller_id": 2
    },
    db.session.add(product)
    {
        "name": "DJI Mavic 3 Pro",
        "description": "The latest drone from DJI, featuring a Hasselblad camera, 4K video recording, and obstacle avoidance.",
        "price": 1999.00,
        "quantity": 20,
        "created_at": datetime.now() - timedelta(days=180),
        "updated_at": datetime.now() - timedelta(days=30),
        "seller_id": 3
    },
    db.session.add(product)
    {
        "name": "Bose QuietComfort 45",
        "description": "The latest noise-cancelling headphones from Bose, featuring improved noise cancellation, voice assistant support, and long battery life.",
        "price": 329.99,
        "quantity": 100,
        "created_at": datetime.now() - timedelta(days=210),
        "updated_at": datetime.now() - timedelta(days=35),
        "seller_id": 2
    },
    db.session.add(product)

    db.session.commit()


def undo_products():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.products RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM products"))

    db.session.commit()
