from PyQt5.QtWidgets import QMainWindow, QLabel, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QPixmap

class Proba():
    broj = 5
    drugiBroj=6

    def __init__(self, parent):
        super().__init__(parent)

    def nekaFunkcija(self, param1, param2):
        self.broj= param1
        self.drugiBroj= param2