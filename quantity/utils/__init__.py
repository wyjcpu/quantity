# -*- coding: utf-8 -*-
# from .timeutils import *
# from .stock import *s
# __version__ = '0.1.2'

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