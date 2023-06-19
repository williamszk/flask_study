import uuid
from flask import Flask, request
from flask_smorest import abort

from db import stores, items

app = Flask(__name__)


# ------ section for Stores ------
@app.get("/store")
def get_all_stores():
    return {"stores": list(stores.values())}


@app.get("/store/<string:store_id>")
def get_specific_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message="Store not found")


@app.post("/store")
def create_store():
    store_data = request.get_json()

    # ensure that name field is included
    # (i.e. name must be provided)
    if "name" not in store_data:
        abort(
            400, message="Bad request. Ensure 'name' is included in the JSON payload."
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


@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    try:
        del stores[store_id]
        return {"message": "Store deleted."}
    except KeyError:
        abort(404, message="Store not found")


@app.put("/store/<string:store_id>")
def update_store(store_id):
    store_data = request.get_json()

    # ensure that name field is included
    # (i.e. name must be provided)
    if "name" not in store_data:
        abort(
            400, message="Bad request. Ensure 'name' is included in the JSON payload."
        )

    # ensure the store is not duplicated
    # (i.e. name must be unique)
    for store in stores.values():
        if store_data["name"] == store["name"]:
            abort(400, message=f"Store already exists.")

    # store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    return store, 201


# ------ section for Items ------


@app.get("/item/<string:item_id>")
def get_specific_item(item_id):
    print(f"Debug: {item_id=}")
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item not found")


@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}


@app.post("/item")
def create_item():
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


@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message": "Item deleted."}
    except KeyError:
        abort(404, message="Item not found")


@app.put("/item/<string:item_id>")
def update_item(item_id):
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
