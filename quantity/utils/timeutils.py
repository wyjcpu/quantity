# -*- coding: utf-8 -*-
from datetime import timedelta
import datetime
import requests
import time

try:
    from functools import lru_cache
except ImportError as e:
    def lru_cache(maxsize=100):
        """Double-barrel least-recently-used cache decorator. This is a simple
        LRU algorithm that keeps a primary and secondary dict. Keys are checked
        in the primary dict, and then the secondary. Once the primary dict fills
        up, the secondary dict is cleared and the two dicts are swapped.
        
        This function duplicates (more-or-less) the protocol of the
        ``functools.lru_cache`` decorator in the Python 3.2 standard library.

        Arguments to the cached function must be hashable.

        View the cache statistics named tuple (hits, misses, maxsize, currsize)
        with f.cache_info().  Clear the cache and statistics with f.cache_clear().
        Access the underlying function with f.__wrapped__.
        """

        def decorating_function(user_function):
            # Cache1, Cache2, Pointer, Hits, Misses
            stats = [{}, {}, 0, 0, 0]

            @wraps(user_function)
            def wrapper(*args):
                ptr = stats[2]
                a = stats[ptr]
                b = stats[not ptr]
                key = args

                if key in a:
                    stats[3] += 1  # Hit
                    return a[key]
                elif key in b:
                    stats[3] += 1  # Hit
                    return b[key]
                else:
                    stats[4] += 1  # Miss
                    result = user_function(*args)
                    a[key] = result
                    if len(a) >= maxsize:
                        stats[2] = not ptr
                        b.clear()
                    return result

            def cache_info():
                """Report cache statistics"""
                return (stats[3], stats[4], maxsize, len(stats[0]) + len(stats[1]))

            def cache_clear():
                """Clear the cache and cache statistics"""
                stats[0].clear()
                stats[1].clear()
                stats[3] = stats[4] = 0

            wrapper.cache_info = cache_info
            wrapper.cache_clear = cache_clear

            return wrapper
        return decorating_function



@lru_cache()
def is_holiday(day):
    """
    判断是否节假日, api 来自百度 apistore: http://apistore.baidu.com/apiworks/servicedetail/1116.html
    :param day: 日期， 格式为 '20160404'
    :return: bool
    """
    api = 'http://tool.bitefu.net/jiari/'
    params = {'d': day, 'apiserviceid': 1116}
    rep = requests.get(api, params)
    res = rep.text

    return True if res != "0" else False


def is_holiday_today():
    """
    判断今天是否时节假日
    :return: bool
    """
    today = datetime.date.today().strftime('%Y%m%d')

    return is_holiday(today)


def is_tradetime_now():
    """
    判断目前是不是交易时间, 并没有对节假日做处理
    :return: bool
    """
    now_time = time.localtime()
    now = (now_time.tm_hour, now_time.tm_min, now_time.tm_sec)
    
    if (9, 15, 0) <= now <= (11, 30, 0) or (13, 0, 0) <= now <= (15, 0, 0):
        return True

    return False


def calc_next_trade_time_delta_seconds():
    now_time = datetime.datetime.now()
    now = (now_time.hour, now_time.minute, now_time.second)
    
    if now < (9, 15, 0):
        next_trade_start = now_time.replace(hour=9, minute=15, second=0, microsecond=0)
    elif (12, 0, 0) < now < (13, 0, 0):
        next_trade_start = now_time.replace(hour=13, minute=0, second=0, microsecond=0)
    elif now > (15, 0, 0):
        distance_next_work_day = 1
        
        while True:
            target_day = now_time + timedelta(days=distance_next_work_day)
            
            if is_holiday(target_day.strftime('%Y%m%d')):
                distance_next_work_day += 1
            else:
                break

        day_delta = timedelta(days=distance_next_work_day)
        next_trade_start = (now_time + day_delta).replace(hour=9, minute=15, second=0, microsecond=0)
    else:
        return 0

    time_delta = next_trade_start - now_time

    return time_delta.total_seconds()
