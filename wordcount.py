# put your code here.
def wordcount_dict(filename):
    """ Takes a .txt as an argument and prints each word (as separated by a space) 
        and how frequently it appears in the file
    """

    the_file = open(filename)

    wordcounts = {}

    for line in the_file:
        
        # clean_line = line.rstrip() <--Unneccessary due to ".split()" below

        # Converts line to lower-case
        line = line.lower()
        #evaluates each character in the line, and if it is not alphanumeric, replaces it with a space.
        for char in line:
            if char.isalnum():
                continue
            else:
                line = line.replace(char," ")
    
        words = line.split()
        
        # If the word exists in the dictionary already, the word count is incremented by 1. 
        # If the word does not exist, it is added as a key and the count is incremented by one.
        for word in words:
            if word.isalnum() == False:
                for char in word:
                    if char.isalnum():
                        continue
                    else:
                        word = word.replace(char," ")
            if word in wordcounts:
                wordcounts[word] += 1
            else:
                wordcounts[word] = 1

    the_file.close()
    print "This is how often each word appears:"
    
    # This for loop uses ".items" to create a list of tuples for each key-value pair.
    # Each tuple is unpacked to identifiers word and count and those are printed.
    for word, count in wordcounts.items():
        print word , count
    pass

wordcount_dict("twain.txt")