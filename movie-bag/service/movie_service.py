### MovieService: Handle logic processing for movie requests

from flask import jsonify
from repository.movie_repository import MovieRepository

movie_repository = MovieRepository()

class MovieService():
  def get_movies(self):
    try:
      movies = movie_repository.query_movies()
      return {"message": "SUCCESS", "result": movies}, 200
    except Exception as e:
      print("[MOVIE_SERVICE] ERROR", e)
      return {"message": str(e)}, 500

  def add_movie(self, movie):
    try:
      movie_repository.insert_movie(movie)
      return {"message": "SUCCESS"}, 200
    except Exception as e:
      print("[MOVIE_SERVICE] ERROR", e)
      return {"message": str(e)}, 500

  def update_movie(self, movie):
    try:
      movie_repository.update_movie(movie)
      return {"message": "SUCCESS"}, 200
    except Exception as e:
      print("[MOVIE_SERVICE] ERROR", e)
      return {"message": str(e)}, 500

  def delete_movie(self, movie_id):
    try:
      movie_repository.delete_movie(movie_id)
      return {"message": "SUCCESS"}, 200
    except Exception as e:
      print("[MOVIE_SERVICE] ERROR", e)
      return {"message": str(e)}, 500
