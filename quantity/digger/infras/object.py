# -*- coding: utf-8 -*-
class _HashObjectImpl(object):
    def __str__(self):
        keys = filter(lambda k: not k.startswith('__'), dir(self))
        d = {}
        for k in keys:
            d[k] = getattr(self, k)
        return str(d)


class HashObject(object):
    @staticmethod
    def new(**kwargs):
        obj = _HashObjectImpl()
        for k, v in kwargs.items():
            setattr(obj, k, v)
        return obj
