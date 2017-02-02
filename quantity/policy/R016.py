# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from policy import Policy


class R016(Policy):
    '''
    今日成交量小于近1月内任意一天成交量，且今日收盘价高于昨日收盘价或今日收盘价高于今日开盘价但低于昨日收盘价.
    今日改昨日 昨天改前天，今日的成交量是昨日1倍+
    '''

    name = u'倍量起步'
    lines = 30

    def process(self):
        df = self.data.iloc[:31]

        return (df.loc[(df.volume == df.volume.min())].iloc[0].volume == df.iloc[1].volume) and \
               (df.iloc[1].close > df.iloc[2].close or df.iloc[2].close > df.iloc[1].close > df.iloc[2].open) and \
               (df.iloc[0].volume >= (df.iloc[1].volume * 1.8))
