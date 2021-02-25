import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(50, 50, 500, 500)
        self.UI()

    def UI(self):

        #Creation of the QLable for implementation of the giving image
        self.logo= QLabel(self)

        #searchs for the given image
        self.logo.setPixmap(QPixmap('images/image.png'))

        removebutton=QPushButton("Remove",self)
        removebutton.move(50,170)
        removebutton.clicked.connect(self.removeLogo)
        showbutton = QPushButton("Show", self)
        showbutton.move(150,170)
        showbutton.clicked.connect(self.showLogo)
        self.show()

    def removeLogo(self):
        #Remove the logo
        self.logo.close()

    def showLogo(self):
        #Reshow the Logoe
        self.logo.show()


def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()