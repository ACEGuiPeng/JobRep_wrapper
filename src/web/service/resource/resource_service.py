# -*- coding:utf-8 -*-
from orm.tables import Base, Resources
from wrappers.mysql_wrapper import MysqlWrapper
from common.const import CONST

mysql_wrapper = MysqlWrapper()
mysql_wrapper.connect_mysql(CONST.DB_NAME)


def insert_resource(dict_data):
    with mysql_wrapper.session_scope() as session:
        resource = Resources()
        resource.__dict__.update(dict_data)
        session.add(resource)

    return 'success'


def del_resource(dict_data):
    with mysql_wrapper.session_scope() as session:
        target_obj = session.query(Resources).filter_by(id=dict_data['id']).first()
        session.delete(target_obj)
    return 'success'


def update_resource(dict_data):
    with mysql_wrapper.session_scope() as session:
        session.query(Resources).filter_by(id=dict_data['id']).update(dict_data)
    return 'success'


def select_resource(uid=None, asin=None, sorted_way=-1, key_words=None):
    column_list = [
        'id',
        'uid',
        'asin',
        'update_time',
        'type',
        'keywords',
        'addr'
    ]
    with mysql_wrapper.session_scope() as session:
        if sorted_way == -1:
            exce_query = session.query(Resources).order_by(Resources.update_time.desc())
        else:
            exce_query = session.query(Resources).order_by(Resources.update_time.asc())

        obj_list = exce_query.filter_by(uid=uid, asin=asin).filter(
            Resources.keywords.like("%{}%".format(key_words))).all()

        result_dict = [{key: obj.__dict__[key] for key in obj.__dict__ if key in column_list} for obj in obj_list]
    return result_dict
