from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc as bd

class Ui_FrmDepto(object):
    def setupUi(self, FrmDepto):
        FrmDepto.setObjectName("FrmDepto")
        FrmDepto.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(FrmDepto)
        self.centralwidget.setObjectName("centralwidget")
        self.btnListar = QtWidgets.QPushButton(self.centralwidget)
        self.btnListar.setGeometry(QtCore.QRect(150, 120, 100, 30))
        self.btnListar.setObjectName("btnListar")
        FrmDepto.setCentralWidget(self.centralwidget)

        self.retranslateUi(FrmDepto)
        QtCore.QMetaObject.connectSlotsByName(FrmDepto)

        # Conectando o botão à função de listagem
        self.btnListar.clicked.connect(self.listar)

    def retranslateUi(self, FrmDepto):
        _translate = QtCore.QCoreApplication.translate
        FrmDepto.setWindowTitle(_translate("FrmDepto", "Departamentos"))
        self.btnListar.setText(_translate("FrmDepto", "Listar"))

    def listar(self):
        try:
            conexao = bd.connect(driver="{SQL Server}",
                                 server="regulus.cotuca.unicamp.br",
                                 database="BD24140",
                                 uid="BD24140",
                                 pwd="sua_senha_aqui")
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM daroca.produtos WHERE categoria = 5")
            registros = cursor.fetchall()
            for prod in registros:
                print(f"{prod[0]}\t{prod[1]}\t{prod[2]}\t{prod[3]}\t{prod[4]}\t{prod[5]}")
            conexao.close()

        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Erro", f"Erro na busca dos dados: {e}")
