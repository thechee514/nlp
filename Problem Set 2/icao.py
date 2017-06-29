def speak_ICAO(a_string):
    d = {'a':'alfa', 'b':'bravo', 'c':'charlie','d':'delta', 'e':'echo',
         'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett',
         'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar',
         'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango',
         'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee',
         'z':'zulu'}
    translated_string = ""
    for char in a_string.lower():
        if d.has_key(char):
            translated_string += d[char]
            translated_string += " "
        elif char != " ":
            translated_string += char
    return translated_string
