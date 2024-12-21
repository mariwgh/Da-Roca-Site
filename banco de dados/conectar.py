import os
import getpass as gp
import pyodbc as bd

def seletor():   # CRUD:  Create Retrieve Update Delete
    opcao = 1
    while opcao != 0:
        os.system('cls') or None
        print("Operações disponíveis: ")
        print("0 - Terminar este programa")
        print("1 - Incluir produtos/clientes")
        print("2 - Alterar produtos/clientes")     
        print("3 - Excluir produtos/clientes")
        print("4 - Listar produtos/clientes")
        opcao = int(input("\nDigite o número da opção desejada: "))
        match opcao:
            case 1: incluir()
            case 2: alterar()
            case 3: excluir()
            case 4: listar()
            

def conectouAoBancoDeDados() -> bool: # informará se conseguiu ou não conectar
    global conexao
    os.system('cls') or None
    # conectar este programa ao servidor de banco de dados
    # usuario = input("Digite seu usuário do seu banco de dados: ")
    senha = gp.getpass("Digite a senha do seu banco de dados: ")  # pede a senha
    
    try:
        conexao = bd.connect(driver="{SQL Server}",
                            server="regulus.cotuca.unicamp.br",
                            database=f"BD24140",
                            uid=f"BD24140",
                            pwd=f"{senha}")  # substitui variável senha 
                                             # pela senha digitada
        print("Conexão bem sucedida!")
        return True
    
    except:
        # se o fluxo de execução vem para este trecho, 
        # a conexão ao servidor de BD não deu certo
        print("Não foi possível conectar ao banco de dados.")
        return False

def incluir():
    """fazer um cadastro de usuario, cadastro de produto"""
    # cursor é um objeto que permite que nosso programa execute 
    # comandos de SQL lá no servidor remoto:
    meuCursor = conexao.cursor()  # cursor: objeto de manipulação de dados
    
    print("0 - Sair\n1 - Incluir produto\n2 - Incluir cliente")
    escolha = int(input("Digite o número da opção desejada: "))
    
    match escolha:
        
        case 1:                                                                         #produto
            id_produto = 1
            while id_produto != 0:
                # pedimos que o usuário digite os dados do novo departamento
                id_produto = int(input("ID do novo produto (0 para terminar): "))
                if id_produto != 0:    # usuário não quer terminar o cadastro
                    nome = input("Nome do produto: ")
                    preco = float(input("Preço (r.rr): "))
                    
                    # criamos uma string com o comando Insert para inserir os novos dados
                    sComando = "insert into daroca.produtos " +\
                            " (nome, imagem, valor, descricao, categoria) "+\
                            " values "+\
                            f"({id_produto}, '{nome}', {preco})"
                    
                    # fazemos o cursor executar a string com o comando Insert que criamos
                    try:        # tente executar o comando abaixo:
                        meuCursor.execute(sComando)
                    except:     # em caso de erro
                        print("Não foi possível incluir. Pode haver produto repetido.")
            
            # após digitar numDepto = 0, o fluxo sai do while, paramos 
            # o cadastramento e enviamos os registros inseridos para 
            # serem definitivamente gravados no servidor de banco de dados 
            # remoto
            meuCursor.commit() # enviar as mudanças para o BD     
            
        case 2:                                                                                 #usuario
            usuario = "-"
            while usuario != " ":
                # pedimos que o usuário digite os dados do novo departamento
                usuario = input("Usuário (0 para terminar): ")
                if usuario != "0":    # usuário não quer terminar o cadastro
                    nome_comp = input("Nome completo: ")
                    senha = input("Senha: ")
                    nascimento = input("Data de nascimento (aaaa-mm-dd): ")
                    email = input("E-mail: ")
                    frequencia = input("Frequência: ")
                    
                    # criamos uma string com o comando Insert para inserir os novos dados
                    sComando = "insert into DaRoca_clientes " +\
                            "       (usuario, nome, senha, nascimento, email, frequencia)"+\
                            " values "+\
                            f"({usuario}, '{nome_comp}', '{senha}', '{nascimento}', '{email}', '{frequencia}')"
                    
                    # fazemos o cursor executar a string com o comando Insert que criamos
                    try:        # tente executar o comando abaixo:
                        meuCursor.execute(sComando)
                    except:     # em caso de erro
                        print("Não foi possível incluir. Pode haver usuário repetido.")
            
            # após digitar numDepto = 0, o fluxo sai do while, paramos 
            # o cadastramento e enviamos os registros inseridos para 
            # serem definitivamente gravados no servidor de banco de dados 
            # remoto
            meuCursor.commit() # enviar as mudanças para o BD     

