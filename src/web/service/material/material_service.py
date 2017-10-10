# -*- coding:utf-8 -*-
from orm.tables import Material
from web.service.globals import Globals


def insert_material(dict_data):
    with Globals.get_mysql_wrapper.session_scope() as session:
        ad_material = Material()
        ad_material.__dict__.update(dict_data)
        session.add(ad_material)

    return 'success'


def del_material(dict_data):
    with Globals.get_mysql_wrapper.session_scope() as session:
        target_obj = session.query(Material).filter_by(asin=dict_data['asin']).first()
        session.delete(target_obj)
    return 'success'


def update_material(dict_data):
    with Globals.get_mysql_wrapper.session_scope() as session:
        session.query(Material).filter_by(asin=dict_data['asin']).update(dict_data)
    return 'success'


def select_material(asin, uid, sorted_way=-1, key_word=None):
    column_list = [
        'asin',
        'uid',
        'update_time',
        'product_name',
        'price',
        'name',
        'description',
        'links',
        'land_page_ids',
        'keywords'
    ]
    with Globals.get_mysql_wrapper.session_scope() as session:
        if sorted_way == -1:
            exc_query = session.query(Material).order_by(Material.update_time.desc())
        else:
            exc_query = session.query(Material).order_by(Material.update_time.asc())

        obj_list = exc_query.filter_by(asin=asin, uid=uid).filter(
            Material.keywords.like("%{}%".format(key_word))).all()
        result_dict = [{key: obj.__dict__[key] for key in obj.__dict__ if key in column_list} for obj in obj_list]
    return result_dict
