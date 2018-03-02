# -*- coding: utf-8 -*-
# @Author: mithril

from __future__ import unicode_literals, print_function, absolute_import, division

from converter import to_char, to_pinyin, to_wubi
from converter import sent2char, sent2pinyin, sent2wubi


texts = [
    '本文哈哈出品。使用双向LSTM+CRFs 模型用于NLP序列标注问题（POS、分块、命名实体识别）。'
]

def test_aligning(s):
    
    chars = list(sent2char(s))
    pinyins = list(sent2pinyin(s))
    wubis = list(sent2wubi(s))

    print('chars: ',chars)
    print()
    print('pinyins: ', pinyins)
    print()
    print('wubis:' , wubis)

    assert len(chars) == len(pinyins)
    assert len(chars) == len(wubis)

def main():
    for i in texts:
        test_aligning(i)



if __name__ == '__main__':
    main()