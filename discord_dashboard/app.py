# Imports Flask
from flask import Flask, request, Blueprint, render_template, jsonify, url_for, redirect, g, session
from flask_cors import CORS

# Imports Discord
from zenora import APIClient
from discord_oauth.auth import get_code
from discord.ext import ipc

# Imports Outros
from datetime import timedelta
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash, generate_password_hash
import json
import config
import requests
import os

# Imports Module
from pages.home import page_home
from pages.login import page_login

print("Server Iniciado. [working]")


'''# Função para pegar o arquivo json padrão de resposta para o frontend.
def back_to_front():
    with open('pages/front_json.json', 'r') as data_json:
        front_default = json.load(data_json)
    return front_default'''


# Flask Instance
app = Flask(__name__)
# app.register_blueprint(page_home, url_prefix='')
# app.register_blueprint(page_login, url_prefix='/dashboard')
# ipc_client = ipc.Client(secret_key="Vortex_painel_SAS_secret_jkdawiodjawiodnmawildjwal")

# App Configs
app.config['DEBUG'] = config.DEBUG
app.config['SECRET_KEY'] = config.SECRET_KEY
app.permanent_session_lifetime = timedelta(hours=4)


CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins": ""
    }
})


@app.before_request
def before():
    pass


@app.route('/')
@app.route('/home/')
def home():
    if "token" in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()

        return render_template(f'home.html', client_url_login=config.client_url_login, current_user=current_user)
    return render_template(f'home.html', client_url_login=config.client_url_login)


@app.route('/callback/', methods=['GET'])
def callback_teste():
    if "token" in session:
        return redirect(url_for("painel"))
    else:
        try:
            code = request.args['code']
            get_code(code)
            return redirect(url_for(f"painel"))
        except Exception as e:
            print(e)
            return redirect(url_for(f"home"))


@app.route('/logout')
def logout():
    try:
        session.clear()
    except:
        try:
            session.pop("user_id", None)
        except:
            return "Falha ao deslogar."
    finally:
        return redirect(url_for("home"))


@app.route('/painel/', methods=['GET'])
def dashboard():
    if "token" in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        return render_template(f'painel.html', client_url_login=config.client_url_login, current_user=current_user)
    else:
        return redirect(url_for(f"home"))


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True, threaded=True)
    # from waitress import serve
    # serve(app, host='0.0.0.0', port=5000)
    # serve(app, port=5000)
    app.run(debug=True)

# Fontes
"""
# Flask Tutorial
https://www.youtube.com/watch?v=iIhAfX4iek0&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX&index=5
# Bootstrap
https://getbootstrap.com/docs/4.3/getting-started/introduction/
# Login with Discord on Flask
https://www.youtube.com/watch?v=KFt8BpWakMg
# Flask-Discord?
https://github.com/weibeu/Flask-Discord
https://github.com/weibeu/Flask-Discord/blob/master/tests/test_app.py
"""

