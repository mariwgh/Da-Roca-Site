# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrmConexao.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_dlgConectar(object):
    def setupUi(self, dlgConectar):
        if not dlgConectar.objectName():
            dlgConectar.setObjectName(u"dlgConectar")
        dlgConectar.resize(308, 166)
        font = QFont()
        font.setPointSize(10)
        dlgConectar.setFont(font)
        self.buttonBox = QDialogButtonBox(dlgConectar)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 130, 261, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.widget = QWidget(dlgConectar)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 291, 108))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.edServidor = QLineEdit(self.widget)
        self.edServidor.setObjectName(u"edServidor")

        self.gridLayout.addWidget(self.edServidor, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.edBancoDeDados = QLineEdit(self.widget)
        self.edBancoDeDados.setObjectName(u"edBancoDeDados")

        self.gridLayout.addWidget(self.edBancoDeDados, 1, 1, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.edUsuario = QLineEdit(self.widget)
        self.edUsuario.setObjectName(u"edUsuario")

        self.gridLayout.addWidget(self.edUsuario, 2, 1, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.edSenha = QLineEdit(self.widget)
        self.edSenha.setObjectName(u"edSenha")
        self.edSenha.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.edSenha, 3, 1, 1, 1)


        self.retranslateUi(dlgConectar)
        self.buttonBox.accepted.connect(dlgConectar.accept)
        self.buttonBox.rejected.connect(dlgConectar.reject)

        QMetaObject.connectSlotsByName(dlgConectar)
    # setupUi

    def retranslateUi(self, dlgConectar):
        dlgConectar.setWindowTitle(QCoreApplication.translate("dlgConectar", u"Conex\u00e3o ao banco de Dados", None))
        self.label.setText(QCoreApplication.translate("dlgConectar", u"Endere\u00e7o do servidor:", None))
        self.edServidor.setText(QCoreApplication.translate("dlgConectar", u"regulus.cotuca.unicamp.br", None))
        self.label_2.setText(QCoreApplication.translate("dlgConectar", u"Nome do banco de dados:", None))
        self.edBancoDeDados.setText(QCoreApplication.translate("dlgConectar", u"chico", None))
        self.label_3.setText(QCoreApplication.translate("dlgConectar", u"Nome de usu\u00e1rio:", None))
        self.edUsuario.setText(QCoreApplication.translate("dlgConectar", u"chico", None))
        self.label_4.setText(QCoreApplication.translate("dlgConectar", u"Senha:", None))
        self.edSenha.setPlaceholderText(QCoreApplication.translate("dlgConectar", u"Digite sua senha", None))
    # retranslateUi

