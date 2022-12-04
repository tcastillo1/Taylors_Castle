# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    y = 0
    for x in sentence:
        if x in (["a", "e", "i", "o", "u"]):
            y = y + 1
        else:
            y = y
    return y


get_count("testing")
