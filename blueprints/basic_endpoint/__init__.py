from flask import Blueprint, request

blueprint = Blueprint('api', __name__, url_prefix='/api/')


@blueprint.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == "GET":
        return {'message': 'Hello World!', 'method': request.method}
    if request.method == "POST":
        return {'message': 'Hello World!', 'method': request.method}


@blueprint.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def get_user(user_id):
    if request.method == "GET":
        return {'user_id': user_id, 'message': 'Hello World!', 'method': request.method}
    if request.method == "PUT":
        return {'user_id': user_id, 'message': 'Hello World!', 'method': request.method}
    if request.method == "DELETE":
        return {'user_id': user_id, 'message': 'Hello World!', 'method': request.method}
