import unittest, random

from .. import game

class Test_Phases(unittest.TestCase):

    def test_Phase_1(self):
        """
        TBA
        """
        
        self.assert____()

    def test_Phase_2(self):
        """
        TBA
        """
        
        legal = game.board.LEGAL
        tiles = random.choices(legal, 18)
        
        for tile in tiles: pass

        self.assert____()

    def test_Phase_3(self):
        """
        TBA
        """
        
        self.assert____()

if __name__ == '__main__':

    unittest.main()