import nltk
from nltk.corpus import names
import random

## create feature set
def gender_features(word):
    feature_dictionary = {'last_letter': word[-1]}
    return feature_dictionary
#print gender_features("Kristina")


## prepare data sets for training and testing
name_gender_pairs = ([(name, 'male') for name in names.words('male.txt')] +
                     [(name, 'female') for name in names.words('female.txt')])
random.shuffle(name_gender_pairs)
#print names[:10]

featuresets = [(gender_features(n), g) for (n,g) in name_gender_pairs]
train_set, dev_test_set, test_set = featuresets[1000:], featuresets[500:1000], featuresets[:500]
train_names, dev_test_names, test_names = name_gender_pairs[1000:], name_gender_pairs[500:1000], name_gender_pairs[:500]


## train classifier
classifier = nltk.NaiveBayesClassifier.train(train_set)


## analyze classifier
print nltk.classify.accuracy(classifier, dev_test_set)

errors = []
for (name, tag) in dev_test_names:
    guess = classifier.classify(gender_features(name))
    if guess != tag:
        errors.append( (tag, guess, name) )

for (tag, guess, name) in sorted(errors): 
    print 'correct=%-8s guess=%-8s name=%-30s' % (tag, guess, name)
