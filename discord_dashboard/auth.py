from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from discord_oauth.auth import get_code


auth = Blueprint('auth', __name__)


@auth.route('/callback', methods=['GET'])
def login():
    if "token" in session:
        return redirect(url_for('views.painel'))

    else:
        try:
            if request.args['error']:
                # error=access_denied&error_description=The+resource+owner+or+authorization+server+denied+the+request
                error = request.args['error']
                erro_description = request.args['error_description']
                return render_template("discord_error.html", error=error, erro_description=erro_description)
            code = request.args['code']
            get_code(code)
            return redirect(url_for('views.painel'))
        except Exception as e:
            print(f"Sem code no callback. Erro: {e}")
            return redirect(url_for('views.home'))


@auth.route('/logout')
def logout():
    try:
        session.clear()
    except:
        try:
            session.pop("user_id", None)
        except:
            return "Falha ao deslogar."
    finally:
        return redirect(url_for('views.home'))
