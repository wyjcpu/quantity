# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal

import numpy as np

from . import Policy


class R015(Policy):
    '''
    今日开收低，10日内最大量的开收低之间上下浮动1分钱
    '''

    name = u'精准回踩'
    lines = 13

    def process(self):
        df = self.data
        df = df.iloc[:14].dropna()

        today = df.iloc[0].loc[['open', 'close', 'low']].apply(lambda x: '%.2f' % x)
        yestoday = df.iloc[1].loc[['open', 'close', 'low']].apply(lambda x: '%.2f' % x)
        maxis = df.loc[(df.volume == df.volume.max())][['open', 'close', 'low']].apply(lambda x: '%.2f' % x)

        s = np.append(today, maxis)
        s = np.append(s, yestoday)

        n = None
        v = []
        p = []

        try:
            for x in s:
                if n is not None:
                    # if (abs(Decimal(x) - Decimal(n)) / Decimal(x)) <= 0.005:
                    # return True
                    v.append(abs(Decimal(x) - Decimal(n)))
                    p.append((abs(Decimal(x) - Decimal(n)) / Decimal(x)))

                n = x
        except Exception as e:
            return False

        # print 'no'
        # print min(v)
        # return 0.01 in v
        if min(p) <= 0.005:
            ln = "'" + df.iloc[0].code + ',' + today[0] + ',' + today[1] + ',' + today[2] + ',' + yestoday[0] + ',' + \
                 yestoday[1] + ',' + yestoday[2] + ',' + \
                 maxis[0] + ',' + maxis[1] + ',' + maxis[2] + ',%.6f\n' % min(p)
            with open('R015.csv', 'a') as f:
                f.write(ln)

        return min(p) <= 0.005
