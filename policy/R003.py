# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from . import Policy


class R003(Policy):
    '''
    今日收盘价低于今日开盘价但高于昨日收盘价

    (C < O) AND (C > REF(C, 1))

    '''

    name = u'假阴真阳'
    lines = 2

    def process(self):
        df = self.data

        return df.iloc[1].close < df.iloc[0].close < df.iloc[0].open
