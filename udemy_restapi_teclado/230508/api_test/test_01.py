import json
import requests


def main():
    url = "http://localhost"
    port = "5000"

    # TODO: [ ] are we testing all endpoints?

    # create a store ----------------------------------------------------
    res = requests.post(f"{url}:{port}/store", json={"name": "bob marley"})
    print_res(res)
    store_id = res.json()["id"]

    # get all stores ----------------------------------------------------

    # get a specific store ----------------------------------------------
    res = requests.get(f"{url}:{port}/store/{store_id}")
    print_res(res)

    # create an item in that new store ----------------------------------

    # get all items -----------------------------------------------------


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
