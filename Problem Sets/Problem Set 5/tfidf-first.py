## Kristina Striegnitz, modified by Vincent Chee
##
## 04/05/15
##
## Retrieve documents relevant to a given keyword from a collection of
## articles using tf-idf scoring. Modified to exclude stopwords. 
##

import nltk
import math
import re
import timeit

def create_idf_index (corpus):
    """
    create inverted index
    """
    stopwords = nltk.corpus.stopwords.words('english')

    params = []
    for doc in corpus.fileids():
        for word in corpus.words(doc):
            c = clean_word(word)
            if c not in stopwords and c:
                params.append((c, doc))

    idf_index = nltk.ConditionalFreqDist(p for p in params)
    return idf_index


def clean_word (word):
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
    stopwords = nltk.corpus.stopwords.words('english')
    initial_query = query.split()
    filtered_query = exclude(initial_query, stopwords)
    keys = set(filtered_query)
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

def exclude (word_list_source, word_list_complement):
    '''returns a sublist of source that is disjoint from complement'''
    to_return = []
    for word in word_list_source:
        if not word in word_list_complement:
            to_return.append(word)
    return to_return

##---------------- main ------------------------------------------------- 

from nltk.corpus import PlaintextCorpusReader
corpus_root = '/Users/thechee514/Google Drive/Union/2 Sophomore Year/3Spring Semester/Natural Language Processing/Exercises/tfidf/wikipedia-preprocessed-step-2'

# full set
wiki = PlaintextCorpusReader(corpus_root, 'doc.*\.txt')

## example retrieval
idf_index = create_idf_index (wiki)
pretty_print_results ( retrieve("hippocratic oath", wiki, idf_index), wiki)
start=timeit.default_timer()
results=retrieve("hippocratic oath", wiki, idf_index)
stop = timeit.default_timer()
print stop-start
