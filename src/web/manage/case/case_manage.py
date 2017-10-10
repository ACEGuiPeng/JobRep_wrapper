# -*- coding:utf-8 -*-
import json

from flask import request
from flask_restful import Resource

from web.service.case.case_service import *


class Case(Resource):
    def get(self):
        dict_data = request.args
        sorted_way = dict_data['sorted_way']
        page_no = dict_data['page_no']
        page_size = dict_data['page_size']
        result = select_case(dict_data, page_no, page_size, sorted_way)
        return json.dumps(result)

    def post(self):
        json_data = request.get_json(force=True)
        message = insert_case(json_data)
        return json.dumps({'message': message})

    def put(self):
        json_data = request.get_json(force=True)
        message = update_case(json_data)
        return json.dumps({'message': message})

    def delete(self):
        json_data = request.get_json(force=True)
        message = del_case(json_data)
        return json.dumps({'message': message})
