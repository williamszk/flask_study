import requests
import json


BASE_URL = "http://localhost:5000"


def print_response(r: requests.Response):
    print(r)
    print(json.dumps(r.json(), indent=4))
    # print(f"{r.elapsed = }")
    print(f"Elapsed time: {r.elapsed.seconds}.{r.elapsed.microseconds} seconds")


from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class AbstractReqType(ABC):
    @abstractmethod
    def make_request(self):
        pass


@dataclass
class ReqGet(AbstractReqType):
    def make_request(self, endpoint):
        print("=" * 130)
        print(f"GET request to: {endpoint}")
        url = "".join([BASE_URL, endpoint])
        r = requests.get(url)
        print_response(r)


@dataclass
class ReqPost(AbstractReqType):
    def make_request(self, endpoint, json):
        print("=" * 130)
        print(f"POST request to: {endpoint}")
        url = "".join([BASE_URL, endpoint])
        r = requests.post(url, json=json)
        print_response(r)


OPTIONS = {
    "create new store": {
        "func": ReqPost().make_request,
        "kwargs": {"endpoint": "/store", "json": {"name": "My Store"}},
    },
    "get all stores": {
        "func": ReqGet().make_request,
        "kwargs": {"endpoint": "/store"},
    },
    "create item": {
        "func": ReqPost().make_request,
        "kwargs": {
            "endpoint": "/store/My Store/item",
            "json": {"name": "Table", "price": 17.99},
        },
    },
    "exit": None,
    "get options": None,
}


def show_options():
    print("The options that we have:")
    for key in OPTIONS:
        print(f"- '{key}'")


def main():

    show_options()

    while True:
        print(">>> ", end="")

        try:
            user_input = input()
        except KeyboardInterrupt:
            return

        if user_input == "exit":
            print("Good bye :)")
            return

        if user_input == "get options":
            show_options()
            continue

        if OPTIONS.get(user_input) is None:
            print(f"Sorry, we couldn't find the option: '{user_input}'.")
            continue

        try:
            function = OPTIONS[user_input]["func"]
            kwargs = OPTIONS[user_input]["kwargs"]
            function(**kwargs)
        except Exception as e:
            print(e)
            continue


if __name__ == "__main__":
    main()
