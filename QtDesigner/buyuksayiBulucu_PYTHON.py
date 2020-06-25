#Bismillah

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def clicked():
    print("clicked")
    label.setText("Basma")

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("Selam")

    label = QtWidgets.QLabel(win)
    label.setText("my first label!")
    label.move(50, 100)

    b1 = QtWidgets.QPushButton(win)
    b1.move(50, 50)
    b1.setText("Click Me")
    b1.clicked.connect(clicked)
    
    win.show()
    sys.exit(app.exec_())

    
window()
