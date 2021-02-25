import sys
from PyQt5.QtWidgets import *

# used to import the font
from PyQt5.QtGui import QFont


#Allows you to pick the font
font = QFont("Times", 11)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(250, 250, 350, 350)
        self.UI()

    def UI(self):
        button = QPushButton("Click Me Please",self)
        button.move(100,100)
        # sets given font to the message buttons
        button.setFont(font)
        button.clicked.connect(self.messagebox)

        self.show()

    def messagebox(self):
        #The commented out sections are used to create a question
        #mbox = QMessageBox.question(self, "Warning!!!", "You are trying to exit the application, are you sure?" , QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel , QMessageBox.No)
        #if mbox == QMessageBox.Yes:
           # sys.exit()
        #elif mbox == QMessageBox.No:
            #print("You chose not to exit")
        #else:
            #print("canceled")
        mbox = QMessageBox.information(self,"Warning!","You logged out")
def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()