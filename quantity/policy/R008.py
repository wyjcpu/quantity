# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from policy import Policy


class R008(Policy):
    '''
    连续两日成交量高于前日成交量1.9+倍及1倍以上

    (VOL / REF(VOL, 1) > 1.9) AND (REF(VOL, 1)  / REF(VOL, 2) > 1.9)
    
    '''

    name = u'量活跃'
    lines = 3

    def process(self):
        df = self.data
        return df.iloc[0].volume >= (df.iloc[1].volume * 1.9) and df.iloc[1].volume >= (df.iloc[2].volume * 1.9)
