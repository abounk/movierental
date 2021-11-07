import csv
from movie import Movie


class MovieCatalog:

    def __init__(self, movies_file='movies.csv'):
        file = open(movies_file, "r")
        self.movies = (movie for movie in csv.DictReader(file))

    def get_movie(self, title):
        for movie in self.movies:
            if movie['title'] == title:
                return Movie(movie['title'], movie['year'], movie['genres'])
