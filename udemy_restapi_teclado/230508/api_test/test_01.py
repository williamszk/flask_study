import json
import requests


def main():
    url = "http://localhost"
    port = "5000"

    # TODO: [ ] are we testing all endpoints?

    print("-- create a store ----------------------------------------------------")
    res = requests.post(f"{url}:{port}/store", json={"name": "The Middle Earth Store"})
    # res = requests.post(f"{url}:{port}/store") // error 422
    print_res(res)
    store_id = res.json()["id"]

    print("-- get all stores ----------------------------------------------------")
    res = requests.get(f"{url}:{port}/store")
    print_res(res)

    print("-- get a specific store ----------------------------------------------")
    res = requests.get(f"{url}:{port}/store/{store_id}")
    print_res(res)

    print("-- create an item in that new store ----------------------------------")
    res = requests.post(
        f"{url}:{port}/item",
        json={"price": 10.00, "store_id": store_id, "name": "Kitchen Chair"},
    )
    print_res(res)

    print("-- get all items -----------------------------------------------------")
    res = requests.get(f"{url}:{port}/item")
    print_res(res)
    item_id = res.json()[0]["id"]

    print("-- get specific item -------------------------------------------------")
    res = requests.get(f"{url}:{port}/item/{item_id}")
    print_res(res)


def print_res(res, headers=False, raw=False):
    # if res.status_code == 200:
    #     print(">>> POST request successful")
    # if res.status_code == 201:
    #     print(">>> POST request successful, CREATED")
    # else:
    #     print(">>> POST request failed. Status code:", res.status_code)
    print(">>>", res.request.method, res.request.url)
    print(res.text)

    if headers:
        print(">>> Response Headers:", res.headers)
    if raw:
        print(">>> Response Raw:", res.raw)

    # if json:
    #     try:
    #         response_data = res.json()
    #         print(">>> Response JSON:", response_data)
    #     except json.JSONDecodeError as e:
    #         print(">>> Error decoding JSON response:", str(e))

    if res.status_code == 400:
        raise Exception("Sorry, we got a 400")
    elif res.status_code == 404:
        raise Exception("Sorry, we got a 404")


if __name__ == "__main__":
    main()
