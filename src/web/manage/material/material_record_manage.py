# -*- coding:utf-8 -*-
import json

from flask import request
from flask_restful import Resource

from web.service.material.material_record_service import *


class MaterialRecord(Resource):
    def get(self):
        result = select_material_record()
        return json.dumps(result)

    def post(self):
        json_data = request.get_json(force=True)
        message = insert_material_record(json_data)
        return json.dumps({'message': message})

    def put(self):
        json_data = request.get_json(force=True)
        message = update_material_record(json_data)
        return json.dumps({'message': message})

    def delete(self):
        json_data = request.get_json(force=True)
        message = del_material_record(json_data)
        return json.dumps({'message': message})
