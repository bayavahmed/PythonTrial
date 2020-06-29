#Bismillah

from PyQt5.QtWidgets import *


class firstGUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        labelText = QLabel("Merhabalar")

        verticalLayout = QVBoxLayout()
        verticalLayout.addWidget(labelText)
        self.setLayout(verticalLayout)

uygulama = QApplication([])
pencere = firstGUI()
pencere.resize(500, 500)
pencere.setWindowTitle("PyCharm")

pencere.show()
uygulama.exec_()