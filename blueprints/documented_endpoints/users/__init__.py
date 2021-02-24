from flask import request
from flask_restplus import Namespace, Resource, fields
from data import DataExample

data = DataExample()

namespace = Namespace('users', 'Users fake endpoints')

user_elem_model = namespace.model('UserElement', {
    'id': fields.Integer(
        readonly=True,
        description='User identifier'
    ),
    'first_name': fields.String(
        required=True,
        description='User first name'
    ),
    'last_name': fields.String(
        required=True,
        description='User last name'
    )
})

user_list_model = namespace.model('UserList', {
    'users': fields.Nested(
        user_elem_model,
        description='List of users',
        as_list=True
    ),
    'total records': fields.Integer(
        description='Total number of users',
    ),
})

user_model = namespace.clone('User', user_elem_model, {
    'bio': fields.String(
        description='User description'
    )
})


@namespace.route('')
class Users(Resource):
    '''Get all users list and create new users'''

    @namespace.doc('get_users')
    @namespace.marshal_with(user_list_model)
    def get(self):
        '''List with all the users'''

        # Get all the users from the users variable and exclude the bio since the list requires
        # less information to be sent to the client. If all the information from a user is needed,
        # rely on GET /users/<user_id>
        user_list = data.user_list

        return {
            'users': user_list,
            'total_records': len(user_list)
        }

    @namespace.expect(user_model)
    @namespace.marshal_with(user_model)
    def post(self):
        '''Fake method related to users creation'''

        data.add_user(namespace.payload)

        return {'message': 'Hello World!', 'method': request.method, 'sent_body': namespace.payload}


@namespace.route('/<int:user_id>')
class Users(Resource):
    '''Comments'''
    @namespace.doc('get_users')
    def get(self, user_id):
        '''Fake method to get list with all the users'''

        return {'message': 'Hello World!', 'method': request.method}

    def put(self, user_id):
        '''Fake method related to users creation'''

        return {'message': 'Hello World!', 'method': request.method, 'sent_body': namespace.payload}

    def delete(self, user_id):
        '''Fake method related to users creation'''

        return {'message': 'Hello World!', 'method': request.method, 'sent_body': namespace.payload}
