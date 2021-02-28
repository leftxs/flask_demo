from flask import Flask
from blueprints.basic_endpoints import blueprint as basic_endpoint
from blueprints.jinja_endpoint import blueprint as jinja_template_blueprint
from blueprints.documented_endpoints import blueprint as documented_endpoint

app = Flask(__name__)
app.config['RESTPLUS_MASK_HEADER'] = False
app.register_blueprint(basic_endpoint)
app.register_blueprint(jinja_template_blueprint)
app.register_blueprint(documented_endpoint)

# @app.route('/')
# def base():
#     return { 'message': 'Hello World!' }


# @app.route('/', methods=['GET', 'POST'])
# def base():
#     if request.method == "GET":
#         return { 'message': 'Hello World!', 'method': request.method }
#     if request.method == "POST":
#         return { 'message': 'Hello World!', 'method': request.method }

if __name__ == "__main__":
    app.run()
