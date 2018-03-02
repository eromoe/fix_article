# -*- coding: utf-8 -*-
# @Author: mithril

'''
split into pinyin space line
'''

from __future__ import unicode_literals, print_function, absolute_import

import codecs
from pypinyin import pinyin, Style
from utils import buffwrite


def gen_pinyin_line(path):
    with codecs.open(path, 'r', 'utf-8') as f:
        for line in f:
            line = line.strip()
            if len(line) > 5:
                lst = [i[0] for i in pinyin(line, strict=False)]
                yield " ".join(lst)


if __name__ == "__main__":

    inp = 'I:\\Corpus\\txt\\qq_news.txt'
    outp = 'I:\\Corpus\\txt\\qq_news.pinyin.txt'

    buffwrite(gen_pinyin_line(inp), outp)
