from flask import Blueprint, request
from flask_restplus import Api, Resource, fields

blueprint = Blueprint('api', __name__)
api = Api(blueprint)


@api.route('/hello_world')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


new_member_fields = api.model('NewMember', {
    'name': fields.String(description='Member name', required=True),
})

member_fields = api.inherit('Member', new_member_fields, {
    'id': fields.Integer(description='Member id', required=True),
})


class Members(object):

    def __init__(self):
        self._members = []

    def get(self, mid):
        try:
            return self._members[mid]
        except IndexError:
            api.abort(404, 'Could not find member with id: {}'.format(mid))

    def list(self):
        return self._members

    def create(self, data):
        if self._member_exists(data['name']):
            api.abort(
                409,
                'Member with name \'{}\' already exists'.format(data['name'])
            )

        new_id = len(self._members)
        self._members.append({
            'id': new_id,
            'name': data['name']
        })
        return self._members[new_id]

    def _member_exists(self, name):
        return any(
            member
            for member in self._members
            if member['name'] == name
        )


members = Members()
members.create({'name': 'Tom'})
members.create({'name': 'Matt'})


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
        return members.get(id)
