from db import db

class StoreModel(db.Model):
  __tablename__ = "stores"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(88), unique=True, nullable=False)
  
  # one-to-many relationships with Item
  items = db.relationship("ItemModel", back_populates="store", lazy="dynamic")