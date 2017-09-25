# -*- coding: UTF-8 -*-
import threading

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

from common.const import CONST
from loggers.logger import log

Lock = threading.Lock()


class MysqlWrapper(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            try:
                Lock.acquire()
                if not hasattr(cls, '_instance'):
                    cls._instance = super(MysqlWrapper, cls).__new__(cls)
            finally:
                Lock.release()
        return cls._instance

    def __init__(self):
        self.session = None
        self.engine = None
        log.info('init mysql: {}'.format(CONST.DB_URL))

    def connect_mysql(self, db_name, base):
        try:
            self.engine = create_engine(
                'mysql+mysqlconnector://{username}:{pwd}@{db_url}/{db_name}'.format(
                    username=CONST.MYSQL_USERNAME, pwd=CONST.MYSQL_PWD, db_url=CONST.DB_URL, db_name=db_name),
                echo=True)

            DB_Session = sessionmaker(bind=self.engine)

            self.session = DB_Session()
            base.metadata.create_all(self.engine)

        except Exception as e:
            log.error('{}'.format('', str(e)))
            raise Exception(str(e))

    def add_info(self, table_obj):
        try:
            self.session.add(table_obj)
            self.session.commit()
        except Exception as e:
            log.error('{}'.format('', str(e)))
            raise Exception(str(e))

    def add_info_list(self, table_obj_list):
        try:
            self.session.add_all(table_obj_list)
            self.session.commit()
        except Exception as e:
            log.error('{}'.format('', str(e)))
            raise Exception(str(e))

    def delete_info(self, table_obj):
        try:
            self.session.delete(table_obj)
            self.session.commit()
        except Exception as e:
            log.error('{}'.format('', str(e)))
            raise Exception(str(e))

    def update_info(self, target_obj, target_criteria, data_dict):
        try:
            self.session.query(target_obj).filter(target_criteria).updata(data_dict)
            self.session.commit()
        except Exception as e:
            log.error('{}'.format('', str(e)))
            raise Exception(str(e))

    def query_all_info(self, target_obj):
        try:
            result = self.session.query(target_obj).all()
            return result
        except Exception as e:
            log.error('{}'.format('', str(e)))
            raise Exception(str(e))
