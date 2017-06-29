# Author: Peter Norvig
# 
# from: http://norvig.com/spell-correct.html
#

import re, collections

def words(text):
    return re.findall('[a-z]+', text.lower()) 

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

# a dictionary representing the frequency distribution of words in a
# biggish text file
NWORDS = train(words(file('big.txt').read()))

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
    """edits1 provides possible options for replacing wrong word"""
    """the splits varibale splits up into all possible splits"""
    """deletes every letter one at a time starting from first letter"""
    """transposes swaps the neighboring elements"""
    """substitutes every letter of the alphabet into each letter of word"""
    """inserts every letter of the alphabet in between all possible spaces of
    the word"""
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    """known_edits2 filters the correct word from the possible options in
    edits1"""
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(words): return set(w for w in words if w in NWORDS)
"""known"""
# This is the main function where the program would start.
def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=NWORDS.get)

