# -*- coding:utf-8 -*-
import time

from web.service.resource.resource_service import *
from wrappers.hdfs_wrapper import HdfsWrapper

hdfs_wrapper = HdfsWrapper()
hdfs_wrapper.connect_hdfs()


def upload_files(file_obj, data):
    file_suff_name = file_obj.filename.split('.')[0]
    file_ext = '.{}'.format(file_obj.filename.split('.', 1)[1])
    file_obj.filename = file_suff_name + '{}'.format(int(time.time())) + file_ext

    hdfs_path = CONST.UPLOAD_FOLDER + '/{}/{}/{}'.format(data['uid'], data['asin'], file_obj.filename)
    file_data = file_obj.read()
    upload_path = hdfs_wrapper.write_hdfs(hdfs_path, file_data)

    data['addr'] = upload_path
    insert_resource(data)
    return CONST.HDFS_URL + upload_path


def delete_files():
    pass


def get_files():
    pass
