import unittest
from pawn import Pawn

class TestPawn(unittest.TestCase):
    def setUp(self):
        # Crear un tablero vacío antes de cada test
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def test_pawn_initialization(self):
        pawn = Pawn("white")
        self.assertEqual(pawn.color, "white")
        self.assertEqual(str(pawn), "white Pawn")

    def test_pawn_moves_white_starting_position(self):
        pawn = Pawn("white")
        position = (6, 4)  # Posición inicial para peón blanco
        expected_moves = [(5, 4), (4, 4)]  # Movimientos iniciales
        self.assertCountEqual(pawn.get_valid_moves(position, self.board), expected_moves)

    def test_pawn_moves_black_starting_position(self):
        pawn = Pawn("black")
        position = (1, 4)  # Posición inicial para peón negro
        expected_moves = [(2, 4), (3, 4)]  # Movimientos iniciales
        self.assertCountEqual(pawn.get_valid_moves(position, self.board), expected_moves)

    def test_pawn_moves_with_blocking_piece(self):
        pawn = Pawn("white")
        self.board[5][4] = Pawn("white")  # Peón blanco bloqueando el camino
        position = (6, 4)  # Posición inicial para peón blanco
        expected_moves = []  # No debe haber movimientos porque está bloqueado
        self.assertCountEqual(pawn.get_valid_moves(position, self.board), expected_moves)

    def test_pawn_capturing(self):
        position = (3, 3)  # Posición del peón
        pawn = Pawn("white")

        # Colocar un peón blanco en la posición (3, 3)
        self.board[3][3] = pawn

        # Colocar piezas enemigas en posiciones capturables
        self.board[2][2] = Pawn("black")  # Peón negro en diagonal izquierda
        self.board[2][4] = Pawn("black")  # Peón negro en diagonal derecha

        # Movimientos esperados (capturas diagonales)
        expected_moves = [(2, 2), (2, 4)]

        # Verificar que los movimientos válidos incluyan las capturas diagonales
        self.assertCountEqual(pawn.get_valid_moves(position, self.board), expected_moves)

if __name__ == '__main__':
    unittest.main()
