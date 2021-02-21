from PyQt5.QtWidgets import QGridLayout, QPushButton, QWidget

# Code for gameboard. Accepts n rows and returns n x n matrix
# of tiles
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
        
        self.setFixedSize(50, 50)
    
# for running as a single file during debugging
if __name__ == '__main__':

    from PyQt5.QtWidgets import QApplication

    Qapp = QApplication([])
    board = Board(None, 5)
    board.show()
    Qapp.exec_()