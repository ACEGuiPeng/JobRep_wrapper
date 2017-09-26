# -*- coding:utf-8 -
from flask import Flask
from flask_restful import Api, Resource

app = Flask('asdasd')
api = Api(app)


class R(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(R, '/')

if __name__ == '__main__':
    app.run(debug=True)
