# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from . import Policy


class R013(Policy):
    '''
    满足黄金后 3量 > 2量 > 1量, 3涨 2涨 1涨 三天连涨

    -----------------------------------------------------------------------------
    ((V < REF(V,3)) AND (REF(V,1) < REF(V,3)) AND (REF(V, 2) < REF(V,3))) AND
    ((C > REF(C,3)) AND (REF(C,1) > REF(C,3)) AND (REF(C, 2) > REF(C,3))) AND
    (REF(C,3) > REF(O,3)) AND (UPNDAY(C, 3) AND UPNDAY(V, 3))

    '''

    name = u'喇叭口'
    lines = 5

    def process(self):
        df = self.data

        return (df.iloc[2].volume >= df.iloc[1].volume >= df.iloc[0].volume) and \
               (df.iloc[3].close > df.iloc[3].open) and \
               (df.iloc[2].close > df.iloc[2].open) and \
               (df.iloc[1].close > df.iloc[1].open) and \
               (df.iloc[0].close > df.iloc[0].open) and \
               (df.iloc[3].volume == df.volume.max()) and \
               (df.iloc[:3].close > df.iloc[3]['open']).all()
