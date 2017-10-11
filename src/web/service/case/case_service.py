# -*- coding:utf-8 -*-
from sqlalchemy import func

from orm.tables import AdCase
from web.service.globals import Globals


def insert_case(dict_data):
    with Globals.get_mysql_wrapper().session_scope() as session:
        ad_case = AdCase()
        ad_case.__dict__.update(dict_data)
        session.add(ad_case)
        new_id = session.query(func.max(AdCase.id)).one()[0]

    return new_id


def del_case(dict_data):
    with Globals.get_mysql_wrapper().session_scope() as session:
        session.query(AdCase).filter_by(uid=dict_data['uid']).filter(AdCase.id.in_(dict_data['id'])).delete(
            synchronize_session=False)
    return 'success'


def update_case(dict_data):
    with Globals.get_mysql_wrapper().session_scope() as session:
        session.query(AdCase).filter_by(id=dict_data['id']).update(dict_data)
    return 'success'


def select_case(dict_data, page_no=1, page_size=10, sorted_way=-1):
    column_list = [
        'id',
        'uid',
        'type',
        'update_time',
        'ad_records',
        'target_id',
        'status',
        'bidding'
    ]
    with Globals.get_mysql_wrapper().session_scope() as session:
        if sorted_way == -1:
            exce_query = session.query(AdCase).order_by(AdCase.update_time.desc())
        else:
            exce_query = session.query(AdCase).order_by(AdCase.update_time.asc())

        obj_list = exce_query.filter_by(status=dict_data['status'], asin=dict_data['asin']).offset(page_no - 1).limit(
            page_size)

        all_count = len(obj_list)
    result_dict = {'all_count': all_count, 'cases':
        [{key: obj.__dict__[key] for key in obj.__dict__ if key in column_list} for obj in obj_list]}
    return result_dict


def update_case_status(dict_data):
    with Globals.get_mysql_wrapper().session_scope() as session:
        session.query(AdCase).filter_by(id=dict_data['id']).update(status=dict_data['status'])
    return 'success'
