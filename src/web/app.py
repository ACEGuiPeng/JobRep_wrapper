# -*- coding:utf-8 -*-
from threading import Thread

import time
from flask import Flask
from flask_restful import Api
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

from common.const import CONST
from web.manage.fbad_matirial_manage import Material
from web.manage.fbad_case_manage import Case
from web.manage.verification_manage import CaseManage

app = Flask(__name__)
api = Api(app)

api.add_resource(Case, '/ygfbad/web/cases')
api.add_resource(Material, '/ygfbad/web/materials')
api.add_resource(CaseManage, '/ygfbad/web/case_manage')


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
