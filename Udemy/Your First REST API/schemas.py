from marshmallow import Schema, fields

class ItemSchema(Schema):
    id = fields.Str(dump_only= True) #Oznacza tylko do odczytu, nie może być
    name = fields.Str(required= True) # jest wymagane
    price = fields.Float(required= True)
    store_id = fields.Str(required= True)

class ItemUpdateSchema(Schema):
    name = fields.Str() #jest opcjonalne
    price = fields.Float()

class StoreSchema(Schema):
    id = fields.Str(dump_only=True)  # Oznacza tylko do odczytu, nie może być
    name = fields.Str(required=True)