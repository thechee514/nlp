# Vincent Chee
# 24/04/15
# Program normalizes some tokenized text

import nltk
from nltk.corpus import brown
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()

def stemmers(text):
    """Calls stemmer on each word of some sort of text."""
    text = tokens = nltk.word_tokenize(text)
    print [porter.stem(t) for t in tokens]
    print [lancaster.stem(t) for t in tokens]

stemmers("""DENNIS: Listen, strange women lying in ponds distributing swords
is no basis for a system of government.  Supreme executive power derives from
a mandate from the masses, not from some farcical aquatic ceremony.""")
