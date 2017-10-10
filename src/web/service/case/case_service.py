# -*- coding:utf-8 -*-
from orm.tables import AdCase
from web.service.globals import Globals


def insert_case(dict_data):
    with Globals.get_mysql_wrapper.session_scope() as session:
        ad_case = AdCase()
        ad_case.__dict__.update(dict_data)
        session.add(ad_case)

    return 'success'


def del_case(dict_data):
    with Globals.get_mysql_wrapper.session_scope() as session:
        target_obj = session.query(AdCase).filter_by(id=dict_data['id']).first()
        session.delete(target_obj)
    return 'success'


def update_case(dict_data):
    with Globals.get_mysql_wrapper.session_scope() as session:
        session.query(AdCase).filter_by(id=dict_data['id']).update(dict_data)
    return 'success'


def select_case(case_ids=None):
    column_list = [
        'id',
        'uid',
        'type',
        'ad_records',
        'target_id',
        'status',
        'bidding'
    ]
    with Globals.get_mysql_wrapper.session_scope() as session:
        if case_ids is None:
            obj_list = session.query(AdCase).all()
        else:
            obj_list = session.query(AdCase).filter(AdCase.id.in_(tuple(case_ids))).all()
    result_dict = [{key: obj.__dict__[key] for key in obj.__dict__ if key in column_list} for obj in obj_list]
    return result_dict


def update_case_status(dict_data):
    with Globals.get_mysql_wrapper.session_scope() as session:
        session.query(AdCase).filter_by(id=dict_data['id']).update(status=dict_data['status'])
    return 'success'
