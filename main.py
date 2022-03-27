import discord
from predict import predict_intent
from features import *
from keep_alive import keep_alive

import os
token = os.environ['token']

client = discord.Client()


import pickle
import itertools

filehandler = open('movies.pck', 'rb')     
movies = pickle.load(filehandler)

def extract_movie(sentence):
    words = sentence.lower().split(' ')
    chains = [(" ").join(words[i:j]) for i, j in itertools.combinations(range(len(words) + 1), 2)]
    res = list(filter(lambda chain: chain in movies, chains))
    if len(res) != 0:
        return res[0]
    else:
        return None

def extract_person(sentence):
    text = ner(sentence)
    res = [x for x in text.ents if x.label_ == 'PERSON'][0]
    if len(res) != 0:
        return res[0]
    else:
        return None

@client.event
async def on_ready():
    print("The Movie Chatbot is ready !")

@client.event
async def on_member_join(member):
    general_channel = client.get_channel(942783658413146165)
    general_channel.send(f"Welcome in the server {member.display_name} !")



async def respond(message, intent):
    if intent == 'greeting':
        res = 'Hello there'
    elif intent == 'year':
        movie = extract_movie(message.content)
        logging.debug('The movie extracted from the sentence is : {0}'.format(movie))
        res = year_response(movie)
    elif intent == 'length':
        movie = extract_movie(message.content)
        res = length_response(movie)
    elif intent == 'plot':
        movie = extract_movie(message.content)
        res = plot_response(movie)
    elif intent == 'director':
        movie = extract_movie(message.content)
        res = director_response(movie)
    elif intent == 'cast':
        movie = extract_movie(message.content)
        res = cast_response(movie)
    elif intent == 'rating':
        movie = extract_movie(message.content)
        res = rating_response(movie)
    elif intent == 'similar':
        movie = extract_movie(message.content)
        res = similar_response(movie)
    elif intent == 'recommendations':
        movie = extract_movie(message.content)
        res = recommendations_response(movie)
    elif intent == 'poster':
        movie = extract_movie(message.content)
        path = poster_response(movie)
        with open(path, "rb") as filehandler:
            extension = path.split(".")[-1]
            f = discord.File(filehandler, filename = 'poster.{0}'.format(extension))
            await message.channel.send(file = f)
        return
    elif intent == 'director_movies':
        person = extract_person(message.content)
        res = director_movies_response(person)
    elif intent == 'actor_movies':
        person = extract_person(message.content)
        res = actor_movies_response(person)
    else:
        res = "Could you please rephrase what you've just said ?"
    await message.channel.send(res)


import logging
logging.basicConfig(level=logging.DEBUG)

@client.event
async def on_message(message):
    """
        Function for the chatbot to respond

    """
    if message.author == client.user:
        return
    
    logging.debug('The following message has been received : {0}'.format(message.content))

    # intent = predict_intent(message.content)
    intent = predict_intent(message.content)
    logging.debug('The predicted intent is : {0}'.format(intent))
    
    await respond(message, intent)
    
keep_alive()
client.run(token)