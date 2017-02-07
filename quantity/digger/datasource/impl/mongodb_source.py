# -*- coding: utf-8 -*-

import pandas as pd
import pymongo
from pymongo import MongoClient

from quantity.digger.datasource import datautil
from quantity.digger.datasource.dsutil import *
from quantity.digger.datasource.source import SourceWrapper, DatasourceAbstract


@register_datasource('mongodb', 'address', 'port', 'dbname')
class MongoDBSource(DatasourceAbstract):
    '''MongoDBs数据源'''

    def __init__(self, address, port, dbname):
        # TODO address, port
        self._client = MongoClient()
        self._db = self._client[dbname]

    def _get_collection_name(self, period, exchange, code):
        return '{period}.{exchange}.{code}'.format(
            period=str(period).replace('.', ''),
            exchange=exchange,
            code=code)

    def _parse_collection_name(self, collection_name):
        return collection_name.split('.')

    def get_bars(self, pcontract, dt_start, dt_end):
        dt_start = pd.to_datetime(dt_start)
        dt_end = pd.to_datetime(dt_end)
        id_start, _ = datautil.encode2id(pcontract.period, dt_start)
        id_end, _ = datautil.encode2id(pcontract.period, dt_end)
        colname = self._get_collection_name(
            pcontract.period,
            pcontract.contract.exchange,
            pcontract.contract.code)
        cursor = self._db[colname].find({
            'id': {
                '$gt': id_start,
                '$lt': id_end
            }
        }).sort('id', pymongo.ASCENDING)
        data = pd.DataFrame(list(cursor)).set_index('datetime')
        return SourceWrapper(pcontract, data, len(data))

    def get_last_bars(self, pcontract, n):
        raise NotImplementedError

    def get_contracts(self):
        colname = 'contract'
        cursor = self._db[colname].find()
        return pd.DataFrame(list(cursor))

    def get_code2strpcon(self):
        symbols = {}
        period_exchange2strpcon = {}
        names = self._db.collection_names()
        symbols = {}
        period_exchange2strpcon = {}
        for name in filter(lambda n: n == 'system.indexes', names):
            period, exch, code = self._parse_collection_names(name)
            period_exch = '%s-%s' % (exch, period)
            strpcon = '%s.%s' % (code, period_exch)
            lst = symbols.setdefault(code, [])
            lst.append(strpcon)
            lst = period_exchange2strpcon(period_exch, [])
            lst.append(strpcon)
            return symbols, period_exchange2strpcon
