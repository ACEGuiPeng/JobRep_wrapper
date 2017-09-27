# -*- coding:utf-8 -*-
import json

from flask import request
from flask_restful import Resource

from web.service.material_manage_service import query_material, add_material, update_material, del_material


class Material(Resource):
    def get(self):
        result = query_material()
        return json.dumps(result)

    def post(self):
        json_data = request.get_json(force=True)
        message = add_material(json_data)
        return json.dumps({'message': message})

    def put(self):
        json_data = request.get_json(force=True)
        message = update_material(json_data)
        return json.dumps({'message': message})

    def delete(self):
        json_data = request.get_json(force=True)
        message = del_material(json_data)
        return json.dumps({'message': message})
