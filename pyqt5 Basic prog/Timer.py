import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer

font = QFont("Times", 11)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(250, 250, 550, 550)
        self.UI()

    def UI(self):
        self.bkg= QLabel(self)
        self.bkg.resize(250,250)
        self.bkg.setStyleSheet("background-color:green")
        self.bkg.move(150,100)
        self.timer=QTimer(self)
        self.timer.setInterval(200)
        button=QPushButton("start",self)
        button2=QPushButton("stop",self)
        button.move(150,400)
        button2.move(300,400)
        button.clicked.connect(self.start)
        button2.clicked.connect(self.stop)
        self.timer.timeout.connect(self.changecolor)
        self.value = 0
        self.show()

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()

    def changecolor(self):
        if self.value == 0:
            self.bkg.setStyleSheet("background-color:pink")
            self.value = 1
        else:
            self.bkg.setStyleSheet("background-color:orange")
            self.value = 0

def main():
    App = QApplication(sys.argv)
    window=Window()
    window.start()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()