#movie-bag/app.py

from flask import Flask #, jsonify, request
# import pymysql
# import json

from controller.movie_controller import movie_api

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route('/')
def hello():
  return {"hello": "world"}

app.register_blueprint(movie_api)
