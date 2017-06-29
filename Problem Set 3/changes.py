# Vincent Chee
# 17/04/15
# Program counts the occurrences of men, women, and people in each State of the
# Union address and prints out the results
import nltk
from nltk.corpus import state_union
def changes():
    """Function counts occurrences of men, women and people in State of the
    Union addresses."""
    print "m w p"
    for fileid in state_union.fileids():
        words = [word.lower() for word in state_union.words(fileid)]
        men = words.count('men')
        women = words.count('women')
        people = words.count('people')
        print men,women,people
changes()
