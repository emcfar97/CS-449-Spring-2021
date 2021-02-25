import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(50, 50, 350, 350)
        self.UI()

    def UI(self):
        self.name=QLineEdit(self)
        self.name.setPlaceholderText("Enter your name")
        self.name.move(150,80)
        self.surname=QLineEdit(self)
        self.surname.setPlaceholderText("Enter your SurName")
        self.surname.move(150,130)

        #Creates the checkbox Widget
        self.remember=QCheckBox("remember me", self)
        self.remember.move(150,170)

        savebutton = QPushButton ("Save",self)
        savebutton.move(150,200)
        savebutton.clicked.connect(self.saveNames)
        self.show()

    def saveNames(self):
        #isChecked() can be used check whether or not the box has been clicked
        if self.remember.isChecked():
            #.text() is needed to show what is used get what user enteres in widget
            print ("Name: " + self.name.text() +"\nSurname:"+ self.surname.text() + "\nremember me checked")
        else:
            print ("Name: " + self.name.text() +"\nSurname:"+ self.surname.text() + "\nremember me not checked")

def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()