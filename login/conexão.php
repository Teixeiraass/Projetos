<?php
define('HOST', '127.0.0.1');
define('USUARIO', 'root');
define('SENHA', '84568302');
define('DB', 'Login');

$conexao = mysqli_conect(HOST, USUARIO, SENHA, DB) or die("Não foi possivel conectar");