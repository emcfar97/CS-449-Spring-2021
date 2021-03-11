import board, logic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QWidget, QStatusBar, QHBoxLayout
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

        self.placeholder = QWidget(self)
        self.placeholder.setStyleSheet('color:red')
        self.board = board.Board(self)

        self.layout.addWidget(self.placeholder, 1)
        self.layout.addWidget(self.board, 1)

        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.statusbar.setFixedHeight(25)
        self.update_status()

    def update_status(self):
        
        num = 8
        self.statusbar.showMessage(
            f'\tBlack Pieces: {num} \tWhite Pieces: {num}'
            )

    def complete_turn(self, start, end):

        pass

    def keyPressEvent(self, event): 
        
        key_press = event.key()
        if key_press == Qt.Key_Escape: self.close()

Qapp = QApplication([])

app = Game()

Qapp.exec_()