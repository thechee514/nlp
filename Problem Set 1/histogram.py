# Vincent Chee
# Code snippet takes a list containing ints and prints out a histographic representation.

def histogram(histo_list):
    for number_of_stars in histo_list:
        histo_string = ""
        for i in range(number_of_stars):
            histo_string+="*"
        print histo_string
    print "\n"

