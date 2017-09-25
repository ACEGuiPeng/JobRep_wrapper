from wrapper.mysql_wrapper import MysqlWrapper


mysql_wrapper = MysqlWrapper()

if __name__ == '__main__':
    mysql_wrapper.connect_mysql()
