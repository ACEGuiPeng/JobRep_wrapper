# -*- coding:utf-8 -*-

from flask_restful import Resource

todoList = {
    '0': 'show',
    '1': 'pass',
    '-1': 'reject'
}


class CaseManage(Resource):
    def get(self, case_id, opt_num):
        if opt_num == '0':
            pass
        elif opt_num == '1':
            pass
        elif opt_num == '-1':
            pass

    def post(self):
        pass
