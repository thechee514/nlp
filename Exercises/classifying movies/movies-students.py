import random

import nltk
from nltk.corpus import movie_reviews

from nltk.corpus import stopwords
#from nltk.util import bigrams
#from nltk.corpus import wordnet as wn


#### Feature extraction
stopword_list = stopwords.words("english")
all_words = [w.lower() for w in movie_reviews.words() if w not in stopword_list]

# only use 2000 most common words
word_frequencies = nltk.FreqDist(all_words)
word_features = word_frequencies.keys()[:2000]

def document_features(document_words):
    document_words = set([w.lower() for w in document_words])
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


#### Preparing the training and test sets
negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')

# this takes time
negfeats = [(document_features(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(document_features(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
 
negcutoff = len(negfeats)*3/4
poscutoff = len(posfeats)*3/4

train_set = negfeats[:negcutoff] + posfeats[:poscutoff]
test_set = negfeats[negcutoff:] + posfeats[poscutoff:]

random.shuffle(train_set)
random.shuffle(test_set)


#### Building the classifier
# this takes time
classifier = nltk.NaiveBayesClassifier.train(train_set)


#### Evaluating the classifier

# this takes time
print nltk.classify.accuracy(classifier, test_set)

classifier.show_most_informative_features(20)
