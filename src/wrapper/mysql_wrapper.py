# -*- coding: UTF-8 -*-

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

from common.const import CONST


class MysqlWrapper(object):
    def __init__(self):
        self.session = None
        self.metadata = MetaData()  # 获取元数据

    def connect_mysql(self, db_name):
        engine = create_engine(
            'mysql+mysqlconnector://{username}:{pwd}@{db_url}/{db_name}?charset=utf8",encoding="utf-8"'.format(
                username=CONST.MYSQL_USERNAME, pwd=CONST.MYSQL_PWD, db_url=CONST.DB_URL, db_name=db_name))
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def create_table(self):
        pass

    def add_info(self, obj):
        self.session.add(obj)
        self.session.commit()

    def add_info_list(self, obj_list):
        self.session.add_all(obj_list)
        self.session.commit()

    def delete_info(self, obj):
        self.session.delete(obj)
        self.session.commit()

    def update_info(self, target_obj, target_criteria, data_dict):
        self.session.query(target_obj).filter(target_criteria).updata(data_dict)
        self.session.commit()

    def query_all_info(self, target_obj):
        result = self.session.query(target_obj).all()
        return result
