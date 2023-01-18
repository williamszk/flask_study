from repl_endpoints import ReqGet, ReqPost


def test_01():
    print()
    ReqGet().make_request(**{"endpoint": "/store"})
    ReqPost().make_request(**{"endpoint": "/store", "json": {"name": "My Store"}})
    ReqGet().make_request(**{"endpoint": "/store"})
    ReqPost().make_request(
        **{
            "endpoint": "/store/My Store/item",
            "json": {"name": "Table", "price": 17.99},
        }
    )

    # A store that doesn't exist...
    ReqPost().make_request(
        **{
            "endpoint": "/store/Banana Store/item",
            "json": {"name": "Table", "price": 17.99},
        }
    )

    ReqPost().make_request(
        **{
            "endpoint": "/store/My Store/item",
            "json": {"name": "Laptop", "price": 799.99},
        }
    )

    ReqGet().make_request(**{"endpoint": "/store"})

    # Get a specific store
    ReqGet().make_request(**{"endpoint": "/store/My Store"})

    # Get items from a store
    ReqGet().make_request(**{"endpoint": "/store/My Store/item"})
