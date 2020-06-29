from PyQt5.QtWidgets import *
from ders3 import Ui_MainWindow

class ders_3(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_1.setText("Ders 3")


uygulama = QApplication([])
pencere = ders_3()
pencere.show()
uygulama.exec_()