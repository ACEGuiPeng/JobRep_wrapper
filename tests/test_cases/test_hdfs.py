# -*- coding:utf-8 -*-

from hdfs import InsecureClient
from os.path import exists

if __name__ == '__main__':
    hdsf_cli = InsecureClient('http://192.168.0.222:50070')
    path_list = hdsf_cli.list('/home/yiguo/yiguo_fbad/uploads/000001/23429')
    # path = hdsf_cli.upload('/home/yiguo/yiguo_fbad', '../../data/uploads/001.jpg', overwrite=True)
    #print(path)
    # hdsf_cli.delete('/home/yiguo/yiguo_fbad/uploads/000001/23429')
    exists
    print(path_list)
