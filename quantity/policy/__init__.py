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
submodules = (R001, R002, R003, R004, R005, R006, R008, R009, R010, R011, R012, R013, R014, R015, R016,)

