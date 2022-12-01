import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
# from db import stores
from schemas import StoreSchema

# flask-sqlalchemy
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from db import db
from models import StoreModel

blp = Blueprint("stores", __name__, description="Operations on stores")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
  @blp.response(200, StoreSchema)
  def get(self, store_id):
    print(store_id)
    # try:
    #   return stores[store_id]
    # except KeyError:
    #   abort(404, message = "Store not found")
    store = StoreModel.query.get_or_404(store_id)
    return store

  def delete(self, store_id):
    print(store_id)
    # try:
    #   del stores[store_id]
    #   return {"message": "Store deleted"}
    # except KeyError:
    #   abort(404, message = "Store not found")
    store = StoreModel.query.get_or_404(store_id)
    # raise NotImplementedError("Deleting a store is not implemented.")
    db.session.delete(store)
    db.session.commit()
    return {"message": "store deleted"}

@blp.route("/store")
class StoreList(MethodView):
  @blp.response(200, StoreSchema(many=True))
  def get(self):
    # return {"stores": list(stores.values())}
    return StoreModel.query.all()

  @blp.arguments(StoreSchema)
  @blp.response(201, StoreSchema)
  def post(self, store_data):
    # store_data = request.get_json()
    print(store_data)

    # if "name" not in store_data:
    #   abort(400, message = "Bad request. Ensure name are included in the JSON payload.")

    # for store in stores.values():
    #   if (store_data["name"] == store["name"]):
    #     abort(400, message = "Store already exists.")
    
    # store_id = uuid.uuid4().hex #afafabadfa32d
    # new_store = {**store_data, "id": store_id}
    # stores[store_id] = new_store

    # Use flask-sqlalchemy
    new_store = StoreModel(**store_data)
    try:
      db.session.add(new_store)
      db.session.commit()
    except IntegrityError:
      abort(400, message="A store with that name already exists.")
    except SQLAlchemyError:
      abort(500, message="An error occurred while inserting the item.")
    
    return new_store