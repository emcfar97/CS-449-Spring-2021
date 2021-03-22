from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QHBoxLayout, QVBoxLayout, QSizePolicy
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

# Code for gameboard. Accepts n rows and returns n x n matrix
# of tiles with rank and file
class Board(QWidget):
    'TBA'

    def __init__(self, parent, rings=7):

        super(Board, self).__init__(parent)
        self.configure_gui()
        self.create_widgets(rings)

    def configure_gui(self):

        self.recorded_moves = []

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
        # self.bank = Bank(self, 0), Bank(self, 1)

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
    'Accepts n rows and returns n x n matrix of tiles'

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

        self.tiles = []
        
        for row in range(rings):

            for col in range(rings):
                tile = Tile(self, [row, col])
                self.layout.addWidget(tile, row, col)

class Bank(QWidget):
    'TBA'

    def __init__(self, parent, type_):

        super(Bank, self).__init__(parent)
        self.enabled = type_
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.pieces = [
            Piece(self, type_) for i in range(9)
            ]
        for piece in self.pieces: 
            
            self.layout.addWidget(piece)

    def toggleEnabled(self):

        for piece in self.pieces:

            piece.draggable = not piece.draggable

# Tile for gameboard. 
class Tile(QLabel):
    'Tile for gameboard'

    def __init__(self, parent, coordinate):

        super(Tile, self).__init__(parent)
        self.game_manager = self.parent().parent().parent()
        if coordinate in LEGAL: self.setAcceptDrops(True)
        self.coordinate = coordinate
        
        self.setStyleSheet('border: 1px solid black')

    def dragEnterEvent(self, event): 

        event.accept()

    def dragLeaveEvent(self, event): 
        
        if self.game_manager.stage == 0: pass

        elif self.game_manager.stage == 1: 

            self.game_manager.board.recorded_moves.append(
                [self.coordinate]
                )

        elif self.game_manager.stage == 2: pass

        
    def dropEvent(self, event):

        self.parent().layout.addWidget(
            event.source(), 
            self.coordinate[0], 
            self.coordinate[1]
            )

        if self.game_manager.stage == 0: pass

        elif self.game_manager.stage == 1: pass

        elif self.game_manager.stage == 2: pass


# Code for game pieces. Can be white or black based on type_
# variable.
class Piece(QLabel):
    'TBA'

    def __init__(self, parent, type_):

        super(Piece, self).__init__(parent)

        self.type = type_
        if self.type == 0:
            path = r'Resources\black_piece.png'
        elif self.type == 1:
            path = r'Resources\white_piece.png'
        else:
            raise ValueError
        
        pixmap = QPixmap(path)
        self.setPixmap(pixmap)
        self.setAlignment(Qt.AlignCenter)

    def mousePressEvent(self, event):
        
        drag = QDrag(self)
        drag.setMimeData(QMimeData())
        drag.setPixmap(self.pixmap())
        drag.setHotSpot(event.pos())
        drag.exec_(Qt.MoveAction)

# for running as a single file during debugging
if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    Qapp = QApplication([])
    board = Board(None, 7)
    board.showMaximized()
    Qapp.exec_()