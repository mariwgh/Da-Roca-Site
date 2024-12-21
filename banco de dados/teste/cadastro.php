<?php
// Verifica se o formulário foi enviado
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Conecta ao banco de dados (substitua 'host', 'usuario', 'senha' e 'nome_banco' pelos seus valores)
    $conexao = new mysqli("host", "usuario", "senha", "nome_banco");

    // Verifica se a conexão foi bem-sucedida
    if ($conexao->connect_error) {
        die("Falha na conexão: " . $conexao->connect_error);
    }

    // Obtém os dados do formulário
    $nome = $_POST["nome"];
    $email = $_POST["email"];
    $senha = $_POST["senha"];

    // Criptografa a senha (você deve usar uma função de hash segura)
    $senhaCriptografada = password_hash($senha, PASSWORD_DEFAULT);

    // Insere os dados na tabela de usuários
    $sql = "INSERT INTO usuarios (nome, email, senha) VALUES ('$nome', '$email', '$senhaCriptografada')";

    if ($conexao->query($sql) === TRUE) {
        echo "Usuário cadastrado com sucesso!";
    } else {
        echo "Erro ao cadastrar o usuário: " . $conexao->error;
    }

    // Fecha a conexão com o banco de dados
    $conexao->close();
}
?>
