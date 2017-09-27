# -*- coding:utf-8 -*-
from orm.tables import Base, Material
from wrappers.mysql_wrapper import MysqlWrapper

mysql_wrapper = MysqlWrapper()
mysql_wrapper.connect_mysql('test_db', Base)


def add_material(dict_data):
    with mysql_wrapper.get_session() as session:
        ad_material = Material()
        ad_material.__dict__.update(dict_data)
        session.add(ad_material)

    return 'success'


def del_material(dict_data):
    with mysql_wrapper.get_session() as session:
        target_obj = session.query(Material).filter_by(sid=dict_data['sid']).first()
        session.delete(target_obj)
    return 'success'


def update_material(dict_data):
    with mysql_wrapper.get_session() as session:
        session.query(Material).filter_by(sid=dict_data['sid']).update(dict_data)
    return 'success'


def query_material():
    column_list = [
        'sid',
        'timestamp',
        'content'
    ]
    with mysql_wrapper.get_session() as session:
        obj_list = session.query(Material).all()
        print(obj_list)
        result_dict = [{key: obj.__dict__[key] for key in obj.__dict__ if key in column_list} for obj in obj_list]
    return result_dict
