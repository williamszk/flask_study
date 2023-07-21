import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db import items, stores

# A Blueprint is used to divide the API in many segments
blp = Blueprint("items", __name__, description="Operations on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            abort(404, message="Item not found")

    def put(self, item_id):
        item_data = request.get_json()
        if (
            "price" not in item_data
            or "store_id" not in item_data
            or "name" not in item_data
        ):
            abort(
                400,
                message="Bad request. Ensure 'price', 'store_id' and 'name' are included in the JSON payload.",
            )

        # check to not insert an item that already exists
        for item in items.values():
            if (
                item["name"] == item_data["name"]
                and item["store_id"] == item_data["store_id"]
            ):
                abort(400, message=f"Item already exists.")

        # Check if the store_id in the json payload already exists in the stores data structure
        if item_data["store_id"] not in stores:
            abort(404, message="Store not found")
            # abort will exit and will auto document this error message
        # "name"
        # "price"
        # "store_id"
        # item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[item_id] = item

        return item, 200


@blp.route("/item")
class ItemList(MethodView):
    def get(self):
        return {"items": list(items.values())}

    def post(self):
        item_data = request.get_json()
        # The id of the store should come inside the json payload

        # This is where the checking for the incoming payload is checked
        # We still need to check if price is a number, store_id and name are strings
        if (
            "price" not in item_data
            or "store_id" not in item_data
            or "name" not in item_data
        ):
            abort(
                400,
                message="Bad request. Ensure 'price', 'store_id' and 'name' are included in the JSON payload.",
            )

        # check to not insert an item that already exists
        for item in items.values():
            if (
                item["name"] == item_data["name"]
                and item["store_id"] == item_data["store_id"]
            ):
                abort(400, message=f"Item already exists.")

        # Check if the store_id in the json payload already exists in the stores data structure
        if item_data["store_id"] not in stores:
            abort(404, message="Store not found")
            # abort will exit and will auto document this error message
        # "name"
        # "price"
        # "store_id"
        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[item_id] = item

        return item, 201
