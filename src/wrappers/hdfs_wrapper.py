# -*- coding:utf-8 -*-
import traceback

from hdfs import InsecureClient
from os.path import exists

from common.const import CONST
from loggers.logger import log


class HdfsWrapper:
    def __init__(self):
        self.client = None

    def connect_hdfs(self):
        self.client = InsecureClient(CONST.HDFS_URL, user=CONST.HDFS_USER)

    def mkdir_hdfs(self, path):
        if not exists(path):
            self.client.makedirs(path)

    def list_hdfs(self, path):
        return self.client.list(path)

    def read_hdfs(self, hdfs_path):
        try:
            with self.client.read(hdfs_path)as reader:
                return reader.read()
        except:
            log.error(traceback.format_exc())
            self.connect_hdfs()
            log.error('reconnect hdfs...')

    def write_hdfs(self, hdfs_path, data, overwrite=False):
        try:
            with self.client.write(hdfs_path, overwrite=overwrite)as writer:
                writer.write(data)
            return hdfs_path
        except:
            log.error(traceback.format_exc())
            self.connect_hdfs()
            log.error('reconnect hdfs...')

    def delete_hdfs(self, hdfs_path, recursive=False):
        return self.client.delete(hdfs_path, recursive)
