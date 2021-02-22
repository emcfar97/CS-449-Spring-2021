from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QLabel
from PyQt5.QtCore import Qt

# Code for gameboard. Accepts n rows and returns n x n matrix
# of tiles with rank and file
class Board(QWidget):
    'TBA'

    def __init__(self, parent, rings=3):
        
        super(Board, self).__init__(parent)
        self.configure_gui()
        self.create_widgets(rings)

    def configure_gui(self):

        self.layout = QGridLayout()
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

    def create_widgets(self, rings):
        
        # create main components of board
        self.grid = Grid(self, rings)
        self.file = QHBoxLayout(), QHBoxLayout()
        self.rank = QVBoxLayout(), QVBoxLayout()

        # populate rank and file with appropriate literals
        for i in range(rings):

            rank_1 = QLabel(str(i + 1), self)
            rank_1.setAlignment(Qt.AlignCenter)
            file_1 = QLabel(chr(i + 97), self)
            file_1.setAlignment(Qt.AlignCenter)
            
            rank_2 = QLabel(str(i + 1), self)
            rank_2.setAlignment(Qt.AlignCenter)
            file_2 = QLabel(chr(i + 97), self)
            file_2.setAlignment(Qt.AlignCenter)

            self.rank[0].addWidget(rank_1)
            self.rank[1].addWidget(rank_2)
            self.file[0].addWidget(file_1)
            self.file[1].addWidget(file_2)
        
        # add grid, rank, and file to board
        self.layout.addWidget(self.grid, 1, 1)
        self.layout.addLayout(self.file[0], 0, 1)
        self.layout.addLayout(self.file[1], 2, 1)
        self.layout.addLayout(self.rank[0], 1, 0)
        self.layout.addLayout(self.rank[1], 1, 2)

# Code for grid. Accepts n rows and returns n x n matrix
# of tiles 
class Grid(QWidget):
    'TBA'

    def __init__(self, parent, rings=3):
        
        super(Grid, self).__init__(parent)
        self.configure_gui()
        self.create_widgets(rings)

    def configure_gui(self):

        self.layout = QGridLayout()
        self.layout.setSpacing(50)
        self.setLayout(self.layout)

    def create_widgets(self, rings):
        
        self.tiles = []

        for row in range(rings):

            for col in range(rings):
                
                tile = Tile(self, f'{row}-{col}')
                self.layout.addWidget(tile, row, col)
                self.tiles.append(tile)

# Tile for gameboard. Currently pushbuttons, but would like
# to make them generic widgets in future
class Tile(QPushButton):
    'TBA'

    def __init__(self, parent, name):
        
        super(Tile, self).__init__(name, parent)
        self.configure_gui()
    
    def configure_gui(self):
        
        self.setFixedSize(25, 25)
    
# for running as a single file during debugging
if __name__ == '__main__':

    from PyQt5.QtWidgets import QApplication

    Qapp = QApplication([])
    board = Board(None, 5)
    board.show()
    Qapp.exec_()