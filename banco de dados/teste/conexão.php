<?php

$bd = "nome_do_banco_de_dados"; //variavel pra guardar o nome do BD
$usuario = "nome_do_usuario"; // variavel que guarda o nome do usuario pra conexao no BD
$senha = "senha" //variavel que guarda a senha;

mysql_connect($bd,$usuario,$senha) or die ("nao foi possivel fazer a conexao com o banco de dados");
/*mysql_connect tenta a conexão com o BD, pra isso ele precisa dos parametros "nome do banco", "usuario" e "senha" 

se ele conectar beleza, caso contrario ele exibe a mensagem de erro graças ao "or die" rs*/