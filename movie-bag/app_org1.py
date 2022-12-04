#movie-bag/app.py
#Without any database

from flask import Flask, jsonify, request

app = Flask(__name__)

#List of movies
movies = [
  {
    "name": "The Shawshank Redemption",
    "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
    "genres": ["Drama"]
  },
  {
    "name": "The Godfather",
    "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
    "genres": ["Crime", "Drama"]
  }
]

@app.route('/')
def hello():
  return {"hello": "world"}

@app.route('/movies')
def get_movies():
  print(movies)
  return jsonify(movies)

@app.route('/movies', methods = ['POST'])
def add_movie():
  movie = request.get_json()
  movies.append(movie)
  print(movies)
  return {'message': 'SUCCESS', "id": len(movies) - 1}, 200

@app.route('/movies/<int:index>', methods = ['PUT'])
def update_movie(index):
  print('index = ', index)
  movie = request.get_json()
  movies[index] = movie
  print(jsonify(movies[index]))
  return {'message': 'SUCCESS', "updated_movie": movies[index]}, 200

@app.route('/movies/<int:index>', methods = ['DELETE'])
def remove_movie(index):
  print('index = ', index)
  movies.pop(index)
  return {'message': 'SUCCESS', "updated_movie": movies}, 200

app.run()
