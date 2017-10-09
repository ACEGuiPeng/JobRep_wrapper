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
from web.manage.material.material_record_manage import MaterialRecord
from web.manage.img.img_manage import Img
from web.manage.landing_page.landing_page_manage import LandingPage
from web.manage.landing_page.landing_page_record import LandingPageRecord
from web.manage.resource.resource_manage import Resources
from web.manage.resource.resource_record_manage import ResourcesRecord

app = Flask(__name__)
api = Api(app)

api.add_resource(Case, '/ygfbad/web/case')
api.add_resource(CaseManage, '/ygfbad/web/case_manage')
api.add_resource(Material, '/ygfbad/web/material')
api.add_resource(MaterialRecord, '/ygfbad/web/mater_record')
api.add_resource(LandingPage, '/ygfbad/web/land_page')
api.add_resource(LandingPageRecord, '/ygfbad/web/lp_record')
api.add_resource(Img, '/ygfbad/web/img')
api.add_resource(Resources, '/ygfbad/web/res')
api.add_resource(ResourcesRecord, '/ygfbad/web/res_record')


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
