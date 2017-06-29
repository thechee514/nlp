###
### Author: Kristina Striegnitz
### Version: Fall 2010
### Reusing code from Wikipedia: http://en.wikipedia.org/wiki/Viterbi_algorithm
### License: Creative Commons Attribution-ShareAlike License
###          http://en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License
###

import nltk, math
from nltk.corpus import brown


def viterbi(obs, states, start_p, trans_p, emit_p, pretty_print=False):
    """
    The Viterbi algorithm. Calculates what sequence of states is most
    likely to produce the given sequence of observations.

    The function is working with the log of probabilities instead of
    the probabilities themselves in order to avoid underflow; i.e.,
    the situation where the probabilities get so small that they are
    smaller than the smallest value greater than 0 that Python can
    represent.
    """
    V = [{}] # the Viterbi probabilities
    path = {} # the most likely path
 
    # Calculate the Viterbi probabilities for the first step, i.e.,
    # the first observation: t = 0.
    for y in states:
        V[0][y] = log(start_p[y]) + log(emit_p[y][obs[0]])
        path[y] = [y]
 
    # Run Viterbi for all of the subsequent steps/observations: t > 0.
    for t in range(1,len(obs)):
        V.append({})
        newpath = {}

        # For every state, calculate the Viterbi probability of being
        # in that state at time t and the most likely previous state.
        for y in states:

            (prob, prev_state) = max([(V[t-1][y0] + log(trans_p[y0][y]) + log(emit_p[y][obs[t]]), y0) for y0 in states])
            V[t][y] = prob
            newpath[y] = path[prev_state] + [y]
 
        # Don't need to remember the old paths
        path = newpath

    if pretty_print:
        pretty_print_trellis(V)
    (prob, state) = max([(V[len(obs) - 1][y], y) for y in states])
    return (prob, path[state])



def log (number):
    """
    Returns the log of a number or Python's expression for negative
    infinity, if the number is 0.
    """
    if number != 0.0:
        return math.log (number)
    else:
        return float('-inf')



def pretty_print_trellis(V):
    print "    ",
    for i in range(len(V)): print "%7s" % ("%d" % i),
    print
 
    for y in V[0].keys():
        print "%.5s: " % y,
        for t in range(len(V)):
            print "%.7s" % ("%f" % V[t][y]),
        print
 
###
## Example HMM specification for a part of speech tagging HMM.
##
## The start-, transition-, and emission probabilities are computed
## based on NLTK's brown corpus.
###

tagged_words = brown.tagged_words(tagset='universal')
states = set([tag for (word, tag) in tagged_words])

tags = [t for (w,t) in brown.tagged_words(tagset='universal')]
tag_tag_pairs = nltk.bigrams(tags)
transition_freq = nltk.ConditionalFreqDist(tag_tag_pairs)

start_probability = {}
for state in states:
    start_probability[state] = transition_freq['.'].freq(state)
 
transition_probability = {}
for state in states:
    transition_probability[state] = {}
    for next_state in states:
        transition_probability[state][next_state] = transition_freq[state].freq(next_state)

tag_word_pairs = [(tag, word.lower()) for (word, tag) in tagged_words]
observation_freq = nltk.ConditionalFreqDist(tag_word_pairs)
words = set([w for (tag, w) in tag_word_pairs])
emission_probability = {}
for state in states:
    emission_probability[state] = {}
    for word in words:
        if word in observation_freq[state]:
            emission_probability[state][word] = observation_freq[state].freq(word)
        else:
            emission_probability[state][word] = 0.0


###
## Run on example observations
###

def run_example(string, pretty_print=True):
    observations = [w.lower() for w in string.split()]
    print observations
    return viterbi(observations,
                   states,
                   start_probability,
                   transition_probability,
                   emission_probability,
                   pretty_print)


print run_example("The quick brown fox jumps over the lazy dog .")

# to suppress the output of the trellis:
# print run_example("Peter likes to eat cake .", pretty_print=False)
