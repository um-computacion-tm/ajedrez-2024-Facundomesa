import unittest
from piezas.Pawn import Pawn

class TestPawn(unittest.TestCase):
    def test_pawn_initialization(self):
        pawn = Pawn("white")
        self.assertEqual(pawn.color, "white")
        self.assertEqual(str(pawn), "white Pawn")

    def test_pawn_moves_white_starting_position(self):
        pawn = Pawn("white")
        board = [[None for _ in range(8)] for _ in range(8)]
        position = (6, 4)
        expected_moves = [(5, 4), (4, 4)]
        self.assertCountEqual(pawn.get_valid_moves(position, board), expected_moves)

    def test_pawn_moves_black_starting_position(self):
        pawn = Pawn("black")
        board = [[None for _ in range(8)] for _ in range(8)]
        position = (1, 4)
        expected_moves = [(2, 4), (3, 4)]
        self.assertCountEqual(pawn.get_valid_moves(position, board), expected_moves)

    def test_pawn_moves_with_blocking_piece(self):
        pawn = Pawn("white")
        board = [[None for _ in range(8)] for _ in range(8)]
        board[5][4] = Pawn("white")  # Peón blanco bloqueando el camino
        position = (6, 4)
        expected_moves = []
        self.assertCountEqual(pawn.get_valid_moves(position, board), expected_moves)

    def test_pawn_capturing(self):
        pawn = Pawn("white")
        board = [[None for _ in range(8)] for _ in range(8)]
        board[5][3] = Pawn("black")  # Peón negro en la diagonal izquierda
        board[5][5] = Pawn("black")  # Peón negro en la diagonal derecha
        position = (6, 4)
        expected_moves = [(5, 4), (5, 3), (5, 5)]
        self.assertCountEqual(Pawn.get_valid_moves(position, board), expected_moves)

if __name__ == '__main__':
    unittest.main()