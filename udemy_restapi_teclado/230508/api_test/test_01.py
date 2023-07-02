import json
import requests


def main():
    url = "http://localhost"
    port = "5000"

    # create a store
    res = requests.post(f"{url}:{port}/store", json={"name": "bob marley"})

    if res.status_code == 200:
        print(">>> POST request successful")
    if res.status_code == 201:
        print(">>> POST request successful, CREATED")
    else:
        print(">>> POST request failed. Status code:", res.status_code)

    print(">>> Response:", res.text)
    print(">>> Response Headers:", res.headers)
    print(">>> Response Raw:", res.raw)

    try:
        response_data = res.json()
        print(">>> Response JSON:", response_data)
    except json.JSONDecodeError as e:
        print(">>> Error decoding JSON response:", str(e))

    # get all stores ----------------------------------------------------

    # get a specific store ----------------------------------------------

    # create an item in that new store ----------------------------------

    # get all items -----------------------------------------------------


if __name__ == "__main__":
    main()
