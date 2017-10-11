# -*- coding:utf-8 -*-
import time

from common.const import CONST
from orm.tables import ResourceRecord
from orm.tables import Resources
from web.service.globals import Globals


def upload_files(file_objs, data):
    upload_paths = []
    for file in file_objs:
        file_suff_name = file.filename.split('.')[0]
        file_ext = '.{}'.format(file.filename.split('.', 1)[1])
        file.filename = file_suff_name + '{}'.format(int(time.time())) + file_ext

        hdfs_path = CONST.UPLOAD_FOLDER + '/resources/{}/{}/{}'.format(data['uid'], data['asin'], file.filename)
        file_data = file.read()
        upload_path = Globals.get_hdfs_wrapper.write_hdfs(hdfs_path, file_data)

        data['addr'] = upload_path
        insert_resource(data)
        upload_paths.append(CONST.HDFS_URL + upload_path)
    return upload_paths


def insert_resource(dict_data):
    with Globals.get_mysql_wrapper().session_scope() as session:
        resource = Resources()
        resource.__dict__.update(dict_data)
        session.add(resource)

    return 'success'


def delete_resource(dict_data):
    # 查询resource_record表看是否有记录
    with Globals.get_mysql_wrapper().session_scope as session:
        res_record = session.query(ResourceRecord).filter_by(depot_id=dict_data['id']).all()
    if len(res_record) > 0:
        # 有记录，返回提示信息
        return 'failed to delete,this resource has been used in other ad_case'
    else:
        # 无记录，先查记录,再通过hdfs删除，再删除记录
        with Globals.get_mysql_wrapper().session_scope() as session:
            target_obj = session.query(Resources).filter_by(id=dict_data['id']).first()
            if Globals.get_hdfs_wrapper.delete_hdfs(target_obj.addr):
                session.delete(target_obj)
                return 'success'
            else:
                return 'failed'


def update_resource(dict_data):
    with Globals.get_mysql_wrapper().session_scope() as session:
        session.query(Resources).filter_by(id=dict_data['id']).update(dict_data)
    return 'success'


def select_resource(uid=None, asin=None, sorted_way=-1, key_word=None):
    column_list = [
        'id',
        'uid',
        'asin',
        'update_time',
        'type',
        'fb_hash',
        'keywords',
        'addr'
    ]
    with Globals.get_mysql_wrapper().session_scope() as session:
        if sorted_way == -1:
            exce_query = session.query(Resources).order_by(Resources.update_time.desc())
        else:
            exce_query = session.query(Resources).order_by(Resources.update_time.asc())

        obj_list = exce_query.filter_by(uid=uid, asin=asin).filter(
            Resources.keywords.like("%{}%".format(key_word))).all()

        result_dict = [{key: obj.__dict__[key] for key in obj.__dict__ if key in column_list} for obj in obj_list]
    return result_dict
