import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db import items, stores
from schemas import ItemSchema, ItemUpdateSchema

# A Blueprint is used to divide the API in many segments
blp = Blueprint("items", __name__, description="Operations on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
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

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        try:
            item = items[item_id]
            # this is dict concatenation
            item |= item_data
            return item
        except KeyError:
            abort(404, message="Item not found.")


@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return items.values()

    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
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
