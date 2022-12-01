from marshmallow import Schema, fields

# Update schemas after one-to-many relationships
class PlainItemSchema(Schema):
  id = fields.Int(dump_only=True) #return only when getting
  name = fields.Str(required=True)
  price = fields.Float(required=True)

class PlainStoreSchema(Schema):
  id = fields.Int(dump_only=True) #return only when getting
  name = fields.Str()

class ItemUpdateSchema(Schema):
  name = fields.Str()
  price = fields.Float()
  store_id = fields.Int() #can be passed or not. To create item if it does not exist

class ItemSchema(PlainItemSchema):
  store_id = fields.Int(required=True, load_only=True) #receive when creating
  store = fields.Nested(PlainStoreSchema(), dump_only=True) #return only when getting

class StoreSchema(PlainStoreSchema):
  items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True) #Prevent circular nested object

# class ItemSchema(Schema):
#   id = fields.Str(dump_only=True)
#   name = fields.Str(required=True)
#   price = fields.Float(required=True)
#   store_id = fields.Str(required=True)

# class ItemUpdateSchema(Schema):
#   name = fields.Str()
#   price = fields.Float()

# class StoreSchema(Schema):
#   id = fields.Str(dump_only=True)
#   name = fields.Str(required=True)

# Section 8: User Authentication
class UserSchema(Schema):
  id = fields.Int(dump_only=True)
  username = fields.Str(required=True)
  password = fields.Str(required=True)