#Section 6	Flask-SQLAlchemy

import os
import datetime
from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager

from resources.store import blp as StoreBlueprint
from resources.item import blp as ItemBlueprint
from resources.user import blp as UserBlueprint

from db import db
import models

def create_app(db_url=None):
  app = Flask(__name__)

  app.config["PROPAGATE_EXCEPTIONS"] = True
  app.config["API_TITLE"] = "Stores REST API"
  app.config["API_VERSION"] = "v1"
  app.config["OPENAPI_VERSION"] = "3.0.3"
  app.config["OPENAPI_URL_PREFIX"] = "/"
  app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
  app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
  
  # db config
  app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  db.init_app(app)

  # JWT config
  app.config["JWT_SECRET_KEY"] = "TungBui"
  app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(days=1)
  app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies"]
  app.config["JWT_HEADER_NAME"] = "Authorization-token"
  jwt = JWTManager(app)

  @jwt.expired_token_loader
  def expired_token_callback(jwt_header, jwt_payload):
    return (
      jsonify({"message": "The token has expired.", "error": "token_expired"}),
      401,
    )

  @jwt.invalid_token_loader
  def invalid_token_callback(error):
    return (
      jsonify({"message": "Signature verification failed.", "error": "invalid_token"}),
      401,
    )

  @jwt.unauthorized_loader
  def missing_token_callback(error):  
    return (
      jsonify({"message": "Request does not contain an access token.", "error": "authorization_required",}),
      401,
    )
  
  @jwt.additional_claims_loader
  def add_claims_to_jwt(identity):
    if identity == 1:
      return {"is_admin": True}
    return {"is_admin": False}

  api = Api(app)

  @app.before_first_request
  def create_tables():
  # with app.ap_context():
    db.create_all()

  api.register_blueprint(StoreBlueprint)
  api.register_blueprint(ItemBlueprint)
  api.register_blueprint(UserBlueprint)

  return app

