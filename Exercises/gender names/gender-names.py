import nltk
from nltk.corpus import names
import random

## create feature set
def gender_features(word):
    feature_dictionary = {'last_letter': word[-1],'first_letter': word[0], 'second_last': word[-2], 'word_length': len(word)}
    return feature_dictionary
#print gender_features("Kristina")


## prepare data sets for training and testing
name_gender_pairs = ([(name, 'male') for name in names.words('male.txt')] +
                     [(name, 'female') for name in names.words('female.txt')])
random.shuffle(name_gender_pairs)
#print name_gender_pairs[:10]

featuresets = [(gender_features(n), g) for (n,g) in name_gender_pairs]
train_set, test_set = featuresets[500:], featuresets[:500]


## train classifier
classifier = nltk.NaiveBayesClassifier.train(train_set)


## use classifier
# print classifier.classify(gender_features('Neo'))
# print classifier.classify(gender_features('Trinity'))


## analyze classifier
# print nltk.classify.accuracy(classifier, test_set)
# classifier.show_most_informative_features(5)
