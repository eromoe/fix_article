# -*- coding: utf-8 -*-
# @Author: mithril

from __future__ import unicode_literals, print_function, absolute_import, division

import pandas as pd
from collections import OrderedDict
import json


df = pd.read_excel('CorpusCharacterlist.xls')

df.iloc[:, [3]].astype(float)
x = df.iloc[:,[1,3]].to_records(index=False)
a = OrderedDict(x)

with open('char.json', 'w') as f:
    f.write(json.dumps(a))

