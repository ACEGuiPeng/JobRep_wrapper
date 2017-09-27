# -*- coding:utf-8 -*-
import json
from flask import request
from flask_restful import Resource
from service.case_manage_service import add_case, del_case, query_case, update_case


class Case(Resource):
    def get(self):
        result = query_case()
        return json.dumps(result)

    def post(self):
        json_data = request.get_json(force=True)
        message = add_case(json_data)
        return json.dumps({'message': message})

    def put(self):
        json_data = request.get_json(force=True)
        message = update_case(json_data)
        return json.dumps({'message': message})

    def delete(self):
        json_data = request.get_json(force=True)
        message = del_case(json_data)
        return json.dumps({'message': message})

class CaseList(Resource):
    pass