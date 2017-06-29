###
### Author: Kristina Striegnitz
### Version: Spring 2012
### Reusing code from Wikipedia: http://en.wikipedia.org/wiki/Viterbi_algorithm
### License: Creative Commons Attribution-ShareAlike License
###          http://en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License
###
 
def viterbi(obs, states, start_p, trans_p, emit_p, pretty_print=False):
    """
    The Viterbi algorithm. Calculates what sequence of states is most
    likely to produce the given sequence of observations.

    V is the main data structure that represents the trellis/grid of
    Viterbi probabilities. It is a list of dictionaries. Each element
    of the list is a dictionary and represents one step in the
    sequence or one column of nodes in the trellis graph.

    The variable 'path' maintains the currently most likely path. For
    example, once we have finished processing the third observation,
    then 'path' contains for each possible state, the currently most
    likely path that leads to that state. 'path' is a dictionary with
    one entry for each possible state. And each value is a list of
    states, representing the most likely sequence of states leading to
    the state represented by the key.
    """
    V = [{}]
    path = {}
 
    # Calculate the Viterbi probabilities for the first step, i.e.,
    # the first observation: t = 0.
    for y in states:
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]
 
    # Run Viterbi for all of the subsequent steps/observations: t > 0.
    for t in range(1,len(obs)):
        V.append({})
        newpath = {}

        # For every state, calculate the Viterbi probability of being
        # in that state at time t and the most likely previous state.
        for y in states:
            prob = 0
            prev_state = None
            for p in states:
                prob_p = trans_p[p][y] * emit_p[y][obs[t]] * V[t-1][p]
                if prob_p > prob:
                    prob = prob_p
                    prev_state = p
                    
            V[t][y] = prob 
            newpath[y] = path[prev_state] + [y]

        # Don't need to remember the old paths
        path = newpath

    if pretty_print:
        pretty_print_trellis(V)
    (prob, state) = max([(V[len(obs) - 1][y], y) for y in states])
    return (prob, path[state])


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
## Example HMM specification
###

states = ('Hot', 'Cold')
  
start_probability = {'Hot': 0.8, 'Cold': 0.2}
 
transition_probability = {
   'Hot' : {'Hot': 0.7, 'Cold': 0.3},
   'Cold' : {'Hot': 0.4, 'Cold': 0.6},
   }
 
emission_probability = {
   'Hot' : {'1': 0.2, '2': 0.4, '3': 0.4},
   'Cold' : {'1': 0.5, '2': 0.4, '3': 0.1},
   }

###
## Run on example observations
###

def run_example(observations,pretty_print=True):
    return viterbi(observations,
                   states,
                   start_probability,
                   transition_probability,
                   emission_probability,
                   pretty_print)

print run_example(('3', '1', '3'))
