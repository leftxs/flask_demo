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
    'total_records': fields.Integer(
        description='Total number of users',
    ),
})

user_model = namespace.clone('User', user_elem_model, {
    'bio': fields.String(
        description='User description'
    )
})

message_model = namespace.model('Message', {
    'message': fields.Integer(
        readonly=True,
        description='Message detailing the request result'
    )
})


@namespace.route('')
class Users(Resource):
    '''Get all users list and create new users'''

    @namespace.marshal_list_with(user_list_model)
    def get(self):
        '''List with all the users'''

        users_list = data.user_list()
        return {
            'users': users_list,
            'total_records': len(users_list)
        }

    @namespace.expect(user_model)
    @namespace.marshal_with(user_model)
    def post(self):
        '''Create a new user'''

        user = data.add_user(namespace.payload)

        return user, 201


@namespace.route('/<int:user_id>')
class Users(Resource):
    '''Read, update and delete a specific user'''

    @namespace.marshal_with(user_model)
    def get(self, user_id):
        '''Get user information'''

        user_info = data.get_user(user_id)

        return user_info

    @namespace.expect(user_model, validate=True)
    @namespace.marshal_with(user_model)
    def put(self, user_id):
        '''Update user information'''

        updated_user = data.update_user(user_id, namespace.payload)

        return updated_user

    @namespace.marshal_with(message_model)
    def delete(self, user_id):
        '''Delete a specific user'''

        data.delete_user(user_id)

        return {'message': 'User with id {} has been deleted.'.format(user_id)}, 200
