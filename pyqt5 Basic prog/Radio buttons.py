import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(50, 50, 350, 350)
        self.UI()

    def UI(self):

        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Enter your name here")
        self.name.move(100,100)
        self.surname = QLineEdit(self)
        self.surname.setPlaceholderText("Enter your surname here")
        self.surname.move(100,150)

        #Cretaes a Radio button
        self.male = QRadioButton("Male",self)
        self.male.move(100,180)
        self.male.isChecked()
        self.female = QRadioButton("Female",self)
        self.female.move(170,180)
        self.female.isChecked()
        button = QPushButton("Save",self)
        button.move(150,200)
        button.clicked.connect(self.getValues)

        self.show()

    def getValues(self):
        name = self.name.text()
        surname = self.surname.text()
        if self.male.isChecked():
            print(name+ " " + surname + " Identifies as a male")
        else:
            print(name+ " " + surname + " Identifies as a female")

def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()