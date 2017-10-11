# -*- coding:utf-8 -*-
from orm.tables import MaterialRecord
from web.service.globals import Globals


def insert_material_record(dict_data):
    with Globals.get_mysql_wrapper.session_scope() as session:
        material_record = MaterialRecord()
        material_record.__dict__.update(dict_data)
        session.add(material_record)

    return 'success'


def del_material_record(dict_data):
    with Globals.get_mysql_wrapper.session_scope() as session:
        target_obj = session.query(MaterialRecord).filter_by(id=dict_data['id']).first()
        session.delete(target_obj)
    return 'success'


def update_material_record(dict_data):
    with Globals.get_mysql_wrapper.session_scope() as session:
        session.query(MaterialRecord).filter_by(id=dict_data['id']).update(dict_data)
    return 'success'


def select_material_record():
    column_list = [
        'id',
        'case_id',
        'asin',
        'resource',
        'name',
        'description',
        'type',
        'link'
    ]
    with Globals.get_mysql_wrapper.session_scope() as session:
        obj_list = session.query(MaterialRecord).all()
        result_dict = [{key: obj.__dict__[key] for key in obj.__dict__ if key in column_list} for obj in obj_list]
    return result_dict
