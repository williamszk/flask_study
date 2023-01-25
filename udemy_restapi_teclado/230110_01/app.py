import uuid
from flask import Flask, request
from flask_smorest import abort
from db import ITEMS, STORES


app = Flask(__name__)


@app.get("/store")
def get_all_stores():
    return {"stores": STORES}


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return STORES[store_id]
    except KeyError:
        abort(
            404, message=f"Sorry, we couldn't find a store with store_id '{store_id}'."
        )


@app.post("/store")
def create_store():
    store_info = request.get_json()
    if "name" not in store_info:
        abort(
            400, message="Bad request. Ensure 'name' is included in the JSON payload."
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

@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    try:
        del STORES[store_id]
        return {"message": "Store deleted."}
    except KeyError:
        abort(404, message=f"Sorry, we couldn't find a item with item_id'{store_id}'.")


@app.get("/item")
def get_all_items():
    return {"items": ITEMS}

@app.post("/item")
def create_item():
    item_info = request.get_json()
    if (
        "price" not in item_info
        or "store_id" not in item_info
        or "name" not in item_info
    ):
        return abort(
            404,
            message="Ensure that 'price', 'store_id' and 'name' are in the request body.",
        )

    for it in ITEMS.values():
        if item_info["name"] == it["name"] and item_info["store_id"] == it["store_id"]:
            abort(404, message=f"Sorry, item already exists.")

    if item_info["store_id"] not in STORES:
        abort(
            404,
            message=f"Sorry, we couldn't find a store with name '{item_info['store_id']}'.",
        )

    item_id = uuid.uuid4().hex
    new_item = {**item_info, "id": item_id}
    ITEMS[item_id] = new_item

    return item_info, 201


@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return ITEMS[item_id]
    except KeyError:
        abort(404, message=f"Sorry, we couldn't find a item with item_id'{item_id}'.")


@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del ITEMS[item_id]
        return {"message": "Item deleted."}
    except KeyError:
        abort(404, message=f"Sorry, we couldn't find a item with item_id'{item_id}'.")

@app.put("/item/<string:item_id>")
def update_item(item_id):
    item_info = request.get_json()
    if "price" not in item_info or "name" not in item_info:
        abort(400, message="Bad request. Ensure that 'price' and 'name' are in the JSON payload.")
    try:
        item = ITEMS[item_id]
        item |= item_info
        return item
    except KeyError:
        abort(404, message="Item no found.")