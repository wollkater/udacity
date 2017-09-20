import json

import website
from models.movie import Movie

movies = []

for json_movie in json.load(open("./data/movies.json")):
    movies.append(
        Movie(
            json_movie['title'],
            json_movie['story_line'],
            json_movie['trailer_youtube_url'],
            json_movie['poster_image_url']
        )
    )
# generates and opens the html page with the movies
website.open_movies_page(movies)
