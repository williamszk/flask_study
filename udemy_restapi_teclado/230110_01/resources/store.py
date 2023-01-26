import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import STORES

blp = Blueprint("stores", __name__, description="Operations on Stores")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        try:
            return STORES[store_id]
        except KeyError:
            abort(
                404,
                message=f"Sorry, we couldn't find a store with store_id '{store_id}'.",
            )

    def delete(self, store_id):
        try:
            del STORES[store_id]
            return {"message": "Store deleted."}
        except KeyError:
            abort(
                404, message=f"Sorry, we couldn't find a item with item_id'{store_id}'."
            )


@blp.route("/store")
class StoreList(MethodView):
    def get(self):
        return {"stores": STORES}

    def post(self):
        store_info = request.get_json()
        if "name" not in store_info:
            abort(
                400,
                message="Bad request. Ensure 'name' is included in the JSON payload.",
            )
        for store in STORES.values():
            if store_info["name"] == store["name"]:
                abort(400, message="Store already exists.")
        store_id = uuid.uuid4().hex
        new_store = {**store_info, "id": store_id}
        # stores.append(new_store)
        STORES[store_id] = new_store
        # return 201: Ok everything went well
        return store_info, 201
