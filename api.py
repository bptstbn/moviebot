import requests
import pandas as pd

import os
tmdb_key = os.environ['tmdb_key']

tmdb_url = "https://api.themoviedb.org/3"


def get_id(search):
    url = "{0}/search/movie?api_key={1}&query={2}".format(tmdb_url, tmdb_key, search)
    return requests.get(url).json()['results'][0]['id']

def get_details(movie_id):
    url = "{0}//movie/{2}?api_key={1}".format(tmdb_url, tmdb_key, movie_id)
    return requests.get(url).json()

def get_person_id(search):
    url = "{0}/search/person?api_key={1}&query={2}".format(tmdb_url, tmdb_key, search)
    return requests.get(url).json()['results'][0]['id']

def get_name(person_id):
    url = "{0}/person/{2}?api_key={1}".format(tmdb_url, tmdb_key, person_id)
    return requests.get(url).json()['name']

def get_title(movie_id):
    return get_details(movie_id)['title']

def get_year(movie_id):
    return get_details(movie_id)['release_date'][:4]

def get_length(movie_id):
    runtime = get_details(movie_id)['runtime']
    t = pd.to_datetime(runtime, unit = 'm')
    return "{0}h {1}min".format(t.hour, t.minute)

def get_plot(movie_id):
    return get_details(movie_id)['overview']

def get_genres(movie_id):
    res = get_details(movie_id)['genres']
    res = [x['name'] for x in res]
    return ", ".join(res)

def get_director(movie_id):
    url = "{0}//movie/{2}/credits?api_key={1}".format(tmdb_url, tmdb_key, movie_id)
    res = requests.get(url).json()['crew']
    res = list(filter(lambda x: x['job'] == 'Director', res))[0]
    return res['name']

def get_cast(movie_id):
    url = "{0}//movie/{2}/credits?api_key={1}".format(tmdb_url, tmdb_key, movie_id)
    res = requests.get(url).json()['cast']
    res = [(x['name'], x['character']) for x in res]
    res = [" : ".join(x) for x in res]
    return "\n".join(res[:10])

def get_similar(movie_id):
    url = "{0}//movie/{2}/similar?api_key={1}".format(tmdb_url, tmdb_key, movie_id)
    res = requests.get(url).json()['results']
    res = [x['title'] for x in res]
    return "\n".join(res[:5])

def get_recommendations(movie_id):
    url = "{0}//movie/{2}/recommendations?api_key={1}".format(tmdb_url, tmdb_key, movie_id)
    res = requests.get(url).json()['results']
    res = [x['title'] for x in res]
    return "\n".join(res[:5])

def get_poster(movie_id):
    root_path = "https://image.tmdb.org/t/p/original/"
    poster_path = get_details(movie_id)['poster_path']
    link = root_path + poster_path
    return link
    
def get_director_movies(person_id):
    url = "{0}/person/{2}/movie_credits?api_key={1}".format(tmdb_url, tmdb_key, person_id)
    res = requests.get(url).json()['crew']
    res = list(filter(lambda x: x['job'] == 'Director', res))
    res = [x['title'] for x in res]
    return "\n".join(res[:7])

def get_actor_movies(person_id):
    url = "{0}/person/{2}/movie_credits?api_key={1}".format(tmdb_url, tmdb_key, person_id)
    res = requests.get(url).json()['cast']
    res = [x['title'] for x in res]
    return "\n".join(res[:7])

def get_rating(movie_id):
    return get_details(movie_id)['vote_average']
