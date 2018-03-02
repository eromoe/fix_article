# -*- coding: utf-8 -*-
# @Author: mithril

from __future__ import unicode_literals, print_function, absolute_import, division


import numpy as np
from random import choice
from converter import changeCNform, to_char, to_pinyin, to_wubi

def mutate_wubi(char, wubi=None):
    '''
    使用五笔规则mutate char
    '''
    

    return  1

def mutate_pinyin(char, py=None):
    '''
    s: pinyin
    '''

    return  1

# mutfuncs = [mutate_wubi, mutate_pinyin]

# def mutate_mix(s):
#     return choice(mutfuncs)(s)

def mutate_squence(squence, size, pinyin=None, wubi=None, mtype=None):
    '''
    squence: string
    size: mutate number
    '''
    assert len(squence) >= size
    
    # 随机选择出不重复的size 个 index

    idx = 1

    # mutate squence 的index的值
    if not pinyin:
        pinyin = to_pinyin(squence)
    if not wubi:
        wubi = to_wubi(squence)

    if mtype == 'pinyin':
        squence[idx], pinyin[idx] = mutate_pinyin(pinyin[idx])
    elif mtype== 'wubi':
        squence[idx], wubi[idx] = mutate_wubi(wubi[idx])
    else:
        raise Exception('Unknow mutate type')

    return squence, pinyin, wubi
    

def _vectorize(questions, answers, ctable):
    """Vectorize the data as numpy arrays"""
    len_of_questions = len(questions)
    X = np_zeros((len_of_questions, CONFIG.max_input_len, ctable.size), dtype=np.bool)
    for i in xrange(len(questions)):
        sentence = questions.pop()
        for j, c in enumerate(sentence):
            try:
                X[i, j, ctable.char_indices[c]] = 1
            except KeyError:
                pass # Padding
    y = np_zeros((len_of_questions, CONFIG.max_input_len, ctable.size), dtype=np.bool)
    for i in xrange(len(answers)):
        sentence = answers.pop()
        for j, c in enumerate(sentence):
            try:
                y[i, j, ctable.char_indices[c]] = 1
            except KeyError:
                pass # Padding
    return X, y

def vectorize(sentences):
    total_sentence = len(sentences)
    EMBEDDING_DIM = 200
    X = np.zeros((total_sentence, max_input_len, EMBEDDING_DIM))
    
    


    