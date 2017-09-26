import time

from wrappers.mysql_wrapper import MysqlWrapper
from orm.tables import *

if __name__ == '__main__':
    mysql_wrapper = MysqlWrapper()
    # 测试连接/创建表
    mysql_wrapper.connect_mysql('test_db', Base)
    # 增加
    material = Material(sid='000001', timestamp=str(time.time()), content='测试添加内容')
    mysql_wrapper.add_info(material)
