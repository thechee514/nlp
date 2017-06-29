import nltk

groucho_grammar = nltk.CFG.fromstring("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | PN | Det Adj N
VP -> V NP | VP PP
Det -> 'an' | 'my'
N -> 'elephant' | 'pajamas'
V -> 'snorted'
P -> 'in'
AdjP -> Adj AdjP | Adj
Adj -> 'big' | 'long' | 'green'
""")

sent = "a big elephant with a long trunk snorted"

parser = nltk.ChartParser(groucho_grammar)
parse_results = parser.parse(sent.split())

for tree in parse_results:
    print(tree)
