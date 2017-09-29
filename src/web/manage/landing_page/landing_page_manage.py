# -*- coding:utf-8 -*-
import json

from flask import request
from flask_restful import Resource

from web.service.landing_page.landing_page_service import *


class LandingPage(Resource):
    def get(self):
        result = select_landing_page()
        return json.dumps(result)

    def post(self):
        json_data = request.get_json(force=True)
        message = insert_landing_page(json_data)
        return json.dumps({'message': message})

    def put(self):
        json_data = request.get_json(force=True)
        message = update_landing_page(json_data)
        return json.dumps({'message': message})

    def delete(self):
        json_data = request.get_json(force=True)
        message = del_landing_page(json_data)
        return json.dumps({'message': message})
