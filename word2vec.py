# -*- coding: utf-8 -*-
# @Author: mithril

from __future__ import unicode_literals, print_function, absolute_import, division


import gensim
from gensim.models.fasttext import FastText
from gensim.models.word2vec import LineSentence


def update_fasttext():

    model = FastText.load_fasttext_format('/data/dataset/wiki.zh')

    # 注意，因为用的是fasttext 官方的模型，model.corpus_count 是0
    # 需要手动指定一个 corpus_count
    model.train([['今天', '天气', '很好', '。']], total_examples=model.corpus_count)


def sentence_generator():
    f = []
    for line in f:
        for i in line:
            print

def wubi2vec(sentences):
    model = FastTex()


if __name__ == '__main__':
    sentence = '今天我们去动物园看ufo怎么样啊~。 哈哈, 好啊。'

    d = to_wubi(sentence)
    print(list(d))


