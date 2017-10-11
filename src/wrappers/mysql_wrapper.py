# -*- coding: UTF-8 -*-
import contextlib
import logging
import threading
import traceback

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from common.const import CONST
from loggers.logger import log

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

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

    def create_tables(self, base):
        try:
            log.info('creating sql tables.')
            base.metadata.create_all(self.engine)
        except Exception as e:
            log.error('create tables failed {}'.format(str(e)))

    def connect_mysql(self, db_name):
        try:
            self.engine = create_engine(
                'mysql+mysqlconnector://{username}:{pwd}@{db_url}/{db_name}'.format(
                    username=CONST.MYSQL_USERNAME, pwd=CONST.MYSQL_PWD, db_url=CONST.DB_URL, db_name=db_name))

            DB_Session = sessionmaker(bind=self.engine)

            self.session = DB_Session()

        except Exception as e:
            log.error('{}'.format('', str(e)))
            raise traceback.format_exc(30)

    @contextlib.contextmanager
    def session_scope(self):
        try:
            # with 代码执行的部分
            yield self.session
            # with包裹的代码
            self.session.commit()
        except Exception:
            self.session.rollback()
            log.error(traceback.format_exc(30))
        finally:
            self.session.close()
