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
    categoria = 1
    while categoria != 0:
        # pedimos que o usuário digite os dados do novo departamento
        categoria = int(input("Categoria do produto (0 para terminar): "))
        if categoria != 0:    # usuário não quer terminar o cadastro
            imagem = input("Imagem do produto: ")
            nome_produto = input("Nome do novo produto: ")
            valor = float(input("Preço (r.rr): "))
            descricao = input("Descrição do produto: ")
            
            
            # criamos uma string com o comando Insert para inserir os novos dados
            sComando = "insert into daroca.produtos " +\
                    " (nome, imagem, valor, descricao, categoria) "+\
                    " values "+\
                    f"('{nome_produto}', '{imagem}', {valor} , '{descricao}' , {categoria})"
            
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
            

def alterar():  
    """alterar preço de produto, cadastro do usuario"""
    # cursor é um objeto que permite que nosso programa execute comandos
    # de SQL lá no servidor remoto:
    meuCursor = conexao.cursor()  # objeto de manipulação de dados
            
    id_produto = 1
    while id_produto != 0:
        # pedimos que o usuário digite o número do departamento a ser alterado
        id_produto = int(input("ID do produto (0 para terminar): "))
        if id_produto != 0:    # usuário não quer terminar o cadastro
            # verifica no BD se existe um departamento com esse número digitado
            sComando =  'select nome , imagem , valor , descricao , categoria from daroca.produtos where id = ?'
            
            result = meuCursor.execute(sComando, id_produto)
            registros = result.fetchall()  # fetchall recupera os dados e os armazena na variável registros
            if len(registros) == 0:
                print("Produto não encontrado.")
            else:
                print("Registro encontrado:")
                print(registros)
                nome_produto = registros[0][0]      # 1o registro, 1o campo do select acima
                valor = registros[0][2]             # 1o registro, 2o campo do select acima
                imagem = registros[0][1]
                descricao = registros[0][3]
                categoria = registros[0][4]
                print("Nome do produto: "+nome_produto)
                print("Imagem: "+imagem)
                print("Valor: "+valor)
                print("Descrição: "+descricao)
                print("Categoria: "+categoria)
                
                print("Abaixo, digite [Enter] para manter a informação atual: ")
                
                nome_produto = input("Novo nome do produto: ")
                valor = float(input("Novo valor do produto: "))
                imagem = input("Nova imagem do produto: ")
                descricao = input("Nova descrição do produto: ")
                categoria = int(input("Nova categoria do produto: "))
                    
                if nome_produto == "":  # usuário digitou [Enter]
                    nome_produto = registros[0][0]    # nome original do BD
                    
                if valor == "":   # usuário digitou [Enter]
                    valor = registros[0][2]   # gerente original do BD

                if imagem == "":   # usuário digitou [Enter]
                    imagem = registros[0][1]   # gerente original do BD

                if descricao == "":   # usuário digitou [Enter]
                    descricao = registros[0][3]   # gerente original do BD
                    
                if categoria == "":   # usuário digitou [Enter]
                    categoria = registros[0][4]   # gerente original do BD
                        
            # criamos uma string com o comando Update para atualizar os novos dados
                sComando = "update daroca.produtos set nome = ?, imagem = ?, valor = ?, descricao = ? , categoria = ?  where id = ? "
                
                # fazemos o cursor executar a string com o comando Update que criamos
                try:        # tente executar o comando abaixo:
                    meuCursor.execute(sComando, nome_produto, imagem , valor, descricao , categoria, id_produto)
                except:     # em caso de erro
                    print("Não foi possível incluir. Pode haver produto repetido.")
    
    # após digitar numDepto = 0, paramos o cadastramento
    # e enviamos os registros inseridos para serem definitivamente
    # gravados no servidor de banco de dados remoto
    meuCursor.commit() # enviar as mudanças para o BD   
            
        
def excluir():
    """deletar a conta de um usuario, excluir um produto"""
    # cursor é um objeto que permite que nosso programa execute comandos
    # de SQL lá no servidor remoto:
    meuCursor = conexao.cursor()  # objeto de manipulação de dados
                                                             #produto
    id_produto = 1
    while id_produto != 0:
        # pedimos que o usuário digite o número do departamento a ser excluído
        id_produto = int(input("ID do produto (0 para terminar): "))
        if id_produto != 0:    # usuário não quer terminar o cadastro
            # verifica no BD se existe um departamento com esse número digitado
            result = meuCursor.execute(
                    'select nome , imagem, valor , descricao , categoria from daroca.produtos where id = ?', id_produto)
            registros = result.fetchall()
            
            if len(registros) == 0:
                print("Produto não encontrado.")
            else:
                print("Produto encontrado: ")
                nome_produto = registros[0][0]
                imagem = registros[0][1]
                valor = registros[0][2]
                descricao = registros[0][3]
                categoria = registros[0][4]
                
                print("Nome do produto: "+nome_produto)
                print("Imagem: "+imagem)
                print("Valor: "+valor)
                print("Descrição: "+descricao)
                print("Categoria: "+categoria)
                
                resposta = input("Deseja realmente excluir (s/n)?")
                if resposta == "s":
                    # criamos uma string com o comando Delete para excluir o registro lido
                    sComando = "delete from daroca.produtos where id = ? "
                    
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

def listar():
    """lista os produtos e os usuarios"""
    # cursor é um objeto que permite que nosso programa execute comandos
    # de SQL lá no servidor remoto:
    meuCursor = conexao.cursor()  # objeto de manipulação de dados                    #produto
    categoria = 5
    while categoria != 0:
        categoria=  int(input('Digite a categoria do produto desejado: '))
        # busca no BD os registros de departamentos
        try: 
            result = meuCursor.execute(
                        'select * from daroca.produtos where categoria = ? ', categoria)   
            registros = result.fetchall()
        except:
            print("Erro na busca dos dados\n")
        print("ID  Nome       Imagem        Valor       Descrição       Categoria")
        # print(registros)
        
        for prod in registros:
            print(f"{prod[0]}\t{prod[1]}\t{prod[2]}\t{prod[3]}\t{prod[4]}\t{prod[5]}")
            
    input("Tecle [enter] para terminar")


if __name__ == "__main__":
    if conectouAoBancoDeDados():
        seletor()
        conexao.close()
        
print("Programa encerrado.")