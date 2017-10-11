# -*- coding:utf-8 -*-
from unittest import TestCase

from initializer.initializer import init, de_init
from web.service.globals import Globals


class WrapperTest(TestCase):
    def setUp(self):
        init()

    def tearDown(self):
        de_init()

    # Hbase
    def test_connect(self):
        Globals.get_hbase_wrapper().connect()

    def test_create_table(self):
        families = {
            'cf1': dict(max_versions=10),
            'cf2': dict(max_versions=1, block_cache_enabled=False),
            'cf3': dict(),  # use defaults
        }
        Globals.get_hbase_wrapper().create_table('test_table', families)
        table = Globals.get_hbase_wrapper().get_table('test_table')
        print(table)
