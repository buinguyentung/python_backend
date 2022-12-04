### MovieRepository: Interact with database for movie requests

import pymysql
import json


class MovieRepository():
  def getDbConnection(self):
    return pymysql.connect(
      host="localhost",
      db="TUNG_server",
      user="root",
      password="Testing123",
      charset="utf8",
      cursorclass=pymysql.cursors.DictCursor)


  def query_movies(self):
    connection = self.getDbConnection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM movie")
    movies = cursor.fetchall()
    print("[USER_REPOSITORY] ", movies)

    cursor.close()
    connection.close()

    return movies

  def insert_movie(self, movie):
    connection = self.getDbConnection()
    cursor = connection.cursor()
    
    sql = "INSERT INTO movie (name, casts, genres) VALUES (%s, %s, %s)"
    data = (movie["name"], json.dumps(movie["casts"]), json.dumps(movie["genres"]))
    cursor.execute(sql, data)
    result = connection.commit()
    print("[USER_REPOSITORY] Insert result = ", result)

    cursor.close()
    connection.close()

    return None

  def update_movie(self, movie):
    connection = self.getDbConnection()
    cursor = connection.cursor()

    sql = "UPDATE movie SET name=%s, casts=%s, genres=%s WHERE movie_id=%s"
    data = (movie["name"], json.dumps(movie["casts"]), json.dumps(movie["genres"]), movie["movie_id"])
    cursor.execute(sql, data)
    result = connection.commit()
    print("[USER_REPOSITORY] Insert result = ", result)

    cursor.close()
    connection.close()

    return None

  def delete_movie(self, movie_id):
    connection = self.getDbConnection()
    cursor = connection.cursor()

    sql = "DELETE FROM movie WHERE movie_id = %s"
    data = (movie_id,)
    cursor.execute(sql, data)
    result = connection.commit()
    print("[USER_REPOSITORY] Delete result = ", result)

    cursor.close()
    connection.close()

    return None