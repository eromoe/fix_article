# -*- coding: utf-8 -*-
# @Author: mithril

from __future__ import unicode_literals, print_function, absolute_import, division

from collections import Counter
import codecs
import json


inp = 'I:\\Corpus\\txt\\qq_news.wubi.txt'
outp = 'wubi.json'

c= Counter()

with codecs.open(inp, 'r', 'utf-8') as f:
    c.update(f.readline())

with codecs.open(outp, 'w', 'utf-8') as f:
    f.write(json.dumps(c))
