import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(250, 250, 350, 350)
        self.UI()

    def UI(self):
        #Creates a QComboBox in widget
        self.combo = QComboBox(self)
        self.combo.move(150,100)

        #Add an object to the combobox, usefull for loops
        self.combo.addItem("Iron man")

        #Adds muntiple items to the combobox
        self.combo.addItems(["Hulk","Thor","hawkeye"])
        button = QPushButton("Save",self)
        button.move(150,150)
        button.clicked.connect(self.getValue)
        self.show()

        # adds muntiple items to combobox
        for number in range(18,222):
            self.combo.addItem(str(number))

    def getValue(self):
        #retrives the crrent item in the combobox
        value = self.combo.currentText()
        print(value)

def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()