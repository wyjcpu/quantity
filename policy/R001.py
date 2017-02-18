# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from . import Policy


class R001(Policy):
    '''
    昨天涨幅8%+，今天交易量少于昨天的30%及以上

    (REF(CLOSE,1) / REF（CLOSE，2）>= 1.08) and (VOL / REF(VOL, 1) <= 0.30)
    '''

    name = u'缩量三一'
    lines = 3

    def process(self):
        df = self.data
        return (df.iloc[1].close > df.iloc[2].close) and \
               (((df.iloc[1].close - df.iloc[2].close) / df.iloc[2].close) >= 0.08) and \
               (df.iloc[0].volume < df.iloc[1].volume) and \
               (((df.iloc[0].volume - df.iloc[1].volume) / df.iloc[1].volume) >= 0.30)
