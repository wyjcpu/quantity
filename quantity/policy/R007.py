# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from policy import Policy


class R007(Policy):
    '''
    1.今日收盘价低于前13日内成交量最大当日（注：成交量最大当日的收盘价高于它的开盘价）的收盘价，且最低价高于成交量最大当日的最低价。
    2.成交量最大当日之后到今日之间，任何一天的最低价高于成交量最大当日的最低价，收盘价低于成交量最大当日的收盘价，且当日成交量低于成交量最大当日，
    3.成交量最大当日的股价振幅超过5%及以上
    
    振幅 = (当日最高点的价格 － 当日最低点的价格) / 昨天收盘价 × 100%

    时间周期 3 - 13 内容

    量大低最小
    
    量大收最大 
    
    振幅 > 5%

    MX1:=FINDMAXBAGS(3,13,10,VOL);
    MC1:=REF(CLOSE, MX1) = LLV(LOW, 13);
    ML1:=REF(LOW, MX1) = LLV(LOW, 13);
    ((REF(H, MX1) - REF(L, MX1)) / REF(C, MX1)) >= 1.5



    高量不破:REF(V,7)=HHV(V,8) AND REF(L,7)<REF(L,6) AND REF(L,7)<REF(L,5) AND REF(L,7)<REF(L,4) AND REF(L,7)<REF(L,3) AND REF(L,7)<REF(L,2) AND REF(L,7)<REF(L,1) AND REF(L,7)<L;



    mx = df.loc[(df['volume'] == df['volume'].max())].iloc[0]
    (mx.low == df.loc[(df['low'] == df['low'].min())].iloc[0].low) and \
    (mx.close == df.loc[(df['close'] == df['close'].max())].iloc[0].low) and \
    ((df.iloc[0].high - df.iloc[0].low) / df.iloc[1].close) > 5 %

    MX: =
    '''

    name = u'高量不破'
    lines = 15

    def process(self):
        df = self.data
        ds = self.data

        df = df.iloc[:13]
        mx = df.loc[(df['volume'] == df['volume'].max())].iloc[0]
        m1 = ds.loc[ds.date < mx.date].iloc[0]
        td = ds.loc[ds.date >= mx.date]

        return (mx.low == td.loc[(df['low'] == td['low'].min())].iloc[0].low) and \
               (mx.close == td.loc[(df['close'] == td['close'].max())].iloc[0].close) and \
               (((mx['high'] - mx['low']) / m1['close']) >= 0.05) and \
               (ds.iloc[:3].date > mx.date).all()
