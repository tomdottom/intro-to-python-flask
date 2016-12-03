from flask import Blueprint
from flask_restplus import Api, Resource

blueprint = Blueprint('api', __name__)
api = Api(blueprint)


@api.route('/hello_world')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
