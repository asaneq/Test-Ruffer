#
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle('Здоровье') 
        self.move(win_x, win_y)
        self.resize(win_height, win_widht)
 
    def initUI(self):
        pass
    def connects(self):
        pass


app = QApplication([])
main_win = MainWin()
app.exec_()
