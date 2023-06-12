import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import TagModel, StoreModel
from schemas import TagSchema

blp = Blueprint("tags", __name__, description="Operations on tags")

@blp.route("/store/<string:store_id>/tags")
class TagsInStore(MethodView):
    @blp.response(200, TagSchema(many=True))
    def get(self,store_id):
        store = TagSchema.query.get_or_404(store_id)
        return store.tags.all()

    @blp.arguments(TagSchema)
    @blp.response(200, TagSchema(many=True))
    def get(self, tag_data, store_id):
        tag = TagModel(**tag_data, store_id=store_id)
        # if TagModel.query.filter(TagModel.store_id == store_id, TagModel.name == tag_data["name"]).first():
        #     abort(400, message="A tagg with thart name already exists in that store")
        try:
            db.session.add(tag)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500,
                  message=str(e))

@blp.route("/tag/<string:tag_id>")
class Tag(MethodView):
    @blp.response(200, TagSchema())
    def get(self,tag_id):
        tag = TagSchema.query.get_or_404(tag_id)
        return tag