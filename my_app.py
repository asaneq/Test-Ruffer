from PyQt5.QtCore import Qt , QTime , QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.move(win_x, win_y)
        self.resize(win_height, win_widht)
 
    def initUI(self):
        self.hello_txt = QLabel(txt_hello) #для текста добро пожаловать
        self.instruction = QLabel(txt_instruction) #для текста инструкции
        self.button = QPushButton(txt_next) #для кнопки начать
        
        self.VLayout = QVBoxLayout() #для вертикального расположения виджетов
        '''Добавление в вертикальное расположение виджетов'''
        self.VLayout.addWidget(self.hello_txt)
        self.VLayout.addWidget(self.instruction)
        self.VLayout.addWidget(self.button)

        self.setLayout(self.VLayout) #установить расположение для окна


    def connects(self):
        self.button.clicked.connect(self.next_click)
    
    def next_click(self):
        self.hide()
        self.tw = TestWin()


app = QApplication([])
main_win = MainWin()
app.exec_()
