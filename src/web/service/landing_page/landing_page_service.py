# -*- coding:utf-8 -*-
from orm.tables import LandingPage
from web.service.globals import Globals


def insert_landing_page(dict_data):
    with Globals.get_mysql_wrapper.session_scope() as session:
        landing_page = LandingPage()
        landing_page.__dict__.update(dict_data)
        session.add(landing_page)

    return 'success'


def del_landing_page(dict_data):
    with Globals.get_mysql_wrapper.session_scope() as session:
        target_obj = session.query(LandingPage).filter_by(id=dict_data['id']).first()
        session.delete(target_obj)
    return 'success'


def update_landing_page(dict_data):
    with Globals.get_mysql_wrapper.session_scope() as session:
        session.query(LandingPage).filter_by(id=dict_data['id']).update(dict_data)
    return 'success'


def select_landing_page(data_dict, sorted_way=-1):
    column_list = [
        'id',
        'uid',
        'update_time',
        'template_id',
        'attributes',
    ]
    with Globals.get_mysql_wrapper.session_scope() as session:
        if sorted_way == -1:
            exec_query = session.query(LandingPage).order_by(LandingPage.update_time.desc())
        else:
            exec_query = session.query(LandingPage).order_by(LandingPage.update_time.asc())
        obj_list = exec_query.filter_by(uid=data_dict['uid'], id=data_dict['id'])
        result_dict = [{key: obj.__dict__[key] for key in obj.__dict__ if key in column_list} for obj in obj_list]
    return result_dict
