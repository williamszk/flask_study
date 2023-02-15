from marshmallow import Schema, fields
from marshmallow.fields import Int, Str, Float, List, Nested


class PlainItemSchema(Schema):
    id = Int(dump_only=True)
    name = Str(required=True)
    price = Float(required=True)


class PlainStoreSchema(Schema):
    id = Int(dump_only=True)
    name = Str(required=True)


class PlainTagsSchema(Schema):
    id = Int(dump_only=True)
    name = Str()


class StoreSchema(PlainStoreSchema):
    items = List(Nested(PlainItemSchema()), dump_only=True)
    tags = List(Nested(PlainTagsSchema()), dump_only=True)


class TagSchema(PlainTagsSchema):
    store_id = Int(load_only=True)
    store = Nested(PlainStoreSchema(), dump_only=True)
    items = List(Nested(PlainItemSchema()), dump_only=True)


class ItemSchema(PlainItemSchema):
    store_id = Int(required=True, load_only=True)
    store = Nested(PlainStoreSchema(), dump_only=True)
    tags = List(Nested(PlainTagsSchema()), dump_only=True)


class ItemUpdateSchema(Schema):
    name = Str()
    price = Float()
    store_id = Int()


class ItemsAndTagsSchema(Schema):
    message = Str()
    item = Nested(ItemSchema)
    tag = Nested(TagSchema)
