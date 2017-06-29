# Vincent Chee
# 24/04/15
# Program measures readability and determines ARI 

import nltk
from nltk.corpus import brown

def calculated_ari():
    """Calculates ARI based on mean word length and mean sentence length"""
    for genre in brown.categories():
        num_chars = len(brown.raw(categories = genre))
        num_words = len(brown.words(categories = genre))
        num_sents = len(brown.sents(categories = genre))
        mean_word_length = num_chars/num_words
        mean_sent_length =  num_words / num_sents
        ari = 4.71 * mean_word_length + 0.5 * mean_sent_length - 21.43
        print mean_word_length, mean_sent_length, genre, ari
print calculated_ari()
