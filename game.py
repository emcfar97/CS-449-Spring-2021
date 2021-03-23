import board, logic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStatusBar, QHBoxLayout
from PyQt5.QtCore import Qt

class Game(QMainWindow):

    def __init__(self):
        
        super(Game, self).__init__()
        self.setWindowTitle("Nine Men's Morris")
        self.stage = 0
        self.turn = 1
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
        self.board = board.Board(self)

        self.layout.addWidget(self.placeholder, 1)
        self.layout.addWidget(self.board, 1)

        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.statusbar.setFixedHeight(30)
        self.update_status()

    def update_status(self):
        
        black, white = self.board.piece_count()
        self.statusbar.showMessage(
            f'\tBlack Pieces: {black} \tWhite Pieces: {white}'
            )

    def complete_turn(self):
        
        if self.stage == 0: 
            
            if sum(self.board.piece_count()) == 16: pass
            else: pass

        elif self.stage == 1: pass

        elif self.stage == 2: pass

        self.update_status()
        self.turn = not self.turn

    def keyPressEvent(self, event):
        
        key_press = event.key()
        if key_press == Qt.Key_Escape: self.close()

Qapp = QApplication([])

app = Game()

Qapp.exec_()