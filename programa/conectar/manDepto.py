import sys
from PySide6.QtCore import QtMsgType
from PySide6.QtWidgets import QApplication, QMainWindow, QStatusBar, QDialog, QTableWidgetItem
from FrmDepto_ui import Ui_FrmDepto
from FrmConexao_ui import Ui_dlgConectar
import pyodbc as bd
from datetime import datetime

global conexao, meuCursor

class FormPrincipal(QMainWindow, Ui_FrmDepto):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        # associa o evento Click de cada botão a um método
        # da classe FormPrincipal que implementa o algoritmo
        # que se espera que esse botão dispare para execução
        self.action_Sair.triggered.connect(self.sairDoPrograma)
        self.action_Novo.triggered.connect(self.novoRegistro)
        self.action_Editar.triggered.connect(self.editarRegistro)
        self.action_Salvar.triggered.connect(self.salvarRegistro)
        self.action_Excluir.triggered.connect(self.excluirRegistro)
        self.action_Cancelar.triggered.connect(self.cancelarAcao)       
        self.abas.currentChanged.connect(self.mudarTab)  

        self.osDados = []
        self.quantosDados = 0
        self.registroAtual = -1  # índice do registro visitado (na tela)
        self.buscarDados()

        self.action_Inicio.triggered.connect(self.irAoInicio)
        self.action_Anterior.triggered.connect(self.irAoAnterior)
        self.action_Proximo.triggered.connect(self.irAoProximo)
        self.action_Fim.triggered.connect(self.irAoFim)
        self.atualizarTela()    # exibirá o registro atual da tabela 

        self.show()
        self.situacao = "navegando"

    def buscarDados(self):
        try:
            sComando = "SELECT numDepto, nomeDepto, "+\
                " gerente_numSegSocial, gerente_dataInicial "+\
                " FROM EmpM.Departamento "+\
                " ORDER BY numDepto"
            resultado = meuCursor.execute(sComando)
            self.osDados = resultado.fetchall()    # vetor de registros
            self.quantosDados = len(self.osDados)  # quantos registros
            if self.quantosDados > 0:   # dados foram trazidos
                self.registroAtual = 0  # posiciona no primeiro índice
        except:
            print("Erro ao buscar os dados para navegação.")

    def irAoInicio(self):
        self.registroAtual = 0
        self.atualizarTela()
        
    def irAoAnterior(self):
        if self.registroAtual > 0:
            self.registroAtual -= 1			# recua índice
            self.atualizarTela()
            
    def irAoProximo(self):
        if self.registroAtual < self.quantosDados - 1:
            self.registroAtual += 1			# avança índice
            self.atualizarTela()
            
    def irAoFim(self):
        self.registroAtual = self.quantosDados - 1
        self.atualizarTela()
        
    def atualizarTela(self):
        if self.quantosDados > 0:        # há dados para exibir
            self.spbNumDepto.setValue(self.osDados[self.registroAtual][0])
            self.edNomeDepto.setText(self.osDados[self.registroAtual][1])
            self.edNumSegSocial.setText(self.osDados[self.registroAtual][2])
            data = datetime.strptime(self.osDados[self.registroAtual][3], '%Y-%m-%d')
            self.deDataInicialGerente.setDate(data)
        else:
            self.limparTela()    # tabela de dados está vazia
            
    def limparTela(self):
        self.spbNumDepto.setValue(1)
        self.edNomeDepto.setText("")
        self.edGerente_NumSegSocial.setText("")
        self.deData_Inicial_Gerente.setDate(datetime.now)

    def novoRegistro(self):
        self.spbNumDepto.setValue(0)
        self.edNomeDepto.setText("")
        self.edNumSegSocial.setText("")
        self.deDataInicialGerente.setDate(datetime.today())
        self.situacao = "incluindo"
        self.spbNumDepto.setReadOnly(False)
        self.spbNumDepto.setFocus()
        self.statusBar.showMessage("Digite os dados acima")

    def editarRegistro(self):
        self.situacao = "editando"
        self.edNomeDepto.setFocus()             # coloca cursor nesse campo
        self.spbNumDepto.setReadOnly(True)      # impede digitação
        self.statusBar.showMessage("Altere os dados acima")

    def salvarRegistro(self):
        if self.situacao == "incluindo":
            sComando = "Insert into EmpM.Departamento "+\
                " (numDepto, nomeDepto, gerente_numSegSocial, "+\
                " gerente_dataInicial) "+\
                " values( ?, ?, ?, Convert(date, ?, 103) ) "

            try:        # tente executar o comando abaixo:
                meuCursor.execute(sComando,
                                           int(self.spbNumDepto.value()), 
                                           self.edNomeDepto.text(), 
                                           self.edNumSegSocial.text(),
            f"{self.deDataInicialGerente.date().toString('dd/MM/yyyy')}")
                meuCursor.commit()  # enviar as mudanças para o BD
                self.statusBar.showMessage("Inserido") 
   
            except Exception as erro:     # em caso de erro
                if hasattr(erro, 'message'):
                    mensagem = erro.message
                else:
                    mensagem = erro.args[1]
                self.statusBar.showMessage(mensagem)

        elif self.situacao =="editando":
            sComando = "Update EmpM.Departamento "+\
                " set nomeDepto = ?, gerente_numSegSocial = ?, "+\
                " gerente_dataInicial = ? "+\
                " where numDepto = ? "

            try:        # tente executar o comando abaixo:
                data = self.deDataInicialGerente.date()
                data = data.toString('yyyy-MM-dd')
                meuCursor.execute(sComando, self.edNomeDepto.text(),
                                         self.edNumSegSocial.text(),
                                         data,
                                         int(self.spbNumDepto.value()))
                meuCursor.commit()  # enviar as mudanças para o BD
                self.statusBar.showMessage("Alterado")  
  
            except Exception as erro:     # em caso de erro
                if hasattr(erro, 'message'):
                    mensagem = erro.message
                else:
                    mensagem = erro.args[1]
                self.statusBar.showMessage(mensagem)
        self.situacao = "navegando"
        self.buscarDados()
        self.atualizarTela()

    def excluirRegistro(self):
        self.situacao = "excluindo"
        sComando = "Delete from EmpM.Departamento "+\
                   " where numDepto = ? "
        try:        # tente executar o comando abaixo:
            meuCursor.execute(sComando, self.spbNumDepto.value())
            meuCursor.commit()  # enviar as mudanças para o BD
            self.statusBar.showMessage("Excluído")    
        except Exception as erro:     # em caso de erro
            if hasattr(erro, 'message'):
                mensagem = erro.message
            else:
                mensagem = erro.args[1]
            self.statusBar.showMessage(mensagem)
        self.situacao = "navegando"
        self.buscarDados()
        self.atualizarTela()

    def cancelarAcao(self):
        self.situacao = "navegando"
    
    def mudarTab(self):
        if self.abas.currentIndex() == 1: # busca no BD os registros 
            try: 
                sComando =  "SELECT D.numdepto, NOMEDEPTO, "+\
                    " GERENTE_NUMSEGSOCIAL, "+\
                    " PreNome+' '+InicialMeio+' '+Sobrenome as Nome, "+\
                    " GERENTE_DATAINICIAL "+\
                    " FROM EMPm.DEPARTAMENTO D, Empm.Empregado E"+\
                    " WHERE D.Gerente_numSegSocial = E.numSegSocial "+\
                    " ORDER BY NomeDepto"
                
                result = meuCursor.execute(sComando)
                regs = result.fetchall()
                numeroDeLinhas = len(regs)
                self.gridDepto.setRowCount(numeroDeLinhas)
                for indice in range(0, numeroDeLinhas, 1):
                    item_numDepto    = QTableWidgetItem(regs[indice][0])
                    item_nomeDepto   = QTableWidgetItem(regs[indice][1])
                    item_numGerente  = QTableWidgetItem(regs[indice][2])
                    item_nomeGerente = QTableWidgetItem(regs[indice][3])
                    item_dataGerente = QTableWidgetItem(regs[indice][4])
                    
                    self.gridDepto.setItem(indice, 0, item_numDepto)
                    self.gridDepto.setItem(indice, 1, item_nomeDepto)
                    self.gridDepto.setItem(indice, 2, item_numGerente)
                    self.gridDepto.setItem(indice, 3, item_nomeGerente)
                    self.gridDepto.setItem(indice, 4, item_dataGerente)

                self.gridDepto.resizeColumnsToContents()
                self.gridDepto.resizeRowsToContents()
                self.statusBar.showMessage("Listagem")
            except Exception as erro:     # em caso de erro
                if hasattr(erro, 'message'):
                    mensagem = erro.message
                else:
                    mensagem = erro.args[1]
                self.statusBar.showMessage(mensagem)





    def sairDoPrograma(self):
        self.close()

class DialogoConexao(QDialog, Ui_dlgConectar):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setModal(True)

aplicacao = QApplication(sys.argv)
dlgCon = DialogoConexao()   # cria instância da janela de conexão ao BD
if dlgCon.exec() == QDialog.Accepted:
    try:
        conexao = bd.connect(driver="SQL Server",
                            server=f"{dlgCon.edServidor.text()}",
                            database=f"{dlgCon.edBancoDeDados.text()}",
                            uid=f"{dlgCon.edUsuario.text()}",
                            pwd=f"{dlgCon.edSenha.text()}") 
        print("Conexão bem sucedida!")
        meuCursor = conexao.cursor()  # cursor: objeto de acesso ao BD
        janela = FormPrincipal()
        aplicacao.exec()
    except:
        print("Não foi possível conectar ao banco de dados")




