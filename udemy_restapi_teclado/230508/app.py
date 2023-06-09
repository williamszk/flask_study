import uuid
from flask import Flask, request

from db import stores, items

app = Flask(__name__)


@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}


@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    return stores, 201


@app.post("/item")
def create_item():
    item_data = request.get_json()
    # The id of the store should come inside the json payload

    # Check if the store_id in the json payload already exists in the stores data structure
    if item_data["store_id"] not in stores:
        return {"message": "Store not found"}, 404
    # "name"
    # "price"
    # "store_id"
    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items["item_id"] = item

    return item, 201


@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}


def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {"message": "Store not found"}, 404


@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return {"message": "Store not found"}, 404
