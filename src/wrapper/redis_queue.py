# -*-coding:utf-8-*-

from loggers.logger import log

from src.common.const import CONST


class RedisQueue(object):
    def __init__(self, name, redis_conn, namespace='queue'):
        self.redis_conn = redis_conn
        self.key = '%s:%s' % (namespace, name)

    def reset_conn(self, redis_conn):
        self.redis_conn = redis_conn

    def get_redis_conn(self):
        return self.redis_conn

    def queue_size(self):
        return self.redis_conn.llen(self.key)

    def is_empty(self):
        return self.queue_size() == 0

    def put(self, item):
        self.redis_conn.rpush(self.key, item)

    def delete(self):
        self.redis_conn.delete(self.key)

    def get(self, block=False, timeout=None):
        try:
            if block:
                item = self.redis_conn.blpop(self.key, timeout=timeout)
            else:
                item = self.redis_conn.lpop(self.key)

            if item:
                item_result = item.decode(CONST.UTF_8)
            else:
                item_result = None
        except Exception as error:
            log.error(str(error))
            item_result = None

        return item_result
