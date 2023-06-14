from marshmallow import Schema, fields

class PlainItemSchema(Schema):
    id = fields.Int(dump_only= True) #Oznacza tylko do odczytu, nie może być
    name = fields.Str(required= True) # jest wymagane
    price = fields.Float(required= True)
    # store_id = fields.Str(required= True) # usunięte po zastosowaniu Alchemy

class PlainStoreSchema(Schema):
    id = fields.Int(dump_only= True)  # Oznacza tylko do odczytu, nie może być
    name = fields.Str(required= True)

class PlainTagSchema(Schema):
    id = fields.Int(dump_only= True)  # Oznacza tylko do odczytu, nie może być
    name = fields.Str(required= True)

class ItemUpdateSchema(Schema):
    name = fields.Str() #jest opcjonalne
    price = fields.Float()
    store_id = fields.Int()

class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)

class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()),dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)

class TagSchema(PlainTagSchema):
    store_id = fields.Int(load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)

class TagAndItems(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagSchema)