# config Discord
api_endpoint = 'https://discord.com/api/v8'  # Nao altere
avatar_base_url = 'https://cdn.discordapp.com/'  # Nao altere
client_id = '940740145034960916'  # ID do BOT (app criado no discord)
client_secret = '-yUMSe-GTmhKLCJ2WqJguMR4OOciPUAd'  # Secret do app criado no bot, nao é o token do bot
client_scope = "identify guilds guilds.members.read"  # Scope, Pedir o q p/ usuario autorizar. Default=identify
# redirect_url = 'https://portal.sasbrasil.tk/callback'
redirect_url = 'http://localhost:5000/callback'
client_token = ''
client_url_login = f"https://discord.com/api/oauth2/authorize?client_id={client_id}&redirect_uri={redirect_url}&response_type=code&scope={client_scope}"
ch_historico = 941899483837509672
id_servidor_sas = 605389794641707018  # SAS - The Isle

# Config MySQL
servidor_host = "192.168.1.2"  # Endereco IP/domino do Banco de Dados
servidor_user = "user"  # usuario do Banco de dados
servidor_mydb = "DB"  # Nome da database do Banco de dados
servidor_pass = "pass"  # Senha do Banco de dados

# Config Flask APP
SECRET_KEY = 'super_very_secret_key-bys4e5516by45ea35by14'  # Client Secret_Key -> Keycloak
TESTING = True  # Ativar ou nao modo Teste
DEBUG = True  # Ativar ou nao o Debug

# diretorios
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
