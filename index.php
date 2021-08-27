<?php

# Enabling error display
error_reporting(E_ALL);
ini_set('display_errors', 1);


# Including all the required scripts for demo
require __DIR__ . "/includes/functions.php";
require __DIR__ . "/includes/discord.php";
require __DIR__ . "/config.php";

?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="src/css/bootstrap.min.css">
    <link rel="stylesheet" href="src/css/main.css">
    <link rel="stylesheet" href="src/css/now-ui-kit.css">
    <link href="https://fonts.googleapis.com/css?family=Poppins:300,400,600,700,800,900&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Montserrat:400,600,700,800,900&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Lato:300,400,600,700,800,900&display=swap" rel="stylesheet">
    <title>Black Holita - S.A.S</title>
</head>
<body>
<nav class="navbar navbar-expand-lg bg-transparent">
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <img src="src/assets/menuIcon.svg" width="20px" height="20px" style="max-width: none !important;">
    </button>
    <a href="../discord/"><img src="src/img/holita.jpg" width="50" height="50"></a>
    <div class="collapse navbar-collapse" id="navbarSupportedContent" style="margin-left: 20px !important">
        <ul class="navbar-nav mr-auto">
            <li class="nav-item active">
                <a class="nav-link" href="../discord/">Início <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#">Recursos</a>
            </li>
            <?php
            if (isset($_SESSION['user'])) { ?>
            <li class="nav-item">
                <a class="nav-link" href="#">Painel de Controle</a>
            </li>
            <?php } ?>
            <li class="nav-item">
                <a class="nav-link" href="#">Doação (Donate)</a>
            </li>
        </ul>
        <div class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                Documentação
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                <a class="dropdown-item" href="#">Comandos</a>
                <a class="dropdown-item" href="#">Tutoriais</a>
                <div class="dropdown-divider"></div>
                <a class="dropdown-item" href="#">Configurações do servidor</a>
            </div>
        </div>
        <div class="nav-item">
            <a class="nav-link" href="#">Equipe</a>
        </div>
        <?php
			$auth_url = url($client_id, $redirect_url, $scopes);
			if (isset($_SESSION['user'])) {
				echo '<a href="includes/logout.php"><button class="btn login-btn btn-outline-accent my-2 my-sm-0">SAIR</button></a>';
			} else {
				echo "<a href='$auth_url'><button class='btn login-btn btn-outline-accent my-2 my-sm-0'>LOGIN | ENTRAR</button></a>";
			}
		?>
        <!--<button class="btn login-btn btn-outline-accent my-2 my-sm-0" style="font-size: 10px !important;font-family: poppins !important;">LOGIN | ENTRAR</button>-->
    </div>
</nav>
<div class="heading">
    <?php
        if (isset($_SESSION['user'])) {
            echo '<h1 class="display-5 title">Bem Vindo(a)</h1>';
            echo '<p> Name : ' . $_SESSION['username'] . '#' . $_SESSION['discrim'] . '';
            echo '<p> ID : ' . $_SESSION['user_id'] . '</p>';
            $extention = is_animated($_SESSION['user_avatar']);
            echo '<p><img src="https://cdn.discordapp.com/avatars/' . $_SESSION['user_id'] . "/" . $_SESSION['user_avatar'] . $extention . '" /></p>';

            echo '<p>'; # Mostrar apenas as guilds onde o usuario é dono.
            for($i = 0; $i < sizeof($_SESSION['guilds']); $i++)
{
            if ($_SESSION['guilds'][$i]['owner'] == true) 
            {
                echo('<div>');
                echo $_SESSION['guilds'][$i]['name'];
                echo('</div>');
            }
            }
            echo '</p>';

            echo '<button class="btn login-btn btn-outline-accent my-2 my-sm-0" style="font-size: 10px !important;font-family: poppins !important;">PAINEL DE CONTROLE</button>';
            echo '<br />';
        } else {
            echo '<br />';
        }
	?>

    <h1 class="display-5 title">É hora de usar o Bot em seu servidor.</h1>
    <p class="subtitle">BOT serve para aumentar as habilidades e impulsionar o seu servidor Discord<br />Também possui moderação automática, administração e muito mais!</p>
    <a class="btn btn-primary btn-lg" href="#start_link" target="_blank" role="button">Como usar</a>
    <a class="btn btn-secondary btn-lg" href="#server_link" target="_blank" role="button">Adicionar ao Servidor</a>
    <br /><br /><br /><br /><br /><br />
</div>
<div class="features">
    <div class="title">Características do bot</div>
    <div class="subtitle">Nós fornecemos os melhores recursos do Bot!</div>
    <div class="cards">
        <div class="card" style="width: 18rem;">
        <div class="card-body">
            <h5 class="card-title">SLOTs #1</h5>
            <p class="card-text">Você guarda seu Dinossauro em um SLOT e no outro SLOT você pode jogar com outro dinossauro de outra espécie sem perder os outros dinossauros que você lutou para crescer.</p>
        </div>
    </div>
        <div class="card" style="width: 18rem;">
            <div class="card-body">
                <h5 class="card-title">Future #2</h5>
                <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent ex ante, mattis vel dapibus vel, tempor facilisis justo. Vivamus dignissim ut nisi eu consequat.</p>
            </div>
        </div>
        <div class="card" style="width: 18rem;">
            <div class="card-body">
                <h5 class="card-title">Future #3</h5>
                <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent ex ante, mattis vel dapibus vel, tempor facilisis justo. Vivamus dignissim ut nisi eu consequat.</p>
            </div>
        </div>
    </div>
</div>
<div class="statistics">
    <div class="cards">
        <div class="card statistic" style="width: 18rem;">
            <div class="card-body">
                <p class="card-title" style="font-size: 50px !important;line-height: 15px !important;letter-spacing: -0.06em !important;font-weight: bold !important;">001</p>
                <p style="font-weight: bold !important;font-size: 20px !important; color: #ff9102;">Servidores</p>
            </div>
        </div>
        <div class="card statistic" style="width: 18rem;">
            <div class="card-body">
                <p class="card-title" style="font-size: 50px !important;line-height: 15px !important;letter-spacing: -0.06em !important;font-weight: bold !important;">
                    
                0000

                </p>
                <p style="font-weight: bold !important;font-size: 20px !important; color: #ff9102;">Usuários</p>
            </div>
        </div>
        <div class="card statistic" style="width: 18rem;">
            <div class="card-body">
                <p class="card-title" style="font-size: 50px !important;line-height: 15px !important;letter-spacing: -0.06em !important;font-weight: bold !important;">136</p>
                <p style="font-weight: bold !important;font-size: 20px !important; color: #ff9102;">Chats</p>
            </div>
        </div>
    </div>
</div>
<div class="page_end">
    <div class="start">
        <div class="card">
            <div class="card-body gs-card">
                <div class="title">Pronto para experimentar o Bot?</div>
                <div class="subtitle">Convide o Bot e comece a dar vantagens incríveis ao seu servidor!</div>
                <br />
                <a class="btn btn-primary btn-lg" href="#start_link" role="button">Como usar</a>
            </div><br />
        </div>
    </div>
    <div class="footer">
        <div class="bot-footer">
            <!--<img src="src/img/holita.jpg" width="150"><br />-->
            <h2>BLACK HOLITA</h2>
            Copyright © [VORTEX] - 2019 - 2021
        </div><br/>
        <div class="nouridio">site desenvolvido por <a href="https://nouridio.com" target="_blank"> nouridio</a></div>
    </div>
</div>
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
<script src="src/js/now-ui-kit.min.js"></script>
</body>
</html>
