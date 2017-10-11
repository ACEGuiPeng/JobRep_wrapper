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
        key_word = data_dict['key_word']
        result = select_resource(uid, asin, sorted_way, key_word)
        return json.dumps(result)

    def post(self):
        up_files = request.files['file']
        form_data = request.form
        up_files = [x for x in up_files if x and self.allowed_file(x.filename)]
        upload_paths = upload_files(up_files, form_data)
        return json.dumps({'file_path': upload_paths})

    def put(self):
        json_data = request.get_json(force=True)
        message = update_resource(json_data)
        return json.dumps({'message': message})

    def delete(self):
        json_data = request.get_json(force=True)
        message = delete_resource(json_data)
        return json.dumps({'message': message})
