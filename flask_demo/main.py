from flask import Flask
from flask_demo.basic_endpoint import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)

# @app.route('/')
# def base():
#     return { 'message': 'Hello World!' }


# @app.route('/', methods=['GET', 'POST'])
# def base():
#     if request.method == "GET":
#         return { 'message': 'Hello World!', 'method': request.method }
#     if request.method == "POST":
#         return { 'message': 'Hello World!', 'method': request.method }