def alterar():  
    """alterar preço de produto, cadastro do usuario"""
    # cursor é um objeto que permite que nosso programa execute comandos
    # de SQL lá no servidor remoto:
    meuCursor = conexao.cursor()  # objeto de manipulação de dados
    
    print("0 - Sair\n1 - Alterar produto\n2 - Alterar cliente")
    escolha = int(input("Digite o número da opção desejada: "))
    
    match escolha:
        
        case 1:                                                             #produto
            id_produto = 1
            while id_produto != 0:
                # pedimos que o usuário digite o número do departamento a ser alterado
                id_produto = int(input("ID do produto (0 para terminar): "))
                if id_produto != 0:    # usuário não quer terminar o cadastro
                    # verifica no BD se existe um departamento com esse número digitado
                    sComando =  'select nome, preco from DaRoca_produtos where id = ?'
                    
                    result = meuCursor.execute(sComando, id_produto)
                    registros = result.fetchall()  # fetchall recupera os dados e os armazena na variável registros
                    if len(registros) == 0:
                        print("Produto não encontrado.")
                    else:
                        print("Registro encontrado:")
                        print(registros)
                        nome_produto = registros[0][0]      # 1o registro, 1o campo do select acima
                        preco = registros[0][1]             # 1o registro, 2o campo do select acima
                        print("Nome do produto: "+nome_produto)
                        print("Preço: "+preco)
                        
                        print("Abaixo, digite [Enter] para manter a informação atual: ")
                        
                        nome_produto = input("Novo nome do produto: ")
                        preco = float(input("Novo preço do produto: "))
                        
                        if nome_produto == "":  # usuário digitou [Enter]
                            nome_produto = registros[0][0]    # nome original do BD
                            
                        if preco == "":   # usuário digitou [Enter]
                            preco = registros[0][1]   # gerente original do BD
                                
                    # criamos uma string com o comando Update para atualizar os novos dados
                        sComando = "update DaRoca_produtos set nome = ?, preco = ?, where id = ? "
                        
                        # fazemos o cursor executar a string com o comando Update que criamos
                        try:        # tente executar o comando abaixo:
                            meuCursor.execute(sComando, nome_produto, preco, id_produto)
                        except:     # em caso de erro
                            print("Não foi possível incluir. Pode haver produto repetido.")
            
            # após digitar numDepto = 0, paramos o cadastramento
            # e enviamos os registros inseridos para serem definitivamente
            # gravados no servidor de banco de dados remoto
            meuCursor.commit() # enviar as mudanças para o BD   
            
        case 2:                                                                     #cliente
            usuario = 1
            while usuario != 0:
                # pedimos que o usuário digite o número do departamento a ser alterado
                usuario = int(input("Usuário (0 para terminar): "))
                if usuario != 0:    # usuário não quer terminar o cadastro
                    # verifica no BD se existe um departamento com esse número digitado
                    sComando =  'select nome, senha, nascimento, email, frequencia from DaRoca_clientes where usuario = ?'
                    
                    result = meuCursor.execute(sComando, usuario)
                    registros = result.fetchall()  # fetchall recupera os dados e os armazena na variável registros
                    
                    if len(registros) == 0:
                        print("Usuário não encontrado.")
                    else:
                        print("Usuário encontrado:")
                        print(registros)
                        nome_comp = registros[0][0]     # 1o registro, 1o campo do select acima
                        senha = registros[0][1]       # 1o registro, 2o campo do select acima
                        nascimento = registros[0][2]       # 1o registro, 3o campo do select acima
                        email = registros[0][3]       # 1o registro, 4o campo do select acima
                        frequencia = registros[0][4]       # 1o registro, 5o campo do select acima
                        
                        print("Nome: "+nome_comp)
                        print("Senha: "+senha)
                        print("Nascimento: "+nascimento)
                        print("E-mail: "+email)
                        print("Frequência: "+frequencia)
                        
                        print("Abaixo, digite [Enter] para manter a informação atual: ")
                        nome_comp = input("Novo nome: ")
                        senha = input("Nova senha: ")
                        nascimento = input("Novo nascimento (dd/mm/aaaa): ")
                        email = input("Novo email: ")
                        frequencia = input("Nova frequencia: ")
                        
                        if nome_comp == "":  # usuário digitou [Enter]
                            nome_comp = registros[0][0]    # nome original do BD
                            
                        if senha == "":   # usuário digitou [Enter]
                            senha = registros[0][1]   # gerente original do BD
                            
                        if nascimento == "":   # usuário digitou [Enter]
                            nascimento = registros[0][2]   # gerente original do BD
                            
                        if email == "":   # usuário digitou [Enter]
                            email = registros[0][3]   # gerente original do BD
                            
                        if frequencia == "":   # usuário digitou [Enter]
                            frequencia = registros[0][4]   # gerente original do BD
                                
                    # criamos uma string com o comando Update para atualizar os novos dados
                        sComando = "update DaRoca_clientes set nome = ?, senha = ?, nascimento = ?, email = ?, frequencia = ? where usuario = ? "
                        
                        # fazemos o cursor executar a string com o comando Update que criamos
                        try:        # tente executar o comando abaixo:
                            meuCursor.execute(sComando, nome_comp, senha, nascimento, email, frequencia, usuario)
                        except:     # em caso de erro
                            print("Não foi possível incluir. Pode haver usuário repetido.")
            
            # após digitar numDepto = 0, paramos o cadastramento
            # e enviamos os registros inseridos para serem definitivamente
            # gravados no servidor de banco de dados remoto
            meuCursor.commit() # enviar as mudanças para o BD   

