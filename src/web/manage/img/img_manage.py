# -*- coding:utf-8 -*-
import json

from flask import request
from flask_restful import Resource

from web.service.img.img_service import *


class Img(Resource):
    def allowed_file(self, filename):
        return '.' in filename and filename.split('.', 1)[1] in CONST.ALLOW_EXTENSIONS

    def post(self):
        # 上传resource
        up_file = request.files['file']
        form_data = request.form
        if up_file and self.allowed_file(up_file.filename):
            upload_path = upload_files(up_file, form_data)
            return json.dumps({'file_path': upload_path})

    def get(self):
        pass

    def delete(self):
        # 删除图片
        pass


    def put(self):
        pass
