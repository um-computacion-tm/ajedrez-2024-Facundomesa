import unittest
from game.piece import Piece

class MockPiece(Piece):
    """Una subclase de Piece para propósitos de testeo, ya que Piece es abstracta."""
    def __str__(self):
        return "MockPiece"

    def movements(self, row, col, board):
        # Para propósitos de testeo, devolvemos una lista vacía
        return []

class TestPiece(unittest.TestCase):

    def setUp(self):
        """
        Configura un tablero de 8x8 con una pieza blanca en la posición (4,4).
        """
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.white_piece = MockPiece("WHITE", self.board)
        self.black_piece = MockPiece("BLACK", self.board)
        self.board[4][4] = self.white_piece

    def test_is_move_valid_within_bounds_and_empty(self):
        """
        Prueba movimientos válidos dentro de los límites del tablero y hacia casillas vacías.
        """
        self.assertTrue(self.white_piece.is_move_valid(3, 4, self.board), "El movimiento debería ser válido (3,4).")
        self.assertTrue(self.white_piece.is_move_valid(4, 3, self.board), "El movimiento debería ser válido (4,3).")

    def test_is_move_valid_out_of_bounds(self):
        """
        Prueba movimientos fuera de los límites del tablero.
        """
        self.assertFalse(self.white_piece.is_move_valid(-1, 4, self.board), "El movimiento fuera de límites (-1,4) debería ser inválido.")
        self.assertFalse(self.white_piece.is_move_valid(4, 8, self.board), "El movimiento fuera de límites (4,8) debería ser inválido.")
        self.assertFalse(self.white_piece.is_move_valid(8, 8, self.board), "El movimiento fuera de límites (8,8) debería ser inválido.")
        self.assertFalse(self.white_piece.is_move_valid(0, -1, self.board), "El movimiento fuera de límites (0,-1) debería ser inválido.")

    def test_is_move_valid_with_own_piece(self):
        """
        Prueba movimientos hacia casillas ocupadas por piezas del mismo color.
        """
        self.board[3][4] = MockPiece("WHITE", self.board)  # Coloca una pieza blanca en (3,4)
        self.assertFalse(self.white_piece.is_move_valid(3, 4, self.board), "El movimiento hacia una pieza del mismo color debería ser inválido.")

    def test_is_move_valid_with_opponent_piece(self):
        """
        Prueba movimientos hacia casillas ocupadas por piezas del color contrario.
        """
        self.board[3][4] = MockPiece("BLACK", self.board)  # Coloca una pieza negra en (3,4)
        self.assertTrue(self.white_piece.is_move_valid(3, 4, self.board), "El movimiento hacia una pieza del oponente debería ser válido.")

    def test_is_move_valid_same_position(self):
        """
        Prueba un intento de movimiento a la misma posición.
        """
        self.assertFalse(self.white_piece.is_move_valid(4, 4, self.board), "Moverse a la misma posición (4,4) debería ser inválido.")

    def test_is_move_valid_out_of_bounds_negative(self):
        """
        Verifica movimientos negativos fuera de los límites.
        """
        self.assertFalse(self.white_piece.is_move_valid(-5, -5, self.board), "El movimiento (-5,-5) fuera de límites debería ser inválido.")
        self.assertFalse(self.white_piece.is_move_valid(10, 10, self.board), "El movimiento (10,10) fuera de límites debería ser inválido.")

if __name__ == "__main__":
    unittest.main()
