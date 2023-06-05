import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import StoreModel
from schemas import StoreSchema

blp = Blueprint("stores", __name__, description="Operations on store")

@blp.route("/stores")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return stores.values()

@blp.route("/store/<string:store_id>")
class StoresID(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            return abort(404, message="Store not found")
    def delete(self, store_id):
        try:
            del (stores[store_id])
            return {"message": "Store deleted"}
        except KeyError:
            return abort(404, message="Store not found")

@blp.route("/store")
class Store(MethodView):
    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)
    def post(self,store_data):
        # store_data = request.get_json()
        # if (
        #         "name" not in store_data
        # ):
        #     return abort(
        #         400,
        #         message="Ensure that 'name' is included in JSON payload"
        #     )

        # for store in stores.values():
        #     if (
        #             store_data["name"] == store["name"]
        #     ):
        #         return abort(
        #             400,
        #             message="Store already exist in store"
        #         )
        #
        # store_id = uuid.uuid4().hex
        # store = \
        #     {
        #         **store_data, "id": store_id
        #     }
        # stores[store_id] = store

        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, "A store with that name already exists")
        except SQLAlchemyError:
            abort(500, "An error occurred while inserting the item")

        # return 200 -> OK
        # return 201 -> operacja udana
        return store