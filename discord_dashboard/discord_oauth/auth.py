from discord_dashboard import config
from flask import Flask, redirect, request, session, url_for
import requests
import json


# Função para pegar o arquivo json padrão de resposta para o frontend.
def discord_to_front():
    with open('discord_oauth/user_infos.json', 'r') as data_json:
        discord_default = json.load(data_json)
    return discord_default
    

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

        # abre o json para salvar todas as informaçoes e preparar para voltar ao frontend.
        j_discord = discord_to_front()

        j_discord['discordarray']['iddiscord'] = f"{data_user['id']}"
        j_discord['discordarray']['discord'] = f"{data_user['username']}#{data_user['discriminator']}"
        j_discord['discordarray']['username'] = f"{data_user['username']}"
        j_discord['discordarray']['avatar_url'] = f"{user_avatar_url}"
        j_discord['discordarray']['avatar_hash'] = f"{data_user['avatar']}"
        j_discord['discordarray']['discriminator'] = f"{data_user['discriminator']}"
        j_discord['discordarray']['locale'] = f"{data_user['locale']}"
        j_discord['discordarray']['roles_id'] = user_roles
        j_discord['discordarray']['log_msg'] = f"Informacoes obtidas do Discord com sucesso!"'''

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

        session['token'] = acess_token
        print(f"Solicitação de login executada com sucesso!")
        return redirect(url_for(f"home"))

    except Exception as e:
        print(e)
        return redirect("home")
