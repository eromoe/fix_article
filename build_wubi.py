# -*- coding: utf-8 -*-
# @Author: mithril

from __future__ import unicode_literals, print_function, absolute_import, division

import requests
from pyquery import PyQuery
from lxml import html
from collections import defaultdict
import json

from multiprocess import Pool, Process

from six.moves.urllib.parse import quote
from tqdm import tqdm


from config import build_logger

logger = build_logger('wubi', filename='wubi.log')
# from pprint import pprint as print


# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36',
#     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Language':'en-us;q=0.5,en;q=0.3',
#     'Accept-Encoding':'gzip, deflate',
#     'Connection':'keep-alive',
#     'Cache-Control':'max-age=0'
# }

def query_wubi(char):
    
    url = 'http://www.chaiwubi.com/bmcx/'

    data = {
        'wz': char,
        'select_value': '查单字'
    }

    r = requests.post(url, data=data)

    h = html.fromstring(r.text)
    tb = h.cssselect('.dw-bmcx')[0]


    # 五笔王码86版
    # 大一统新世纪版五笔编码
    d = defaultdict(list)
    trs = tb.cssselect('tr')

    # 前三个大写 后三个小写

    tr86 = trs[0]
    tds= PyQuery(tr86).children('td')
    d['86'] = [
        tds.eq(2).text().strip() or None, 
        tds.eq(3).text().strip() or None, 
        tds.eq(4).text().strip() or None, 
        tds.eq(5).text().strip() or None, 
    ]
    for tr in trs[1:3]:
        tds= PyQuery(tr).children('td')
        d[tds.eq(0).text()] = [
            tds.eq(1).text().strip() or None, 
            tds.eq(2).text().strip() or None, 
            tds.eq(3).text().strip() or None, 
            tds.eq(4).text().strip() or None, 
            ]

    return d

def task(k):
    logger.info('Process %s' % k)
    try:
        return k, query_wubi(k)
    except:
        return k, None
        logger.error('Get error on %s' % k)

def main():
    with open('char.json') as f:
        d = json.loads(f.read())

    result = {}

    pool = Pool(4)

    for k, d in tqdm(pool.imap_unordered(task, d.keys())):
        result[k] = d

    with open('wubi.json', 'w') as f:
        f.write(json.dumps(result))


if __name__ == '__main__':
    # s = query_wubi('的')
    # print(s)

    main()