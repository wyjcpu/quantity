# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from . import Policy


class R014(Policy):
    '''
    今日收盘价高于4日开盘价15%及以上

    C / REF(O, 3) >= 1.15

    '''

    name = u'价活跃'
    lines = 4

    def process(self):
        df = self.data
        return df.iloc[0].close >= (df.iloc[3].open * 1.15)
