import unittest
from test_piezas.test_Queen import Queen  

class TestQueen(unittest.TestCase):

    def setUp(self):
        """Configura un tablero vacío para cada prueba."""
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def test_valid_moves_center(self):
        """Prueba los movimientos válidos de la reina desde una posición central sin obstrucciones."""
        queen = Queen("White")
        position = (3, 3)
        expected_moves = [
            (2, 3), (1, 3), (0, 3),  
            (4, 3), (5, 3), (6, 3), (7, 3),  # Movimientos verticales hacia abajo
            (3, 2), (3, 1), (3, 0),  # Movimientos horizontales hacia la izquierda
            (3, 4), (3, 5), (3, 6), (3, 7),  # Movimientos horizontales hacia la derecha
            (2, 2), (1, 1), (0, 0),  # Movimientos diagonales hacia arriba a la izquierda
            (4, 4), (5, 5), (6, 6), (7, 7),  # Movimientos diagonales hacia abajo a la derecha
            (2, 4), (1, 5), (0, 6),  # Movimientos diagonales hacia arriba a la derecha
            (4, 2), (5, 1), (6, 0)  # Movimientos diagonales hacia abajo a la izquierda
        ]
        valid_moves = queen.get_valid_moves(position, self.board)
        self.assertEqual(set(valid_moves), set(expected_moves))

    def test_valid_moves_with_pieces(self):
        """Prueba los movimientos válidos de la reina con piezas bloqueando el camino."""
        queen = Queen("White")
        self.board[2][3] = Queen("Black")  # Bloqueo en la dirección vertical
        self.board[3][5] = Queen("Black")  # Bloqueo en la dirección horizontal
        self.board[4][4] = Queen("Black")  # Bloqueo en la dirección diagonal
        position = (3, 3)
        expected_moves = [
            (2, 3),  # Movimiento vertical hacia arriba
            (4, 3), (5, 3), (6, 3), (7, 3),  # Movimientos verticales hacia abajo
            (3, 2), (3, 1), (3, 0),  # Movimientos horizontales hacia la izquierda
            (3, 4),  # Movimiento horizontal hacia la derecha bloqueado
            (2, 2), (1, 1), (0, 0),  # Movimientos diagonales hacia arriba a la izquierda
            (4, 4)  # Movimiento diagonal hacia abajo a la derecha bloqueado
        ]
        valid_moves = queen.get_valid_moves(position, self.board)
        self.assertEqual(set(valid_moves), set(expected_moves))

    def test_no_moves(self):
        """Prueba el caso en el que la reina está bloqueada en todas las direcciones."""
        queen = Queen("White")
        self.board[0][1] = Queen("Black")  # Bloqueo en la dirección vertical hacia arriba
        self.board[1][0] = Queen("Black")  # Bloqueo en la dirección horizontal hacia la izquierda
        self.board[1][1] = Queen("Black")  # Bloqueo en la dirección diagonal
        position = (0, 0)
        expected_moves = []
        valid_moves = queen.get_valid_moves(position, self.board)
        self.assertEqual(valid_moves, expected_moves)

if __name__ == '__main__':
    unittest.main()
