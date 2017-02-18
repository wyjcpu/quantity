# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from policy import Policy


class R004(Policy):
    '''
    今日收盘价高于今日开盘价但低于昨日收盘价

    (C > O) AND (C < REF(C, 1))
    '''

    name = u'假阳真阴'
    lines = 2

    def process(self):
        df = self.data
        return df.iloc[1].close > df.iloc[0].close > df.iloc[0].open
