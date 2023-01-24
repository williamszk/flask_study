import uuid
from flask import Flask, request
from db import items, stores

app = Flask(__name__)


@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}


@app.post("/store")
def create_store():
    store = request.get_json()
    store_id = uuid.uuid4().hex
    new_store = {**store, "id": store_id}
    # stores.append(new_store)
    stores[store_id] = new_store
    # return 201: Ok everything went well
    return store, 201


@app.post("/item")
def create_item():
    item = request.get_json()
    if item["store_id"] not in stores:
        return {
            "Error": f"Sorry, we couldn't find a store with name '{item['store_id']}'."
        }, 404

    item_id = uuid.uuid4().hex
    new_item = {**item, "id": item_id}
    items[item_id] = new_item

    return item, 201


@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {
            "Error": f"Sorry, we couldn't find a store with store_id '{store_id}'."
        }, 404


@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return {"Error": f"Sorry, we couldn't find a store with name '{item_id}'."}, 404
