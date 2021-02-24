from flask import Blueprint, request, render_template

blueprint = Blueprint('jinja_template', __name__, url_prefix='/jinja_template')


@blueprint.route('')
def get_template():
    top = request.args.get('top')
    bottom = request.args.get('bottom')

    return render_template('example.html', top=top, bottom=bottom)
