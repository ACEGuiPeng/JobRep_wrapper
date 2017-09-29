# -*- coding:utf-8 -*-
import json

from flask import request
from flask_restful import Resource

from web.service.landing_page.landing_page_record_service import *


class LandingPageRecord(Resource):
    def get(self):
        data_dict = request.args
        sorted_way = data_dict['sorted_way']
        result = select_landing_page_record(sorted_way)
        return json.dumps(result)

    def post(self):
        json_data = request.get_json(force=True)
        message = insert_landing_page_record(json_data)
        return json.dumps({'message': message})

    def put(self):
        json_data = request.get_json(force=True)
        message = update_landing_page_record(json_data)
        return json.dumps({'message': message})

    def delete(self):
        json_data = request.get_json(force=True)
        message = del_landing_page_record(json_data)
        return json.dumps({'message': message})
