import hdfs
import traceback

from common.utils import error_exception_decorate
from loggers.logger import log


class HdfsOperation:
    _client = None
    _parm_handler = None
    _dns_name_handler = None

    @classmethod
    def set_parm_handler(cls, parm_handler):
        cls._parm_handler = parm_handler

    @classmethod
    def set_dns_name_handler(cls, dns_name_handler):
        cls._dns_name_handler = dns_name_handler

    @classmethod
    def connect_hdfs(cls):
        cls._client = hdfs.Client(**cls._parm_handler())
        cls.handle_dns()

    @classmethod
    def handle_dns(cls):
        try:
            dns_name_set = cls._dns_name_handler()
            with open('/etc/hosts')as f:
                old_dns_name_set = set(f.readlines())

            new_dns_name_set = dns_name_set - old_dns_name_set
            if new_dns_name_set:
                with open('/etc/hosts', 'a')as f:
                    f.writelines(new_dns_name_set)
        except Exception as e:
            log.warning(str(e))

    @classmethod
    def read_hdfs(cls, path):
        try:
            with cls._client.read(path)as reader:
                return reader.read()
        except:
            log.error(traceback.format_exc())
            cls.connect_hdfs()
            log.error('reconnect hdfs...')

    @classmethod
    def write_hdfs(cls, path, value, overwrite=True):
        try:
            with cls._client.write(path, overwrite=overwrite)as writer:
                writer.write(value)
        except:
            log.error(traceback.format_exc())
            cls.connect_hdfs()
            log.error('reconnect hdfs...')

    @classmethod
    @error_exception_decorate
    def list_hdfs(cls, path):
        return cls._client.list(path)

    @classmethod
    @error_exception_decorate
    def mkdirs_hdfs(cls, path):
        cls._client.makedirs(path)
