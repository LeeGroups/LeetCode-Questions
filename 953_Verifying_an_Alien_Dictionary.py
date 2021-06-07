

def isAlienSorted(words, order) -> bool:
    if len(words)== 0:
        return True

    # a helper function that builds a hash table from order
    def build_hash(string):
        dictionary = {}
        for i in range(len(string)):
            a = string[i]
            dictionary[a] = i 
        return dictionary

    # the hash table
    dictionary = build_hash(order)

    # a helper function that takes in an array of two strings and a dictionary, and outputs whether or not the strings are in order
    def check_one_layer(x: list[str], alphabet: dict):
        if x[0] == "":
            return True
        elif x[1] == "":
            return False
        elif alphabet[x[0][0]] < alphabet[x[1][0]]:
            return True
        elif alphabet[x[0][0]] > alphabet[x[1][0]]:
            return False
        else:
            y = [x[0][1:],x[1][1:]]
            return check_one_layer(y,alphabet)

    dummy = True
    # compares the adjacent pairs of words
    for i in range(len(words)-1):
        if not check_one_layer([words[i],words[i+1]], dictionary):
            dummy = False
    return dummy

# sample inputs:

#Expect true
print( isAlienSorted(["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz"))

#Expect false
print( isAlienSorted(["word","world","row"],"worldabcefghijkmnpqstuvxyz"))

#Expect false
print( isAlienSorted(["apple","app"],"abcdefghijklmnopqrstuvwxyz"))