# -*- coding:utf-8 -*-
import json

from flask import request
from flask_restful import Resource

from web.service.case_manage_service import query_case, update_case_status


class CaseManage(Resource):
    def get(self):
        result = query_case()
        return json.dumps(result)

    def put(self):
        json_data = request.get_json(force=True)
        message = update_case_status(json_data)
        return json.dumps({'message': message})
