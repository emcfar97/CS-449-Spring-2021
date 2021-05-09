"""
Code for game's GUI
"""
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QHBoxLayout, QVBoxLayout, QSizePolicy, QStyle, QStyleOption
from PyQt5.QtGui import QPixmap, QDrag, QPainter
from PyQt5.QtCore import Qt, QMimeData

LEGAL = [
    [1, 0, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [1, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 1],
    ]

class Board(QWidget):
    """
    Code for gameboard. Accepts n rows and returns n x n grid with rank and file
    """
    def __init__(self, parent, rings=7):

        super(Board, self).__init__(parent)
        self.game_manager = parent
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
            rank_1.setSizePolicy(
                QSizePolicy.Minimum, QSizePolicy.Minimum
                )
            file_1 = QLabel(chr(i + 97), self)
            file_1.setAlignment(Qt.AlignCenter)
            file_1.setSizePolicy(
                QSizePolicy.Minimum, QSizePolicy.Minimum
                )

            rank_2 = QLabel(str(i + 1), self)
            rank_2.setAlignment(Qt.AlignCenter)
            rank_2.setSizePolicy(
                QSizePolicy.Minimum, QSizePolicy.Minimum
                )
            file_2 = QLabel(chr(i + 97), self)
            file_2.setAlignment(Qt.AlignCenter)
            file_2.setSizePolicy(
                QSizePolicy.Minimum, QSizePolicy.Minimum
                )

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

    def piece_count(self, type_=0):
        """
        Returns count for black and white pieces based on type_
        type_ = 1 will return integer of pieces on board
        type_ = 2 will return integer of pieces in play
        type_ = 3 will return list of pieces on board
        """
        stats = [0, 0]

        if   type_ == 0:

            for num, bank in enumerate(self.bank):

                stats[num] = len([
                    piece for piece in bank
                    if piece.in_play
                    ])

        elif type_ == 1:
            
            for num, bank in enumerate(self.bank):

                stats[num] = len([
                    piece for piece in bank
                    if piece.index is None
                    ])

        elif type_ == 2:

            for num, bank in enumerate(self.bank):

                stats = [
                    piece for piece in bank
                    if piece.index is not None
                    and (self.game_manager.turn % 2) == piece.type
                    ]

        return stats

    def mill(self):
        """
        Returns whether a mill has been formed for given piece
        """
        pieces = self.piece_count(2)
        if len(pieces) < 3: return

        for piece in pieces:
            
            return

class Grid(QWidget):
    """
    Code for Grid. Accepts n rows and returns n x n matrix of tiles
    """
    def __init__(self, parent, rings):

        super(Grid, self).__init__(parent)
        self.configure_gui()
        self.create_widgets(rings)

    def configure_gui(self):

        self.setStyleSheet(
            'Grid{border-image: url(Resources/game_board.png)}'
            )
        self.setAcceptDrops(True)
        self.setMinimumSize(512, 512)

        self.layout = QGridLayout(self)
        self.setLayout(self.layout)

    def create_widgets(self, rings):

        for row in range(rings):
            
            for col in range(rings):

                tile = Tile(self, [row, col])
                self.layout.addWidget(tile, row, col)

    def adjacent(self, start, end):
        """
        Returns bool for adjacency of given indexes
        """

        if start is None: return False

        for i in range(2):

            # indexes are on the same line
            if start[i] == end[i]:
                
                indexes = []
                sorted_indexes = sorted(
                    (start[not i], end[not i])
                    )
                
                # get list of legal indexes between start and end
                for j in range(*sorted_indexes):

                    index = [j, start[i]]
                    if index == [3, 3]: return True
                    
                    tile = self.layout.itemAtPosition(*index).widget()
                    if tile.acceptDrops(): indexes.append(index)

                return len(indexes) > 1

        return True

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
        
        self.setMinimumHeight(parent.height())
        self.game_manager = parent.game_manager

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)
        
        self.type = type_
        self.pieces = []
    
    def __iter__(self): return iter(self.pieces)

    def start(self):

        for _ in range(9):
            
            piece = Piece(self, self.type)
            self.layout.addWidget(piece)
            self.pieces.append(piece)

    def clear(self):

        for piece in self.pieces: piece.close()

        self.pieces.clear()

class Tile(QLabel):
    """
    Code for tile. Can be legal or illegal
    """
    def __init__(self, parent, index):

        super(Tile, self).__init__(parent)
        self.game_manager = self.parent().parent().parent()
        
        if __name__ == '__main__': self.game_manager = debug

        if LEGAL[index[0]][index[1]]: self.setAcceptDrops(True)
        self.index = index
        
    def dragEnterEvent(self, event):

        if self.game_manager.phase == 0: 
            
            if self.parent().adjacent(event.source().index, self.index):
                
                return

        elif self.game_manager.phase == 1: 
            
            if self.parent().adjacent(event.source().index, self.index):
                
                return

        elif self.game_manager.phase == 2: pass

        event.accept()

    def dropEvent(self, event):

        piece = event.source()
        piece.index = self.index
        self.parent().layout.addWidget(piece, *self.index)
        
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
        self.game_manager = parent.game_manager
        if __name__ == '__main__': self.game_manager = debug
        self.in_play = True
        self.index = None

        self.type = type_
        if   self.type == 0: self.path = r'Resources\black_piece.png'
        elif self.type == 1: self.path = r'Resources\white_piece.png'
        
        pixmap = QPixmap(self.path)
        self.setPixmap(pixmap)
        self.setAlignment(Qt.AlignCenter)

    def mousePressEvent(self, event):
        
        if (self.game_manager.turn % 2) == self.type:

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
