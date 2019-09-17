def word_count(phrase):
    import re
    phrase = re.compile(r"[a-z]+'?[a-z]|[0-9]").findall(phrase.lower())
    d = {}
    for key in phrase: 
        d[key] = d.get(key, 0) + 1
    return d