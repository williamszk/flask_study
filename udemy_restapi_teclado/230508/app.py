from flask import Flask, request

app = Flask(__name__)

stores  = [
    {
        "name": "The Middle Earth",
        "items": [
            {"name": "The One Ring", "price": 1999.99},
        ]
    }
]

@app.get("/store")
def get_stores():
    return {"stores": stores}

@app.post("/store")
def create_store():
    request_data = request.get_json() 
    # TODO: how do we guarantee that the incoming json has some necessary fields?
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    # TODO: there should be a way to check if the store is already there
    stores.append(new_store)

    return new_store, 201

@app.post("/store/<string:name>/item")
def create_item(name):
    store_name = name
    store = next(filter(lambda store: store["name"] == store_name , stores), None)
    if store is None:
        return {
            "message": 
            f"The store '{store_name}' does not exist."
            }, 404
    items = store["items"]
    request_data = request.get_json()
    # TODO: how to check if the incoming json has all the required fields?
    new_item_name = request_data["name"]
    if next(filter(lambda item: item["name"] == new_item_name, items), None):
        return {
            "message": 
            f"An item with name '{new_item_name}' already exists in store '{store_name}'."
            }, 403
    
    new_item = {
        "name": new_item_name,
        "price": request_data["price"]
    }

    store["items"].append(new_item)

    return new_item, 201













