import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using LineEdits")
        self.setGeometry(50, 50, 350, 350)
        self.UI()

    def UI(self):
        #Creatione of an editable text box
        self.nameTextBox = QLineEdit(self)
        self.nameTextBox.move(10,10)

        #Used to place text within the editable text box
        self.nameTextBox.setPlaceholderText("Enter your name here")
        self.passwordTextBox = QLineEdit(self)
        self.passwordTextBox.move(10,60)
        self.passwordTextBox.setPlaceholderText("Enter your password here")

        #SetEchoMode is used to block out the passwords
        self.passwordTextBox.setEchoMode(QLineEdit.Password)
        button= QPushButton("Save",self)
        button.move(55,90)
        button.clicked.connect(self.getValues)
        self.show()

    def getValues(self):
        name = self.nameTextBox.text()
        password = self.passwordTextBox.text()
        self.setWindowTitle(" Your name is " + name +" Your password is "+ password)


def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()