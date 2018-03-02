#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os.path
import sys
import multiprocessing

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # inp = 'I:\\Corpus\\txt\\qq_news.char.txt'
    # outp1 = 'I:\\Corpus\\txt\\qq_news_char.vec'
    # outp2 = 'I:\\Corpus\\txt\\qq_news_char_trainable.vec'


    inp = 'I:\\Corpus\\txt\\qq_news.pingyin.txt'
    outp1 = 'I:\\Corpus\\txt\\qq_news_pinyin.vec'
    outp2 = 'I:\\Corpus\\txt\\qq_news_pinyin_trainable.vec'


    '''
    LineSentence need space split string
    '''
    model = Word2Vec(LineSentence(inp), size=300, window=5, min_count=10,
            workers=multiprocessing.cpu_count(), iter=3)

    # trim unneeded model memory = use(much) less RAM
    #model.init_sims(replace=True)

    model.wv.save(outp1) # :func:`~gensim.models.*2vec.*2VecKeyedVectors.load` which supports

    #model.wv.save_word2vec_format(outfile + '.model.bin', binary=True)  # C binary format 磁盘空间比上一方法减半
    model.wv.save_word2vec_format(outp2, binary=False)  # load_word2vec_format

    # Word2VecKeyedVectors/KeyedVectors
    # get_keras_embedding

    print('OK')

