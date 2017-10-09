# -*- coding:utf-8 -*-


class __Globals:
    __redis_wrapper = None
    __etcd_wrapper = None
    __

    __heartbeat_dict = {}

    def __init__(self):
        pass

    def get_redis_wrapper(self):
        return self.__redis_wrapper

    def set_redis_wrapper(self, redis_wrapper):
        self.__redis_wrapper = redis_wrapper


Globals = __Globals()
