import unittest
from piezas.rook import Rook
from game.board import Board 

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_positions(self):
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertEqual(self.board.get_piece(0, 0).color, "black")  # Cambiado a "black"
        
        self.assertIsInstance(self.board.get_piece(0, 7), Rook)
        self.assertEqual(self.board.get_piece(0, 7).color, "black")  # Cambiado a "black"
        
        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertEqual(self.board.get_piece(7, 0).color, "white")  # Cambiado a "white"
        
        self.assertIsInstance(self.board.get_piece(7, 7), Rook)
        self.assertEqual(self.board.get_piece(7, 7).color, "white")  # Cambiado a "white"
        
        for row in range(8):
            for col in range(8):
                if (row, col) not in [(0, 0), (0, 7), (7, 0), (7, 7)]:
                    self.assertIsNone(self.board.get_piece(row, col))

if __name__ == "__main__":
    unittest.main()

