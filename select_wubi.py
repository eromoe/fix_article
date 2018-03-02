# -*- coding: utf-8 -*-
# @Author: mithril

from __future__ import unicode_literals, print_function, absolute_import

import pandas as pd
import json
from collections import Counter

df = pd.read_excel('CorpusCharacterlist.xls')

chars = set(df.iloc[:, [1]].values.flatten())

with open('wubi_all.json') as f:
    d = json.loads(f.read())

def build_unique_wubi(d, output):
    c = Counter()

    for k, v in d.items():
        p = c.get(v, 0)
        c[v]+=1

        if p:
            d[k] +=str(p)

    open(output, 'w').write(json.dumps(d))

    print(c.most_common(10))

def build_usual_unique_wubi(d, output):

    for k in d.keys():
        if k not in chars:
            del d[k]

    build_unique_wubi(d, output)

    return d

# build_unique_wubi(d, 'wubi_unique_all.json')



if __name__ == '__main__':
    # from IPython.core import debugger
    # debugger.Pdb().set_trace()
    build_unique_wubi(d, 'wubi_unique_all.json')
    build_usual_unique_wubi(d, 'wubi_unique_usual.json')
    



