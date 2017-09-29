# -*- coding:utf-8 -*-
from orm.tables import Base, Resources
from wrappers.mysql_wrapper import MysqlWrapper
from common.const import CONST

mysql_wrapper = MysqlWrapper()
mysql_wrapper.connect_mysql(CONST.DB_NAME)


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


def select_resource():
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
        obj_list = session.query(Resources).all()
        result_dict = [{key: obj.__dict__[key] for key in obj.__dict__ if key in column_list} for obj in obj_list]
    return result_dict
