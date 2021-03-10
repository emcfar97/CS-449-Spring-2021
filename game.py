import board, logic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStatusBar
from PyQt5.QtCore import Qt

class Game(QMainWindow):

    def __init__(self):
        
        super(Game, self).__init__()
        self.setWindowTitle("Nine Men's Morris")
        self.configure_gui()
        self.create_widgets()
        self.showMaximized()

    def configure_gui(self):  
        
        self.center = QWidget(self)
        self.layout = QHBoxLayout()

        self.center.setLayout(self.layout)
        self.setCentralWidget(self.center)
        
    def create_widgets(self):

        # self.board = board.Board(self)
        self.statusbar = QStatusBar(self)
        self.setSatusBar(self.statusbar)
        self.statusbar.setFixedHeight(25)

    def keyPressEvent(self, event): 
        
        key_press = event.key()
        if key_press == Qt.Key_Escape: self.close()

Qapp = QApplication([])

app = Game()

Qapp.exec_()