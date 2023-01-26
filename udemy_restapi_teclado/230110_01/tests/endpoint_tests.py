# %%
import requests
from requests import JSONDecodeError
import json
import uuid
from typing import Optional

# %%
BASE_URL = "http://localhost:5000"


def print_response(r: requests.Response):
    print(r)
    try:
        print(json.dumps(r.json(), indent=4))
    except JSONDecodeError:
        print(r.content)
    print(f"Elapsed time: {r.elapsed.seconds}.{r.elapsed.microseconds} seconds")


def make_request(typeof: str, endpoint: str, json_body: Optional[dict] = None):
    print("=" * 130)
    url = "".join([BASE_URL, endpoint])
    if typeof == "get":
        r = requests.get(url, json=json_body)
    elif typeof == "post":
        r = requests.post(url, json=json_body)
    elif typeof == "delete":
        r = requests.delete(url, json=json_body)
    elif typeof == "put":
        r = requests.put(url, json=json_body)

    print_response(r)

    return r.json()


# %%
# --------------------------------------------------------------------------------------------------------------------------- #
#                   The endpoint calls:
# --------------------------------------------------------------------------------------------------------------------------- #


# %%
# ----------------------------------------- #
# Get All Items                             #
# ----------------------------------------- #
make_request("get", f"/item", None)

# %%
# ----------------------------------------- #
# Create a Store                            #
# ----------------------------------------- #
make_request("post", f"/store", {"name": "The Westeros Store"})

# %%
# ----------------------------------------- #
# Create an Item                            #
# ----------------------------------------- #
output = make_request("get", f"/store", None)
_ = make_request(
    "post",
    f"/item",
    {
        "price": 99.99,
        "name": "The Iron Throne",
        "store_id": list(output["stores"].keys())[0],
    },
)

# %%
# ----------------------------------------- #
# Get all Item                              #
# ----------------------------------------- #
output = make_request("get", "/item", None)

# %%
# ----------------------------------------- #
# Delete an Item                            #
# ----------------------------------------- #
item_id = list(output["items"].keys())[0]
make_request("delete", f"/item/{item_id}", None)

_ = make_request("get", "/item", None)

# %%
# ----------------------------------------- #
# Update an Item                              #
# ----------------------------------------- #
item_id = "1"
make_request(
    "put",
    f"/item/{item_id}",
    {
        "name": "The Grand Chair of the Vizir",
        "price": 99.99,
    },
)

_ = make_request("get", "/item", None)

# %%
# ----------------------------------------- #
# Create a Store and delete it right after
# ----------------------------------------- #
_ = make_request("post", f"/store", {"name": "The MiddleEarth Store"})

output = make_request("get", "/store", None)
store_id = list(output["stores"].keys())[0]

make_request("delete", f"/store/{store_id}")
_ = make_request("get", "/store", None)
