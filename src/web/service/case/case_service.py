# -*- coding:utf-8 -*-
from common.const import CONST
from orm.tables import Base, AdCase
from wrappers.mysql_wrapper import MysqlWrapper

mysql_wrapper = MysqlWrapper()
mysql_wrapper.connect_mysql(CONST.DB_NAME, Base)


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
        result_dict = [{key: obj.__dict__[key] for key in obj.__dict__ if key in column_list} for obj in obj_list]
    return result_dict


def update_case_status(dict_data):
    with mysql_wrapper.get_session() as session:
        session.query(AdCase).filter_by(sid=dict_data['sid']).update(status=dict_data['status'])
    return 'success'
