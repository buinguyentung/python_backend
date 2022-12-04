#movie-bag/app.py
#Original code that interacting with database without any layers.

from flask import Flask, jsonify, request
import pymysql
import json

app = Flask(__name__)

def getDbConnection():
  return pymysql.connect(
    host="localhost",
    db="TUNG_server",
    user="root",
    password="Testing123",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def hello():
  return {"hello": "world"}

@app.route('/movies')
def get_movies():
  connection = getDbConnection()
  cursor = connection.cursor()
  
  cursor.execute("SELECT * FROM movie")
  movies = cursor.fetchall()
  print(movies)

  cursor.close()
  connection.close()

  return jsonify(movies)

@app.route('/movie', methods = ['POST'])
def add_movie():
  movie = request.get_json()
  print(movie)
  print(movie['name'], ' ', type(movie['name']))
  print(movie['casts'], ' ', type(movie['casts']))
  print(movie['genres'], ' ', type(movie['genres']))
  
  connection = getDbConnection()
  cursor = connection.cursor()
  
  sql = "INSERT INTO movie (name, casts, genres) VALUES (%s, %s, %s)"
  data = (movie['name'], json.dumps(movie['casts']), json.dumps(movie['genres']))
  cursor.execute(sql, data)
  result = connection.commit()
  print('result = ', result)

  cursor.close()
  connection.close()

  return {'message': 'SUCCESS'}, 200

@app.route('/movie/<int:index>', methods = ['PUT'])
def update_movie(index):
  print('index = ', index)
  movie = request.get_json()
  print(movie)

  connection = getDbConnection()
  cursor = connection.cursor()

  sql = "UPDATE movie SET name=%s, casts=%s, genres=%s WHERE movie_id=%s"
  data = (movie['name'], json.dumps(movie['casts']), json.dumps(movie['genres']), index)
  print('sql: ', sql)
  cursor.execute(sql, data)
  result = connection.commit()

  return {'message': 'SUCCESS'}, 200

@app.route('/movie/<int:index>', methods = ['DELETE'])
def remove_movie(index):
  print('index = ', index)
  movies.pop(index)
  return {'message': 'SUCCESS', "updated_movie": movies}, 200

# app.run()
