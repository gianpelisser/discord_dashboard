from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from discord_dashboard import config

page_login = Blueprint('login', __name__, template_folder='templates', static_folder='static')


@page_login.route('/')
def show_l():
    return render_template(f'dashboard/login.html')


@page_login.route('/', defaults={'page': 'index'})
@page_login.route('/<page>')
def show_1(page):
    try:
        return render_template(f'dashboard/{page}.html', client_url_login=config.client_url_login)
    except TemplateNotFound:
        abort(404)


@page_login.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', client_url_login=config.client_url_login)
