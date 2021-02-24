from flask import Blueprint, request, render_template

blueprint = Blueprint('jinja_template', __name__, url_prefix='/jinja_template')


@blueprint.route('/<string:name>')
def get_template():
    return render_template('templates/template.html', my_string="Wheeeee!", my_list=[0, 1, 2, 3, 4, 5])
