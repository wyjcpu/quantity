# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from . import Policy


class R009(Policy):
    '''
    今日成交量小于近30个交易日内任意一天成交量（指30天内今日最低）必须，
    今日收盘价高于昨日收盘价，
    或今日收盘价高于今日开盘价但低于昨日收盘价

    '''

    name = u'百日低量'
    lines = 30

    def process(self):
        df = self.data.iloc[:31]

        return (df.loc[(df.volume == df.volume.min())].iloc[0].volume == df.iloc[0].volume) and \
               (df.iloc[0].close > df.iloc[1].close or df.iloc[1].close > df.iloc[0].close > df.iloc[1].open)
