from .db import db, environment, SCHEMA


class ShoppingCart(db.Model):
    __tablename__ = "shopping_carts"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(
        "products.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.id"), nullable=False)

    products = db.relationship("Product", back_populates="shopping_carts")
    user = db.relationship("User", back_populates="shopping_carts")

    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "products": [product.to_dict() for product in self.products],
            "user_id": self.user_id
        }
