# -*- coding: UTF-8 -*-
import contextlib
import threading
import traceback

from sqlalchemy import create_engine
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
            raise traceback.format_exc(30)

    @contextlib.contextmanager
    def get_session(self):
        try:
            # with 代码执行的部分
            yield self.session
            # with包裹的代码
            self.session.commit()
        except Exception:
            log.error(traceback.format_exc(30))
