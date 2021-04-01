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
        num = random.randint(14, 18)
        tiles = random.choices(legal, num)
        black = random.randint(4, len(tiles) // 2)
        white = len(tiles) - black
        
        for tile in tiles: pass

        self.assert____()

    def test_Phase_3(self):
        """
        TBA
        """
        
        legal = game.board.LEGAL
        num = random.randint(3, 6)
        tiles = random.choices(legal, num)
        black = random.randint(4, len(tiles) // 2)
        white = len(tiles) - black
        
        for tile in tiles: pass
        
        self.assert____()

if __name__ == '__main__':

    unittest.main()