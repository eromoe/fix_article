# -*- coding: utf-8 -*-
# @Author: mithril

from __future__ import unicode_literals, print_function, absolute_import, division

import logging
from logging.handlers import RotatingFileHandler


WUBI_USAUAL_PATH = 'wubi_unique_usual.json'

WUBI_ALL_PATH = 'wubi_unique_all.json'

def build_logger(name=None, level=logging.DEBUG, filename=None):
    
    # logging.basicConfig(level=level)
    # logging.getLogger(name).setLevel(logging.ERROR)
    logger = logging.getLogger(name or __file__)

    formatter = logging.Formatter(
        '[%(levelname)s]'
        '  %(asctime)s %(levelname)s: %(message)s '
    )
    detail_formatter = logging.Formatter(
        '[%(levelname)s][%(pathname)s:%(lineno)d][%(funcName)s]'
        '  %(asctime)s %(levelname)s: %(message)s '
    )
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    
    if filename:
        file_handler = RotatingFileHandler(filename, maxBytes=1024*1024, backupCount=2)
        file_handler.setLevel(level)
        file_handler.setFormatter(detail_formatter)
        logger.addHandler(file_handler)

    return logger
