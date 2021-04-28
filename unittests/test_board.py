import unittest

from .. import game

class TestBoard(unittest.TestCase):

    def setUp(self):
        
        Qapp = game.QApplication([])

        self.app = game.Game()

        Qapp.exec_()

    def test_____(self):
        """
        TBA
        """
        
        self.assert____()

    def test_____(self):
        """
        TBA
        """
        
        self.assert____()

    def test_____(self):
        """
        TBA
        """
        
        self.assert____()

    def test_____(self):
        """
        TBA
        """
        
        self.assert____()

if __name__ == '__main__':

    unittest.main()