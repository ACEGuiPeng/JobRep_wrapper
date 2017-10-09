# -*- coding:utf-8 -*-
from wrappers.hdfs_wrapper import HdfsWrapper

if __name__ == '__main__':
    hdfs_wrapper = HdfsWrapper()
    hdfs_wrapper.connect_hdfs()
    print(hdfs_wrapper.list_hdfs('/home/yiguo/yiguo_fbad/uploads/000001/23429'))
    file = hdfs_wrapper.read_hdfs('/home/yiguo/yiguo_fbad/uploads/000001/23429')
    print(file)
