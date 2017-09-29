# -*- coding:utf-8 -*-
from wrappers.hdfs_wrapper import HdfsWrapper

hdfs_wrapper = HdfsWrapper()

if __name__ == '__main__':
    hdfs_wrapper.connect_hdfs()
    hdfs_wrapper.list_hdfs('/etc/hosts')
