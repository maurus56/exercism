def is_pangram(sentence):
    import re
    if isinstance(sentence,str):
        w = sentence.lower()
        w = re.compile("[^a-z]").sub("", w)
        return 26 == len(set(w)) if w else False
    else:
        raise TypeError('Argument should be a string')

def is_pan(sentence):
    import string
    return set(filter(str.isalpha, sentence.lower())) == set(string.ascii_lowercase)

print(is_pan('the quick brown fox-jumps over the lazy dog'))