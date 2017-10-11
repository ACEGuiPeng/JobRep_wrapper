# -*- coding:utf-8 -*-
from orm.tables import LandingPageRecord
from web.service.globals import Globals


def insert_landing_page_record(dict_data):
    with Globals.get_mysql_wrapper.session_scope() as session:
        landing_page_record = LandingPageRecord()
        landing_page_record.__dict__.update(dict_data)
        session.add(landing_page_record)

    return 'success'


def del_landing_page_record(dict_data):
    with Globals.get_mysql_wrapper.session_scope() as session:
        target_obj = session.query(LandingPageRecord).filter_by(id=dict_data['id']).first()
        session.delete(target_obj)
    return 'success'


def update_landing_page_record(dict_data):
    with Globals.get_mysql_wrapper.session_scope() as session:
        session.query(LandingPageRecord).filter_by(id=dict_data['id']).update(dict_data)
    return 'success'


def select_landing_page_record(sorted_way=-1):
    column_list = [
        'id',
        'case_id',
        'landing_page_id',
        'uid',
        'template_id',
        'attributes'
    ]
    with Globals.get_mysql_wrapper.session_scope() as session:
        exec_query = session.query(LandingPageRecord)
        if sorted_way == -1:
            obj_list = exec_query.order_by(LandingPageRecord.update_time.desc()).all()
        else:
            obj_list = exec_query.order_by(LandingPageRecord.update_time.asc()).all()
        result_dict = [{key: obj.__dict__[key] for key in obj.__dict__ if key in column_list} for obj in obj_list]
    return result_dict
