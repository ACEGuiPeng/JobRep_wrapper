# -*- coding:utf-8 -*-
import json

from flask import request
from flask_restful import Resource

from web.service.resource.resource_service import *


class Resources(Resource):
    def allowed_file(self, filename):
        return '.' in filename and filename.split('.', 1)[1] in CONST.ALLOW_EXTENSIONS

    def get(self):
        data_dict = request.args
        uid = data_dict['uid']
        asin = data_dict['asin']
        sorted_way = data_dict['sorted_way']
        key_words = data_dict['key_words']
        result = select_resource(uid, asin, sorted_way, key_words)
        return json.dumps(result)

    def post(self):
        # 上传resource
        up_file = request.files['file']
        form_data = request.form
        if up_file and self.allowed_file(up_file.filename):
            upload_path = upload_files(up_file, form_data)
            return json.dumps({'file_path': upload_path})

    def put(self):
        json_data = request.get_json(force=True)
        message = update_resource(json_data)
        return json.dumps({'message': message})

    def delete(self):
        json_data = request.get_json(force=True)
        message = del_resource(json_data)
        return json.dumps({'message': message})
