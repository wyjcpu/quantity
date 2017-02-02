# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from . import Policy


class R010(Policy):
    '''
    昨日成交量是前日成交量1倍及1倍以上，且昨日收盘价高于昨日开盘价；
    今日成交量为昨日成交量1倍及1倍以下，且今日收盘价高于昨日开盘价

    (REF(VOL, 1) / REF(VOL, 2) > 1.8) AND (REF(CLOSE, 1) > REF(OPEN, 1)) AND
    (VOL / REF(VOL, 2) < 0.6) AND (CLOSE > REF(OPEN, 1))

    '''

    name = u'伸缩倍量'
    lines = 5

    def process(self):
        df = self.data.iloc[:3]

        if len(df) < self.lines:
            return False

        return (df.iloc[1].volume >= (df.iloc[2].volume * 1.8)) and (df.iloc[1].close > df.iloc[1].open) and \
               (df.iloc[0].volume <= (df.iloc[1].volume * 0.6)) and (df.iloc[0].close > df.iloc[1].open)
