from itertools import groupby

def encode_(string):
    string_ = ''
    for k, g in groupby(string):
        count = len(list(g))
        if count != 1:
            string_ += str(count)+k
        else:
            string_ += k
    return string_

def decode_(string):
    string_ = ''
    count = ''
    for i in string:
        if i.isdigit():
            count += i
        elif count == '':
            string_ += i
        else:
            string_ += int(count) * i
            count = ''
    return string_

import re

def decode(s):
	return re.sub(r'(\d+)([^\d])', lambda c: c.group()[-1] * int(c.group()[:-1]), s)

def encode(s):
	return re.sub(r'([^\d])\1+', lambda c: '%i%s' % (len(c.group()), c.group()[0]), s)