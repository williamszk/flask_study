import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from db import STORES
from db import db
from schemas import StoreSchema
from models import StoreModel

blp = Blueprint("stores", __name__, description="Operations on Stores")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
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
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        # return {"stores": STORES}
        return STORES.values()

    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)
    def post(self, store_info):

        store = StoreModel(**store_info)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Sorry, the store name already exist.")

        except SQLAlchemyError:
            abort(500, message="Sorry, an error happened while creating the store.")

        return store