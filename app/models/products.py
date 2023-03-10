from .db import db, environment, SCHEMA, add_prefix_for_prod


class Product(db.Model):
    __tablename__ = "products"
    if environment == "production":
        __table_args__ = {"schema": SCHEMA}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    category = db.Column(db.String)
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)
    seller_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    seller = db.relationship("User", back_populates="products")
    product_images = db.relationship("ProductImage", back_populates="product")
    reviews = db.relationship("Review", back_populates="product")
    shopping_cart = db.relationship("ShoppingCart", back_populates="product")


class ProductImage(db.Model):
    __tablename__ = "product_images"
    if environment == "production":
        __table_args__ = {"schema": SCHEMA}
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    preview = db.Column(db.Boolean)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))

    product = db.relationship("Product", back_populates="product_images")
