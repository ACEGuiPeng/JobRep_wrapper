# -*- coding:utf-8 -*-
from orm.tables import Base, Material
from wrappers.mysql_wrapper import MysqlWrapper
from common.const import CONST

mysql_wrapper = MysqlWrapper()
mysql_wrapper.connect_mysql(CONST.DB_NAME)


def insert_material(dict_data):
    with mysql_wrapper.session_scope() as session:
        ad_material = Material()
        ad_material.__dict__.update(dict_data)
        session.add(ad_material)

    return 'success'


def del_material(dict_data):
    with mysql_wrapper.session_scope() as session:
        target_obj = session.query(Material).filter_by(asin=dict_data['asin']).first()
        session.delete(target_obj)
    return 'success'


def update_material(dict_data):
    with mysql_wrapper.session_scope() as session:
        session.query(Material).filter_by(asin=dict_data['asin']).update(dict_data)
    return 'success'


def select_material(asin=None, uid=None, sorted_way=-1, key_words=None):
    '''
    :param uid:
    :param sorted_way: 默认值-1表示倒序排列，1表示正序排列
    :return:
    '''
    column_list = [
        'asin',
        'uid',
        'update_time',
        'name',
        'price',
        'title',
        'ad_text',
        'links',
        'keywords'
    ]
    with mysql_wrapper.session_scope() as session:
        if sorted_way == -1:
            exc_query = session.query(Material).order_by(Material.update_time.desc())
        else:
            exc_query = session.query(Material).order_by(Material.update_time.asc())

        obj_list = exc_query.filter_by(asin=asin, uid=uid).filter(
            Material.keywords.like("%{}%".format(key_words))).all()
        result_dict = [{key: obj.__dict__[key] for key in obj.__dict__ if key in column_list} for obj in obj_list]
    return result_dict
