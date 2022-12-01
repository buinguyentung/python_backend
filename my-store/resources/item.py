import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
# from db import items, stores
from schemas import ItemSchema, ItemUpdateSchema

# flask-sqlalchemy
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from db import db
from models import ItemModel

blp = Blueprint("items", __name__, description="Operations on items")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
  @blp.response(200, ItemSchema)
  def get(self, item_id):
    # try:
    #   return items[item_id]
    # except KeyError:
    #   abort(404, message = "Item not found")
    item = ItemModel.query.get_or_404(item_id)
    return item

  def delete(self, item_id):
    print(item_id)
    # try:
    #   del items[item_id]
    #   return {"message": "Item deleted"}
    # except KeyError:
    #   abort(404, message = "Item not found")
    item = ItemModel.query.get_or_404(item_id)
    # raise NotImplementedError("Deleting an item is not implemented.")
    db.session.delete(item)
    db.session.commit()
    return {"message": "item deleted"}

  @blp.arguments(ItemUpdateSchema)
  @blp.response(200, ItemSchema)
  def put(self, item_data, item_id):
    item = ItemModel.query.get(item_id)
    if item:
        item.price = item_data["price"]
        item.name = item_data["name"]
    else:
        item = ItemModel(id=item_id, **item_data)

    db.session.add(item)
    db.session.commit()

    return item

@blp.route("/item")
class ItemList(MethodView):
  @blp.response(200, ItemSchema(many=True))
  def get(self):
    # return {"items": list(items.values())}
    return ItemModel.query.all()

  @blp.arguments(ItemSchema)
  @blp.response(201, ItemSchema)
  def post(self, item_data):
    # item_data = request.get_json()
    # if (
    #   "price" not in item_data
    #   or "store_id" not in item_data
    #   or "name" not in item_data
    # ):
    #   abort(400, message = "Bad request. Ensure price, store_id, name are included in the JSON payload.")
    
    # print("store_id = ", item_data["store_id"])
    # for item in items.values():
    #   if (item_data["name"] == item["name"]
    #     and item_data["store_id"] == item["store_id"]):
    #     abort(400, message = "Item already exists.")

    # if item_data["store_id"] not in stores:
    #   abort(404, message = "Store not found")
    
    # item_id = uuid.uuid4().hex
    # new_item = {**item_data, "id": item_id}
    # items[item_id] = new_item
    # Use flask-sqlalchemy
    new_item = ItemModel(**item_data)
    try:
      db.session.add(new_item)
      db.session.commit()
    except SQLAlchemyError:
      abort(500, message="An error occurred while inserting the item.")

    return new_item, 201