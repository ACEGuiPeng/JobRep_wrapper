# -*- coding:utf-8 -*-

from flask import Flask
from flask_restful import Api
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

from common.const import CONST
from web.manage.admin.verification_manage import CaseManage
from web.manage.case.case_manage import Case
from web.manage.landing_page.landing_page_manage import LandingPage, LandingPageTemplate, LandingPageTempList
from web.manage.material.material_manage import Material
from web.manage.resource.resource_manage import Resources

app = Flask(__name__)
api = Api(app)

api.add_resource(Case, '/ygfbad/web/cases')
api.add_resource(CaseManage, '/ygfbad/web/case_manage')
api.add_resource(Material, '/ygfbad/web/materials')
api.add_resource(LandingPage, '/ygfbad/web/landing_pages')
api.add_resource(LandingPageTemplate, '/ygfbad/web/landing_page_templates')
api.add_resource(LandingPageTempList, '/ygfbad/web/template_list')
api.add_resource(Resources, '/ygfbad/web/resources')


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
