from flask import Blueprint, render_template, redirect, url_for, session, request, flash, jsonify
from zenora import APIClient
import config
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
@views.route('/home', methods=['GET'])
def home():
    if "token" in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        return render_template("home.html", client_url_login=config.client_url_login, current_user=current_user)

    return render_template("home.html", client_url_login=config.client_url_login)


@views.route('/painel', methods=['GET'])
def painel():
    if "token" in session:
        bearer_client = APIClient(session.get('token'), bearer=True)

        current_user = bearer_client.users.get_current_user()
        current_guilds = bearer_client.users.get_my_guilds()
        guild_adm = []
        for guild in current_guilds:
            if int(guild.permissions) == 2199023255551:
                guild_adm.append(guild.id)

        return render_template(f'painel.html', client_url_login=config.client_url_login, current_user=current_user, current_guilds=current_guilds,
                               guild_adm=guild_adm)
    else:
        return redirect(url_for('views.home'))
