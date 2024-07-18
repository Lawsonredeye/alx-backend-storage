#!/usr/bin/env python3
"""
cache file which connects to the redis server and pass a redis.Redis object
connection to an instance
"""

import redis
from uuid import uuid4
import typing
from functools import wraps


def count_calls(method: callable):
    @wraps(count_calls)
    def increment(__qualname__):
        count = 0
        if __qualname__:
            count += 1
            return count
    return increment

class Cache:
    """
    stores the data into hash on the redis server but flushes the db first
    before adding into the cache system
    """

    def __init__(self) -> None:
        """initilizer"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: typing.Any) -> str:
        """
        stores the persisted data into the redis cache system with a uuid4

        Parameter:
            data: typing.Any
                data to be stored into the database which could ne a byte, str
                integer, or even list

        Returns:
            key: str
                string value of what was passed to the cache
        """
        key: str = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: typing.Callable = None):
        get_key = self._redis.get(key)
        if not get_key:
            return None
        if fn:
            return fn(get_key)
        return get_key

    def get_str(cls):
        """Auto parameterize the cache" into str"""
        return str(cls.get)

    def get_int(cls):
        """Auto parameterize the cache" into int"""
        return int(cls.get)
