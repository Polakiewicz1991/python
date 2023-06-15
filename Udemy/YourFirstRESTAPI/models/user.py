# from db import db
from db import db

class UserModel(db.Model):
    __tablename__ = "users" #stworzenie tablicy "items"

    id = db.Column(db.Integer, primary_key=True) #będzie generowane przez baze danych
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
