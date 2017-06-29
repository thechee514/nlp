def char_freq(word):
    d = {}
    for char in word.lower():
        if d.has_key(char):
            d[char] += 1
        elif char != " ":
            d[char] = 1
    return d
print char_freq("Abra! Cadabra!")
