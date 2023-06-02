import uuid

from DataBase import stores
from schemas import StoreSchema
from flask.views import MethodView
from flask_smorest import abort, Blueprint

blp = Blueprint("stores", __name__, description="Operations on store")

@blp.route("/stores")
class StoreList(MethodView):
    def get(self):
        return {"stores": list(stores.values())}

@blp.route("/store/<string:store_id>")
class StoresID(MethodView):
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
    def post(self,store_data):
        # store_data = request.get_json()
        # if (
        #         "name" not in store_data
        # ):
        #     return abort(
        #         400,
        #         message="Ensure that 'name' is included in JSON payload"
        #     )

        for store in stores.values():
            if (
                    store_data["name"] == store["name"]
            ):
                return abort(
                    400,
                    message="Store already exist in store"
                )

        store_id = uuid.uuid4().hex
        store = \
            {
                **store_data, "id": store_id
            }
        stores[store_id] = store
        # return 200 -> OK
        # return 201 -> operacja udana
        return store, 201