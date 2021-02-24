from flask import Blueprint, request
from flask_restplus import Api, Namespace, Resource


blueprint = Blueprint('documented_api', __name__, url_prefix='/test')

api_extension = Api(
    blueprint,
    title='Flask RESTplus Demo',
    version='1.0',
    description='Application tutorial to demonstrate Flask RESTplus extension\
        for better project structure and auto generated documentation',
    doc='/doc'
)

namespace = Namespace('users', 'Users fake endpoints')

users = [
    {
        'id': 1,
        'first_name': 'Pedro',
        'last_name': 'Martinho',
        'bio': 'Information you can only read in the show used detail endpoint'
    }
]


@namespace.route('')
class Users(Resource):
    '''FAKE - Get all users list and create new users'''

    @namespace.doc('get_users')
    def get(self):
        '''Fake method to get list with all the users'''

        return {
            'message': "Here! You can take a look to our user",
            'users': list(map(lambda user: {key: user[key] for key in user if key != 'bio'}, users)),
            'total_records': len(users),
            'method': request.method
        }

    def post(self):
        '''Fake method related to users creation'''

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


api_extension.add_namespace(namespace)
