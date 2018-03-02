# -*- coding: utf-8 -*-
# @Author: mithril

from __future__ import unicode_literals, print_function, absolute_import

import regex as re

from pypinyin import Style, pinyin

from utils import load_json

from config import WUBI_USAUAL_PATH, \
                    WUBI_ALL_PATH

from io import StringIO

# 英文，特殊串，邮箱，英文数字串联
en_pt = '[a-zA-Z0-9@+#&\._%]'
han_pt = '[\u4E00-\u9FD5]'
jpall_pt = '[\p{Hiragana}\p{Katakana}\p{Han}○●]'

re_encnjp = re.compile('({en}+)|({cn}+)|({jp}+)'.format(
    en=en_pt,
    cn=han_pt,
    jp=jpall_pt) , re.U)

re_en = re.compile('({}+)'.format(en_pt) , re.U)

re_han_default = re.compile("([\u4E00-\u9FD5a-zA-Z0-9+#&\._%]+)", re.U)
re_skip_default = re.compile("(\r\n|\s)", re.U)
re_han = re.compile("([\u4E00-\u9FD5]+)", re.U)
re_skip = re.compile("[^a-zA-Z0-9+#]", re.U)

re_num = re.compile("[^0-9+]", re.U)

re_jp = re.compile('([\p{Hiragana}\p{Katakana}]+)', re.U)
re_jpall = re.compile('([\p{Hiragana}\p{Katakana}\p{Han}○●]+)', re.U)


re_lang = re.compile('(?P<num>\d+)|(?P<en>[a-zA-Z+#&\._%]+)|(?P<jp>[\p{Hiragana}\p{Katakana}\p{Han}○●]+)')


re_delimiter_cn =  re.compile('([。？！；…]+)')

cnend = set('。？！；…')

ord_cnend = set(ord(i) for i in cnend)

wubi = load_json(WUBI_USAUAL_PATH)
wubi_all = load_json(WUBI_ALL_PATH)


class MultpleReplacer(object):
    def __init__(self, subdict):
        '''
        k: regex
        v: replace string

        better to be OrderedDict
        '''
        self.subdict = subdict
        self.pt = re.compile("(%s)" % "|".join(map(re.escape, subdict.keys())))

    def multiple_replace(self, text):
        # For each match, look-up corresponding value in dictionary
        return self.pt.sub(lambda mo: self.subdict[mo.string[mo.start():mo.end()]], text) 


def refomart_sentence(text):
    '''
    return list of tag,  <jp>, <en>, <num>
    '''
    for i in re.finditer(re_lang, text):
        for k, v in i.capturesdict().items():
            if v:
                yield '<%s>' % k
                break
        else:
            yield text[i.start(), i.end()]


def resplit_by(text, pt):
    '''
    注意，不能处理拼音，要先用中文输入处理
    因为拼音含有英文
    '''
    return pt.splititer(text)

def to_sentences(text):
    '''
    keep delimiter
    '''
    tmp = ''
    for i, chunk in enumerate(re.splititer(re_delimiter_cn, text)):
        if i%2:
            tmp += chunk
            yield tmp
        else:
            tmp = chunk
            
    if tmp:
        yield tmp 


def rows(f, chunksize=1024, sep='|'):
    """
    Read a file where the row separator is '|' lazily.

    Usage:

    >>> with open('big.csv') as f:
    >>>     for r in rows(f):
    >>>         process(row)
    """
    incomplete_row = None
    while True:
        chunk = f.read(chunksize)
        if not chunk: # End of file
            if incomplete_row is not None:
                yield incomplete_row
                break
        # Split the chunk as long as possible
        while True:
            i = chunk.find(sep)
            if i == -1:
                break
            # If there is an incomplete row waiting to be yielded,
            # prepend it and set it back to None
            if incomplete_row is not None:
                yield incomplete_row + chunk[:i]
                incomplete_row = None
            else:
                yield chunk[:i]
            chunk = chunk[i+1:]
        # If the chunk contained no separator, it needs to be appended to
        # the current incomplete row.
        if incomplete_row is not None:
            incomplete_row += chunk
        else:
            incomplete_row = chunk


def changeCNform(sentence, converter, split_other=True):
    '''
    修改句子中中文的形态
    变为 字分割， 拼音分割，五笔分割
    '''
    blocks = re_han.split(sentence)
    for blk in blocks:
        if not blk:
            continue
        if re_han.match(blk):
            for i in converter(blk):
                yield i
        else:
            for i in blk:
                yield i

            # if split_other:
            #     for i in blk:
            #         yield i
            # else:
            #     yield blk


def to_char(sentence):
    for i in sentence:
        yield i

def to_wubi(sentence):
    for i in sentence:
        yield wubi.get(i, wubi_all.get(i))

def to_pinyin(sentence):
    '''
    https://github.com/mozillazg/python-pinyin

    >>> from pypinyin import Style, pinyin
    >>> pinyin('下雨天', style=Style.INITIALS)
    [['x'], [''], ['t']]
    >>> pinyin('下雨天', style=Style.INITIALS, strict=False)
    [['x'], ['y'], ['t']]
    '''
    for i in pinyin(sentence):
        yield i[0]


def test():
    # 日语中的汉字会被识别为中文
    text = '涼子さんはおち○ちんが大好き'
    text = '涼子さんはおち○ちんが大好き。 ~dehepero　～　1111 haha・　·啊哈哈哈....'
    print(re_han.findall(text))
    print(re_jp.findall(text))
    print(re_jpall.findall(text))
    print(re_lang.findall(text))


    test_delimiters = [
        '今天天气，很不错的？ 为啥呢。我突然，不像“高这个” 啥啥啥？！哈哈哈；…',
        '今天天气很好',
        '今天天气很好？为啥呢',
        '。？哈哈。',
        '？？？,'
        '。',
    ]

    for text in test_delimiters:
        print(list(to_sentences(text)))


sent2char = lambda s:changeCNform(s, to_char)
sent2wubi = lambda s:changeCNform(s, to_wubi)
sent2pinyin = lambda s:changeCNform(s, to_pinyin)

    
if __name__ == '__main__':
    test()