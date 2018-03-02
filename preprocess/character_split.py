# -*- coding: utf-8 -*-
'''
split into char space line
'''
import itertools, unicodedata

import os
import pickle
import codecs
from utils import buffwrite

def gen_char_line(path):
    with codecs.open(path, 'r', 'utf-8') as f:
        for line in f:
            line = line.strip()
            if len(line) > 5:
                yield " ".join(group_words(line))

def group_words(s):
    # This is a closure for key(), encapsulated in an array to work around
    # 2.x's lack of the nonlocal keyword.
    sequence = [0x10000000]

    def key(part):
        val = ord(part)
        if part.isspace():
            return 0

        # This is incorrect, but serves this example; finding a more
        # accurate categorization of characters is up to the user.
        asian = unicodedata.category(part) == "Lo"
        if asian:
            # Never group asian characters, by returning a unique value for each one.
            sequence[0] += 1
            return sequence[0]

        return 2

    result = []
    for key, group in itertools.groupby(s, key):
        # Discard groups of whitespace.
        if key == 0:
            continue

        s = "".join(group)
        result.append(s)

    return result


if __name__ == "__main__":

    inp = 'I:\\Corpus\\txt\\qq_news.txt'
    outp = 'I:\\Corpus\\txt\\qq_news.char.txt'


    buffwrite(gen_char_line(inp), outp)


    # d = group_words('今天是2013年30号，#￥@！#%￥， 听说天气dehepero很好，我们去看ufo')
    # print(d)