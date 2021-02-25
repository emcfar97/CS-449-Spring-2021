import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont("Times", 11)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(250, 250, 550, 550)
        self.UI()

    def UI(self):
       self.editor = QTextEdit(self)
       self.editor.move(100,200)
       self.editor.setAcceptRichText(False)
       button=QPushButton("Send",self)
       button.move(260,410)
       button.clicked.connect(self.getText)
       self.show()

    def getText(self):
        text = self.editor.toPlainText()
        print(text)

def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()