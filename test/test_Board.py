import unittest
from piezas.Rook import Rook
from piezas.Knight import Knight
from piezas.Bishop import Bishop
from piezas.Queen import Queen
from piezas.King import King
from piezas.Pawn import Pawn
from game.Board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_positions(self):
        # Verificar las torres en las posiciones correctas
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertEqual(self.board.get_piece(0, 0).color, "black")
        self.assertIsInstance(self.board.get_piece(0, 7), Rook)
        self.assertEqual(self.board.get_piece(0, 7).color, "black")
        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertEqual(self.board.get_piece(7, 0).color, "white")
        self.assertIsInstance(self.board.get_piece(7, 7), Rook)
        self.assertEqual(self.board.get_piece(7, 7).color, "white")

        # Verificar los caballos en las posiciones correctas
        self.assertIsInstance(self.board.get_piece(0, 1), Knight)
        self.assertEqual(self.board.get_piece(0, 1).color, "black")
        self.assertIsInstance(self.board.get_piece(0, 6), Knight)
        self.assertEqual(self.board.get_piece(0, 6).color, "black")
        self.assertIsInstance(self.board.get_piece(7, 1), Knight)
        self.assertEqual(self.board.get_piece(7, 1).color, "white")
        self.assertIsInstance(self.board.get_piece(7, 6), Knight)
        self.assertEqual(self.board.get_piece(7, 6).color, "white")

        # Verificar los alfiles en las posiciones correctas
        self.assertIsInstance(self.board.get_piece(0, 2), Bishop)
        self.assertEqual(self.board.get_piece(0, 2).color, "black")
        self.assertIsInstance(self.board.get_piece(0, 5), Bishop)
        self.assertEqual(self.board.get_piece(0, 5).color, "black")
        self.assertIsInstance(self.board.get_piece(7, 2), Bishop)
        self.assertEqual(self.board.get_piece(7, 2).color, "white")
        self.assertIsInstance(self.board.get_piece(7, 5), Bishop)
        self.assertEqual(self.board.get_piece(7, 5).color, "white")

        # Verificar la reina y el rey
        self.assertIsInstance(self.board.get_piece(0, 3), Queen)
        self.assertEqual(self.board.get_piece(0, 3).color, "black")
        self.assertIsInstance(self.board.get_piece(0, 4), King)
        self.assertEqual(self.board.get_piece(0, 4).color, "black")
        self.assertIsInstance(self.board.get_piece(7, 3), Queen)
        self.assertEqual(self.board.get_piece(7, 3).color, "white")
        self.assertIsInstance(self.board.get_piece(7, 4), King)
        self.assertEqual(self.board.get_piece(7, 4).color, "white")

        # Verificar los peones en la segunda y séptima fila
        for col in range(8):
            self.assertIsInstance(self.board.get_piece(1, col), Pawn)
            self.assertEqual(self.board.get_piece(1, col).color, "black")
            self.assertIsInstance(self.board.get_piece(6, col), Pawn)
            self.assertEqual(self.board.get_piece(6, col).color, "white")

        # Verificar que las demás posiciones estén vacías
        for row in range(2, 6):
            for col in range(8):
                self.assertIsNone(self.board.get_piece(row, col))

    def test_invalid_positions(self):
        # Verificar que acceder a una posición fuera del tablero devuelva None o lance una excepción
        with self.assertRaises(IndexError):
            self.board.get_piece(-1, 0)
        with self.assertRaises(IndexError):
            self.board.get_piece(8, 0)
        with self.assertRaises(IndexError):
            self.board.get_piece(0, 8)

if __name__ == "__main__":
    unittest.main()
