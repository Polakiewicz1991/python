from marshmallow import Schema, fields

class PlainItemSchema(Schema):
    id = fields.Str(dump_only= True) #Oznacza tylko do odczytu, nie może być
    name = fields.Str(required= True) # jest wymagane
    price = fields.Float(required= True)
    # store_id = fields.Str(required= True) # usunięte po zastosowaniu Alchemy

class ItemUpdateSchema(Schema):
    name = fields.Str() #jest opcjonalne
    price = fields.Float()
    store_id = fields.Int()

class PlainStoreSchema(Schema):
    id = fields.Str(dump_only= True)  # Oznacza tylko do odczytu, nie może być
    name = fields.Str(required= True)

class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)

class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()),dump_only=True)