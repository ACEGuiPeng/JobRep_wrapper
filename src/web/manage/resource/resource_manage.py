# -*- coding:utf-8 -*-
import json

from flask import request
from flask_restful import Resource

from web.service.resource.resource_service import *


class Resources(Resource):
    def get(self):
        data_dict = request.args
        uid = data_dict['uid']
        asin = data_dict['asin']
        sorted_way = data_dict['sorted_way']
        key_words = data_dict['key_words']
        result = select_resource(uid, asin, sorted_way, key_words)
        return json.dumps(result)

    def post(self):
        json_data = request.get_json(force=True)
        message = insert_resource(json_data)
        return json.dumps({'message': message})

    def put(self):
        json_data = request.get_json(force=True)
        message = update_resource(json_data)
        return json.dumps({'message': message})

    def delete(self):
        json_data = request.get_json(force=True)
        message = del_resource(json_data)
        return json.dumps({'message': message})
