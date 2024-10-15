import unittest
from queen import Queen 
from board import Board

class TestQueen(unittest.TestCase):

    def setUp(self):
        """Configura un tablero vacío para cada prueba."""
        self.board = Board(forTest=True)

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
        # Colocar la reina blanca en (3, 3)
        queen = Queen("white")
        self.board.set_piece(3, 3, queen)

        # Colocar piezas que bloquean el camino de la reina
        self.board.set_piece(5, 3, Queen("white"))  # Pieza del mismo color bloqueando abajo
        self.board.set_piece(3, 5, Queen("black"))  # Pieza enemiga bloqueando a la derecha
        self.board.set_piece(1, 1, Queen("black"))  # Pieza enemiga bloqueando en diagonal izquierda arriba

        # Posición de la reina
        position = (3, 3)

        # Movimientos esperados teniendo en cuenta las piezas bloqueando
        expected_moves = [
            (2, 3), (1, 3), (0, 3),  # Arriba
            (4, 3),  # Abajo, deteniéndose en (5, 3)
            (3, 4), (3, 5),  # Derecha, deteniéndose en (3, 5) por la pieza enemiga
            (3, 2), (3, 1), (3, 0),  # Izquierda
            (2, 4), (1, 5), (0, 6),  # Diagonal superior derecha
            (4, 2), (5, 1), (6, 0),  # Diagonal inferior izquierda
            (4, 4)  # Diagonal inferior derecha
            # No más diagonal superior izquierda porque está bloqueada en (1, 1)
        ]

        # Obtener los movimientos válidos generados por la reina
        valid_moves = queen.get_valid_moves(position, self.board)

        # Comparar los movimientos válidos con los movimientos esperados
        # self.assertEqual(set(valid_moves), set(expected_moves))


    def test_no_moves(self):
        # Colocar la reina blanca en el centro (4, 4)
        queen = Queen("white")
        self.board.set_piece(4, 4, queen)

        # Bloquear todos los posibles movimientos de la reina
        self.board.set_piece(3, 4, Queen("white"))  # Bloqueo arriba
        self.board.set_piece(5, 4, Queen("white"))  # Bloqueo abajo
        self.board.set_piece(4, 3, Queen("white"))  # Bloqueo izquierda
        self.board.set_piece(4, 5, Queen("white"))  # Bloqueo derecha
        self.board.set_piece(3, 3, Queen("white"))  # Bloqueo diagonal arriba izquierda
        self.board.set_piece(3, 5, Queen("white"))  # Bloqueo diagonal arriba derecha
        self.board.set_piece(5, 3, Queen("white"))  # Bloqueo diagonal abajo izquierda
        self.board.set_piece(5, 5, Queen("white"))  # Bloqueo diagonal abajo derecha

        # La posición de la reina
        position = (4, 4)

        # La reina no debería tener movimientos válidos porque está completamente bloqueada
        expected_moves = []

        # Obtener los movimientos válidos
        valid_moves = queen.get_valid_moves(position, self.board)

        # Verificar que no hay movimientos válidos
        self.assertEqual(valid_moves, expected_moves)


if __name__ == '__main__':
    unittest.main()
