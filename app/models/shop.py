from .db import db, environment, SCHEMA, add_prefix_for_prod


class Shop(db.Model):
    __tablename__ = "shops"
    if environment == "production":
        __table_args__ = {"schema": SCHEMA}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    owner = db.relationship("User", back_populates="shops")
    products = db.relationship("Product", back_populates="shop")
