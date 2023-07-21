import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db import stores

# A Blueprint is used to divide the API in many segments
blp = Blueprint("stores", __name__, description="Operations on stores")


# this decorator from flask_smorest will make sure that get and delete functions
# will be used depending on the http method that the client made
@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="Store not found")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted."}
        except KeyError:
            abort(404, message="Store not found")


@blp.route("/store")
class StoreList(MethodView):
    def get(self):
        return {"stores": list(stores.values())}

    def post(self):
        store_data = request.get_json()
        # ensure that name field is included
        # (i.e. name must be provided)
        if "name" not in store_data:
            abort(
                400,
                message="Bad request. Ensure 'name' is included in the JSON payload.",
            )

        # ensure the store is not duplicated
        # (i.e. name must be unique)
        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(400, message=f"Store already exists.")

        store_id = uuid.uuid4().hex
        store = {**store_data, "id": store_id}
        stores[store_id] = store
        return store, 201
