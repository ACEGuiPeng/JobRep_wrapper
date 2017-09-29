# -*- coding:utf-8 -*-
from common.const import CONST
from orm.tables import Base, LandingPage
from wrappers.mysql_wrapper import MysqlWrapper

mysql_wrapper = MysqlWrapper()
mysql_wrapper.connect_mysql(CONST.DB_NAME)


def insert_landing_page(dict_data):
    with mysql_wrapper.session_scope() as session:
        landing_page = LandingPage()
        landing_page.__dict__.update(dict_data)
        session.add(landing_page)

    return 'success'


def del_landing_page(dict_data):
    with mysql_wrapper.session_scope() as session:
        target_obj = session.query(LandingPage).filter_by(id=dict_data['id']).first()
        session.delete(target_obj)
    return 'success'


def update_landing_page(dict_data):
    with mysql_wrapper.session_scope() as session:
        session.query(LandingPage).filter_by(id=dict_data['id']).update(dict_data)
    return 'success'


def select_landing_page():
    column_list = [
        'id',
        'uid',
        'update_time',
        'template_id',
        'attributes',
    ]
    with mysql_wrapper.session_scope() as session:
        obj_list = session.query(LandingPage).all()
        result_dict = [{key: obj.__dict__[key] for key in obj.__dict__ if key in column_list} for obj in obj_list]
    return result_dict
