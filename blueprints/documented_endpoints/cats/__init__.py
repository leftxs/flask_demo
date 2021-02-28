from flask import request
from flask_restplus import Namespace, Resource, fields
from data import DataExample

data = DataExample()

namespace = Namespace('cats', 'Cats fake endpoints')

cat_model = namespace.model('Cat', {
    'id': fields.Integer(
        readonly=True,
        description='Cat identifier'
    ),
    'first_name': fields.String(
        required=True,
        description='Cat first name'
    )
})

cat_list_model = namespace.model('CatList', {
    'cats': fields.Nested(
        cat_model,
        description='List of cats',
        as_list=True
    ),
    'total_records': fields.Integer(
        description='Total number of cats',
    ),
})

message_model = namespace.model('Message', {
    'message': fields.Integer(
        readonly=True,
        description='Message detailing the request result'
    )
})

cat_example = {'id': 1, 'first_name': 'Baltazar'}


@namespace.route('')
class Cats(Resource):
    '''Get cats list and create new cats'''

    @namespace.marshal_list_with(cat_list_model)
    def get(self):
        '''List with all the cats'''

        return {
            'cats': [cat],
            'total_records': 1
        }

    @namespace.expect(cat_model)
    @namespace.marshal_with(cat_model)
    def post(self):
        '''Create a new cat'''

        return cat_example, 201


@namespace.route('/<int:cat_id>')
class Cat(Resource):
    '''Read, update and delete a specific cat'''

    @namespace.marshal_with(cat_model)
    def get(self, cat_id):
        '''Get cat_example information'''

        return cat_example

    @namespace.expect(cat_model, validate=True)
    @namespace.marshal_with(cat_model)
    def put(self, cat_id):
        '''Update cat information'''

        return cat_example

    @namespace.marshal_with(message_model)
    def delete(self, cat_id):
        '''Delete a specific cat'''

        return {'message': 'Cat with id {cat_id} has been deleted.'.format(cat_id)}, 200
