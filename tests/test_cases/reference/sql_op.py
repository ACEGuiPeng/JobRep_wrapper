from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .utils import log, error_exception_decorate

ModelBase = declarative_base()


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


@singleton
class SqlConnection:

    def __init__(self):
        self.engine = None

    def connect(self, conn_str, debug=False, pool_recycle=900):
        self.engine = create_engine(conn_str, echo=debug, pool_recycle=pool_recycle)

    @error_exception_decorate
    def create_table(self):
        log.info('creating sql tables.')
        ModelBase.metadata.create_all(self.engine)

    @error_exception_decorate
    def get_global_session(self):
        return sessionmaker(bind=self.engine)

    @error_exception_decorate
    def get_session(self):
        return scoped_session(sessionmaker(bind=self.engine))


class SqlSession:
    def __enter__(self):
        self.conn = SqlConnection()
        self.session = self.conn.get_session()
        # log.info('enter session: {} of {}'.format(self.session, self.conn))
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        # log.info('remove sql session: {} of {}'.format(self.session, self.conn))
        self.session.remove()


