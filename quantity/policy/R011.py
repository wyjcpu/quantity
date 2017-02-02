# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from . import Policy


class R011(Policy):
    '''
    今日，昨日，前日成交量均低于大前日成交量， 增长 且今日，昨日，前日收盘价高于3日前当天 开盘价(最小) 振幅 > 4%+


    ((V > REF(V,3)) AND (REF(V,1) > REF(V,3)) AND (REF(V, 2) > REF(V,3))) AND
    ((C < REF(C,3)) AND (REF(C,1) < REF(C,3)) AND (REF(C, 2) < REF(C,3))) AND
    ((REF(H,3) - REF(L,3)) / REF(C,3) >= 0.04) AND (REF(C,3) > REF(O,3))

    '''

    name = u'将军'
    lines = 5

    def process(self):
        # ds = self.data.iloc[:15]
        df = self.data

        # 最大值行
        # mx = df.loc[(df.iloc[3]['volume'] == df['volume'].max())].iloc[0]

        # 最大值前一天
        # m1 = ds.loc[ds.date < mx.date].iloc[0]

        return (df.iloc[3].close > df.iloc[3].open) and \
               (df.iloc[3].volume == df.volume.max()) and \
               (((df.iloc[3]['high'] - df.iloc[3]['low']) / df.iloc[3]['close']) >= 0.04) and \
               (df.iloc[:3].close > df.iloc[3].open).all()
