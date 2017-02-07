# -*- coding: utf-8 -*-

from quantity.digger.engine.strategy import *
from quantity.digger.config import settings
from quantity.digger.configutil import ConfigUtil
from quantity.digger.engine.series import NumberSeries, DateTimeSeries
from quantity.digger.technicals.common import *
from quantity.digger.util import rlogger, deprecated

__version__ = '0.4.0'


@deprecated
def set_config(cfg):
    """"""
    # from quantity.digger.datasource.data import locd
    # if 'source' in cfg:
    #     cfg['source'] = cfg['source'].lower()
    #     assert(cfg['source'] in ['sqlite', 'csv', 'mongodb'])
    settings.update(cfg)
    # locd.set_source(settings)


# set_config(settings)
