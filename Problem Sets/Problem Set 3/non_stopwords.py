# Vincent Chee
# 17/04/15
# Program returns 50 most frequently occurring non-stopwords in a text.
import nltk
from nltk.corpus import stopwords
from nltk.corpus import gutenberg
def non_stopwords(textfile):
""" This function finds the 50 most frequently occurring words of a text that
    are not stopwords. The function takes a text as its parameter and returns
    its results as a list. """
    stopwords = nltk.corpus.stopwords.words('english')
    filtered_words = [w for w in textfile if w.lower() not in stopwords]
    freq = nltk.probability.FreqDist(filtered_words)
    return filtered_words[:50]

print non_stopwords(gutenberg.words('austen-emma.txt'))

