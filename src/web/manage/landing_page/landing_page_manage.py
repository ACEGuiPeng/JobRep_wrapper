# -*- coding:utf-8 -*-
import json

from flask import request, Response
from flask_restful import Resource

from web.service.landing_page.landing_page_service import *
from wrappers.hdfs_wrapper import HdfsWrapper

hdfs_wrapper = HdfsWrapper()
hdfs_wrapper.connect_hdfs()


class LandingPage(Resource):
    def get(self):
        # 已有落地页
        data_dict = request.args
        sorted_way = data_dict['sorted_way']
        result = select_landing_page(data_dict,sorted_way)
        return json.dumps(result)

    def post(self):
        # 新建落地页
        json_data = request.get_json(force=True)
        message = insert_landing_page(json_data)
        return json.dumps({'message': message})

    def put(self):
        # 修改落地页
        json_data = request.get_json(force=True)
        message = update_landing_page(json_data)
        return json.dumps({'message': message})

    def delete(self):
        # 删除落地页
        json_data = request.get_json(force=True)
        message = del_landing_page(json_data)
        return json.dumps({'message': message})


class LandingPageTemplate(Resource):
    def get(self):
        data_dict = request.args
        hdfs_path = CONST.UPLOAD_FOLDER + '/landing_page/templates/{}.html'.format(data_dict['temp_name'])
        # 读取文件的二进制数据
        data = hdfs_wrapper.read_hdfs(hdfs_path)
        # 响应设置解码格式
        response = Response(data, mimetype='text/html')
        return response

    def post(self):
        # 上传落地页模板到hdfs
        pass

    def put(self):
        pass

    def delete(self):
        pass


class LandingPageTempList(Resource):
    def get(self):
        # 得到hdfs模板名称
        hdfs_path = CONST.UPLOAD_FOLDER + '/landing_page/templates'
        file_paths = hdfs_wrapper.list_hdfs(hdfs_path)
        file_names = [name.split('.')[0] for name in file_paths]
        return json.dumps({'file_names': file_names})

    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass
