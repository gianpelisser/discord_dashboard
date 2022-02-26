from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

page_home = Blueprint('home', __name__, template_folder='templates', static_folder='static')


@page_home.route('/', defaults={'page': 'index'})
@page_home.route('/<page>/')
def show(page):
    try:
        return render_template(f'{page}.html')
    except TemplateNotFound:
        abort(404)


@page_home.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
