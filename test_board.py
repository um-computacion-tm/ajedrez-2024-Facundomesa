import unittest
from board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_positions(self):
        # Importación diferida de las piezas para evitar dependencia circular
        from rook import Rook
        from knight import Knight
        from bishop import Bishop
        from queen import Queen
        from king import King
        from pawn import Pawn

        # Verificar las torres en las posiciones correctas
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertEqual(self.board.get_piece(0, 0).color.upper(), "BLACK")
        self.assertIsInstance(self.board.get_piece(0, 7), Rook)
        self.assertEqual(self.board.get_piece(0, 7).color.upper(), "BLACK")
        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertEqual(self.board.get_piece(7, 0).color.upper(), "WHITE")
        self.assertIsInstance(self.board.get_piece(7, 7), Rook)
        self.assertEqual(self.board.get_piece(7, 7).color.upper(), "WHITE")

        # Verificar los caballos en las posiciones correctas
        self.assertIsInstance(self.board.get_piece(0, 1), Knight)
        self.assertEqual(self.board.get_piece(0, 1).color.upper(), "BLACK")
        self.assertIsInstance(self.board.get_piece(0, 6), Knight)
        self.assertEqual(self.board.get_piece(0, 6).color.upper(), "BLACK")
        self.assertIsInstance(self.board.get_piece(7, 1), Knight)
        self.assertEqual(self.board.get_piece(7, 1).color.upper(), "WHITE")
        self.assertIsInstance(self.board.get_piece(7, 6), Knight)
        self.assertEqual(self.board.get_piece(7, 6).color.upper(), "WHITE")

        # Verificar los alfiles en las posiciones correctas
        self.assertIsInstance(self.board.get_piece(0, 2), Bishop)
        self.assertEqual(self.board.get_piece(0, 2).color.upper(), "BLACK")
        self.assertIsInstance(self.board.get_piece(0, 5), Bishop)
        self.assertEqual(self.board.get_piece(0, 5).color.upper(), "BLACK")
        self.assertIsInstance(self.board.get_piece(7, 2), Bishop)
        self.assertEqual(self.board.get_piece(7, 2).color.upper(), "WHITE")
        self.assertIsInstance(self.board.get_piece(7, 5), Bishop)
        self.assertEqual(self.board.get_piece(7, 5).color.upper(), "WHITE")

        # Verificar la reina y el rey
        self.assertIsInstance(self.board.get_piece(0, 3), Queen)
        self.assertEqual(self.board.get_piece(0, 3).color.upper(), "BLACK")
        self.assertIsInstance(self.board.get_piece(0, 4), King)
        self.assertEqual(self.board.get_piece(0, 4).color.upper(), "BLACK")
        self.assertIsInstance(self.board.get_piece(7, 3), Queen)
        self.assertEqual(self.board.get_piece(7, 3).color.upper(), "WHITE")
        self.assertIsInstance(self.board.get_piece(7, 4), King)
        self.assertEqual(self.board.get_piece(7, 4).color.upper(), "WHITE")

        # Verificar los peones en la segunda y séptima fila
        for col in range(8):
            self.assertIsInstance(self.board.get_piece(1, col), Pawn)
            self.assertEqual(self.board.get_piece(1, col).color.upper(), "BLACK")
            self.assertIsInstance(self.board.get_piece(6, col), Pawn)
            self.assertEqual(self.board.get_piece(6, col).color.upper(), "WHITE")

        # Verificar que las demás posiciones estén vacías
        for row in range(2, 6):
            for col in range(8):
                self.assertIsNone(self.board.get_piece(row, col))

    def test_invalid_positions(self):
        with self.assertRaises(IndexError):
            self.board.get_piece(-1, 0)  # Posición inválida, fuera del tablero
        with self.assertRaises(IndexError):
            self.board.get_piece(8, 0)  # Posición inválida, fuera del tablero
        with self.assertRaises(IndexError):
            self.board.get_piece(0, -1)  # Posición inválida, fuera del tablero
        with self.assertRaises(IndexError):
            self.board.get_piece(0, 8)  # Posición inválida, fuera del tablero

if __name__ == "__main__":
    unittest.main()
