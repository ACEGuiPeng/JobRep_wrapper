# -*- coding:utf-8 -*-
import contextlib
import threading
import happybase
import time

from loggers.logger import log

from src.common.const import CONST

DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 9090

Lock = threading.Lock()


class HbaseWrapper(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            try:
                Lock.acquire()
                if not hasattr(cls, '_instance'):
                    cls._instance = super(HbaseWrapper, cls).__new__(cls)
            finally:
                Lock.release()
        return cls._instance

    def __init__(self, host=DEFAULT_HOST, port=DEFAULT_PORT, timeout=None,
                 autoconnect=True
                 ):
        self.hbase_host = host
        self.hbase_port = port
        self.timeout = timeout
        self.autoconnect = autoconnect
        self.connection_pool = happybase.ConnectionPool(CONST.HAPPYBASE_POOL_SIZE, host=self.hbase_host,
                                                        port=self.hbase_port,
                                                        autoconnect=True)
        self.reconnect_count = 0
        log.info('init hbase: {}'.format(host))

    @contextlib.contextmanager
    def connect(self):
        try:
            self.connection_pool.connection(self.timeout)
        except Exception as e:
            while self.reconnect_count < CONST.HAPPYBASE_RECONNECT_TIMES:
                self.reconnect_count += 1
                log.error('connect hbase:  {} error,start reconnecting,has retried {} times'.format(self.hbase_host,
                                                                                                    self.reconnect_count))
                self.connect()
                time.sleep(CONST.HAPPYBASE_RECONNECT_WAIT_SECONDS)
            log.error('reconnect times have been max,please check the error')
            raise Exception(str(e))

    def create_table(self, table_name, families):
        try:
            with self.connection_pool.connection(self.timeout) as connection:
                connection.create_table(
                    table_name,
                    families
                )
            log.info('target table: {} create successfully.'.format(table_name))
        except Exception as e:
            log.error('target table: {} create fail.'.format(table_name, str(e)))
            raise Exception(str(e))

    def get_table(self, table_name):
        try:
            with self.connection_pool.connection(self.timeout) as connection:

                target_table = connection.table(table_name)
            log.debug('target table: {} get successfully.'.format(table_name))
        except Exception as e:
            log.error('target table: {} get fail.'.format(table_name, str(e)))
            raise Exception(str(e))
        return target_table

    def del_table(self, table_name):
        try:
            with self.connection_pool.connection(self.timeout) as connection:

                connection.delete_table(table_name)
            log.debug('delete table: {} successfully.'.format(table_name))
        except Exception as e:
            log.error('delete table: {} get fail.'.format(table_name, str(e)))
            raise Exception(str(e))
