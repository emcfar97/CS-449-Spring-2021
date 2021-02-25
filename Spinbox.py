import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont("Times", 11)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(250, 250, 350, 350)
        self.UI()

    def UI(self):
        self.amount = QLabel("How muHch are you withdrawing?",self)
        self.amount.move(100,100)

        #creates spinbox
        self.spinbox=QSpinBox(self)
        self.spinbox.setFont(font)
        self.spinbox.move(100,150)

        #set the maxximum and the minimum
        self.spinbox.setMinimum(10)
        self.spinbox.setMaximum(100)

        #Sets the orefix and suffix
        self.spinbox.setPrefix("$ ")
        self.spinbox.setSuffix("  #")
        self.spinbox.setSingleStep(10)
        self.spinbox.valueChanged.connect(self.values)
        button = QPushButton("Withdrawal",self)
        button.move(100,180)
        button.clicked.connect(self.withd)
        self.show()

    def values(self):
        print(self.spinbox.value())

    def withd(self):
        ye = self.spinbox.value()
        print("You withdrew " + str(ye) + " dollars")


def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()