from db import db


# a Model will be a mapping from a row in a sql table and a field in a python class
class ItemModel(db.Model):  # type: ignore
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    store_id = db.Column(
        db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False
    )  # we won't be able to create an item if the store_id is not defined
    store = db.relationship("StoreModel", back_populates="items")
