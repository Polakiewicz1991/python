# from db import db
from db import db

class StoreModel(db.Model):
    __tablename__ = "stores" #stworzenie tablicy "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    #nullable -> sprawdza, czy wartość zmiennej istnieje (w wypadku null/none zgłasza błąd)
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")
    #cascade="all, delete" - sprawi, że wraz z rodzicem(store) zabijamy dzieci(item)
    tags = db.relationship("TagModel",back_populates="store", lazy="dynamic")
