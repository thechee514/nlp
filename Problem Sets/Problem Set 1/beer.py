# Vincent Chee
# Code snippet that prints out all the verses of the song '99 bottles of beer'.

def beer():
    for i in range(100):
        bottles_of_beer = 99-i
        if bottles_of_beer != 0:
            if bottles_of_beer != 1:
                print bottles_of_beer,'bottles of beer on the wall',bottles_of_beer,'bottles of beer. Take one down, pass it around,',bottles_of_beer-1,'bottles of beer on the wall.'
            else:
                print bottles_of_beer,'bottle of beer on the wall',bottles_of_beer,'bottle of beer. Take one down, pass it around,',bottles_of_beer-1,'bottles of beer on the wall.'
