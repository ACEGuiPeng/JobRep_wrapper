# -*- coding:utf-8 -*-
from common.const import CONST
from loggers.logger import log
from orm.tables import Base
from web.service.globals import Globals
from wrappers.hbase_wrapper import HbaseWrapper
from wrappers.hdfs_wrapper import HdfsWrapper
from wrappers.mysql_wrapper import MysqlWrapper
from wrappers.redis_wrapper import RedisWrapper


class _BaseInitializer:
    def __init__(self):
        self.has_been_initializer = False

    @classmethod
    def _init_redis(cls):
        redis_wrapper = RedisWrapper(host=CONST.REDIS_HOST,
                                     port=CONST.REDIS_PORT,
                                     password=CONST.REDIS_PASSWORD,
                                     max_connections=CONST.MAX_REDIS_CONNECTION)

        Globals.set_redis_wrapper(redis_wrapper)

    @classmethod
    def _init_mysql(cls):
        mysql_wrapper = MysqlWrapper()
        mysql_wrapper.connect_mysql(CONST.DB_NAME)
        mysql_wrapper.create_tables(Base)
        Globals.set_hbase_wrapper(mysql_wrapper)

    @classmethod
    def _init_hbase(cls):
        hbase_wrapper = HbaseWrapper(host=CONST.HBASE_HOST, port=CONST.HBASE_PORT)
        Globals.set_hbase_wrapper(hbase_wrapper)

    @classmethod
    def _init_hdfs(cls):
        hdfs_wrapper = HdfsWrapper()
        hdfs_wrapper.connect_hdfs()
        Globals.set_hdfs_wrapper(hdfs_wrapper)

    def initialize(self):
        log.info('try to initialize the base wrappers.')
        if self.has_been_initializer:
            log.info('system management has been initialized yet.')
            return

        # Attention: Don't change the order for initializing component.
        # env --> etcd --> setting --> redis --> stat
        self._init_redis()
        self._init_mysql()
        self._init_hdfs()
        self._init_hbase()

        log.info('base initialize successfully.')
        self.has_been_initializer = True

    def de_initialize(self):
        try:
            log.info('try to de-initialize the system management.')
            if not self.has_been_initializer:
                log.info('base has not been initialized.')
                return

            self.has_been_initializer = False
            log.info('base de initialize successfully.')
        except Exception as err:
            log.info('stop base initializer error {}'.format(err))


BS_INITIALIZER = _BaseInitializer()
