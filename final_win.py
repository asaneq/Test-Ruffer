from PyQt5.QtCore import Qt , QTime , QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_finalwin) 
        self.move(win_x, win_y)
        self.resize(win_height, win_widht)

    def initUI(self):
        ind = (4* (self.exp.test1 + self.exp.test2 + self.exp.test3)-200)/10
        ind1 = txt_index + str(ind)
        self.index = QLabel(ind1)
        self.workheart = QLabel(txt_workheart)
        self.m_line = QVBoxLayout()
        self.m_line.addWidget(self.index , alignment = Qt.AlignCenter)
        self.m_line.addWidget(self.workheart , alignment = Qt.AlignCenter)
        self.setLayout(self.m_line)

    def connects(self):
        pass
    
    def next_click(self):
        pass
