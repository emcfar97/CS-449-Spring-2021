"""
Code for game's GUI
"""
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QHBoxLayout, QVBoxLayout, QSizePolicy, QStyle, QStyleOption
from PyQt5.QtGui import QPixmap, QDrag, QPainter
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

class Board(QWidget):
    """
    Code for gameboard. Accepts n rows and returns n x n grid with rank and file
    """
    def __init__(self, parent, rings=7):

        super(Board, self).__init__(parent)
        self.rings = rings
        self.configure_gui()
        self.create_widgets()

    def configure_gui(self):

        self.recorded_moves = []

        self.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
            )
        self.layout = QGridLayout()
        self.setLayout(self.layout)

    def create_widgets(self):

        # create main components of board
        self.grid = Grid(self, self.rings)
        self.file = QHBoxLayout(), QHBoxLayout()
        self.rank = QVBoxLayout(), QVBoxLayout()
        self.bank = Bank(self, 0), Bank(self, 1)

        # populate rank and file with appropriate literals
        for i in range(self.rings):

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

        # add grid, rank, file, and banks to board
        self.layout.addWidget(self.grid, 2, 2)
        self.layout.addLayout(self.file[0], 1, 2)
        self.layout.addLayout(self.file[1], 3, 2)
        self.layout.addLayout(self.rank[0], 2, 1)
        self.layout.addLayout(self.rank[1], 2, 3)
        self.layout.addWidget(self.bank[0], 2, 0)
        self.layout.addWidget(self.bank[1], 2, 4)

    def piece_count(self):
        """
        Returns count for black and white pieces on board
        """
        stats = [0, 0]
        children = self.grid.children()

        for child in children[pow(self.rings, 2) + 1:]:

            stats[child.type] += 1

        if any(stats): return stats

        return [8, 8]

    def adjacent(self, index):
        """
        Returns legal, adjacent indexes for given index
        """
        pass

class Grid(QWidget):
    """
    Code for Grid. Accepts n rows and returns n x n matrix of tiles
    """
    def __init__(self, parent, rings=3):

        super(Grid, self).__init__(parent)
        self.configure_gui()
        self.create_widgets(rings)

    def configure_gui(self):

        self.setStyleSheet(
            'Grid{border-image: url(Resources/game_board.png)}'
            )
        self.layout = QGridLayout()
        self.layout.setSpacing(1)
        self.setLayout(self.layout)

    def create_widgets(self, rings):

        self.tiles = []
        
        for row in range(rings):

            for col in range(rings):

                self.tiles.append(Tile(self, [row, col]))
                self.layout.addWidget(self.tiles[-1], row, col)

    def paintEvent(self, pen):
        """
        Subclassed method. Draws content of stylesheet
        """
        style_option = QStyleOption()
        style_option.initFrom(self)
        painter = QPainter(self)

        self.style().drawPrimitive(
            QStyle.PE_Widget, style_option, painter, self
            )

class Bank(QWidget):
    """
    Code for bank. Keeps track of black or white pieces
    """
    def __init__(self, parent, type_):

        super(Bank, self).__init__(parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.pieces = []

        for _ in range(9): 
            
            piece = Piece(self, type_)
            self.layout.addWidget(piece)
            self.pieces.append(piece)

class Tile(QLabel):
    """
    Code for tile. Can be legal or illegal
    """
    def __init__(self, parent, coordinate):

        super(Tile, self).__init__(parent)
        self.game_manager = self.parent().parent().parent()
        if __name__ == '__main__':
            self.game_manager = debug

        if coordinate in LEGAL: self.setAcceptDrops(True)
        self.coordinate = coordinate
        self.setMinimumSize(64, 64)
        
    def dragEnterEvent(self, event):

        if self.game_manager.phase == 0: pass

        elif self.game_manager.phase == 1: pass

        elif self.game_manager.phase == 2: pass

        event.accept()

    def dragLeaveEvent(self, event):
        
        if self.game_manager.phase == 0: pass

        elif self.game_manager.phase == 1: 

            self.game_manager.board.recorded_moves.append(
                [self.coordinate]
                )

        elif self.game_manager.phase == 2: pass

    def dropEvent(self, event):

        self.parent().layout.addWidget(
            event.source(), 
            self.coordinate[0], 
            self.coordinate[1]
            )
        
        if self.game_manager.phase == 0: pass

        elif self.game_manager.phase == 1: pass

        elif self.game_manager.phase == 2: pass

        self.game_manager.complete_turn()

class Piece(QLabel):
    """
    Code for game pieces. Can be white or black based on type_ variable.
    """
    def __init__(self, parent, type_):

        super(Piece, self).__init__(parent)
        self.game_manager = self.parent().parent().parent()
        if __name__ == '__main__': self.game_manager = debug

        self.type = type_
        if   self.type == 0: self.path = r'Resources\black_piece.png'
        elif self.type == 1: self.path = r'Resources\white_piece.png'
        
        pixmap = QPixmap(self.path)
        self.setPixmap(pixmap)
        self.setAlignment(Qt.AlignCenter)

    def mousePressEvent(self, event):
        
        if self.game_manager.turn % 2 == self.type:

            drag = QDrag(self)
            drag.setMimeData(QMimeData())
            drag.setPixmap(self.pixmap())
            drag.setHotSpot(event.pos())
            drag.exec_(Qt.MoveAction)

# for running as a single file during debugging
if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    class Debug(object):

        def __init__(self):

            self.turn = 1
            self.phase = None

        def complete_turn(self): self.turn += 1

    debug = Debug()
    Qapp = QApplication([])
    board = Board(None, 7)
    board.showMaximized()
    Qapp.exec_()
