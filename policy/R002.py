# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import numpy as np

from . import Policy


class R002(Policy):
    '''
    昨日收盘价高于5日前收盘价10%及以上,今日成交量小于昨日成交量30%及以上

    (REF(C, 1) / REF(C, 4) >= 1.10) AND (VOL / REF(VOL, 1) <= 0.30)
    '''

    name = u'价活跃缩量踩'
    lines = 6

    def process(self):
        df = self.data
        df.volume = df.volume.astype(np.float)

        return (df.iloc[1].close > df.iloc[4].close) and \
               (((df.iloc[1].close - df.iloc[4].close) / df.iloc[4].close) > 0.10) and \
               (df.iloc[0].volume < df.iloc[1].volume) and \
               ((abs(df.iloc[0].volume - df.iloc[1].volume) / df.iloc[1].volume) >= 0.27) and \
               (df.iloc[0].close >= df.iloc[1].open)
