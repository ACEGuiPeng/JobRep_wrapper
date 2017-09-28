# -*- coding:utf-8 -*-
from common.const import CONST
from orm.tables import Base, LandingPage
from wrappers.mysql_wrapper import MysqlWrapper

mysql_wrapper = MysqlWrapper()
mysql_wrapper.connect_mysql(CONST.DB_NAME, Base)


def add_landing_page(dict_data):
    with mysql_wrapper.get_session() as session:
        ad_landing_page = LandingPage()
        ad_landing_page.__dict__.update(dict_data)
        session.add(ad_landing_page)

    return 'success'


def del_landing_page(dict_data):
    with mysql_wrapper.get_session() as session:
        target_obj = session.query(LandingPage).filter_by(sid=dict_data['sid']).first()
        session.delete(target_obj)
    return 'success'


def update_landing_page(dict_data):
    with mysql_wrapper.get_session() as session:
        session.query(LandingPage).filter_by(sid=dict_data['sid']).update(dict_data)
    return 'success'


def query_landing_page():
    column_list = [
        'sid',
        'timestamp',
        'landing_page_name',
        'target_id',
        'material_timestamp',
        'status',
        'bidding'
    ]
    with mysql_wrapper.get_session() as session:
        obj_list = session.query(LandingPage).all()
        result_dict = [{key: obj.__dict__[key] for key in obj.__dict__ if key in column_list} for obj in obj_list]
    return result_dict