def excluir():
    """deletar a conta de um usuario, excluir um produto"""
    # cursor é um objeto que permite que nosso programa execute comandos
    # de SQL lá no servidor remoto:
    meuCursor = conexao.cursor()  # objeto de manipulação de dados
    
    print("0 - Sair\n1 - Alterar produto\n2 - Alterar cliente")
    escolha = int(input("Digite o número da opção desejada: "))
    
    match escolha:
        
        case 1:                                                             #produto
            id_produto = 1
            while id_produto != 0:
                # pedimos que o usuário digite o número do departamento a ser excluído
                id_produto = int(input("ID do produto (0 para terminar): "))
                if id_produto != 0:    # usuário não quer terminar o cadastro
                    # verifica no BD se existe um departamento com esse número digitado
                    result = meuCursor.execute(
                            'select nome, preco from DaRoca_produtos where id = ?', id_produto)
                    registros = result.fetchall()
                    
                    if len(registros) == 0:
                        print("Produto não encontrado.")
                    else:
                        print("Produto encontrado: ")
                        nome_produto = registros[0][0]
                        preco = registros[0][1]
                        
                        print("Nome do produto: "+nome_produto)
                        print("Preço: "+preco)
                        
                        resposta = input("Deseja realmente excluir (s/n)?")
                        if resposta == "s":
                            # criamos uma string com o comando Delete para excluir o registro lido
                            sComando = "delete from DaRoca_produtos where id = ? "
                            
                            # fazemos o cursor executar a string com o comando Update que criamos
                            try:        # tente executar o comando abaixo:
                                meuCursor.execute(sComando, id_produto)
                                print("Produto excluído.")
                            except:     # em caso de erro
                                print("Não foi possível excluir. Deve ser um produto em uso.")
            
            # após digitar numDepto = 0, paramos o cadastramento
            # e enviamos os registros inseridos para serem definitivamente
            # gravados no servidor de banco de dados remoto
            meuCursor.commit() # enviar as mudanças para o BD
            
        case 2:                                                             #produto
            usuario = "-"
            while usuario != "":
                # pedimos que o usuário digite o número do departamento a ser excluído
                usuario = input("Usuário (espaço para terminar): ")
                if usuario != "":    # usuário não quer terminar o cadastro
                    # verifica no BD se existe um departamento com esse número digitado
                    result = meuCursor.execute(
                            'select nome, senha, nascimento, email, frequencia from DaRoca_clientes where usuario = ?', usuario)
                    registros = result.fetchall()
                    
                    if len(registros) == 0:
                        print("Usuário não encontrado.")
                    else:
                        print("Usuário encontrado: ")
                        nome_comp = registros[0][0]
                        senha = registros[0][1]
                        nascimento = registros[0][2]
                        email = registros[0][3]
                        frequencia = registros[0][4]
                        
                        print("Nome: "+nome_comp)
                        print("Senha: "+senha)
                        print("Nascimento: "+nascimento)
                        print("E-mail: "+email)
                        print("Frequência: "+frequencia)
                        
                        resposta = input("Deseja realmente excluir (s/n)?")
                        if resposta == "s":
                            # criamos uma string com o comando Delete para excluir o registro lido
                            sComando = "delete from DaRoca_clientes where usuario = ? "
                            
                            # fazemos o cursor executar a string com o comando Update que criamos
                            try:        # tente executar o comando abaixo:
                                meuCursor.execute(sComando, usuario)
                                print("Usuário excluído.")
                            except:     # em caso de erro
                                print("Não foi possível excluir. Deve ser um usuário em uso.")
            
            # após digitar numDepto = 0, paramos o cadastramento
            # e enviamos os registros inseridos para serem definitivamente
            # gravados no servidor de banco de dados remoto
            meuCursor.commit() # enviar as mudanças para o BD   

