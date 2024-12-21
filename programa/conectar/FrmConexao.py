from PyQt5 import QtCore, QtGui, QtWidgets
import os
import getpass as gp
import pyodbc as bd

class Ui_FrmConexao(object):
    def setupUi(self, FrmConexao):
        FrmConexao.setObjectName("FrmConexao")
        FrmConexao.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(FrmConexao)
        self.centralwidget.setObjectName("centralwidget")
        self.btnConectar = QtWidgets.QPushButton(self.centralwidget)
        self.btnConectar.setGeometry(QtCore.QRect(150, 120, 100, 30))
        self.btnConectar.setObjectName("btnConectar")
        FrmConexao.setCentralWidget(self.centralwidget)

        self.retranslateUi(FrmConexao)
        QtCore.QMetaObject.connectSlotsByName(FrmConexao)

        # Conectando o botão à função de conexão
        self.btnConectar.clicked.connect(self.conectouAoBancoDeDados)

    def retranslateUi(self, FrmConexao):
        _translate = QtCore.QCoreApplication.translate
        FrmConexao.setWindowTitle(_translate("FrmConexao", "Conectar"))
        self.btnConectar.setText(_translate("FrmConexao", "Conectar"))

    def conectouAoBancoDeDados(self):
        senha = gp.getpass("Digite a senha do seu banco de dados: ")

        try:
            self.conexao = bd.connect(driver="{SQL Server}",
                                      server="regulus.cotuca.unicamp.br",
                                      database="BD24140",
                                      uid="BD24140",
                                      pwd=senha)
            QtWidgets.QMessageBox.information(None, "Sucesso", "Conexão bem sucedida!")
            return True

        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Erro", f"Não foi possível conectar ao banco de dados.\n{e}")
            return False
