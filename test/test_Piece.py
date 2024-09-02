import unittest
from game.Piece import Piece

class MockPiece(Piece):
    """Una subclase de Piece para propósitos de testeo, ya que Piece es abstracta."""
    def __str__(self):
        return "MockPiece"

    def movements(self, row, col, board):
        return []

class TestPiece(unittest.TestCase):

    def setUp(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.white_piece = MockPiece("WHITE", self.board)
        self.black_piece = MockPiece("BLACK", self.board)
        self.board[4][4] = self.white_piece

    def test_is_move_valid_within_bounds_and_empty(self):
        # Movimiento dentro de los límites y la casilla está vacía
        self.assertTrue(self.white_piece.is_move_valid(3, 4, self.board))
        self.assertTrue(self.white_piece.is_move_valid(4, 3, self.board))

    def test_is_move_valid_out_of_bounds(self):
        # Movimiento fuera de los límites del tablero
        self.assertFalse(self.white_piece.is_move_valid(-1, 4, self.board))
        self.assertFalse(self.white_piece.is_move_valid(4, 8, self.board))

    def test_is_move_valid_with_own_piece(self):
        # Movimiento hacia una casilla ocupada por una pieza del mismo color
        self.board[3][4] = MockPiece("WHITE", self.board)
        self.assertFalse(self.white_piece.is_move_valid(3, 4, self.board))

    def test_is_move_valid_with_opponent_piece(self):
        # Movimiento hacia una casilla ocupada por una pieza del color contrario
        self.board[3][4] = MockPiece("BLACK", self.board)
        self.assertTrue(self.white_piece.is_move_valid(3, 4, self.board))

if __name__ == "__main__":
    unittest.main()
