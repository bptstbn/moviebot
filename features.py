from api import *

def year_response(movie):
    id = get_id(movie)
    title = get_title(id)
    year = get_year(id)
    return "{0} was released in {1}".format(title, year)

def length_response(movie):
    id = get_id(movie)
    title = get_title(id)
    year = get_length(id)
    return "{0} is {1} long".format(title, year)

def plot_response(movie):
    id = get_id(movie)
    title = get_title(id)
    plot = get_plot(id)
    return "Here is a brief synopsis of {0} :\n{1}".format(title, plot)


def director_response(movie):
    id = get_id(movie)
    title = get_title(id)
    director = get_director(id)
    return "The director of {0} is {1}".format(title, director)


def genres_response(movie):
    id = get_id(movie)
    title = get_title(id)
    genres = get_genres(id)
    return "{0} belongs to the following genres : {1}".format(title, genres)


def cast_response(movie):
    id = get_id(movie)
    title = get_title(id)
    cast = get_cast(id)
    return "Here is the cast of {0} (Actor : Character) :\n{1}".format(title, cast)

def similar_response(movie):
    id = get_id(movie)
    title = get_title(id)
    similar = get_similar(id)
    return "Here are some films which are similar to {0} :\n{1}".format(title, similar)

def recommendations_response(movie):
    id = get_id(movie)
    title = get_title(id)
    recommendations = get_recommendations(id)
    return "Here are some recommendations if you liked {0} :\n{1}".format(title, recommendations)

def poster_response(movie):
    id = get_id(movie)
    link = get_poster(id)
    image = requests.get(link, allow_redirects = True)
    extension = link.split(".")[-1]
    path = "temp/poster.{0}".format(extension)
    open(path, 'wb').write(image.content)
    return path


def director_movies_response(person):
    id = get_person_id(person)
    name = get_name(id)
    works = get_director_movies(id)
    return "Here are some films directed by {0} :\n{1}".format(name, works)

def actor_movies_response(person):
    id = get_person_id(person)
    name = get_name(id)
    works = get_actor_movies(id)
    return "Here are some movies which feature {0} :\n{1}".format(name, works)

def rating_response(movie):
    id = get_id(movie)
    title = get_title(id)
    rating = get_rating(id)
    return  "{0} has an average rating of {1}".format(title, rating)
