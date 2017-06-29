# Vincent Chee
# Code snippet that takes an infinitive verb and returns its third person singular form

def make_3sg_form(infinitive_verb):
    if infinitive_verb.endswith('y'):
        return infinitive_verb[0:-1] + 'ies'
    elif infinitive_verb.endswith(("o", "c", "s", "sh", "x", "z")):
        return infinitive_verb + 'es'
    else:
        return infinitive_verb + 's'


