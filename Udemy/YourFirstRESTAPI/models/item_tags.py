# from db import db
from db import db

class ItemTags(db.Model):
    __tablename__ = "items_tags" #stworzenie tablicy "items"

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"))
