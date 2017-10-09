# -*- coding:utf-8 -*-
import json

from flask import request
from flask_restful import Resource

from web.service.landing_page.landing_page_service import *


class LandingPage(Resource):
    def get(self):
        # 已有落地页
        data_dict = request.args
        sorted_way = data_dict['sorted_way']
        result = select_landing_page(sorted_way)
        return json.dumps(result)

    def post(self):
        # 新建落地页
        json_data = request.get_json(force=True)
        message = insert_landing_page(json_data)
        return json.dumps({'message': message})

    def put(self):
        # 修改落地页
        json_data = request.get_json(force=True)
        message = update_landing_page(json_data)
        return json.dumps({'message': message})

    def delete(self):
        # 删除落地页
        json_data = request.get_json(force=True)
        message = del_landing_page(json_data)
        return json.dumps({'message': message})
