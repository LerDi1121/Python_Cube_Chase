from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QDesktopWidget, QComboBox, QMessageBox
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import Qt
from LevelGenerator import LavirintP
from Pumba import *
import sys

class MainWindow(QWidget):
    MainWindowHeight = 640
    MainWindowWidth = 840

    def __init__(self):
        super().__init__()

        self.initUI()

    def run(self):
        self.LevelGen = LavirintP(self)
        self.hide()

    def quit(self):
        app = QApplication.instance()

    def initUI(self):
        self.initMainMenuButtons()
        self.resize(self.MainWindowHeight, self.MainWindowWidth)
        self.setMinimumHeight(self.MainWindowHeight)
        self.setMinimumWidth(self.MainWindowWidth)
        self.setMaximumHeight(self.MainWindowHeight)
        self.setMaximumWidth(self.MainWindowWidth)
        self.setStyleSheet("background-color: black;")
        self.setWindowTitle("Cub Chase")
        self.center()
        self.show()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2),int( (screen.height() - size.height()) / 2))

    def initMainMenuButtons(self):
        self.startButton = QtWidgets.QPushButton(self)
        self.startButton.setCursor(Qt.PointingHandCursor)
        self.startButton.setStyleSheet("border:1px solid rgb(220, 20, 60); color: gold;font-size: 24px; font-family: Comic Sans MS;");
        self.startButton.setText("START GAME")
        self.startButton.setGeometry(310, 280, 200, 50)
        self.startButton.clicked.connect(self.run)

        self.quitButton = QtWidgets.QPushButton(self)
        self.quitButton.setCursor(Qt.PointingHandCursor)
        self.quitButton.setStyleSheet("border:1px solid rgb(220, 20, 60); color: gold;font-size: 24px; font-family: Comic Sans MS;");
        self.quitButton.setText("EXIT TO DESKTOP")
        self.quitButton.setGeometry(285, 360, 250, 50)
        self.quitButton.clicked.connect(self.quit)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = MainWindow()
    sys.exit(app.exec_())