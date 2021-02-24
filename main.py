from flask import Flask
from blueprints.basic_endpoint import blueprint as basic_endpoint
from blueprints.documented_endpoints import blueprint as documented_endpoint
from blueprints.jinja_example import blueprint as jinja_template_blueprint

app = Flask(__name__)
app.register_blueprint(documented_endpoint)
app.register_blueprint(jinja_template_blueprint)
app.register_blueprint(basic_endpoint)

# @app.route('/')
# def base():
#     return { 'message': 'Hello World!' }


# @app.route('/', methods=['GET', 'POST'])
# def base():
#     if request.method == "GET":
#         return { 'message': 'Hello World!', 'method': request.method }
#     if request.method == "POST":
#         return { 'message': 'Hello World!', 'method': request.method }
