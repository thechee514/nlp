# Vincent Chee
# 17/04/15
# Program finds out how many word types account for a third of all word tokens.

import nltk
from nltk.corpus import brown


def teen_language():
    """This function creates a frequency distribution of the words placing them
    in order then it finds out how many word types account for a third of all
    word tokens, for a variety of text sources provided by the brown corpus."""
    cfd = nltk.FreqDist(brown.words())
    cumulative = 0
    rank = 0
    words = brown.words()
    target_words = []
    while cumulative <= len(words)/3:
        if words[rank].isalpha():
            cumulative += cfd[brown.words()[rank]]
            if words[rank].lower() not in target_words:
                target_words.append(words[rank].lower())
                print words[rank].lower()
        rank += 1
    return target_words

teen_language()