def listar():
    """lista os produtos e os usuarios"""
    # cursor é um objeto que permite que nosso programa execute comandos
    # de SQL lá no servidor remoto:
    meuCursor = conexao.cursor()  # objeto de manipulação de dados
    
    print("0 - Sair\n1 - Alterar produto\n2 - Alterar cliente")
    escolha = int(input("Digite o número da opção desejada: "))
    
    match escolha:
        
        case 1:                                                             #produto
            # busca no BD os registros de departamentos
            try: 
                result = meuCursor.execute(
                            'select id, nome, preco from DaRoca_produtos ')   
                registros = result.fetchall()
            except:
                print("Erro na busca dos dados\n")
            print("ID  Nome       Preço")
            # print(registros)
            
            for prod in registros:
                print(f"{prod[0]}\t{prod[1]}\t{prod[2]}")
                
            input("Tecle [enter] para terminar:")
            
        case 2:                                                         #clientes
            # busca no BD os registros de departamentos
            try: 
                result = meuCursor.execute(
                            'select usuario, nome, senha, nascimento, email, frequencia from DaRoca_clientes ')   
                registros = result.fetchall()
            except:
                print("Erro na busca dos dados\n")
            print("Usuário\tNome\tSenha\tNascimento\tE-mail\tFrequência")
            # print(registros)
            
            for cliente in registros:
                print(f"{cliente[0]}\t{cliente[1]}\t{cliente[2]}\t{cliente[3]}\t{cliente[4]}\t{cliente[5]}")
                
            input("Tecle [enter] para terminar:")
            

if __name__ == "__main__":
    if conectouAoBancoDeDados():
        seletor()
        conexao.close()
        
print("Programa encerrado.")