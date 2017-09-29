# -*- coding:utf-8 -*-
import json

from flask import request
from flask_restful import Resource

from web.service.material.material_service import *


class Material(Resource):
    def get(self):
        data_dict = request.args
        uid = data_dict['uid']
        sorted_way = data_dict['sorted_way']
        result = select_material(uid,sorted_way)
        return json.dumps(result)

    def post(self):
        json_data = request.get_json(force=True)
        message = insert_material(json_data)
        return json.dumps({'message': message})

    def put(self):
        json_data = request.get_json(force=True)
        message = update_material(json_data)
        return json.dumps({'message': message})

        # def delete(self):
        #     json_data = request.get_json(force=True)
        #     message = del_material(json_data)
        #     return json.dumps({'message': message})
