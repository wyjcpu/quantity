# -*- coding: utf-8 -*-
from quantity.digger.configutil import ConfigUtil
from quantity.digger.infras.ioc import *
from quantity.digger.util import dlogger as logger

_ds_container = IoCContainer()


class _DatasourceTrunk(IoCTrunk):

    def __init__(self, cls, args, kwargs):
        super(_DatasourceTrunk, self).__init__(cls, args, kwargs)

    def on_register(self, name):
        logger.info('register datasource: {cls} => {name}',
                    cls=self.cls, name=name)

    def construct(self):
        a = [ConfigUtil.get(k, None) for k in self.args]
        ka = {k: ConfigUtil.get(name, None) for k, name in self.kwargs.items()}
        return self.cls(*a, **ka)


register_datasource = register_to(_ds_container, _DatasourceTrunk)
resolve_datasource = resolve_from(_ds_container)


def get_setting_datasource():
    ds_type = ConfigUtil.get('source')
    return resolve_datasource(ds_type)
