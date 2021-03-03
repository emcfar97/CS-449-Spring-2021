from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QSizePolicy
from PyQt5.QtGui import QPixmap, QDrag
from PyQt5.QtCore import Qt, QMimeData

LEGAL = [
    [0, 0], [0, 3], [0, 6],
    [1, 1], [1, 3], [1, 5],
    [2, 2], [2, 3], [2, 4],
    [3, 0], [3, 1], [3, 2], [3, 4], [3, 5], [3, 6],
    [4, 2], [4, 3], [4, 4],
    [5, 1], [5, 3], [5, 5],
    [6, 0], [6, 3], [6, 6],
    ]

def set_directory():
    '''Temporary function for changing current working directory
    so that relative paths are correctly resolved'''

    import os, pathlib

    path = pathlib.Path(__file__).parent
    os.chdir(path)


# Code for gameboard. Accepts n rows and returns n x n matrix
# of tiles with rank and file
class Board(QWidget):
    'TBA'

    def __init__(self, parent, rings=3):

        super(Board, self).__init__(parent)
        self.configure_gui()
        self.create_widgets(rings)

    def configure_gui(self):

        self.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
            )
        self.layout = QGridLayout()
        self.setLayout(self.layout)

    def create_widgets(self, rings):

        # create main components of board
        self.grid = Grid(self, rings)
        self.file = QHBoxLayout(), QHBoxLayout()
        self.rank = QVBoxLayout(), QVBoxLayout()
        self.bank = QVBoxLayout(), QVBoxLayout()

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

        # populate bank with appropriate pieces
        for i in range(9):

            self.bank[0].addWidget(Piece(self, 0))
            self.bank[1].addWidget(Piece(self, 1))

        # add grid, rank, file, and banks to board
        self.layout.addWidget(self.grid, 2, 2)
        self.layout.addLayout(self.file[0], 1, 2)
        self.layout.addLayout(self.file[1], 3, 2)
        self.layout.addLayout(self.rank[0], 2, 1)
        self.layout.addLayout(self.rank[1], 2, 3)
        self.layout.addLayout(self.bank[0], 2, 0)
        self.layout.addLayout(self.bank[1], 2, 4)

# Code for grid. Accepts n rows and returns n x n matrix
# of tiles
class Grid(QWidget):
    'TBA'

    def __init__(self, parent, rings=3):

        super(Grid, self).__init__(parent)
        self.configure_gui()
        self.create_widgets(rings)

    def configure_gui(self):

        # self.setStyleSheet(
        #     'background-image: url(Resources/game_board.png)'
        #     )
        self.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
            )
        self.layout = QGridLayout()
        self.layout.setSpacing(1)
        self.setLayout(self.layout)

    def create_widgets(self, rings):

        for row in range(rings):

            for col in range(rings):
                tile = Tile(self, [row, col])
                self.layout.addWidget(tile, row, col)

# Tile for gameboard. Currently pushbuttons, but would like
# to make them generic widgets in future
class Tile(QLabel):
    'TBA'

    def __init__(self, parent, coordinate):

        super(Tile, self).__init__(parent)
        self.coordinate = coordinate
        if coordinate in LEGAL: self.setAcceptDrops(True)
        self.setStyleSheet('border: 1px solid black')

    def dragEnterEvent(self, event): event.accept()

    def dropEvent(self, event):

        self.parent().layout.addWidget(
            event.source(), 
            self.coordinate[0], 
            self.coordinate[1]
            )

# Code for game pieces. Can be white or black based on type_
# variable.
class Piece(QLabel):
    'TBA'

    def __init__(self, parent, type_):

        super(Piece, self).__init__(parent)

        if type_ == 0:
            path = r'Resources\black_piece.png'
        elif type_ == 1:
            path = r'Resources\white_piece.png'
        else:
            raise ValueError
        
        pixmap = QPixmap(path)
        self.setPixmap(pixmap)

    def mousePressEvent(self, event):
        
        drag = QDrag(self)
        drag.setMimeData(QMimeData())
        drag.setPixmap(self.pixmap())
        drag.setHotSpot(event.pos())
        drag.exec_(Qt.MoveAction)

set_directory()

# for running as a single file during debugging
if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    Qapp = QApplication([])
    board = Board(None, 7)
    board.showMaximized()
    Qapp.exec_()