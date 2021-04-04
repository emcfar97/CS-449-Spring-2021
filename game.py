import board, logic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStatusBar, QHBoxLayout
from PyQt5.QtCore import Qt

class Game(QMainWindow):
    """
    Contains the primary logic for the game
    """
    
    def __init__(self):
        
        super(Game, self).__init__()
        self.setWindowTitle("Nine Men's Morris")
        self.phase = 0
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
        """
        TBA
        """
        
        if self.phase == 0: 

            black, white = 9, 9

        elif self.phase == 1: 
            
            black, white = self.board.piece_count()

        elif self.phase == 2: 
            
            black, white = self.board.piece_count()

        self.statusbar.showMessage(
            f'\tBlack Pieces: {black} \tWhite Pieces: {white}'
            )

    def complete_turn(self):
        """
        TBA
        """

        if self.phase == 0: 
            
            if sum(self.board.piece_count()) == 18: 
                
                self.phase = 1

        elif self.phase == 1: 
            
            black, white = self.board.piece_count()

            if black == 3 or white == 3:

                self.phase = 2

        elif self.phase == 2: pass

        self.update_status()
        self.turn += 1

    def keyPressEvent(self, event):
        
        key_press = event.key()
        if key_press == Qt.Key_Escape: self.close()

Qapp = QApplication([])

app = Game()

Qapp.exec_()