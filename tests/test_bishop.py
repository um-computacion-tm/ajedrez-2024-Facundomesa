import unittest
from game.bishop import Bishop
from game.board import Board

class TestBishop(unittest.TestCase):
    def setUp(self):
        self.board = Board()
    
    def test_Bishop_initialization(self):
        bishop = Bishop("WHITE", self.board)
        self.assertEqual(bishop.color, "WHITE")
        self.assertEqual(str(bishop), "♗")

    def test_Bishop_moves_from_center(self):
        bishop = Bishop("WHITE", self.board)
        position = (4, 4)
        self.board = Board(forTest=True)
        expected_moves = [
            (3, 3), (2, 2), (1, 1),          # Diagonal arriba izquierda
            (3, 5), (2, 6), (1, 7),          # Diagonal arriba derecha
            (5, 3),           # Diagonal abajo izquierda
            (5, 5)           # Diagonal abajo derecha
        ]
        self.assertCountEqual(bishop.possible_moves(position, self.board), expected_moves)

    def test_Bishop_moves_with_obstructions(self):
        bishop = Bishop("WHITE", self.board)
        self.board.board[2][2] = Bishop("WHITE", self.board)  # Obstrucción del mismo color
        self.board.board[6][6] = Bishop("BLACK", self.board)  # Obstrucción de color contrario
        position = (4, 4)
        expected_moves = [
            (3, 3),  # Diagonal arriba izquierda (parada antes del 2,2)
            (3, 5), (2, 6), (1, 7),  # Diagonal arriba derecha
            (5, 3),  # Diagonal abajo izquierda
            (5, 5), (6, 6)           # Diagonal abajo derecha (parada en 6,6)
        ]
        self.assertCountEqual(bishop.possible_moves(position, self.board), expected_moves)

    def test_Bishop_moves_from_corner(self):
        bishop = Bishop("BLACK", self.board)
        position = (0, 0)
        self.board = Board(forTest=True)
        expected_moves = []
        self.assertCountEqual(bishop.possible_moves(position, self.board), expected_moves)

if __name__ == '__main__':
    unittest.main()
