import nltk
import numpy as np


def predict_intent(sentence):
    
    classes=["greeting", "goodbye", "year", "length", "plot", "director", "genres", "cast", "similar", "recommendations", "poster", "director_movies", "actor_movies", "rating"]
    
    topic_greeting={"greeting":["hi","hey","new","hello","day","whats", "up","good","you","doing"]}
    
    topic_goodbye={"goodbye":["bye","cya","ciao","later","goodbye","leaving","leave","good", "day","well"]}
    
    topic_year={"year":["when","year","released","come out"]}
    
    topic_length={"length":["long", "time", "duration", "length"]}
    
    topic_plot={"plot":["plot", "about", "synopsis", "storyline", "scenario", "summary", "overview", "pitch"]}
    
    topic_director={"director":["who", "director", "directed", "producer", "produced", "filmmaker", "made", "author"]}
                   
    topic_genres={"genres":["genres", "genre", "which", "categories", "category", "kind", "aventure", "action", "drama", "thriller", "comedy"]}

    topic_cast={"cast":["casting", "cast", "who", "actors", "actor", "persons", "star", "stars", "famous", "character", "characters", "main", "personality"]}
    
    topic_similar={"similar":["similar", "likewise", "related", "same", "ressembling"]}
    
    topic_recommendations={"recommendations":["recommend", "recommendations", "recommendation", "other", "same", "like"]}
    
    topic_poster={"poster":["poster","show","display","image","picture"]}
    
    topic_director_movies={"director_movies":["directed", "directed by", "made", "made by", "produced", "produced by", "movies", "films"]}
    
    topic_actor_movies={"actor_movies":["featuring", "appear", "feature", "playing", "movies", "films"]}
    
    topic_rating={"rating":["rating", "ratings", "rated", "average", "score"]}


    topic=[topic_greeting,topic_goodbye,topic_year,topic_length,topic_plot,topic_director,topic_genres,topic_cast,topic_similar,topic_recommendations,topic_poster,topic_director_movies,topic_actor_movies,topic_rating]

    sentence_words = [word.lower() for word in nltk.word_tokenize(sentence)]
    
    scores=[]

    for i, c in enumerate(classes):
        count = 0
        words = topic[i][c]
        for word in sentence_words:
            count += words.count(word.lower())
        scores.append(count)
        
    return classes[np.argmax(scores)]