# -*- coding:utf-8 -*-
from orm.tables import ResourceRecord
from web.service.globals import Globals


def insert_resource_record(dict_data):
    with Globals.get_mysql_wrapper.session_scope() as session:
        resource_record = ResourceRecord()
        resource_record.__dict__.update(dict_data)
        session.add(resource_record)

    return 'success'


def del_resource_record(dict_data):
    with Globals.get_mysql_wrapper.session_scope() as session:
        target_obj = session.query(ResourceRecord).filter_by(id=dict_data['id']).first()
        session.delete(target_obj)
    return 'success'


def update_resource_record(dict_data):
    with Globals.get_mysql_wrapper.session_scope() as session:
        session.query(ResourceRecord).filter_by(id=dict_data['id']).update(dict_data)
    return 'success'


def select_resource_record():
    column_list = [
        'id',
        'case_id',
        'resource_id',
        'uid',
    ]
    with Globals.get_mysql_wrapper.session_scope() as session:
        obj_list = session.query(ResourceRecord).all()
        result_dict = [{key: obj.__dict__[key] for key in obj.__dict__ if key in column_list} for obj in obj_list]
    return result_dict
