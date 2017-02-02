# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from . import Policy


class R012(Policy):
    '''
    今日，昨日，前日成交量均低于大前日成交量， 增长 1,2,3收盘价 > 4收盘价，

    ((V < REF(V,3)) AND (REF(V,1) < REF(V,3)) AND (REF(V, 2) < REF(V,3))) AND
    ((C > REF(C,3)) AND (REF(C,1) > REF(C,3)) AND (REF(C, 2) > REF(C,3))) AND
    (REF(C,3) > REF(O,3))

    '''

    name = u'黄金'
    lines = 5

    def process(self):
        df = self.data.dropna()

        if len(df) < self.lines:
            return False

        return (df.iloc[3].close > df.iloc[3].open) and \
               (df.iloc[3].volume == df.volume.max()) and \
               (df.iloc[:3].close > df.iloc[3].close).all()
               # (((df.iloc[3]['high'] - df.iloc[3]['low']) / df.iloc[4]['close']) >= 0.04) and \
