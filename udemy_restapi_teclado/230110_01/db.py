# stores = [{"name": "My Store 01", "items": [{"name": "Chair", "price": 15.99}]}]
STORES: dict = {}

ITEMS = {
    "1": {
        "name": "Chair",
        "price": 15.99,
        "store_id": "cd2b4b93f15c4cdcbdb7ee70c008c5c1",
    },
    "2": {
        "name": "Table",
        "price": 200.99,
        "store_id": "cddf5818c2ab41ec845b3b367ff4224f",
    },
}

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

