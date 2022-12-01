#Section 3	My first REST API

from flask import Flask, request

app = Flask(__name__)

stores = [
  {
    "name": "Tung Store",
    "items": [
      {
        "name": "laptop",
        "price": 1999.99
      }
    ]
  }
]

@app.get("/store")
def get_stores():
  return {"stores": stores}

@app.post("/store")
def create_store():
  request_data = request.get_json()
  print(request_data)
  new_store = {"name": request_data["name"], "items": []}
  stores.append(new_store)
  return new_store, 201

@app.post("/store/<string:name>")
def create_item(name):
  request_data = request.get_json()
  for store in stores:
    if store["name"] == name:
      new_item = {"name": request_data["name"], "price": request_data["price"]}
      store["items"].append(new_item)
      return new_item, 201
  return {"message": "Store not found"}, 404

@app.get("/store/<string:name>")
def get_store(name):
  for store in stores:
    if store["name"] == name:
      return {"store": store}
  return {"message": "Store not found"}, 404