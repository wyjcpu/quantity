# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import datetime
import os
import sys

import numpy as np
import pandas as pd
import tushare as ts



def day(data, day=1, col='volume'):
    val = data[day - 1:day][col].values
    return val[0]


def shock(df):
    '''
    （当日最高点的价格－当日最低点的价格）/ 昨天收盘价×100%=振幅
    '''
    if len(df) < 2:
        return None

    return round((df.iloc[0].high - df.iloc[0].low) / df.iloc[1].close)


def date_span(today=None, span=4):
    if not today:
        today = datetime.date.today()

    tc = ts.trade_cal()

    # 日期格式转换
    tc['calendarDate'] = pd.to_datetime(tc['calendarDate'])
    cal = tc.loc[(tc.isOpen == 1) & (tc.calendarDate <= today)]

    days = cal.sort_values(['calendarDate'], ascending=False).head(span)
    days = days.calendarDate.values

    return days


class Policy(object):
    data = None
    name = None
    lines = 4
    disable = False

    def __init__(self, data=None, *args, **kwargs):
        self.data = data

    def TD(self, day=1, col=None):
        if not col:
            raise Exception('col is null')

        val = self.data[day - 1:day][col].values

        if val:
            return val[0]

        return None

    def begin(self):
        if len(self.data) < self.lines:
            return False

        df = self.data.iloc[:self.lines + 1].dropna()

        if len(df) < self.lines:
            return False

        return True

    def after(self):
        pass

    def __del__(self):
        del self.data


# def import_submodules(context, root_module, path):
#     """
#     Import all submodules and register them in the ``context`` namespace.
#
#     >>> import_submodules(locals(), __name__, __path__)
#     """
#     for loader, module_name, is_pkg in pkgutil.walk_packages(path, root_module + '.'):
#         module = loader.find_module(module_name).load_module(module_name)
#         for k, v in vars(module).iteritems():
#             if not k.startswith('_'):
#                 context[k] = v
#         context[module_name] = module
#
#
#
# import_submodules(locals(), __name__, __path__)
from .R001 import R001
from .R002 import R002
from .R003 import R003
from .R004 import R004
from .R005 import R005
from .R006 import R006
from .R007 import R007
from .R008 import R008
from .R009 import R009
from .R010 import R010
from .R011 import R011
from .R012 import R012
from .R013 import R013
from .R014 import R014
from .R015 import R015
from .R016 import R016

# submodules = (R001, R002, R003, R004, R005, R006, R007, R008, R009, R010, R011, R012, R013, R014, R015, R016,)
submodules = (R001, R002, R003, R004, R005, R006, R007, R008, R009, R010, R011, R012, R013, R014, R015, R016,)


