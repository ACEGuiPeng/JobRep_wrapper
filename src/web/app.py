# -*- coding:utf-8 -*-
import time
from threading import Thread

from flask import Flask
from flask_restful import Api
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

from common.const import CONST
from web.manage.admin.verification_manage import CaseManage
from web.manage.case.case_manage import Case
from web.manage.material.material_manage import Material

app = Flask(__name__)
api = Api(app)

api.add_resource(Case, '/ygfbad/web/case')
api.add_resource(CaseManage, '/ygfbad/web/case_manage')
api.add_resource(Material, '/ygfbad/web/material')
api.add_resource()
api.add_resource(Case, '/ygfbad/web/case')
api.add_resource(CaseManage, '/ygfbad/web/case_manage')
api.add_resource(Material, '/ygfbad/web/material')


@app.route('/')
def alive():
    return 'yes'


loop = IOLoop.instance()


def run_web_service():
    http_server = HTTPServer(WSGIContainer(app))
    http_server.bind(CONST.WEB_SERVER_PORT)
    http_server.start(1)
    loop.start()


def stop_web_service():
    loop.stop()


if __name__ == '__main__':
    Thread(target=run_web_service).start()
    time.sleep(5)
