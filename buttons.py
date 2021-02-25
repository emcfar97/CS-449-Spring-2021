import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(50, 50, 350, 350)
        self.UI()

    def UI(self):
        self.text1=QLabel("My Text",self)

        # creation of the  a buttonbutton
        enterButton= QPushButton("Enter",self)
        exitButton= QPushButton("Exit",self)
        self.text1.move(100,50)
        enterButton.move(100,80)
        exitButton.move(200,80)

        # clicked.connect is used to attach a function to a button
        enterButton.clicked.connect(self.enterFunc)
        exitButton.clicked.connect(self.exitFunc)
        self.show()

    #used to create a function for the enter button
    def enterFunc(self):
        self.text1.setText("You clicked Enter")
        self.text1.resize(150, 20)

    #Used to create function for the exit button
    def exitFunc(self):
        self.text1.setText("you clicked Exit")
        self.text1.resize(150,20)

def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()