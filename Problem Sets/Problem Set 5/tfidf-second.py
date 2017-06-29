## Kristina Striegnitz, modified by Vincent Chee
##
## 04/05/15
##
## Retrieve documents relevant to a given keyword from a collection of
## articles using tf-idf scoring. Modified to use stemmer to reduce words to
## their stems.
##

import nltk
import math
import re
import timeit

def create_idf_index (corpus):
    """
    create inverted index
    """
    idf_index = nltk.ConditionalFreqDist((clean_word(word), doc) \
                                         for doc in corpus.fileids() \
                                         for word in corpus.words(doc) if clean_word(word))
    return idf_index


def clean_word (word):
    lancaster = nltk.LancasterStemmer()
    word = lancaster.stem(word)
    match = re.search('(\w+)', word.lower())
    if match:
        return match.group(0)
    else:
        return None


def calculate_tfidf (key, docid, idf_index, corpus):
    """
    calculate tfidf score for given idf_index, doc, and keyword
    """
    doc_count = len(idf_index[key])
    idf = math.log(float(len(corpus.fileids()))/float(doc_count+1))

    words = corpus.words(docid)
    key_count_in_doc = idf_index[key][docid]
    tf = float(key_count_in_doc) / float(len(words))

    return tf * idf

    
def retrieve (query, corpus, idf_index):
    """
    find top 10 doc with best tfidf score for the given query
    """
    lancaster = nltk.LancasterStemmer()
    keys = set([lancaster.stem(w) for w in query.split()])

    results = []
    relevant_docs = set([doc for key in keys for doc in idf_index[key].keys()])
    print "RELEVANT DOCS:", len(relevant_docs)
    for doc in relevant_docs:
        tfidf_doc = [calculate_tfidf(key, doc, idf_index, corpus) for key in keys]       
        results.append((sum(tfidf_doc), doc, tfidf_doc))

    results.sort()
    return results[-10:]


def pretty_print_results (results, corpus):
    """
    print first few words of each document in results
    """
    for (tfidf_sum, docid, tfidf_scores) in results:
        print docid
        print corpus.words(docid)[:50]
        print tfidf_sum
        print tfidf_scores
        print

##---------------- main ------------------------------------------------- 

from nltk.corpus import PlaintextCorpusReader
corpus_root = '/Users/thechee514/Google Drive/Union/2 Sophomore Year/3Spring Semester/Natural Language Processing/Exercises/tfidf/wikipedia-preprocessed-step-2'

# full set
wiki = PlaintextCorpusReader(corpus_root, 'doc.*\.txt')

## example retrieval
idf_index = create_idf_index (wiki)
pretty_print_results ( retrieve("binary code", wiki, idf_index), wiki)
start=timeit.default_timer()
results=retrieve("binary code", wiki, idf_index)
stop = timeit.default_timer()
print stop-start
