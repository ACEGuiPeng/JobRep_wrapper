# -*- coding:utf-8 -*-
import traceback

import hdfs
from os.path import exists

from common.const import CONST
from loggers.logger import log


class HdfsWrapper:
    def __init__(self):
        self.client = None

    def connect_hdfs(self):
        self.client = hdfs.Client(CONST.HDFS_URL,CONST.HDFS_ROOT_PATH)

    def mkdir_hdfs(self, path):
        if not exists(path):
            self.client.mkdirs(path)

    def list_hdfs(self, path):
        return self.client.list(path)

    def read_hdfs(self, path):
        try:
            if exists(path):
                with self.client.read(path)as reader:
                    return reader.read()
        except:
            log.error(traceback.format_exc())
            self.connect_hdfs()
            log.error('reconnect hdfs...')

    def write_hdfs(self, path, value, overwrite=True):
        try:
            with self.client.write(path, overwrite=overwrite)as writer:
                writer.write(value)
        except:
            log.error(traceback.format_exc())
            self.connect_hdfs()
            log.error('reconnect hdfs...')

    def upload_hdfs(self):
        pass

    def download_hdfs(self):
        pass
