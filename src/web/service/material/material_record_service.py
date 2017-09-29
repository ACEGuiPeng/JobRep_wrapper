# -*- coding:utf-8 -*-
from common.const import CONST
from orm.tables import Base, MaterialRecord
from wrappers.mysql_wrapper import MysqlWrapper

mysql_wrapper = MysqlWrapper()
mysql_wrapper.connect_mysql(CONST.DB_NAME)


def insert_material_record(dict_data):
    with mysql_wrapper.session_scope() as session:
        material_record = MaterialRecord()
        material_record.__dict__.update(dict_data)
        session.add(material_record)

    return 'success'


def del_material_record(dict_data):
    with mysql_wrapper.session_scope() as session:
        target_obj = session.query(MaterialRecord).filter_by(id=dict_data['id']).first()
        session.delete(target_obj)
    return 'success'


def update_material_record(dict_data):
    with mysql_wrapper.session_scope() as session:
        session.query(MaterialRecord).filter_by(id=dict_data['id']).update(dict_data)
    return 'success'


def select_material_record():
    column_list = [
        'id',
        'asin',
        'record_time',
        'resource',
        'title',
        'ad_text',
        'type',
        'link'
    ]
    with mysql_wrapper.session_scope() as session:
        obj_list = session.query(MaterialRecord).all()
        result_dict = [{key: obj.__dict__[key] for key in obj.__dict__ if key in column_list} for obj in obj_list]
    return result_dict
