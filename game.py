import random, board, computer
from PyQt5.QtWidgets import  QApplication, QMainWindow, QMessageBox, QWidget, QStatusBar, QHBoxLayout, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class Game(QMainWindow):
    """
    Contains the primary logic for the game
    """    
    def __init__(self):
        
        super(Game, self).__init__()
        self.setWindowTitle("Nine Men's Morris")
        self.turn = random.randint(0, 1)
        self.phase = 0
        self.configure_gui()
        self.create_widgets()
        self.showMaximized()

        file1 = open('rules.txt', "r+")
        mbox = QMessageBox.information(self, "RULES!!!!", file1.read())
        file1.close()
        
        first = {
            0: 'Black', 1: 'White'
            }
        QMessageBox.information(
            self, '', 
            f'{first[self.turn]} goes first',
            QMessageBox.Ok
            )

    def configure_gui(self):
        
        self.center = QWidget(self)
        self.layout = QHBoxLayout()

        self.center.setLayout(self.layout)
        self.setCentralWidget(self.center)
        
    def create_widgets(self):

        self.controls = Controls(self)
        self.board = board.Board(self)

        self.layout.addWidget(self.controls)
        self.layout.addWidget(self.board)

        self.statusbar = QStatusBar(self)
        self.statusbar.setFixedHeight(30)
        self.setStatusBar(self.statusbar)
        self.update_status()

    def update_status(self):
        """
        Updates game statusbar for current pieces on 
        board.
        ### Assumes certain things, particularly in
        ### phase 1, that may not be true in all 
        ### situations
        """
        
        if   self.phase == 0:
            # Currently assumes player taking opponent 
            # pieces is not a thing.

            black, white = self.board.piece_count()

        elif self.phase == 1:
            
            black, white = self.board.piece_count()

        elif self.phase == 2:
            
            black, white = self.board.piece_count()

        self.statusbar.showMessage(
            f'\tBlack Pieces: {black} \tWhite Pieces: {white}'
            )

    def complete_turn(self):
        """
        Runs after player completes turn and determines
        whether game should progress to next phase
        ### \# Currently has simple method for determining
        ### phase progress. Will need to make methods more
        ### all-inclusive going forward
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

font = QFont("Times", 20)
small_font = QFont("Times", 15)
class Controls(QWidget):
    """
    Code for the controls of the game
    """
    def __init__(self, parent):

        super(Controls, self).__init__(parent)
        self.configure_gui()
        # self.create_widgets()

    def configure_gui(self):

        layout = QVBoxLayout()
        self.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
            )

        #code for black player options, no funtions yet(in progress)
        BPlayer = QLabel("Black Player",self)
        BPlayer.setFont(font)
        BPlayer.move(700,200)
        self.BPlayerP = QCheckBox("Player", self)
        self.BPlayerP.move(700, 240)
        BPlayer= QLabel(self)
        BPlayer.setPixmap(QPixmap('Resources/black_piece.png'))
        BPlayer.move(600, 220)

        #code for White player options, no funtions yet(in progress)
        WPlayer = QLabel("White Player", self)
        WPlayer.setFont(font)
        WPlayer.move(700, 300)
        self.WPlayerP = QCheckBox("Player", self)
        self.WPlayerP.move(700, 340)
        WPlayer = QLabel(self)
        WPlayer.setPixmap(QPixmap('Resources/white_piece.png'))
        WPlayer.move(600, 320)

        #Game control buttons, no functions (in progress)
        GControl = QLabel("Game controls", self)
        GControl.setFont(small_font)
        GControl.move(700,500)
        startG = QPushButton("Start New Game",self)
        startG.clicked.connect(self.begin)
        startG.move(700,540)
        quitG=   QPushButton("Quit Game", self)
        quitG.move(700,580)
        quitG.clicked.connect(self.end)
        Rules = QPushButton("Display rules",self)
        Rules.move(700,620)
        Rules.clicked.connect(self.display_rules)

    def begin(self):
        if (self.WPlayerP.isChecked() and self.BPlayerP.isChecked()):
            mbox= QMessageBox.information(self,"Players","Two Player's are present, let the battle commence!!!!")
        elif(self.WPlayerP.isChecked()):
            mbox = QMessageBox.information(self, "Players", "White has chosen to face our warrior, may the odds be in your favor!!!!")
        elif(self.BPlayerP.isChecked()):
            mbox = QMessageBox.information(self, "Players","Black has chosen to face our warrior, may the odds be in your favor!!!!")
        else:
            mbox = QMessageBox.information(self, "Players","No player has been chosen new game will not start")

    def end(self):

        mbox = QMessageBox.question(self,"Warning!!!", "Are you sure you want to quit?",QMessageBox.Yes | QMessageBox.No )
        if mbox == QMessageBox.Yes:
          sys.exit()
        elif mbox == QMessageBox.No:
            mbox = QMessageBox.information(self, "Player","We are glad you have chosen to stay!!!!")

    def display_rules(self):
        file1 = open('rules.txt', "r+")
        mbox = QMessageBox.information(self, "Player", file1.read())
        file1.close()

    def create_widgets(self): 
        
        self.ribbon = QWidget(self)
        self.stats = QWidget(self)
        self.ribbon.setStyleSheet(
            'background: red'
            )
        self.stats.setStyleSheet(
            'background: blue'
            )

        self.layout.addWidget(self.stats)
        
Qapp = QApplication([])

app = Game()

Qapp.exec_()
