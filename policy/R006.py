# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from policy import Policy


class R006(Policy):
    '''
    6个月内最低收盘价与最高收盘价价差在50%以,

    V1：= MA（VOL，5）；
    V2：= VOL/REF（V1，1）＞2；
    PZ1：= MA（CLOSE，M）；
    PZ2：=HHV（HIGH，M）；
    PZ3：=LLV（LOW，M）；
    PZ4：=（PZ2-PZ1）/PZ1；
    PZ5：=（PZ1-PZ3）/PZ1；
    PZ：=REF（PZ4，1）＜0.15 AND REF（PZ5，1）＜0.15；
    TP1：HHV（HIGH，M）；
    TP：=HIGH=TP1；
    V2 AND PZ AND TP；
    '''

    name = u'长期横盘'
    lines = 180

    def process(self):
        df = self.data
        ff = df['close'].describe()

        return ((ff['max'] - ff['min']) / ff['max']) <= 0.5
