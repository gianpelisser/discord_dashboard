from discord_dashboard import config
from flask import redirect, session
import requests


def get_code(code):
    try:
        # Pega o Token que volta do Discord
        data = {
            'client_id': config.client_id,
            'client_secret': config.client_secret,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': config.redirect_url
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        r_code = requests.post('%s/oauth2/token' % config.api_endpoint, data=data, headers=headers)
        data_token = r_code.json()
        # Pega o 'access_token'
        acess_token = data_token['access_token']
        # print(acess_token)

        '''# Pega as info do usuario(discord)
        r_discord = requests.get(f"{config.api_endpoint}/users/@me", headers={"Authorization": f"Bearer {acess_token}"})
        data_user = r_discord.json()
        user_avatar_url = f"{config.avatar_base_url}avatars/{data_user['id']}/{data_user['avatar']}.jpeg"
        # print(data_user)'''

        '''# Pega os cargos do usuario no servidor especifico (SAS)
        guild_id = config.id_servidor_sas  # SAS - The Isle
        r_u_server = requests.get(f"{config.api_endpoint}/users/@me/guilds/{guild_id}/member",
                                  headers={"Authorization": f"Bearer {acess_token}"})
        data_user_server = r_u_server.json()
        user_roles = data_user_server['roles']
        '''

        '''try:
            session.permanent = True
            session['user_id'] = data_user['id']
            # if "user_id" in session:
                # user = session['user_id']
            print(f"Usuario Discord_ID: {data_user['id']} fez login no site.\n"
                  f"Nome: {data_user['username']}\n"
                  f"Language: {data_user['locale']}")
            return redirect(url_for("painel"))
            # user_all_info_discord = json.dumps(j_discord)
            # return user_all_info_discord
        except Exception as e:
            print(f"Session Erro: {e}")
            return redirect(url_for("home"))'''

        # Salva o Acess_token como Token em uma Session
        session['token'] = acess_token
        print(f"Solicitação de login executada com sucesso!")
        return

    except Exception as e:
        print(e)
        return redirect("home")
