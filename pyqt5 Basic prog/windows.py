import sys
from PyQt5.QtWidgets import *
# Import for the Widget class

class Window(QWidget): # necessary to inherit from the QWidget class
    def __init__(self):
        super().__init__()
        # Sets the windows demensions
        self.setGeometry(150,250,550,250)

        # sets the sitle of the window
        self.setWindowTitle("This is our window's title")

        self.show()


#folowing code is used to execute the previous code
App = QApplication(sys.argv)
window = Window()
sys.exit((App.exec_()))
