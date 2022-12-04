### MovieController: The interface of movie APIs

from flask import Blueprint, request

from service.movie_service import MovieService

movie_api = Blueprint("Movies", __name__)
movie_service = MovieService()


# Get the list of movies
@movie_api.route('/movies', methods = ['GET'])
def get_movies():
  print("GET movies")
  try:
    return movie_service.get_movies()
  except Exception as e:
    print("[MOVIE_CONTROLLER] ERROR", e)
    return {"message": str(e)}, 500

# Create movie
@movie_api.route('/movie', methods = ['POST'])
def add_movie():
  print("POST movie")
  try:
    movie = request.get_json()
    print(movie)
    print(movie['name'], ' ', type(movie['name']))
    print(movie['casts'], ' ', type(movie['casts']))
    print(movie['genres'], ' ', type(movie['genres']))

    return movie_service.add_movie(movie)

  except Exception as e:
    print("[MOVIE_CONTROLLER] ERROR", e)
    return {"message": str(e)}, 500

# Edit movie
@movie_api.route('/movie/<int:index>', methods = ['PUT'])
def update_movie(index):
  print("PUT movie")
  try:
    print('movie_id = ', index)
    movie = request.get_json()
    movie["movie_id"] = index
    print(movie)
    
    return movie_service.update_movie(movie)

  except Exception as e:
    print("[MOVIE_CONTROLLER] ERROR", e)
    return {"message": str(e)}, 500

# Delete movie
@movie_api.route('/movie/<int:index>', methods = ['DELETE'])
def remove_movie(index):
  print("DELETE movie")
  try:
    print('movie_id = ', index)

    return movie_service.delete_movie(index)

  except Exception as e:
    print("[MOVIE_CONTROLLER] ERROR", e)
    return {"message": str(e)}, 500