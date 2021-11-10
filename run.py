import sys
from PyQt6 import QtWidgets
from src.window import StartScreen

app = QtWidgets.QApplication(sys.argv)
window = StartScreen()
window.show()
app.exec()
