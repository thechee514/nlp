# Vincent Chee
# 17/04/15
# Program creates a table of word frequencies by genre.

import nltk
from nltk.corpus import brown
def genres():
    """This function uses an nltk function to first get the frequency
    distribution of several words under specified genres and then tabulates the
    results."""
    cfd = nltk.ConditionalFreqDist(
        (genre, word)
        for genre in brown.categories()
        for word in brown.words(categories=genre))
    genres = ['news', 'religion', 'hobbies', 'romance', 'humor']
    words = ['president', 'God', 'sports', 'love', 'funny']
    cfd.tabulate(conditions=genres, samples=words)

genres()
