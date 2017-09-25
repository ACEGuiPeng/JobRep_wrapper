# -*-coding:utf-8-*-

from threading import Thread

from wrapper.hbase_wrapper import HbaseWrapper

hbaseWrapper = HbaseWrapper('192.168.0.26', 2)


def connect_one():
    table = hbaseWrapper.get_table('student')
    print(table.rows([b'id1']))


if __name__ == '__main__':
    hbaseWrapper.connect()
    for i in range(1, 100):
        Thread(target=lambda: connect_one()).start()
