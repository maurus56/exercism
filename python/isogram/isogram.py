def is_isogram(string):

    if isinstance(string,str):
        w = string.lower().replace("-","").replace(" ","")
        return len(w) == len(set(w)) if w else True
    else:
        raise TypeError('Argument should be a string')