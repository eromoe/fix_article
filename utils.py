# -*- coding: utf-8 -*-
# @Author: mithril

from __future__ import unicode_literals, print_function, absolute_import

import codecs
import json


def load_json(path):
    with codecs.open(path) as f:
        data = f.read()
        return json.loads(data)

