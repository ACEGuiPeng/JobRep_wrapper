# -*- coding:utf-8 -*-
from flask import request
from flask_restful import Resource


class MatirialManage(Resource):
    def get(self):
        pass

    def post(self):
        json_data = request.get_json(force=True)


    def delete(self):
        pass

    def put(self):
        pass
