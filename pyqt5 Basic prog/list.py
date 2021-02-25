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
        self.enter = QLineEdit(self)
        self.enter.setPlaceholderText("enter super hero name")
        self.enter.move(100,50)
        self.enter.resize(250,20)
        self.list=QListWidget(self)
        self.list.move(100,80)
        list1 = ["superman","spiderman","batman"]
        self.list.addItems(list1)
        self.list.addItem("Ironman")
        Bta = QPushButton("Add",self)
        Btd = QPushButton("Delete",self)
        Btg = QPushButton("Get",self)
        Btda = QPushButton("Delete all",self)
        Bta.move(360,80)
        Btd.move(360,110)
        Btg.move(360,140)
        Btda.move(360,170)
        Bta.clicked.connect(self.add2)
        Btg.clicked.connect(self.get)
        Btd.clicked.connect(self.delete)
        Btda.clicked.connect(self.delete_all)
        self.show()

    def add2(self):
        text = self.enter.text()
        self.list.addItem(text)
        self.enter.setText("")
    def get(self):
        value = self.list.currentItem().text()
        print(value)
        pass

    def delete(self):
        id = self.list.currentRow()
        self.list.takeItem(id)
        pass

    def delete_all(self):
        self.list.clear()
        pass


def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()