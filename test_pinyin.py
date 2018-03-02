# -*- coding: utf-8 -*-
# @Author: mithril

from __future__ import unicode_literals, print_function, absolute_import


def pinyin_factory(libname):

    if libname == 'xpinyin':
        from xpinyin import Pinyin
        p = Pinyin()
        return lambda x : p.get_pinyin(x, show_tone_marks=True, splitter=' ')
    elif libname == 'pypinyin':
        '''
        https://github.com/mozillazg/python-pinyin

        :param hans: 汉字字符串( ``'你好吗'`` )或列表( ``['你好', '吗']`` ).
        :param heteronym: 是否启用多音字

        >>> from pypinyin import Style, pinyin
        >>> pinyin('下雨天', style=Style.INITIALS)
        [['x'], [''], ['t']]
        >>> pinyin('下雨天', style=Style.INITIALS, strict=False)
        [['x'], ['y'], ['t']]
        '''
        from pypinyin import pinyin, lazy_pinyin, Style
        return lambda x: pinyin(x, strict=False)
        
    elif libname == 'pinyin':
        '''
        pip install pinyin
        '''
        import pinyin as _pinyin
        
        return lambda x: _pinyin.get(x,  delimiter=" ", format="numerical")

    return lambda x: x
        

test_texts = [
    '我明天把书还给你',
    '快还我',
    '可恶，还给我搞这套？',
    '还不给我快点。',
    '还有什么事。' # 注意me 没有音标
    'sdasd， english， 中文在这, オカズはオルタちゃん'
]


tools =[
'原始',
'xpinyin',
'pypinyin',
'pinyin',]

for k in tools:
    func = pinyin_factory(k)
    print('========== %s ===========' % k)
    for i in test_texts:
        print(func(i))

    print()
