# -*- coding: utf-8 -*-
# @Author: mithril

from __future__ import unicode_literals, print_function, absolute_import, division

import gensim

from gensim.models.fasttext import FastText
from gensim.models.word2vec import LineSentence



model = FastText.load_fasttext_format('/data/dataset/wiki.zh')


# 注意，因为用的是fasttext 官方的模型，model.corpus_count 是0
# 需要手动指定一个 corpus_count
loaded_model.train([['今天', '天气', '很好', '。']], total_examples=model.corpus_count)