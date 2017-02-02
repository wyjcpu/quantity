# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from policy import Policy


class R005(Policy):
    '''
    1. 昨日收盘价低于前日收盘价
    REF(C, 1) < REF(C, 2)
    2. 而今日收盘价高于昨日开盘价
    C > REF(O, 1)
    3. 且今日成交量大于昨日成交量
    V > REF(V,1)
    4. 昨日收盘价较前日收盘价下跌4%及以上。
    REF(C, 1) / REF(C, 2) <= 0.04

    
    -----------------------------------------
    new: 昨天下跌4%，今天上涨4% 今天量大于昨天的量
    (REF(C,1) / REF(C,2) <= 0.04) AND (C / REF(C, 1) >=1.04) AND (V > REF(V,1))
    '''

    name = u'双阳胜'
    lines = 4

    def process(self):
        df = self.data
        return (df.iloc[1].close < df.iloc[1].open) and \
               ((abs(df.iloc[1].close - df.iloc[1].open) / df.iloc[1].close) >= 0.04) and \
               (df.iloc[0].open < df.iloc[0].close) and \
               ((abs(df.iloc[0].close - df.iloc[0].open) / df.iloc[0].close) >= 0.04) and \
               (df.iloc[1].volume < df.iloc[0].volume)
