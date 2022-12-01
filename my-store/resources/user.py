from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256 #For password hashing
from flask_jwt_extended import create_access_token #For login
from flask_jwt_extended import jwt_required #For route protection

# flask-sqlalchemy
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from db import db
from models import UserModel
from schemas import UserSchema

blp = Blueprint("Users", "users", description="Operations on users")

@blp.route("/register")
class UserRegister(MethodView):
  @jwt_required()
  @blp.arguments(UserSchema)
  def post(self, user_data):
    if UserModel.query.filter(UserModel.username == user_data["username"]).first():
      abort(400, message="User already exists")
    
    user = UserModel(
      username = user_data["username"],
      password = pbkdf2_sha256.hash(user_data["password"])
    )
    db.session.add(user)
    db.session.commit()

    return {"message": "User created successfully"}, 201

@blp.route("/users")
class UserList(MethodView):
  @jwt_required()
  @blp.response(200, UserSchema(many=True))
  def get(self):
    #Authorization
    # jwt = get_jwt()
    # print(jwt)
    # if not jwt.get("is_admin"):
    #   abort(401, message="Admin privilege required.")
    return UserModel.query.all()

@blp.route("/user/<int:user_id>")
class User(MethodView):
  """
  This resource can be useful when testing our Flask app.
  We may not want to expose it to public users, but for the
  sake of demonstration in this course, it can be useful
  when we are manipulating data regarding the users.
  """
  @jwt_required()
  @blp.response(200, UserSchema)
  def get(self, user_id):
      user = UserModel.query.get_or_404(user_id)
      return user

  @jwt_required()
  def delete(self, user_id):
      user = UserModel.query.get_or_404(user_id)
      db.session.delete(user)
      db.session.commit()
      return {"message": "User deleted."}, 200

@blp.route("/login")
class UserLogin(MethodView):
  @blp.arguments(UserSchema)
  def post(self, user_data):
    user = UserModel.query.filter(UserModel.username == user_data["username"]).first()
    
    if not user:
      abort(400, message="User does not exist")
    
    if pbkdf2_sha256.verify(user_data["password"], user.password):
      # access_token = create_access_token(identity=user.id)
      access_token = create_access_token(
        identity={
          "username": user.username,
          "id": user.id,
          "role": "admin"
        }
      )
      return {"access_token": access_token}, 200
    
    abort(401, message="Invalid password")