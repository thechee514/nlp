import nltk
from nltk.corpus import stopwords
from nltk.corpus import gutenberg
def non_stopwords(textfile):
    stopwords = nltk.corpus.stopwords.words('english')
    filtered_words = [w for w in textfile if w.lower() not in stopwords]
    freq = nltk.probability.FreqDist(filtered_words)
    return filtered_words[:50]

print non_stopwords(gutenberg.words('austen-emma.txt'))
