# -*- coding:utf-8 -*-
import json

from flask import request
from flask_restful import Resource

from web.service.case.case_service import *


class Case(Resource):
    def get(self, case_ids=None):
        result = select_case(case_ids)
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
