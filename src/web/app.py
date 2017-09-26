# -*- coding:utf-8 -*-
from flask import Flask
from flask_restful import Api, Resource
from web.tasks.fbad_matirial import ToDo

app = Flask(__name__)
api = Api(app)

api.add_resource(ToDo, '/')

if __name__ == '__main__':
    app.run(debug=True)
