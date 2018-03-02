# -*- coding: utf-8 -*-
# @Author: mithril

from __future__ import unicode_literals, print_function, absolute_import

import os
import pickle
import codecs

def buffwrite(iterable, dst, buff_size=10000):
    if os.path.exists(dst):
        os.remove(dst)
        
    i = 1
    buff = []
    with codecs.open(dst, 'a', 'utf-8') as out:
        for row in iterable:
            buff.append(row)
            i+=1
            if not i % buff_size:
                out.write('\n'.join(buff)+'\n')
                buff =[]
                print(i)
        else:
            out.write('\n'.join(buff)+'\n')
