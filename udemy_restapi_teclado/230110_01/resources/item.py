import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError 
from db import db
from db import ITEMS, STORES
from schemas import ItemSchema, ItemUpdateSchema
from models import ItemModel


blp = Blueprint("items", __name__, description="Operations on Items")


@blp.route("/item/<string:item_id>")
class Items(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return ITEMS[item_id]
        except KeyError:
            abort(
                404, message=f"Sorry, we couldn't find a item with item_id'{item_id}'."
            )

    def delete(self, item_id):
        try:
            del ITEMS[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            abort(
                404, message=f"Sorry, we couldn't find a item with item_id'{item_id}'."
            )

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_info,item_id):
        # item_info = request.get_json()
        # if "price" not in item_info or "name" not in item_info:
        #     abort(
        #         400,
        #         message="Bad request. Ensure that 'price' and 'name' are in the JSON payload.",
        #     )
        try:
            item = ITEMS[item_id]
            item |= item_info
            return item
        except KeyError:
            abort(404, message="Item no found.")


@blp.route("/item")
class ItemsList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return ITEMS.values()

    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_info):
        # for it in ITEMS.values():
        #     if (
        #         item_info["name"] == it["name"]
        #         and item_info["store_id"] == it["store_id"]
        #     ):
        #         abort(404, message=f"Sorry, item already exists.")
        # if item_info["store_id"] not in STORES:
        #     abort(
        #         404,
        #         message=f"Sorry, we couldn't find a store with name '{item_info['store_id']}'.",
        #     )
        # item_id = uuid.uuid4().hex
        # new_item = {**item_info, "id": item_id}
        # ITEMS[item_id] = new_item
        item = ItemModel(**item_info)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Sorry, a problem happened while inserting the item.")

        return item
