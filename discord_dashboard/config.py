# config Discord
api_endpoint = 'https://discord.com/api/v8'  # Nao altere
avatar_base_url = 'https://cdn.discordapp.com/'  # Nao altere
client_id = ''  # ID do BOT (app criado no discord)
client_secret = ''  # Secret do app criado no bot, nao eh o token do bot
client_scope = "identify guilds guilds.members.read"  # Scope, Pedir o q p/ usuario autorizar. Default=identify
redirect_url = 'http://localhost:500/auth'
client_token = ''
ch_historico = 941899483837509672
id_servidor_sas = 605389794641707018  # SAS - The Isle

# Config MySQL Holita
servidor_host = "192.168.1.2"  # Endereco IP/domino do Banco de Dados
servidor_user = "user"  # usuario do Banco de dados
servidor_mydb = "DB"  # Nome da database do Banco de dados
servidor_pass = "pass"  # Senha do Banco de dados

# Config Flask APP
SECRET_KEY = 'super_very_secret_key'  # Client Secret_Key -> Keycloak
TESTING = True  # Ativar ou nao modo Teste
DEBUG = True  # Ativar ou nao o Debug

# diretorios
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
