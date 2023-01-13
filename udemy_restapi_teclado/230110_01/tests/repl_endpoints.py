import requests
import json


BASE_URL = "http://localhost:5000"

def print_response(r: requests.Response):
    print(r)
    print(json.dumps(r.json(), indent=4))
    print(f"{r.elapsed = }")


from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class AbstractReqType(ABC):
    @abstractmethod
    def make_request(self):
        pass


@dataclass
class ReqGet(AbstractReqType):
    endpoint: str
    def make_request(self):
        url = "".join([BASE_URL, self.endpoint])
        r = requests.get(url)
        print("============================================================================================================================================")
        print(f"GET request to: {self.endpoint}")
        print_response(r)


@dataclass
class ReqPost(AbstractReqType):
    endpoint: str
    def make_request(self):
        url = "".join([BASE_URL, self.endpoint])
        r = requests.post(url, data={"name":"My Store"})
        print("============================================================================================================================================")
        print(f"GET request to: {self.endpoint}")
        print_response(r)


def main():
    options = {
        "create new store": ReqPost("/store").make_request,
        "get all stores": ReqGet("/store").make_request,
        "exit": None,
    }

    print("The options that we have:")
    for key in options:
        print(f"- '{key}'")

    while True:
        print(">>> ", end="")

        try:
            user_input = input()
        except KeyboardInterrupt:
            return

        if user_input == "exit":
            print("Good bye :)")
            return

        if options.get(user_input) is None:
            print(f"Sorry, we couldn't find the option: '{user_input}'.")
            continue

        try:
            options[user_input]()
        except Exception as e:
            print(e)
            continue



if __name__ == "__main__":
    main()