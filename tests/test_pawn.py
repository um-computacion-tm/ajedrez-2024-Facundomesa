import unittest
from game.pawn import Pawn
from game.board import Board
#import ipdb

class TestPawn(unittest.TestCase):
    def setUp(self):
        # Crear un tablero vacío antes de cada test
        self.board = Board(forTest=True)

    def test_pawn_initialization(self):
        pawn = Pawn("white")
        self.assertEqual(pawn.color, "WHITE")
        self.assertEqual(str(pawn), "♙")

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
    #ipdb.set_trace()
    def test_pawn_moves_with_blocking_piece(self):
        pawn = Pawn("white")
        self.board.board[5][4] = Pawn("white")  # Peón blanco bloqueando el camino
        position = (6, 4)  # Posición inicial para peón blanco
        expected_moves = []  # No debe haber movimientos porque está bloqueado
        self.assertCountEqual(pawn.get_valid_moves(position, self.board), expected_moves)

    def test_pawn_capturing(self):
    # Suponiendo que estamos probando con un peón blanco en (1, 2)
        self.board.set_piece(2, 3, Pawn("BLACK"))  # Colocar un peón enemigo para capturar en (2, 3)
        self.board.set_piece(1, 2, Pawn("WHITE"))  # Colocar el peón blanco en (1, 2)

    # La posición inicial del peón
        position = (1, 2)

    # Movimientos esperados (captura en diagonal)
        expected_moves = [(2, 3)]  # Debería poder capturar en (2, 3)

    # Verificar que el método get_valid_moves devuelva los movimientos correctos
        pawn = self.board.get_piece(1, 2)
        # self.assertCountEqual(pawn.get_valid_moves(position, self.board), expected_moves)


if __name__ == '__main__':
    unittest.main()