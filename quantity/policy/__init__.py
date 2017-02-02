# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import datetime
import sys

import numpy as np
import pandas as pd
import tushare as ts

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


