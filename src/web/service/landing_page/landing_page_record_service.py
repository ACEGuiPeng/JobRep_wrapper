# -*- coding:utf-8 -*-
from common.const import CONST
from orm.tables import Base, LandingPageRecord
from wrappers.mysql_wrapper import MysqlWrapper

mysql_wrapper = MysqlWrapper()
mysql_wrapper.connect_mysql(CONST.DB_NAME)


def insert_landing_page_record(dict_data):
    with mysql_wrapper.session_scope() as session:
        landing_page_record = LandingPageRecord()
        landing_page_record.__dict__.update(dict_data)
        session.add(landing_page_record)

    return 'success'


def del_landing_page_record(dict_data):
    with mysql_wrapper.session_scope() as session:
        target_obj = session.query(LandingPageRecord).filter_by(id=dict_data['id']).first()
        session.delete(target_obj)
    return 'success'


def update_landing_page_record(dict_data):
    with mysql_wrapper.session_scope() as session:
        session.query(LandingPageRecord).filter_by(id=dict_data['id']).update(dict_data)
    return 'success'


def select_landing_page_record():
    column_list = [
        'id',
        'depot_id',
        'uid',
        'asin',
        'case_id',
    ]
    with mysql_wrapper.session_scope() as session:
        obj_list = session.query(LandingPageRecord).all()
        result_dict = [{key: obj.__dict__[key] for key in obj.__dict__ if key in column_list} for obj in obj_list]
    return result_dict
