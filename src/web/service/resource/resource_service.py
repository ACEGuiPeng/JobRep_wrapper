# -*- coding:utf-8 -*-
from orm.tables import Base, Resources
from wrappers.hdfs_wrapper import HdfsWrapper
from wrappers.mysql_wrapper import MysqlWrapper
from common.const import CONST

mysql_wrapper = MysqlWrapper()
mysql_wrapper.connect_mysql(CONST.DB_NAME)

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


def insert_resource(dict_data):
    with mysql_wrapper.session_scope() as session:
        resource = Resources()
        resource.__dict__.update(dict_data)
        session.add(resource)

    return 'success'


def del_resource(dict_data):
    with mysql_wrapper.session_scope() as session:
        target_obj = session.query(Resources).filter_by(id=dict_data['id']).first()
        session.delete(target_obj)
    return 'success'


def update_resource(dict_data):
    with mysql_wrapper.session_scope() as session:
        session.query(Resources).filter_by(id=dict_data['id']).update(dict_data)
    return 'success'


def select_resource(uid=None, asin=None, sorted_way=-1, key_words=None):
    column_list = [
        'id',
        'uid',
        'asin',
        'update_time',
        'type',
        'keywords',
        'addr'
    ]
    with mysql_wrapper.session_scope() as session:
        if sorted_way == -1:
            exce_query = session.query(Resources).order_by(Resources.update_time.desc())
        else:
            exce_query = session.query(Resources).order_by(Resources.update_time.asc())

        obj_list = exce_query.filter_by(uid=uid, asin=asin).filter(
            Resources.keywords.like("%{}%".format(key_words))).all()

        result_dict = [{key: obj.__dict__[key] for key in obj.__dict__ if key in column_list} for obj in obj_list]
    return result_dict
