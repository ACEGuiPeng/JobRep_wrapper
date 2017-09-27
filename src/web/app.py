# -*- coding:utf-8 -*-
from flask import Flask
from flask_restful import Api
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

from common.const import CONST
from web.manage.fbad_case_manage import CaseManage

app = Flask(__name__)
api = Api(app)

api.add_resource(CaseManage, '/ygfbad/web/cases')


@app.route('/')
def alive():
    return 'yes'


def run_web_service():
    http_server = HTTPServer(WSGIContainer(app))
    http_server.bind(CONST.WEB_SERVER_PORT)
    http_server.start(1)
    IOLoop.instance().start()


if __name__ == '__main__':
    run_web_service()
