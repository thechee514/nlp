###################
#
# Starter code for a program that trains a classifier to determine the
# production category of items being reviewed based on the review
# text.
#
# Kristina Striegnitz
# Spring 2015
#
###################

import random

import nltk
from nltk.corpus import stopwords


#### Read in corpus

f = open("cats_sh.txt")
all_docs = []
all_words = []
categories = []
for line in f:
    ts = line.strip().split()
    words = ts[1:]
    category = ts[0]
    
    ## Different product categories
    if category not in categories:
        categories.append(category)
        
    all_docs.append((words, category))
    all_words += words
f.close()
print 'Total number of docs:', len(all_docs)
print 'Total number of words:', len(all_words)
print 'Categories:', categories

#### Feature extraction
stopword_list = stopwords.words("english")
all_words = [w.lower() for w in all_words if w not in stopword_list]

word_frequencies = nltk.FreqDist(all_words)
word_features = word_frequencies.keys()[:2000]

def document_features(document_words):
    document_words = set([w.lower() for w in document_words])
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


#### Preparing the training and test sets

random.shuffle(all_docs)

# this takes time
docs_as_features = [(document_features(words), category) for (words, category) in all_docs]

train_set = docs_as_features[2000:]
test_set = docs_as_features[:2000]


#### Training a classifier
classifier = nltk.NaiveBayesClassifier.train(train_set)

#### Evaluating the classifier
print nltk.classify.accuracy(classifier, test_set)

classifier.show_most_informative_features(20)

