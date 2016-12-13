from flask import Blueprint, request
from flask_restplus import Api, Resource, fields

from models import Members, NoSuchUserError

blueprint = Blueprint('api', __name__)
api = Api(blueprint)

new_member_fields = api.model('NewMember', {
    'name': fields.String(description='Member name', required=True),
})

member_fields = api.inherit('Member', new_member_fields, {
    'id': fields.Integer(description='Member id', required=True),
})

members = Members()
members.create({'name': 'Tom'})
members.create({'name': 'Matt'})


@api.route('/hello_world')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


@api.route('/members/')
class MemberList(Resource):

    def get(self):
        return members.list()

    @api.doc(body=new_member_fields)
    @api.marshal_with(member_fields, code=201)
    def post(self):
        new_member = members.create(request.json)
        return new_member, 201


@api.route('/members/<int:id>')
@api.doc(params={'id': 'An ID'})
class Member(Resource):
    def get(self, id):
        try:
            return members.get(id)
        except NoSuchUserError as err:
            api.abort(404, err.message)
