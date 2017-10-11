# -*- coding:utf-8 -*-
from wrappers.hbase_wrapper import HbaseWrapper
from wrappers.hdfs_wrapper import HdfsWrapper
from wrappers.mysql_wrapper import MysqlWrapper
from wrappers.redis_queue import RedisQueue
from wrappers.redis_wrapper import RedisWrapper


class __Globals:
    __hbase_wrapper = None
    __hdfs_wrapper = None
    __mysql_wrapper = None
    __redis_queue = None
    __redis_wrapper = None

    def __init__(self):
        pass

    def get_hbase_wrapper(self) -> HbaseWrapper:
        return self.__hbase_wrapper

    def set_hbase_wrapper(self, hbase_wrapper):
        self.__hbase_wrapper = hbase_wrapper

    def get_hdfs_wrapper(self) -> HdfsWrapper:
        return self.__hdfs_wrapper

    def set_hdfs_wrapper(self, hdfs_wrapper):
        self.__hdfs_wrapper = hdfs_wrapper

    def get_mysql_wrapper(self) -> MysqlWrapper:
        return self.__mysql_wrapper

    def set_mysql_wrapper(self, mysql_wrapper):
        self.__mysql_wrapper = mysql_wrapper

    def get_redis_queue(self) -> RedisQueue:
        return self.__redis_queue

    def set_redis_queue(self, redis_queue):
        self.__redis_queue = redis_queue

    def get_redis_wrapper(self) -> RedisWrapper:
        return self.__redis_wrapper

    def set_redis_wrapper(self, redis_wrapper):
        self.__redis_wrapper = redis_wrapper


Globals = __Globals()
