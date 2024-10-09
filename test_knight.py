import unittest
from board import Board
from knight import Knight
class TestKnight(unittest.TestCase):
    def setUp(self):
        """Configura un tablero vacío y un caballo para cada prueba."""
        self.board = Board()
        self.knight_white = Knight("White")
        self.knight_black = Knight("Black")
        self.board.set_piece(4, 4, self.knight_white)

    def test_knight_valid_moves_center(self):
        """Prueba los movimientos válidos del caballo desde una posición central."""
        position = (4, 4)
        expected_moves = [
            (2, 3), (2, 5),  # Movimientos dos filas arriba
            (3, 2), (3, 6),  # Movimientos una fila arriba
            (5, 2), (5, 6),  # Movimientos una fila abajo
            (6, 3), (6, 5)   # Movimientos dos filas abajo
        ]
        valid_moves = self.knight_white.get_valid_moves(position, self.board.grid)
        self.assertEqual(set(valid_moves), set(expected_moves))

    def test_knight_moves_with_friendly_piece(self):
        """Verifica que el caballo no pueda moverse a una casilla ocupada por una pieza amiga."""
        self.board.set_piece(2, 3, Knight("White"))  # Bloquear movimiento
        position = (4, 4)
        expected_moves = [
            (2, 5), (3, 2), (3, 6), 
            (5, 2), (5, 6), (6, 3), (6, 5)
        ]
        valid_moves = self.knight_white.get_valid_moves(position, self.board.grid)
        self.assertEqual(set(valid_moves), set(expected_moves))

    def test_knight_moves_with_enemy_piece(self):
        """Verifica que el caballo pueda capturar una pieza enemiga."""
        self.board.set_piece(2, 5, Knight("Black"))  # Oposición
        position = (4, 4)
        expected_moves = [
            (2, 3), (2, 5), (3, 2), (3, 6), 
            (5, 2), (5, 6), (6, 3), (6, 5)
        ]
        valid_moves = self.knight_white.get_valid_moves(position, self.board.grid)
        self.assertEqual(set(valid_moves), set(expected_moves))

    def test_knight_moves_out_of_bounds(self):
        """Verifica que no se pueda mover fuera de los límites del tablero."""
        knight_out_of_bounds = Knight("White")
        self.board.set_piece(0, 0, knight_out_of_bounds)
        position = (0, 0)
        expected_moves = [
            (1, 2),  # Movimiento a la derecha
            (2, 1)   # Movimiento hacia abajo
        ]
        valid_moves = knight_out_of_bounds.get_valid_moves(position, self.board.grid)
        self.assertEqual(set(valid_moves), set(expected_moves))

if __name__ == "__main__":
    unittest.main()

