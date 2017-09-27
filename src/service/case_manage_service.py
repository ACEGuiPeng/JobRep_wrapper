# -*- coding:utf-8 -*-
from loggers.logger import log
from orm.tables import Base, AdCase
from wrappers.mysql_wrapper import MysqlWrapper

mysql_wrapper = MysqlWrapper()
mysql_wrapper.connect_mysql('test_db', Base)


def add_case(dict_data):
    with mysql_wrapper.get_session() as session:
        ad_case = AdCase()
        ad_case.__dict__.update(dict_data)
        session.add(ad_case)

    return 'success'


def del_case(dict_data):
    with mysql_wrapper.get_session() as session:
        target_obj = session.query(AdCase).filter_by(sid=dict_data['sid']).first()
        session.delete(target_obj)
    return 'success'


def update_case(dict_data):
    with mysql_wrapper.get_session() as session:
        session.query(AdCase).filter_by(sid=dict_data['sid']).update(dict_data)
    return 'success'


def query_case():
    column_list = [
        'sid',
        'timestamp',
        'case_name',
        'target_id',
        'material_timestamp',
        'status',
        'bidding'
    ]
    with mysql_wrapper.get_session() as session:
        obj_list = session.query(AdCase).all()
        print(obj_list)
        result_dict = [{key:obj.__dict__[key] for key in obj.__dict__ if key in column_list} for obj in obj_list]
    return result_dict
