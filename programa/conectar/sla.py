import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from FrmConexao import Ui_FrmConexao
from FrmDepto import Ui_FrmDepto
import conectar

class ConexaoWindow(QMainWindow, Ui_FrmConexao):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnConectar.clicked.connect(self.tentar_conectar)

    def tentar_conectar(self):
        if conectar.conectouAoBancoDeDados():
            QMessageBox.information(self, "Sucesso", "Conexão bem sucedida!")
            self.open_depto_window()
        else:
            QMessageBox.critical(self, "Erro", "Não foi possível conectar ao banco de dados.")

    def open_depto_window(self):
        self.depto_window = QMainWindow()
        self.ui_depto = Ui_FrmDepto()
        self.ui_depto.setupUi(self.depto_window)
        self.depto_window.show()
        self.close()  # Fecha a janela de conexão

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Executa a interface de conexão
    conexao_window = ConexaoWindow()
    conexao_window.show()

    sys.exit(app.exec_())