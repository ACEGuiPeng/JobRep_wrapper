# -*- coding:utf-8 -*-
import json

from flask import request
from flask_restful import Resource

from web.service.resource.resource_service import *


class Resources(Resource):
    def get(self):
        result = select_resource()
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
