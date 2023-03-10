from .db import db, environment, SCHEMA, add_prefix_for_prod


class Purchase(db.Model):
    __tablename__ = "purchases"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    quantity = db.Column(db.Integer)
    total_price = db.Column(db.Integer)
    purchase_date = db.Column(db.Date)

    user = db.relationship("User", back_populates="purchases")
    product = db.relationship("Product", back_populates="purchases")
