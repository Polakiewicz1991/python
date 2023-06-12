# from db import db
from db import db

class TagModel(db.Model):
    __tablename__ = "tags" #stworzenie tablicy "items"

    id = db.Column(db.Integer, primary_key=True) #będzie generowane przez baze danych
    name = db.Column(db.String(80), unique=True, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False)
    store = db.relationship("StoreModel", back_populates="tags")
